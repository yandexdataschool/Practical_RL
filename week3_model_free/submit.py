import sys
import numpy as np
sys.path.append("..")
import grading


def submit_experience_replay(rewards_replay, rewards_baseline, email, token):
    flag1 = np.mean(rewards_replay[:100]) - np.mean(rewards_baseline[:100])
    flag2 = np.mean(rewards_replay[-100:])
    flag3 = np.mean(rewards_baseline[-100:])

    grader = grading.Grader("XUt-8d7yEee8nwq8KJgXXg")
    grader.set_answer("iEQwT", flag1)
    grader.set_answer("8N1Wm", flag2)
    grader.set_answer("F0Am8", flag3)

    grader.submit(email, token)


def submit_qlearning1(rewards, email, token):
    flag1 = np.mean(rewards[-10:])

    grader = grading.Grader("XbjcGd7xEeeDzRKutDCmyA")
    grader.set_answer("5NB4z", flag1)

    grader.submit(email, token)


def submit_qlearning2(rewards, email, token):
    flag1 = np.mean(rewards[-10:])

    grader = grading.Grader("XbjcGd7xEeeDzRKutDCmyA")
    grader.set_answer("CkyJ4", flag1)

    grader.submit(email, token)


def submit_sarsa(rewards_ql, rewards_sarsa, email, token):
    flag1 = np.mean(rewards_ql[-100:])
    flag2 = np.mean(rewards_sarsa[-100:])
    flag3 = np.mean(rewards_sarsa[-100:]) - np.mean(rewards_ql[-100:])

    grader = grading.Grader("pazQX97xEee_JA6t1Myltg")
    grader.set_answer("ZarWJ", flag1)
    grader.set_answer("izJi4", flag2)
    grader.set_answer("frgbU", flag3)

    grader.submit(email, token)