FROM andrewosh/binder-base
MAINTAINER Alexander Panin <justheuristic@gmail.com>
USER root

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list
RUN apt-get -qq update
# W: GPG error: http://archive.ubuntu.com trusty-backports InRelease:
# The following signatures couldn't be verified because the public key is not available

RUN apt-get install -y gcc-4.9 g++-4.9 libstdc++6 wget unzip
RUN apt-get install -y libopenblas-dev liblapack-dev libsdl2-dev libboost-all-dev graphviz
RUN apt-get install -y cmake zlib1g-dev libjpeg-dev 
RUN apt-get install -y xvfb libav-tools xorg-dev python-opengl python3-opengl
RUN apt-get -y install swig3.0
RUN ln -s /usr/bin/swig3.0 /usr/bin/swig


USER main
RUN pip install --upgrade pip==9.0.3
RUN pip install --upgrade --ignore-installed setuptools  #fix https://github.com/tensorflow/tensorflow/issues/622
RUN pip install --upgrade sklearn tqdm nltk editdistance joblib graphviz

# install all gym stuff except mujoco - it fails at "import importlib.util" (no module named util)
RUN pip install --upgrade gym
RUN pip install --upgrade gym[atari]
RUN pip install --upgrade gym[box2d]

RUN pip install --upgrade http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp27-cp27mu-linux_x86_64.whl 
RUN pip install --upgrade torchvision 
RUN pip install --upgrade keras
RUN pip install --upgrade https://github.com/Theano/Theano/archive/master.zip
RUN pip install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip
RUN pip install --upgrade https://github.com/yandexdataschool/AgentNet/archive/master.zip
RUN pip install gym_pull
RUN pip install ppaquette-gym-doom

# BUILD ERROR:
# Could not build doom-py: Command '['make', '-j', '3']' returned non-zero exit
# status 2. (HINT: are you sure cmake is installed? You might also be missing a
# library. Try running 'apt-get install -y python-numpy cmake zlib1g-dev libjpeg-dev
# libboost-all-dev gcc libsdl2-dev wget unzip'


RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade pip==9.0.3

# fix https://github.com/tensorflow/tensorflow/issues/622
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade --ignore-installed setuptools

# python3: fix `GLIBCXX_3.4.20' not found - conda's libgcc blocked system's gcc-4.9 and libstdc++6
RUN bash -c "conda update -y conda && source activate python3 && conda uninstall -y libgcc && source deactivate"
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade matplotlib numpy scipy pandas graphviz

RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade sklearn tqdm nltk editdistance joblib
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade --ignore-installed setuptools  #fix https://github.com/tensorflow/tensorflow/issues/622

# install all gym stuff except mujoco - it fails at "mjmodel.h: no such file or directory"
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade gym
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade gym[atari]
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade gym[box2d]



RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl 
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade torchvision
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade keras
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade https://github.com/Theano/Theano/archive/master.zip
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade https://github.com/yandexdataschool/AgentNet/archive/master.zip

#install TF after everything else not to break python3's pyglet with python2's tensorflow
RUN pip install --upgrade tensorflow==1.4.0
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade tensorflow==1.4.0
#TODO py3 doom once it's no longer broken
