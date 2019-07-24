FROM python:3.7-slim
# install the notebook package
RUN pip install --no-cache --upgrade pip && \
    pip install --no-cache notebook

RUN apt-get -qq update
# RUN apt-get install -y gcc-4.9 g++-4.9 libstdc++6 wget unzip
RUN apt-get install -y gcc g++ libstdc++6 wget curl unzip git
RUN apt-get install -y libopenblas-dev liblapack-dev libsdl2-dev libboost-all-dev graphviz
RUN apt-get install -y cmake zlib1g-dev libjpeg-dev 
RUN apt-get install -y xvfb ffmpeg xorg-dev python-opengl python3-opengl
RUN apt-get -y install swig3.0
RUN ln -s /usr/bin/swig3.0 /usr/bin/swig

RUN pip install --upgrade pip==9.0.3
RUN pip install --upgrade --ignore-installed setuptools  #fix https://github.com/tensorflow/tensorflow/issues/622
RUN pip install --upgrade sklearn tqdm nltk editdistance joblib graphviz pandas matplotlib

# install all gym stuff except mujoco - it fails at "import importlib.util" (no module named util)
RUN pip install --upgrade gym
RUN pip install --upgrade gym[atari]
RUN pip install --upgrade gym[box2d]

RUN pip install --upgrade https://download.pytorch.org/whl/cpu/torch-1.0.1.post2-cp37-cp37m-linux_x86_64.whl
RUN pip install --upgrade torchvision 
RUN pip install --upgrade keras
RUN pip install --upgrade https://github.com/Theano/Theano/archive/master.zip
RUN pip install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip
RUN pip install --upgrade https://github.com/yandexdataschool/AgentNet/archive/master.zip
RUN pip install gym_pull
# RUN pip install ppaquette-gym-doom

# create user with a home directory
ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
WORKDIR ${HOME}
USER ${USER}

RUN cd ${HOME} && git clone https://github.com/yandexdataschool/Practical_RL
