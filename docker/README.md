# EnviRe Dockerfile

## Install Docker

For Ubuntu:

    sudo apt-get install docker.io

## Build Image

Note: The average user does not have to build an image. Usually the image will
be distributed to the users.

    docker build -t envire:latest .

Sometimes it is necessary to clean the docker cache if you want to rebuild the
image. You just have to add `--no-cache` in this case.

## Pulling the Image

A prebuild docker image for EnviRe is available at
[af01/envire](https://hub.docker.com/r/af01/envire/). You can pull it with

    docker pull af01/envire

## Create Container

Without GUI:

    docker run -it af01/envire:latest

With GUI:

    xhost local:root
    docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix --privileged af01/envire:latest

Additionally, you can mount external directories in the container. This can
be useful because you might want to destroy and recreate containers from time
to time. It can be done with the option

    -v <host-directory>:<mount-point>

You can give containers names that can be used like their IDs:

    --name <name>

## Setup GPU

You usually have to set up your GPU if you use the EnviRe visualizer. For
example, to make an Nvidia GPU available in the docker container, the following
steps have to be taken:

On the host, check your driver version:

    # you might have to install this package:
    $ sudo apt-get install mesa-utils
    $ glxinfo |grep "OpenGL version"
    OpenGL version string: 4.5.0 NVIDIA 375.39

In this example, the driver version is "375.39". Now, you have install exactly
the same driver in the container:

    export VERSION=375.39
    wget http://us.download.nvidia.com/XFree86/Linux-x86_64/$VERSION/NVIDIA-Linux-x86_64-$VERSION.run
    chmod +x NVIDIA-Linux-x86_64-$VERSION.run
    apt-get install -y module-init-tools
    ./NVIDIA-Linux-x86_64-$VERSION.run -a -N --ui=none --no-kernel-module

## Working with Docker

Overview of containers:

    docker ps -a

Start container:

    docker start <id>

Connect to container:

    docker attach <id>

Typing the first 2-3 characters of the container ID is usually sufficient.
