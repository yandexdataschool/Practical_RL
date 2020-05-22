ARG device

FROM ubuntu:18.04 AS base-cpu

FROM nvidia/cuda:10.2-base-ubuntu18.04 AS base-gpu

FROM base-$device AS base

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq update && \
    apt-get install -y wget unzip git cmake xvfb sudo freeglut3-dev ffmpeg

RUN adduser --disabled-password --gecos "Default user" jupyter && \
    adduser jupyter sudo && \
    echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    mkdir /notebooks && \
    chown -R jupyter /notebooks

RUN su jupyter -c \
    "wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh \
        -O /tmp/anaconda3.sh" && \
    mkdir -p /opt/conda && \
    chown -R jupyter /opt/conda && \
    su jupyter -c "/bin/bash /tmp/anaconda3.sh -b -p /opt/conda -u" && \
    rm /tmp/anaconda3.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    su jupyter -c "echo '. /opt/conda/etc/profile.d/conda.sh' >> ~/.bashrc" && \
    su jupyter -c "echo 'conda activate base' >> ~/.bashrc"

USER jupyter
SHELL ["/bin/bash", "-i", "-c"]
RUN conda install -y jupyter

ADD deeplearning.yaml /tmp/deeplearning-template.yaml

FROM base AS stage-cpu
RUN sed -e "s/{tensorflow}/tensorflow/g" -e "s/{pytorch}/pytorch/g" /tmp/deeplearning-template.yaml > /tmp/deeplearning.yaml

FROM base AS stage-gpu
RUN sed -e "s/{tensorflow}/tensorflow-gpu/g" -e "s/{pytorch}/pytorch-gpu/g" /tmp/deeplearning-template.yaml > /tmp/deeplearning.yaml

FROM stage-$device as final

LABEL maintainer "Alexander Panin <justheuristic@gmail.com>, Dmitry Mittov <mittov@gmail.com>"

USER jupyter
SHELL ["/bin/bash", "-i", "-c"]

RUN conda env create -f /tmp/deeplearning.yaml && \
    conda activate deeplearning && \
    python -m ipykernel install --user --name python3 --display-name "DeepLearning Python 3"

EXPOSE 8888
VOLUME /notebooks
USER jupyter
WORKDIR /notebooks
ENV PATH /opt/conda/bin:$PATH

COPY run_jupyter.sh /
CMD ["/run_jupyter.sh"]
