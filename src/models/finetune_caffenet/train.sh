#!/usr/bin/env sh

CAFFE=/home/teddy/caffe
$CAFFE/build/tools/caffe train -solver solver.prototxt -weights bvlc_reference_caffenet.caffemodel -gpu 0
