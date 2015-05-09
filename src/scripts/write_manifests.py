#!/usr/bin/env python
import sys, os, inspect
APP_DIRNAME = os.path.abspath(os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe()))))
sys.path.append(APP_DIRNAME)

from models import Image
import random as r

r.seed(22165183631)

if __name__ == "__main__":
    assert len(sys.argv) == 4
    fold = int(sys.argv[1])
    num_folds = int(sys.argv[2])
    output_dir = sys.argv[3]
    assert os.path.isdir(output_dir)
    fold_size = float(1)/num_folds
    low = (fold - 1) * fold_size
    high = low + fold_size
    images = Image.select().where(Image.generation_method == "random" and Image.num_ratings > 0)
    train = []
    val = []
    for img in images:
        if low <= r.random() < high:
            val.append(img)
        else:
            train.append(img)
    with open(os.path.join(output_dir, "train.txt"), 'w') as f:
        for img in train:
            f.write("{}\n".format(img.filename))
    with open(os.path.join(output_dir, "val.txt"), 'w') as f:
        for img in val:
            f.write("{}\n".format(img.filename))
