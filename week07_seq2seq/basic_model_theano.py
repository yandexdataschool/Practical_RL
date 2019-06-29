# code by https://github.com/deniskamazur

from lasagne.layers import *
import theano.tensor as T
import theano

from agentnet.memory import LSTMCell, GRUCell, AttentionLayer
from agentnet import Recurrence
from agentnet.learning.generic import get_mask_by_eos
from agentnet.resolver import ProbabilisticResolver
from agentnet.utils import reapply


class BasicTranslationModel:
    def __init__(self, inp_voc, out_voc, emb_size, hid_size, **kwargs):
        """
        A simple interface for mt
        :param emb_size: Embedding size
        :param hid_size: Number of LSTM units
        :param bidereactional: If the nLSTM layers should be bidirectional
        :param input_dropout: Dropout after embedding layer
        :param recurrent_dropout: Dropout after each LSTM iteration
        :param rdo_size: If int - use dense layer after neck in decoder, if none don't
        :param peepholes: http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-var-peepholes.png
        :param kwargs: recurrence flags
        """
        self.inp_voc = inp_voc
        self.out_voc = out_voc
        # encode input sequence

        class encoder:
            # intput layers
            inp = InputLayer((None, None))
            mask = ExpressionLayer(
                inp,
                lambda x: get_mask_by_eos(T.eq(x, self.out_voc.eos_ix)),
            )

            # embed the tokens
            emb = EmbeddingLayer(
                inp,
                input_size=len(inp_voc),
                output_size=emb_size,
            )

            rnn_fw = GRULayer(
                emb,
                num_units=hid_size,
                mask_input=mask,
                only_return_final=True,
            )

            dec_start = DenseLayer(rnn_fw, hid_size, nonlinearity=None)

        # make encoder a public field
        self.encoder = encoder

        # decoder the encoded sequence
        class decoder:
            # decoder previous memory and tokens
            prev_hid = InputLayer((None, hid_size), name='prev hidden state')
            inp = InputLayer((None,), name="prev phoneme")

            emb = EmbeddingLayer(inp, len(out_voc), emb_size)

            new_hid = GRUCell(prev_hid, emb)

            logits = DenseLayer(new_hid, len(out_voc), nonlinearity=None)

            probs = NonlinearityLayer(logits, nonlinearity=T.nnet.softmax)
            logprobs = NonlinearityLayer(
                logits,
                nonlinearity=T.nnet.logsoftmax,
            )
            out = ProbabilisticResolver(probs, assume_normalized=True)

            state_dict = {
                new_hid: prev_hid,
                # ^^^ this reads "at next step, new_hid will become prev_hid"
                # if you add any more recurrent memory units,
                # please make sure they're here
            }

            init_dict = {
                new_hid: encoder.dec_start
                # ^^^ this reads "before first step, new_hid is set to outputs of dec_start"
                # if you add any more recurrent memory units with non-zero init
                # please make sure they're here
            }

            nonseq_dict = {
                # here you can add anything encoder needs that's gonna be same
                # across time-steps
            }

        self.decoder = decoder

        top_layers = [encoder.dec_start, decoder.out] + \
            list(decoder.state_dict.keys())
        self.weights = get_all_params(top_layers, trainable=True)

    def symbolic_score(self, inp, out, eps=1e-30, **flags):
        """
        Takes symbolic int32 matrices of hebrew words and their english translations.
        Computes the log-probabilities of all possible english characters given english prefices and hebrew word.
        :param inp: input sequence, int32 matrix of shape [batch,time]
        :param out: output sequence, int32 matrix of shape [batch,time]
        :return: log-probabilities of all possible english characters of shape [bath,time,n_tokens]

        NOTE: log-probabilities time axis  is synchronized with out
        In other words, logp are probabilities of __current__ output at each tick, not the next one
        therefore you can get likelihood as logprobas * tf.one_hot(out,n_tokens)
        """

        l_output_sequence = InputLayer([None, None])

        # Defining custom recurrent layer out of decoder
        rec = Recurrence(
            state_variables=self.decoder.state_dict,
            state_init=self.decoder.init_dict,
            input_sequences={self.decoder.inp: l_output_sequence},
            input_nonsequences=self.decoder.nonseq_dict,
            tracked_outputs=self.decoder.logprobs,
            unroll_scan=False
        )

        feed_dict = {
            self.encoder.inp: inp,
            l_output_sequence: out
        }
        logprobs = get_output(rec[self.decoder.logprobs], feed_dict,
                              recurrence_flags=flags, **flags)

        self.auto_updates = rec.get_automatic_updates()
        if len(self.auto_updates) != 0:
            print(
                "symbolic_score: Please collect auto_updates of random states "
                "after you called symbolic_score (available at model.auto_updates)!")

        first_logprobs = T.zeros_like(logprobs[:, :1])
        logprobs = T.concatenate([first_logprobs, logprobs[:, :-1]], axis=1)

        return logprobs

    def symbolic_translate(self, inp, greedy=False, max_len=None,
                           unroll_scan=False, eps=1e-30, **flags):
        """
        takes symbolic int32 matrix of hebrew words, produces output tokens sampled
        from the model and output log-probabilities for all possible tokens at each tick.
        :param inp: input sequence, int32 matrix of shape [batch,time]
        :param greedy: if greedy, takes token with highest probablity at each tick.
            Otherwise samples proportionally to probability.
        :param max_len: max length of output, defaults to 2 * input length
        :param unroll_scan: if True, compiles longer but runs faster.
                            requires max_len to be constant
        :return: output tokens int32[batch,time] and
                 log-probabilities of all tokens at each tick, [batch,time,n_tokens]
        """
        if unroll_scan:
            assert isinstance(
                max_len, int), "if scan is unrolled, max_len must be a constant integer"

        max_len = max_len if max_len is not None else 2 * inp.shape[1]

        # initial output tokens (BOS)
        bos = T.zeros_like(inp[:, 0]) + self.out_voc.bos_ix
        l_start = InputLayer((None,), bos)

        # Defining custom recurrent layer out of decoder
        rec = Recurrence(
            state_variables=merge_dicts(self.decoder.state_dict,
                                        {self.decoder.out: self.decoder.inp}),
            state_init=merge_dicts(self.decoder.init_dict, {self.decoder.out: l_start}),
            input_nonsequences=self.decoder.nonseq_dict,
            tracked_outputs=(self.decoder.out, self.decoder.probs, self.decoder.logprobs),
            n_steps=max_len,
            unroll_scan=unroll_scan
        )

        translations, logprobs = get_output(rec[self.decoder.out, self.decoder.logprobs],
                                            {self.encoder.inp: inp,
                                             l_start: bos},
                                            recurrence_flags=dict(flags, greedy=greedy),
                                            **flags)

        self.auto_updates = rec.get_automatic_updates()
        if len(self.auto_updates) != 0:
            print(
                "symbolic_translate: Please collect auto_updates of random states "
                "after you called symbolic_translate (available at model.auto_updates)!")

        # add first step (bos)
        translations = T.concatenate([bos[:, None], translations], axis=1)
        first_logprobs = T.zeros_like(logprobs[:, :1])
        logprobs = T.concatenate([first_logprobs, logprobs], axis=1)

        return translations, logprobs


def merge_dicts(*dicts, **kwargs):
    """
    Melts several dicts into one. Useful when messing with feed dicts
    :param dicts: dictionaries
    :param check_conflicts: if True, raises error if several dicts have the same key
                    Otherwise uses the key from the latest dict in *dicts
    :return: a dict that contains k-v pairs from  all *dicts
    """
    merged_dict = {}
    for d in dicts:
        merged_dict.update(d)
    if kwargs.get('check_conflicts'):
        assert len(merged_dict) == sum(
            map(len, dicts)), 'dicts have duplicate keys'
    return merged_dict
