#!/usr/bin/env sh

CAFFE=/home/teddy/caffe
$CAFFE/build/tools/caffe train -solver models/finetune_flickr_style/solver.prototxt -weights models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel -gpu 0
