#!/bin/sh

# render a template configuration file
# expand variables + preserve formatting
render_template() {
  eval "echo \"$(cat $1)\""
}

CAFFE_DIR=$HOME/caffe/build/tools
SCRIPTS_DIR=../../scripts

NUM_FOLDS=10

for FOLD in $(seq 1 $NUM_FOLDS); do
  FOLD_DIR=./folds/$FOLD
  mkdir -p $FOLD_DIR
  $SCRIPTS_DIR/write_manifests.py $FOLD $NUM_FOLDS $FOLD_DIR
  $CAFFE_DIR/convert_imageset --shuffle ../images $FOLD_DIR/train.txt $FOLD_DIR/train_lmdb
  $CAFFE_DIR/convert_imageset --shuffle ../images $FOLD_DIR/val.txt $FOLD_DIR/val_lmdb
  # we may not need templating
  render_template solver.prototxt.template > $FOLD_DIR/solver.prototxt
  render_template train_val.prototxt.template > $FOLD_DIR/train_val.prototxt
  break
  $CAFFE_DIR/caffe train --solver=./solver.prototxt --gpu=0
done



# produce ith fold data manifests
# run them through the lmdb generators
# render the experiment prototxt templates
# run experiment, making sure to log
# generate graphs, statistics
