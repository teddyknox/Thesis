#!/usr/bin/env python
import sys, os, inspect
APP_DIRNAME = os.path.abspath(os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe()))))
print APP_DIRNAME
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
    priors = [0, 0]
    for img in images:
        score = int(bool(img.score))
        priors[score] += 1
        place = val if low <= r.random() < high else train
        place.append((img.filename, score))
    with open(os.path.join(output_dir, "train.txt"), 'w') as f:
        for filename, score in train:
            f.write("{}\t{}\n".format(filename, score))
    with open(os.path.join(output_dir, "val.txt"), 'w') as f:
        for filename, score in val:
            f.write("{}\t{}\n".format(filename, score))
    with open(os.path.join(output_dir, "priors.txt"), 'w') as f:
        neg_priors = float(priors[0])/sum(priors)
        pos_priors = float(priors[1])/sum(priors)
        f.write("num neg: {}\nfrac neg:{.2f}\nnum pos: {}\nfrac pos: {.2f}\n".format(priors[0], neg_priors, priors[1], pos_priors))
