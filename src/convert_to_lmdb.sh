#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs

echo "Creating train lmdb..."
HERE=$(pwd)
TOOLS=/home/teddy/caffe/build/tools
echo $HERE
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --shuffle \
    $HERE/images/ \
    $HERE/train.txt \
    $HERE/train_lmdb

echo "Creating val lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --shuffle \
    $HERE/images/ \
    $HERE/val.txt \
    $HERE/val_lmdb

echo "Done."
