#!/usr/bin/env python
import sys, os, inspect
APP_DIRNAME = os.path.abspath(os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe()))))
sys.path.append(APP_DIRNAME)

from models import Image

def avg(data):
    float(sum(data))/len(data)

def stddev(data):
    mu = avg(data)
    return sum([(d - mu)**2 for d in data])/float(len(data)-1)

ratings = {}
for img in Image.select().where(Image.generation_method == "random" and Image.num_ratings > 1):
    ratings[img.score] += 1

print ratings
