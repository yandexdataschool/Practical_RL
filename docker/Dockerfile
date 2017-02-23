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
                       python-dev \
                       python3-dev \
                       python-pip \
                       python3-pip \
                       libopenblas-dev \
                       liblapack-dev \
                       libsdl2-dev \
                       libboost-all-dev \
                       gcc \
                       g++ && \
    ln -s /usr/bin/swig3.0 /usr/bin/swig

RUN pip install --upgrade pip \
                           scipy \
                           numpy && \
    pip install --upgrade sklearn \
                           jupyter \
                           tqdm \
                           gym[all] \
                           matplotlib \
                           seaborn && \
    pip install --upgrade https://github.com/Theano/Theano/archive/master.zip \
                           https://github.com/Lasagne/Lasagne/archive/master.zip \
                           https://github.com/yandexdataschool/AgentNet/archive/master.zip \
                           tensorflow \
                           keras     
                           
RUN pip install --upgrade  gym_pull ppaquette-gym-doom


RUN pip3 install --upgrade pip \
                           scipy \
                           numpy && \
    pip3 install --upgrade sklearn \
                           jupyter \
                           tqdm \
                           gym[all] \
                           matplotlib \
                           seaborn && \
    pip3 install --upgrade https://github.com/Theano/Theano/archive/master.zip \
                           https://github.com/Lasagne/Lasagne/archive/master.zip \
                           https://github.com/yandexdataschool/AgentNet/archive/master.zip \
                           tensorflow \
                           keras && \                           
    python3 -m ipykernel.kernelspec


EXPOSE 8888
VOLUME /notebooks
WORKDIR /notebooks

COPY run_jupyter.sh /
CMD ["/run_jupyter.sh"]
