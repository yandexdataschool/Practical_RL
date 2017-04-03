This week's assignment appears to be unusually grandeur, so please read submission/grading guidelines before you upload it for review.

__Submisson__: To ease mutual pain, please submit
- Some kind of readable report with links to your evaluations, gym uploads, investigation results, etc.
- Explicitly state that you took on a bonus task and where to find it [to make sure it is found and graded].

__Grading__: The main purpose (and source of points) for this notebook is your investigation, not squeezing out average rewards from random environments. 

Getting near/above state of the art performance on one particular game will earn you some bonus points, but you can get much more by digging deeper into what makes the algorithms tick and how they compare to one another.

Okay, now brace yourselves, here comes an assignment!

#### 7.1 rock-paper-sarsa
Go to [the first notebook](https://github.com/yandexdataschool/Practical_RL/blob/master/week7/7.1_rock_paper_scissors.ipynb) and implement basic recurrent SARSA.

_note: there's a bonus task at the end of this notebook_

#### 7.2 Deep kung-fu (3 pts)

Implement and train recurrent actor-critic on `KungFuMaster-v0` env in the second notebook. Try to get a score of >=20k.

Please __upload your algorithm to [gym leaderboard]__(https://gym.openai.com/envs/KungFuMaster-v0) and submit the link to your eval!


#### 7.3 new horizons (7 pts)

_Please read this assignment carefully._

Choose a partially-observable environment for experimentation out of [atari](https://gym.openai.com/envs#atari), [doom](https://gym.openai.com/envs#doom) or [pygame](https://gym.openai.com/envs#pygame) catalogue (if you really want to try some other pomdp, feel free to proceed at your own risk).

Not all atari environements are bug free and these minor bugs can hurt learning performance. 
We recommend to pick one of those:
* [Assault-v0](https://gym.openai.com/envs/Assault-v0) 
* [DoomDefendCenter-v0](https://gym.openai.com/envs/DoomDefendCenter-v0) (use env code from [this](https://github.com/yandexdataschool/Practical_RL/blob/master/week4/Seminar4.2_conv_agent.ipynb) notebook)
* [RoadRunner-v0](https://gym.openai.com/envs/RoadRunner-v0)

Unless you have aesthetical preference, we would appreciate if you chose env out of recommended ones by `random.choice`.

Your task is to implement DRQN and A3C (seminar code may be reused) and apply them __both__ to the environement of your choice. Then compare them on the chosen game (convergence / sample efficiency / final performance).


* It's probably a good idea to compare a3c vs q-learning with similar network complexity. 
* Also remember that you can only use large experience replay for 1-step q-learning


__Tips__:
Your new environment may require some tuning before it gives up to your agent:


* Different preprocessing. Mostly cropping.
 * In some cases, even larger screen size or colorization. 
 * View resulting image to figure that out.


* Reward scaling. 
 * Kung-fu used `rewards=replay.rewards/100.` because you got +100 per success.
 * Just avoid training on raw +100 rewards or it's gonna blow up mean squared error.


* Deterministic/FrameSkip
 * For doom/pygame/custom, use frameskip to speed up learning
   * ```from gym.wrappers import SkipWrapper```
   * ```env = SkipWrapper(how_many_frames_to_skip)(your_env)``` in your make_env
 
 * For atari only, consider __training__ on deterministic version of environment
   * Works by appending Deterministic to env name: `AssaultDeterministic-v0`, `KungFuMasterDeterministic-v0`
   * Expect faster training due to less variance.
   * You still need to __switch back to normal env for evaluation__ (there's no leaderbord for deterministic envs)

* Knowledge transfer
   * If you want to switch network mid-game, you are recommended to use some pre-trained layers
   * At minimum, save convolutional weights and re-use them in every new architecture using fine-tuning
   * At it's darkest, [soft-targets](http://www.kdnuggets.com/2015/05/dark-knowledge-neural-network.html), [policy distillation](https://arxiv.org/pdf/1511.06295.pdf), [net2net](https://arxiv.org/abs/1511.05641) or similar __[bonus points]__.



#### For the curious
- __[4+ bonus points]__ Implement attentive model for DQRN/A3C (see lecture slides for implementation details). How does it compare to the vanilla architecture? 
* __[2+ bonus points]__ If you have any q-learning modiffications from week5 (double q-l, prioritized replay, etc.), they are most welcome here!
* __[2+ bonus points]__ How different memory amounts and types (LSTM / GRU / RNN / combo / custom) affects DRQN / A2C performance? Try to find optimal configuration.
- __[2+ bonus points]__ No one said l2 loss is perfect. Implement Huber or MAE loss for DRQN and/or A2C critic and compare it's performance on the game of your choice (pass proper `loss_function` to `get_elementwise_objective()`) .
- __[1++ bonus points]__ Does it help to add recurrent units when in MDP scenario, e.g fully observable "CartPole-v0"?  How about if you only give it access to position observations? Only speed observations? Try that out!
- __[4+ bonus points]__ See the very end of this notebook. Some of the games (right side) benefit a lot from additional LSTM memory. But others (left side) do not. That is interesting. Pick up one or several games from the left side and try to figure out why A2C performance decreases when adding LSTM to feadforward architecture?

#### Bonus: Neural Maps (a LOT of points if successful)

Pick up either [DoomMyWayHome-v0](https://gym.openai.com/envs/DoomMyWayHome-v0) or  [RaycastMaze-v0](https://gym.openai.com/envs/RaycastMaze-v0) and apply Neural Map to it. Main details of Neural Map are given in lecture slides and you could also benefit from reading [Neural Map article](https://arxiv.org/abs/1702.08360). 

[hse/ysda] Feel free to ask Pavel Shvechikov / Fedor Ratnikov any questions, guidance and clarifications on the topic.

This block is highly experimental and may be connected with some additional difficulties compared to main track. With some brief description of you work you could get additional points

_Scoring points are pre-determined for this task because we're uncertain of implementation complexity._

