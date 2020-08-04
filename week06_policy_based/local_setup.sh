#!/usr/bin/env bash

apt-get install -yqq ffmpeg
apt-get install -yqq python-opengl

python3 -m pip install --user gym==0.14.0
python3 -m pip install --user pygame
python3 -m pip install --user pyglet==1.3.2
python3 -m pip install --user tensorflow==2.0.0
