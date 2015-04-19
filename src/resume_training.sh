#!/usr/bin/env sh

/home/teddy/caffe/build/tools/caffe train \
    --solver=./model/solver.prototxt \
    --snapshot=./model/bvlc_googlenet_cae_iter_4000.solverstate \
    --gpu=0
