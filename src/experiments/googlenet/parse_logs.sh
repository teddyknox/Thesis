#!/bin/bash
set -e
rm -f folds/**/logs/*.train
rm -f folds/**/logs/*.test
for i in $(seq 1 1 10); do
  cd folds/$i/logs
  ../../../parse_log.sh $(readlink caffe.INFO)
  cd ../../..
done
