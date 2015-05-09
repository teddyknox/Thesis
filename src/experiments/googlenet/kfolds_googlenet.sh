#!/bin/sh

# Quit on error code
set -e

cd $(dirname $0)
CAFFE_DIR=$HOME/caffe/build/tools
SCRIPTS_DIR=../../scripts

NUM_FOLDS=10

for FOLD in $(seq 1 $NUM_FOLDS); do
  FOLD_DIR=./folds/$FOLD
  mkdir -p $FOLD_DIR, $FOLD_DIR/snapshots
  rm -rf $FOLD_DIR/train_lmdb $FOLD_DIR/val_lmdb
  cp solver.prototxt $FOLD_DIR/solver.prototxt
  cp train_val.prototxt $FOLD_DIR/train_val.prototxt

  $SCRIPTS_DIR/write_manifests.py $FOLD $NUM_FOLDS $FOLD_DIR
  $CAFFE_DIR/convert_imageset --shuffle ../../images/ $FOLD_DIR/train.txt $FOLD_DIR/train_lmdb
  $CAFFE_DIR/convert_imageset --shuffle ../../images/ $FOLD_DIR/val.txt $FOLD_DIR/val_lmdb
  $CAFFE_DIR/caffe train --solver=$FOLD_DIR/solver.prototxt --gpu=0 --log_dir=$FOLD_DIR
  plot_training_log.py 0 $FOLD_DIR/test_accuracy_vs_iters.png $(./*.log)
  plot_training_log.py 2 $FOLD_DIR/test_loss_vs_iters.png $(./*.log)
  plot_training_log.py 4 $FOLD_DIR/train_lr_vs_iters.png $(./*.log)
  plot_training_log.py 6 $FOLD_DIR/train_loss_vs_iters.png $(./*.log)
  # $CAFFE_DIR/caffe test --model=$FOLD_DIR/train_val.prototxt --weights=googlenet_iter_116000.caffemodel --gpu=0 --log_dir=$FOLD_DIR
done
cd -



# produce ith fold data manifests
# run them through the lmdb generators
# render the experiment prototxt templates
# run experiment, making sure to log
# generate graphs, statistics
