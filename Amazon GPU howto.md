# How to set up GPU on EC2 instance

## Create EC2 instance

Use `p2.xlarge` instance type and `ami-e00a8180` AMI image. [Details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)

Open ports `22` (ssh) and `80` (http) on your freshly created instance, 
you create a [security group](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) 
and attach it your instance to get ports open

## Launch notebook

Instance you have created contains all you need: fresh versions of theano, lasagne, CUDA driver and cuDNN, 
just lunch ipython and get hands dirty:

```bash
$ sudo su
$ export THEANO_FLAGS='cuda.root=/usr/local/cuda,device=gpu,floatX=float32'
$ export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}
$ jupyter notebook
```

