FROM andrewosh/binder-base
MAINTAINER Alexander Panin <justheuristic@gmail.com>
USER root

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list
RUN apt-get -qq update
RUN apt-get install -y cmake
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y libjpeg-dev 
RUN apt-get install -y xvfb libav-tools xorg-dev python-opengl
RUN apt-get -y install swig3.0
RUN ln -s /usr/bin/swig3.0 /usr/bin/swig

USER main

RUN pip install --upgrade sklearn
RUN mkdir ~/gym2 && cd ~/gym2 && git clone https://github.com/openai/gym.git && cd gym && pip install -e .[box2d]

RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade sklearn
RUN mkdir ~/gym3 && cd ~/gym3 && git clone https://github.com/openai/gym.git && cd gym && /home/main/anaconda/envs/python3/bin/pip install -e .[box2d]
