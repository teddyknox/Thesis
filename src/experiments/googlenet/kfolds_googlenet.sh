#!/bin/sh

# Quit on error code
set -e

pushd $(dirname $0)
CAFFE_DIR=$HOME/caffe/build/tools
SCRIPTS_DIR=$(readlink -f ../../scripts)
IMAGES_DIR=$(readlink -f ../../images)/

NUM_FOLDS=10

for FOLD in $(seq 1 $NUM_FOLDS); do
  FOLD_DIR=./folds/$FOLD
  mkdir -p $FOLD_DIR $FOLD_DIR/snapshots $FOLD_DIR/logs
  pushd $FOLD_DIR
  rm -rf train_lmdb val_lmdb
  $SCRIPTS_DIR/write_manifests.py $FOLD $NUM_FOLDS .
  $CAFFE_DIR/convert_imageset --shuffle $IMAGES_DIR train.txt train_lmdb
  $CAFFE_DIR/convert_imageset --shuffle $IMAGES_DIR val.txt val_lmdb
  $CAFFE_DIR/caffe train --solver=../../solver.prototxt --gpu=0 --log_dir=logs
  logfile=$(ls -t logs | grep .log.INFO | head -n 1)
  mv logs/$logfile logs/train.log
  plot_training_log.py 0 test_accuracy_vs_iters.png logs/train.log
  plot_training_log.py 2 test_loss_vs_iters.png logs/train.log
  plot_training_log.py 4 train_lr_vs_iters.png logs/train.log
  plot_training_log.py 6 train_loss_vs_iters.png logs/train.log
  popd
  # $CAFFE_DIR/caffe test --model=$FOLD_DIR/train_val.prototxt --weights=googlenet_iter_116000.caffemodel --gpu=0 --log_dir=$FOLD_DIR
done
popd



# produce ith fold data manifests
# run them through the lmdb generators
# render the experiment prototxt templates
# run experiment, making sure to log
# generate graphs, statistics
