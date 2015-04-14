#!/usr/bin/env python
from models import Image
import peewee
from random import random

val_fraction = 0.25

with open('train.txt', 'w') as train, open('val.txt', 'w') as val:
    # ratings = Rating.select().join(Image).order_by(Image.filename.desc())
    images = Image.select()
    for image in images:
        line = "/{}\t{:.2f}\n".format(image.filename,image.score)
        if random() > val_fraction:
            train.write(line)
        else:
            val.write(line)
