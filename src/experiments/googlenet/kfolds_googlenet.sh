#!/bin/sh

# Quit on error code
set -e

EXPERIMENT_DIR=$(dirname $0)
pushd $EXPERIMENT_DIR
CAFFE_DIR=$HOME/caffe/build/tools
SCRIPTS_DIR=$(readlink -f ../../scripts)
IMAGES_DIR=$(readlink -f ../../images)/

NUM_FOLDS=10

for FOLD in $(seq 1 $NUM_FOLDS); do
  FOLD_DIR=./folds/$FOLD
  # rm -rf $FOLD_DIR/train_lmdb $FOLD_DIR/val_lmdb $FOLD_DIR/logs $FOLD_DIR/snapshots
  # mkdir -p $FOLD_DIR $FOLD_DIR/snapshots $FOLD_DIR/logs
  pushd $FOLD_DIR
  # $SCRIPTS_DIR/write_manifests.py $FOLD $NUM_FOLDS .
  # $CAFFE_DIR/convert_imageset --shuffle $IMAGES_DIR train.txt train_lmdb
  # $CAFFE_DIR/convert_imageset --shuffle $IMAGES_DIR val.txt val_lmdb
  # $CAFFE_DIR/caffe train --solver=../../solver.prototxt --gpu=0 --log_dir=logs
  WEIGHTS=$(ls snapshots/* | grep caffemodel | sort -r | head -n 1)
  $CAFFE_DIR/caffe test --model=../../train_val.prototxt --weights=$WEIGHTS --gpu=0 --log_dir=logs
  # LOGFILE=$(ls -t logs/* | grep .log.INFO | head -n 1)
  # cp $LOGFILE logs/train.log
  # $EXPERIMENT_DIR/plot_training_log.py 0 test_accuracy_vs_iters.png logs/train.log
  # $EXPERIMENT_DIR/plot_training_log.py 2 test_loss_vs_iters.png logs/train.log
  # $EXPERIMENT_DIR/plot_training_log.py 4 train_lr_vs_iters.png logs/train.log
  # $EXPERIMENT_DIR/plot_training_log.py 6 train_loss_vs_iters.png logs/train.log
  popd
  break  
done
popd



# produce ith fold data manifests
# run them through the lmdb generators
# render the experiment prototxt templates
# run experiment, making sure to log
# generate graphs, statistics
