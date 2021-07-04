#!/usr/bin/env bash

apt-get -qq update
apt-get -qq install -y xvfb
wget -q https://raw.githubusercontent.com/yandexdataschool/Practical_RL/master/xvfb -O ../xvfb

# Download & import Atari ROMs (Colab stopped bundling them around the beginning of June 2021)

gdown -q https://drive.google.com/uc?id=1dCLEJcJGDDV4l5ssoexP2TEOVuBfyh7D

# Alternative download:
# wget -q http://www.atarimania.com/roms/Roms.rar

pip install -q unrar
mkdir ./roms
unrar x Roms.rar ./roms > /dev/null 2>&1
python -m atari_py.import_roms ./roms > /dev/null 2>&1
