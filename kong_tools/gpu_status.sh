#!/bin/sh

a=pwd
cd /home/y/yx277/research/kong_tools
python gpu_status.py
cat NodeGpuStatus.out
cd $a