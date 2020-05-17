FROM ubuntu:20.04
LABEL maintainer "Alexander Panin <justheuristic@gmail.com>, Dmitry Mittov <mittov@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq update && \
    apt-get install -y wget unzip git cmake xvfb sudo freeglut3-dev ffmpeg

RUN adduser --disabled-password --gecos "Default user" jupyter && \
    adduser jupyter sudo && \
    echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

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

ADD tensorflow-1.13.yaml /tmp/tensorflow-1.13.yaml
ADD pytorch.yaml /tmp/pytorch.yaml
USER jupyter
SHELL ["/bin/bash", "-i", "-c"]

RUN conda install -y jupyter

RUN conda env create -f /tmp/tensorflow-1.13.yaml && \
    conda activate tensorflow-1.13 && \
    python -m ipykernel install --user --name tensorflow-1.13 --display-name "Tensorflow 1.13"

RUN conda env create -f /tmp/pytorch.yaml && \
    conda activate pytorch && \
    python -m ipykernel install --user --name pytorch --display-name "Pytorch"

EXPOSE 8888
VOLUME /notebooks
USER jupyter
WORKDIR /notebooks
ENV PATH /opt/conda/bin:$PATH

COPY run_jupyter.sh /
CMD ["/run_jupyter.sh"]
