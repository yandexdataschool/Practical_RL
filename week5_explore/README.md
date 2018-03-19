### Slides - [here](https://yadi.sk/i/H0zVBROe3TWWHz)

## Exploration and exploitation
* [__main__] David Silver lecture on exploration and expoitation - [video](https://www.youtube.com/watch?v=sGuiWX07sKw)
* Alternative lecture by J. Schulman - [video](https://www.youtube.com/watch?v=SfCa1HQMkuw)
* Our lecture (russian) - [slides](https://yadi.sk/i/JAeItALT3JmvCL), [video](https://yadi.sk/i/bVHmu9gt3Hi9Ym)
* Our lecture on exploration with bayesian neural networks - [slides](https://yadi.sk/i/OANpkyFn3Jmv4J)
  
## More materials 
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
