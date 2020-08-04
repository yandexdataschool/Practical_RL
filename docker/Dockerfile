ARG device
ARG username="jovyan"

FROM ubuntu:18.04 AS base-cpu

FROM nvidia/cuda:10.2-base-ubuntu18.04 AS base-gpu

FROM base-$device AS base

ARG username
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq update && \
    apt-get install -y wget unzip git cmake xvfb sudo freeglut3-dev ffmpeg

RUN adduser --disabled-password --gecos "Default user" $username && \
    adduser $username sudo && \
    echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    mkdir /notebooks && \
    chown -R $username /notebooks

RUN su $username -c \
    "wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh \
        -O /tmp/anaconda3.sh" && \
    mkdir -p /opt/conda && \
    chown -R $username /opt/conda && \
    su $username -c "/bin/bash /tmp/anaconda3.sh -b -p /opt/conda -u" && \
    rm /tmp/anaconda3.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    su $username -c "echo '. /opt/conda/etc/profile.d/conda.sh' >> ~/.bashrc" && \
    su $username -c "echo 'conda activate base' >> ~/.bashrc"

ADD deeplearning.yaml /tmp/deeplearning-template.yaml

USER $username
SHELL ["/bin/bash", "-i", "-c"]
RUN conda install -y jupyter

FROM base AS stage-cpu
RUN sed -e "s/{tensorflow}/tensorflow/g" -e "s/{pytorch}/pytorch/g" /tmp/deeplearning-template.yaml > /tmp/deeplearning.yaml

FROM base AS stage-gpu
RUN sed -e "s/{tensorflow}/tensorflow-gpu/g" -e "s/{pytorch}/pytorch-gpu/g" /tmp/deeplearning-template.yaml > /tmp/deeplearning.yaml

FROM stage-$device as final

LABEL maintainer "Alexander Panin <justheuristic@gmail.com>, Dmitry Mittov <mittov@gmail.com>"

ARG username
USER $username
SHELL ["/bin/bash", "-i", "-c"]

RUN conda env create -f /tmp/deeplearning.yaml && \
    conda activate deeplearning && \
    python -m ipykernel install --user --name python3 --display-name "Python 3"

RUN sudo rm /tmp/deeplearning*.yaml

EXPOSE 8888
VOLUME /notebooks
WORKDIR /notebooks
ENV PATH /opt/conda/bin:$PATH

COPY run_jupyter.sh /
CMD ["/run_jupyter.sh"]
