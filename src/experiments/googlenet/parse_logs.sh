#!/bin/bash

rm folds/**/logs/*.train
rm folds/**/logs/*.test
for i in $(seq 1 1 10); do
  pushd folds/$i/logs
  echo $(readlink caffe.INFO | tail -n 1)
  popd
done
