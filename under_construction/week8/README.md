## Materials
* [Slides](https://yadi.sk/i/7TkZUDkt3GoPXE)
* Our [lecture](https://yadi.sk/i/-U5w4NpJ3H5TWD), [seminar](https://yadi.sk/i/W3N7-6is3H5TWN)
* The only relevant video-lecture we could find - [video](https://www.youtube.com/watch?v=2tKNpzUvDc4	)
* Will hopefully record our lecture in english soon!
* Self-critical sequence traning [original article](https://arxiv.org/abs/1612.00563)


## More materials
* An [awesome post](http://distill.pub/2016/augmented-rnns/) explaining attention and long-term memory models.
* [BLEU](http://www.aclweb.org/anthology/P02-1040.pdf) and [CIDEr](https://arxiv.org/pdf/1411.5726.pdf) articles.
* Image captioning
  * MSCOCO captioning [challenge](http://mscoco.org/dataset/#captions-challenge2015)
  * Captioning baseline [notebook](https://github.com/yandexdataschool/HSE_deeplearning/blob/master/week7/captioning_solution_ars.ipynb)
* Other articles on reinforcement learning for natural language: 
  * [task-oriented conversation system](https://arxiv.org/abs/1703.07055)
  * [generating dialogues](https://arxiv.org/abs/1606.01541)
  * [sequential adversarial networks](https://arxiv.org/abs/1609.05473) (a.k.a. SeqGAN)
  * A large overview for machine translation (touching on RL, including RL failures) - [article](https://arxiv.org/abs/1609.08144)
  * How _not_ to evaluate conversation models - [article](https://arxiv.org/abs/1603.08023)
* Overview of other non-games applications ("that article again") - https://arxiv.org/abs/1701.07274

## Homework

Homework assignment is described in the [main notebook](https://github.com/yandexdataschool/Practical_RL/blob/master/week8/8.1_translation_scst.ipynb).

It's kinda lengthy, but fear not, that's mostly due to formatting.

__Other frameworks__: as usual, your task remains the same as in the main track:
- Implement or borrow seq2seq model for the same translation task
  * Neat tenworflow [repo](https://github.com/cmusphinx/g2p-seq2seq)
  * __Important__ - this repo uses simplified phoneme dict - make sure you change preprocessing phase to meaningfully compare results.
- Implement self-critical sequence training ( = basic policy gradient with a special baseline, see notebook)
- Beat the baseline (main notebook: step6)
  
Even if you decide to use custom frameworks, it is highly recommended that you reuse evaluation code (e.g. min Levenshtein) from the main notebook to avoid confusion.

