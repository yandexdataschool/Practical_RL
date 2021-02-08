To simplify installation process, you can deploy a container (~virtual machine) with all dependencies pre-installed.

_tl;dr [dockerhub url](https://hub.docker.com/r/justheuristic/practical_rl/)_

## Install Docker

We recommend you to use either native docker (recommended for linux) or kitematic(recommended for windows).
* Installing [kitematic](https://kitematic.com/), a simple interface to docker (all platforms)
* Pure docker: Guide for [windows](https://docs.docker.com/docker-for-windows/), [linux](https://docs.docker.com/engine/installation/), or [macOS](https://docs.docker.com/docker-for-mac/).
* If you want to use your GPU make sure you have [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) and [NVidia driver](https://www.nvidia.com/en-us/drivers/unix/) + [CUDA 10.2](https://developer.nvidia.com/cuda-downloads) installed

Below are the instructions for both approaches.

## Kitematic
Find dmittov/practical_rl in the search menu. Download and launch the container.

Click on "web preview" screen in the top-right __or__ go to settings, ports and find at which port your jupyter is located, usually 32***.

## Native
`docker run --rm -it -v /path/to/your/repo:/notebooks -p <local_port>:8888 dmittov/practical_rl:spring2020-cpu`

For example,
```docker run --rm -it -v /home/myuser/Documents/practical_rl:/notebooks -p 8888:8888 dmittov/practical_rl:spring2020-cpu```


Then you can access your jupyter in a browser at `localhost:<local_port>/?token=<token_you_see_in_container_logs>`, e.g. `localhost:8888/?token=ad1a5a0aab43efb47a9a805388fcf508d0b5f84a16e4542b&token=ad1a5a0aab43efb47a9a805388fcf508d0b5f84a16e4542b`

#### GPU
`docker run --rm -it -v /path/to/your/repo:/notebooks -p <local_port>:8888 --gpus all dmittov/practical_rl:spring2020-cuda-10.2`

## Manual
Build container

`docker build -t practical_rl --build-arg device=cpu .`

to build GPU version

`docker build -t practical_rl --build-arg device=gpu .`

Run it

`$ docker run --rm -it -v <local_dir>:/notebooks -p <local_port>:8888 practical_rl`

to run GPU version

`$ docker run --rm -it -v <local_dir>:/notebooks -p <local_port>:8888 --gpus all practical_rl`

examples:

```$ docker run --rm -it -v `pwd`:/notebooks -p 8888:8888 practical_rl```

Copy the token from console and run
http://localhost:8888/?token=<token>
