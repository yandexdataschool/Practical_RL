FROM ubuntu:16.04
LABEL maintainer "Alexander Panin <justheuristic@gmail.com>, Dmitry Mittov <mittov@gmail.com>"


RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    apt-get -qq update && \
    apt-get install -y cmake \
                       wget \
                       unzip \
                       git \
                       zlib1g-dev \
                       libjpeg-dev \
                       xvfb \
                       libav-tools \
                       xorg-dev \
                       python-opengl \
                       swig3.0 \
                       python3-dev \
                       python-pip \
                       python3-pip \
                       libopenblas-dev \
                       liblapack-dev \
                       libsdl2-dev \
                       libboost-all-dev \
                       graphviz \
                       gcc \
                       g++ && \
    ln -s /usr/bin/swig3.0 /usr/bin/swig

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade setuptools && \
    python3 -m pip install --upgrade numpy scipy && \
    python3 -m pip install --upgrade sklearn \
                           jupyter \
                           tqdm \
                           enum34 \
                           graphviz \
                           gym gym[box2d] gym[atari] \
                           matplotlib \
                           seaborn \
                           scikit-image \
                           imageio \
                           atari-py \
                           psutil && \
    python3 -m pip install --upgrade https://github.com/Theano/Theano/archive/master.zip \
                           https://github.com/Lasagne/Lasagne/archive/master.zip \
                           https://github.com/yandexdataschool/AgentNet/archive/master.zip \
                           torch \
                           torchvision \
                           tensorflow \
                           keras && \                           
    python3 -m ipykernel.kernelspec


EXPOSE 8888
VOLUME /notebooks
WORKDIR /notebooks

COPY run_jupyter.sh /
CMD ["/run_jupyter.sh"]
