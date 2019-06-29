import numpy as np


class Vocab:
    def __init__(self, tokens, bos="__BOS__", eos="__EOS__", sep=''):
        """
        A special class that handles tokenizing and detokenizing
        """
        assert bos in tokens, eos in tokens
        self.tokens = tokens
        self.token_to_ix = {t: i for i, t in enumerate(tokens)}

        self.bos = bos
        self.bos_ix = self.token_to_ix[bos]
        self.eos = eos
        self.eos_ix = self.token_to_ix[eos]
        self.sep = sep

    def __len__(self):
        return len(self.tokens)

    @staticmethod
    def from_lines(lines, bos="__BOS__", eos="__EOS__", sep=''):
        flat_lines = sep.join(list(lines))
        flat_lines = list(flat_lines.split(sep)) if sep else list(flat_lines)
        tokens = list(set(sep.join(flat_lines)))
        tokens = [t for t in tokens if t not in (bos, eos) and len(t) != 0]
        tokens = [bos, eos] + tokens
        return Vocab(tokens, bos, eos, sep)

    def tokenize(self, string):
        """converts string to a list of tokens"""
        tokens = list(filter(len, string.split(self.sep))) \
            if self.sep != '' else list(string)
        return [self.bos] + tokens + [self.eos]

    def to_matrix(self, lines, max_len=None):
        """
        convert variable length token sequences into  fixed size matrix
        example usage:
        >>>print( as_matrix(words[:3],source_to_ix))
        [[15 22 21 28 27 13 -1 -1 -1 -1 -1]
         [30 21 15 15 21 14 28 27 13 -1 -1]
         [25 37 31 34 21 20 37 21 28 19 13]]
        """
        max_len = max_len or max(map(len, lines)) + 2  # 2 for bos and eos

        matrix = np.zeros((len(lines), max_len), dtype='int32') + self.eos_ix
        for i, seq in enumerate(lines):
            tokens = self.tokenize(seq)
            row_ix = list(map(self.token_to_ix.get, tokens))[:max_len]
            matrix[i, :len(row_ix)] = row_ix

        return matrix

    def to_lines(self, matrix, crop=True):
        """
        Convert matrix of token ids into strings
        :param matrix: matrix of tokens of int32, shape=[batch,time]
        :param crop: if True, crops BOS and EOS from line
        :return:
        """
        lines = []
        for line_ix in map(list, matrix):
            if crop:
                if line_ix[0] == self.bos_ix:
                    line_ix = line_ix[1:]
                if self.eos_ix in line_ix:
                    line_ix = line_ix[:line_ix.index(self.eos_ix)]
            line = self.sep.join(self.tokens[i] for i in line_ix)
            lines.append(line)
        return lines
