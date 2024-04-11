#!/bin/bash

mkdir home

PATHIN="$(pwd)/home"

#Channel of the localhost browser where to show the jupyterlab session
CHANNEL=8888

docker run --rm --gpus all\
           -p $CHANNEL:8888 \
           --name single_cell_analysis \
           --mount type=bind,source=$PATHIN,destination=/home/jovyan \
           -e JUPYTER_ENABLE_LAB=yes \
           --runtime=nvidia \
           --device=/dev/nvidia-uvm \
           --device=/dev/nvidia-uvm-tools \
           --device=/dev/nvidia-modeset \
           --device=/dev/nvidiactl \
           --device=/dev/nvidia0 \
           dsblab/single_cell_analysis:0.8