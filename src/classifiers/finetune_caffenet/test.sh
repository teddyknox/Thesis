#!/usr/bin/env sh

/home/teddy/caffe/build/tools/caffe test \
	--model train_val.prototxt \
	--weights finetune_caffenet_iter_30000.caffemodel \
	--gpu 0 \
	--iterations=800 \
