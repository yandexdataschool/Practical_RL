**Warning: this guide has not been updated since we migrated away from Theano/Lasagne, which happened a long time ago.**

# How to set up an Amazon EC2 GPU instance

## Create an instance

Use `p2.xlarge` instance type and `ami-e00a8180` AMI image. [Details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)

Open ports `22` (ssh) and `80` (http) on your freshly created instance, then create a [security group](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) and attach it to your instance to get the ports open.

## Launch notebook

The instance you have created contains all you need: fresh versions of theano, lasagne, CUDA driver and cuDNN,
just launch Jupyter and get your hands dirty:

```bash
$ sudo su
$ export THEANO_FLAGS='cuda.root=/usr/local/cuda,device=gpu,floatX=float32'
$ export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}
$ jupyter notebook
```
