#!/usr/bin/env bash

apt-get update
apt-get install -y xvfb
wget -q https://raw.githubusercontent.com/yandexdataschool/Practical_RL/spring20/xvfb -O ../xvfb
