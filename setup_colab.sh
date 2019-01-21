#!/bin/bash
# a setup script for google colab. Will be updated
pip install gym
apt-get install -y xvfb
wget https://raw.githubusercontent.com/yandexdataschool/Practical_DL/fall18/xvfb -O ../xvfb
apt-get install -y python-opengl ffmpeg
pip install pyglet==1.2.4

