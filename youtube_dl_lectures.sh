#!/bin/bash
#this script utilizes https://github.com/rg3/youtube-dl/ to download __ENGLISH__ lecture materials in the respective folders.
#you can install youtube-dl via `pip install --upgrade youtube-dl` if you don't have it already.
#WARNING! the full script downloads gigabytes of mp4!

#week0
youtube-dl https://www.youtube.com/watch?v=2pWv7GOvuf0 --output week0_intro/Lecture1_Silver.mp4
youtube-dl https://www.youtube.com/watch?v=lfHX2hHRMVQ --output week0_intro/Lecture2_Silver_optional.mp4

#week1
youtube-dl https://www.youtube.com/watch?v=aUrX-rP_ss4 --output week1_blackbox/Lecture_Schulman.mp4

#week2
youtube-dl https://www.youtube.com/watch?v=Nd1-UUMVfz4 --output week2_value_based/Lecture_Silver.mp4
youtube-dl https://www.youtube.com/watch?v=i0o-ui1N35U --output week2_value_based/Alternative_lecture_Abbeel_part1.mp4
youtube-dl https://www.youtube.com/watch?v=Csiiv6WGzKM --output week2_value_based/Alternative_lecture_Abbeel_part2.mp4
youtube-dl https://www.youtube.com/watch?v=IL3gVyJMmhg --output week2_value_based/Alternative_lecture_Schulman.mp4

#week3
youtube-dl https://www.youtube.com/watch?v=PnHCvfgC_ZA --output week3_model_free/Lecture_Silver_part1.mp4
youtube-dl https://www.youtube.com/watch?v=0g4j2k_Ggc4 --output week3_model_free/Lecture_Silver_part2.mp4
youtube-dl https://www.youtube.com/watch?v=ifma8G7LegE --output week3_model_free/Alternative_lecture_Abbeel.mp4
youtube-dl https://www.youtube.com/watch?v=IL3gVyJMmhg --output week3_model_free/Alternative_lecture_Schulmann.mp4

#week3.5
youtube-dl https://www.youtube.com/watch?v=uXt8qF2Zzfo --output week4_\[recap\]_deep_learning/Lecture_basics.mp4
youtube-dl https://www.youtube.com/watch?v=FmpDIaiMIeA --output week4_\[recap\]_deep_learning/Lecture_convnets.mp4
youtube-dl https://www.youtube.com/watch?v=OU8I1oJ9HhI --output week4_\[recap\]_deep_learning/Tutorial_theano.mp4

#week4
youtube-dl https://www.youtube.com/watch?v=UoPei5o4fps --output week4_approx_rl/Lecture_Silver.mp4
youtube-dl https://www.youtube.com/watch?v=h1-pj4Y9-kM --output week4_approx_rl/Lecture_Schulman.mp4

#week5
youtube-dl https://www.youtube.com/watch?v=sGuiWX07sKw --output week5_explore/Lecture_Silver.mp4
youtube-dl https://www.youtube.com/watch?v=SfCa1HQMkuw --output week5_explore/Lecture_Schulmann.mp4

#week6
youtube-dl https://www.youtube.com/watch?v=KHZVXao4qXs --output week6_policy_based/Lecture_Silver.mp4
youtube-dl https://www.youtube.com/watch?v=BB-BhTn6DCM --output week6_policy_based/Alternative_lecture_Schulman_part1.mp4
youtube-dl  https://www.youtube.com/watch?v=Wnl-Qh2UHGg --output week6_policy_based/Alternative_lecture_Schulman_part2.mp4

#week6.5
youtube-dl https://www.youtube.com/watch?v=iX5V1WpxxkY --output week7_\[recap\]_rnn/Lecture_cs231.mp4
youtube-dl https://www.youtube.com/watch?v=Ukgii7Yd_cU --output week7_\[recap\]_rnn/Alternative_lecture_nervana.mp4
youtube-dl https://www.youtube.com/watch?v=xK-bzjIQkmM --output week7_\[recap\]_rnn/Alternative_lecture_Bengio.mp4
youtube-dl https://www.youtube.com/watch?v=G5RY_SUJih4 --output week7_\[recap\]_rnn/Bonus_lecture_seq2seq.mp4

#week7
youtube-dl https://www.youtube.com/watch?v=yCqPMD6coO8 --output week7_pomdp/Lecture_Ng.mp4

#week8
#TODO

#week9
youtube-dl https://www.youtube.com/watch?v=_t5fpZuuf-4 --output week9_policy_II/Lecture_Schulmann.mp4

