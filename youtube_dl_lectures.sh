#!/bin/bash
#this script utilizes https://github.com/rg3/youtube-dl/ to download lecture materials in the respective folders.
#you can install youtube-dl via `pip install --upgrade youtube-dl` if you don't have it already.

#WARNING! the full script downloads gigabytes of mp4!

#week0
youtube-dl https://www.youtube.com/watch?v=2pWv7GOvuf0 --output week0/Lecture1_Silver.mp4
youtube-dl https://www.youtube.com/watch?v=lfHX2hHRMVQ --output week0/Lecture2_Silver_optional.mp4

#week1
youtube-dl https://www.youtube.com/watch?v=aUrX-rP_ss4 --output week1/Lecture_Schulman.mp4

#week2
youtube-dl https://www.youtube.com/watch?v=PnHCvfgC_ZA --output week2/Lecture_Silver.mp4
youtube-dl https://www.youtube.com/watch?v=ifma8G7LegE --output week2/Alternative_lecture_Abbeel.mp4
youtube-dl https://www.youtube.com/watch?v=IL3gVyJMmhg --output week2/Alternative_lecture_Schulman.mp4

#week3
youtube-dl https://www.youtube.com/watch?v=0g4j2k_Ggc4 --output week3/Lecture_Silver.mp4

#week4
youtube-dl https://www.youtube.com/watch?v=UoPei5o4fps --output week4/Lecture_Silver.mp4

#week5
youtube-dl https://www.youtube.com/watch?v=h1-pj4Y9-kM --output week5/Lecture_Schulman.mp4

#week6
youtube-dl https://www.youtube.com/watch?v=KHZVXao4qXs --output week6/Lecture_Silver.mp4
youtube-dl https://www.youtube.com/watch?v=BB-BhTn6DCM --output week6/Alternative_lecture_Schulman_part1.mp4
youtube-dl  https://www.youtube.com/watch?v=Wnl-Qh2UHGg --output week6/Alternative_lecture_Schulman_part2.mp4


