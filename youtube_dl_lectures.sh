#!/usr/bin/env bash

# This script uses https://github.com/rg3/youtube-dl/ to download __ENGLISH__
# lecture materials in the respective folders. You can install youtube-dl via
# `pip install --upgrade youtube-dl` if you do not have it already.
# WARNING! The full script downloads gigabytes of mp4!

# week01
youtube-dl 'https://www.youtube.com/watch?v=2pWv7GOvuf0' --output 'week01_intro/lect/Lecture1_Silver.mp4'
youtube-dl 'https://www.youtube.com/watch?v=aUrX-rP_ss4' --output 'week01_intro/lect/Lecture_Schulman.mp4'
youtube-dl 'https://www.youtube.com/watch?v=lfHX2hHRMVQ' --output 'week01_intro/lect/Lecture2_Silver_optional.mp4'

# week02
youtube-dl 'https://www.youtube.com/watch?v=Nd1-UUMVfz4' --output 'week02_value_based/lect/Lecture_Silver.mp4'
youtube-dl 'https://www.youtube.com/watch?v=i0o-ui1N35U' --output 'week02_value_based/lect/Alternative_lecture_Abbeel_part1.mp4'
youtube-dl 'https://www.youtube.com/watch?v=Csiiv6WGzKM' --output 'week02_value_based/lect/Alternative_lecture_Abbeel_part2.mp4'
youtube-dl 'https://www.youtube.com/watch?v=IL3gVyJMmhg' --output 'week02_value_based/lect/Alternative_lecture_Schulman.mp4'

# week03
youtube-dl 'https://www.youtube.com/watch?v=PnHCvfgC_ZA' --output 'week03_model_free/lect/Lecture_Silver_part1.mp4'
youtube-dl 'https://www.youtube.com/watch?v=0g4j2k_Ggc4' --output 'week03_model_free/lect/Lecture_Silver_part2.mp4'
youtube-dl 'https://www.youtube.com/watch?v=ifma8G7LegE' --output 'week03_model_free/lect/Alternative_lecture_Abbeel.mp4'
youtube-dl 'https://www.youtube.com/watch?v=IL3gVyJMmhg' --output 'week03_model_free/lect/Alternative_lecture_Schulman.mp4'

# week04_recap
youtube-dl 'https://www.youtube.com/watch?v=uXt8qF2Zzfo' --output 'week04_[recap]_deep_learning/lect/Lecture_basics.mp4'
youtube-dl 'https://www.youtube.com/watch?v=FmpDIaiMIeA' --output 'week04_[recap]_deep_learning/lect/Lecture_convnets.mp4'
youtube-dl 'https://www.youtube.com/watch?v=OU8I1oJ9HhI' --output 'week04_[recap]_deep_learning/lect/Tutorial_theano.mp4'

# week04
youtube-dl 'https://www.youtube.com/watch?v=UoPei5o4fps' --output 'week04_approx_rl/lect/Lecture_Silver.mp4'
youtube-dl 'https://www.youtube.com/watch?v=h1-pj4Y9-kM' --output 'week04_approx_rl/lect/Lecture_Schulman.mp4'

# week05
youtube-dl 'https://www.youtube.com/watch?v=sGuiWX07sKw' --output 'week05_explore/lect/Lecture_Silver.mp4'
youtube-dl 'https://www.youtube.com/watch?v=SfCa1HQMkuw' --output 'week05_explore/lect/Lecture_Schulman.mp4'

# week06
youtube-dl 'https://www.youtube.com/watch?v=KHZVXao4qXs' --output 'week06_policy_based/lect/Lecture_Silver.mp4'
youtube-dl 'https://www.youtube.com/watch?v=BB-BhTn6DCM' --output 'week06_policy_based/lect/Alternative_lecture_Schulman_part1.mp4'
youtube-dl 'https://www.youtube.com/watch?v=Wnl-Qh2UHGg' --output 'week06_policy_based/lect/Alternative_lecture_Schulman_part2.mp4'

# week07_recap
youtube-dl 'https://www.youtube.com/watch?v=iX5V1WpxxkY' --output 'week07_[recap]_rnn/lect/Lecture_cs231.mp4'
youtube-dl 'https://www.youtube.com/watch?v=Ukgii7Yd_cU' --output 'week07_[recap]_rnn/lect/Alternative_lecture_nervana.mp4'
youtube-dl 'https://www.youtube.com/watch?v=xK-bzjIQkmM' --output 'week07_[recap]_rnn/lect/Alternative_lecture_Bengio.mp4'
youtube-dl 'https://www.youtube.com/watch?v=G5RY_SUJih4' --output 'week07_[recap]_rnn/lect/Bonus_lecture_seq2seq.mp4'

# week07
youtube-dl 'https://www.youtube.com/watch?v=yCqPMD6coO8' --output 'week07_pomdp/lect/Lecture_Ng.mp4'

# week08
youtube-dl 'https://www.youtube.com/watch?v=yCqPMD6coO8' --output 'week08_pomdp/lect/Lecture_Ng.mp4'
youtube-dl 'https://www.youtube.com/watch?v=9G_KevA8DFY' --output 'week08_pomdp/lect/Alternative_lecture_Ravindran_part1.mp4'
youtube-dl 'https://www.youtube.com/watch?v=dMOUp7YzUpQ' --output 'week08_pomdp/lect/Alternative_lecture_Ravindran_part2.mp4'
youtube-dl 'https://www.youtube.com/watch?v=dMOUp7YzUpQ' --output 'week08_pomdp/lect/Bonus_lecture_Baveja.mp4'

# week09
youtube-dl 'https://www.youtube.com/watch?v=_t5fpZuuf-4' --output 'week09_policy_II/lect/Lecture_Schulman.mp4'
