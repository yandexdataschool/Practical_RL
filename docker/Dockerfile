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

ADD deeplearning.yaml /tmp/deeplearning.yaml
USER jupyter
SHELL ["/bin/bash", "-i", "-c"]

RUN conda install -y jupyter

RUN conda env create -f /tmp/deeplearning.yaml && \
    conda activate deeplearning && \
    python -m ipykernel install --user --name python3 --display-name "Deeplearning Python 3"

EXPOSE 8888
VOLUME /notebooks
USER jupyter
WORKDIR /notebooks
ENV PATH /opt/conda/bin:$PATH

COPY run_jupyter.sh /
CMD ["/run_jupyter.sh"]
