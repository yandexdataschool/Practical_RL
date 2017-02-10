FROM ubuntu:16.04
LABEL maintainer "Alexander Panin <justheuristic@gmail.com>, Dmitry Mittov <mittov@gmail.com>"

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    apt-get -qq update && \
    apt-get install -y cmake \
                       zlib1g-dev \
                       libjpeg-dev \
                       xvfb \
                       libav-tools \
                       xorg-dev \
                       python-opengl \
                       swig3.0 \
                       python3-pip && \
    ln -s /usr/bin/swig3.0 /usr/bin/swig

RUN pip3 install --upgrade pip \
                           scipy \
                           numpy && \
    pip3 install --upgrade sklearn \
                           jupyter \
                           tqdm \
                           gym[all] \
                           matplotlib \
                           seaborn && \
    python3 -m ipykernel.kernelspec

EXPOSE 8888
VOLUME /notebooks
WORKDIR /notebooks

COPY run_jupyter.sh /
CMD ["/run_jupyter.sh"]
