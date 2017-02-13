# Docker machine

* Install Docker
* Build machine
* Run machine
* Write the code

## Install Docker
https://www.docker.com

## Build machine

$ docker build -t rl .

## Run 
$ docker run --rm -it -v <local_dir>:/notebooks -p <local_port>:8888 dl
examples:
$ docker run --rm -it -v /Users/mittov/Documents/shad/semester4/:/notebooks -p 8888:8888 dl

### Write the code
Copy the token from console and run
http://localhost:8888/?token=<token>
