#!/usr/bin/env python
import sys, os
sys.path.append(os.path.dirname(__name__))

import peewee
from random import random
from models import Image


val_fraction = 0.25

with open('../data/train.txt', 'w') as train, open('../data/val.txt', 'w') as val:
    images = Image.select()
    for image in images:
        line = "/{}\t{}\n".format(image.filename,int(round(image.score)))
        if random() > val_fraction:
            train.write(line)
        else:
            val.write(line)
