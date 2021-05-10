# Research project - Docker

This is a simple tutorial, where the basics of Docker will be introduced to you. 

In this tutorial, you will create a small app that 

## What is Docker?
[Docker](https://www.docker.com/) is an open-source tool which provides virtualization on OS level. It uses reusable *containers* to make it more convenient to qucikly and consistently deploy and run applications.

A container isolates the app that it hosts from the operating system, shipping it with a separate libraries and other dependencies. In this sense, containers are like virtual machines, but they are lighter - they do not need to emulate the whole operating system, just the essentials. An *image*, on the other hand, provides a custom file system for the container. It also stores all dependencies, configuration, scripts and other metadata. Docker creates an image by reading data from the `Dockerfile`, which is a text file containing instructions in a specific format and order.


## Install and get started with Docker

Follow [these instructions](https://docs.docker.com/engine/install/) to install Docker appropriate for your machine.

To get acquianted with Docker, run:

```
sudo docker run hello-world
```
This command downloads the `hello-world` image from Docker's servers and runs it in a container. This example is pretty simple, it just prints a message.

Run `sudo docker images` to see what images are stored on your computer. 


## Create your own image

Crete an empty text file and call it `Dockerfile`.

`Dockerfile` follows a simple format: `INSTRUCTION arguments` and it must begin with `FROM`, which specifies the base image of your new image. We will use the latest version of the Ubuntu image.

```
FROM ubuntu:latest
```

Now, add 

Run `docker build -t testimage:1.0 -f [/path/to/Dockerfile]` to build the image. The image has now the name `testimage` and tag (version) `1.0`.

## Configure AWS

## Deploy your image to AWS