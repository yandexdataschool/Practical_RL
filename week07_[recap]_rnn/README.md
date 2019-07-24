## Materials
* [Slides](https://yadi.sk/i/-Iqdhg483GDyoN)
* CS231 lecture on RNNs - [video](https://www.youtube.com/watch?v=iX5V1WpxxkY)
* Our [lecture](https://yadi.sk/i/XHmT5hO53GcCKV), [seminar(pytorch)](https://yadi.sk/i/nCch5I8S3TsXh5), [seminar(theano)](https://yadi.sk/i/19twHESN3GcGKQ) (both russian)
* [alternative] Brief lecture on RNN by nervana - [video](https://www.youtube.com/watch?v=Ukgii7Yd_cU)
* [alternative] More detailed lecture by Y. Bengio - [video](https://www.youtube.com/watch?v=xK-bzjIQkmM)
* Great reading by Karpathy - [blog post](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* LSTM explained in detail by colah - [blog post](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

## More materials
* Seq2seq lecture - [video](https://www.youtube.com/watch?v=G5RY_SUJih4)
* "Awesome rnn" entry point - [repo](https://github.com/kjw0612/awesome-rnn)
* OpenAI research on sentiment analysis that sheds some light on what's inside LSTM language model.

# Homework description
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yandexdataschool/Practical_RL/blob/master/week07_%5Brecap%5D_rnn/seminar_pytorch.ipynb)

This week's practice gets you acquainted with basics of recurrent neural networks. For simplicity, we'll train them on character language modelling task. Pick any one of `seminar_lasagne`, `seminar_lasagne_ingraph` or `seminar_tf`.

As for difference btwn `seminar_lasagne` and `seminar_lasagne_ingraph` - ingraph version shows a lower-level interface to recurrent neural networks. It also requires you to install `pip install https://github.com/yandexdataschool/agentnet/archive/master.zip`. Out-of-graph version cover higher-level syntax from native lasagne.
