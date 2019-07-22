[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yandexdataschool/Practical_RL/blob/master/week05_explore/week5.ipynb) 

### Slides - [here](https://yadi.sk/i/H0zVBROe3TWWHz)

## Exploration and exploitation
* [__main__] David Silver lecture on exploration and expoitation - [video](https://www.youtube.com/watch?v=sGuiWX07sKw)
* Alternative lecture by J. Schulman - [video](https://www.youtube.com/watch?v=SfCa1HQMkuw)
* Alternative lecture by N. de Freitas (with bayesian opt) - [video](https://www.youtube.com/watch?v=vz3D36VXefI)
* Our lectures (russian) 
  - "mathematical" lecture (by Alexander Vorobev) '17 - [slides](https://yadi.sk/i/JAeItALT3JmvCL), [video](https://yadi.sk/i/bVHmu9gt3Hi9Ym)
  - "practical" lecture '18 - [video](https://yadi.sk/i/_myWJ13O3TdzXo)
  - Seminar - [video](https://yadi.sk/i/du7FLXs13TdzZS)
  
  
  
## More materials 
* Gittins Index - the less heuristical approach to bandit exploration - [article](http://www.ece.mcgill.ca/~amahaj1/projects/bandits/book/2013-bandit-computations.pdf)
* "Deep" version: variational information maximizing exploration - [video](https://www.youtube.com/watch?v=sRIjxxjVrnY)
  * Same topics in russian - [video](https://yadi.sk/i/_2_0yqeW3HDbcn)
* Lecture covering intrinsically motivated reinforcement learning - [video](https://www.youtube.com/watch?v=aJI_9SoBDaQ)
  * [Slides](https://yadi.sk/i/8sx42nau3HEYKg)
  * Same topics in russian - [video](https://www.youtube.com/watch?v=WCE9hhPbCmc)
  * Note: UCB-1 is not for bernoulli rewards, but for arbitrary r in [0,1], so you can just scale any reward to [0,1] to obtain a peace of mind. It's derived directly from Hoeffding's inequality.

## Seminar
In this seminar, you'll be solvilg basic and contextual bandits with uncertainty-based exploration like Bayesian UCB and Thompson Sampling. 

You will also need Bayesian Neural Networks. You will need theano/lasagne for this one:
```
# either
conda install Theano
# or
pip install --upgrade https://github.com/Theano/Theano/archive/master.zip
# and then lasagne
pip install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip
```

Everything else is in the notebook :)
