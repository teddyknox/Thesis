#!/usr/bin/env sh

/home/teddy/caffe/build/tools/caffe test \
	--model ./train_val.prototxt \
	--weights ./bvlc_googlenet_cae_iter_116000.caffemodel \
	--gpu 0 \
	--iterations=2000
