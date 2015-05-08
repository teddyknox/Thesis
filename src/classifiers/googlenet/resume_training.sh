#!/usr/bin/env sh

/home/teddy/caffe/build/tools/caffe train \
    --solver=./solver.prototxt \
    --snapshot=./bvlc_googlenet_cae_iter_162000.solverstate \
    --gpu=0
