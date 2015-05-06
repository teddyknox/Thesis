#!/usr/bin/env python
import sys, os
APP_DIRNAME = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print APP_DIRNAME
sys.path.append(APP_DIRNAME)

# from playhouse.migrate import *
from peewee import *
from models import Image
from collections import Counter

db = SqliteDatabase(os.path.join(APP_DIRNAME, '/data/images.db'))

priors = Counter(image.score != 0 for image in Image.select())
total = priors[True] + priors[False]
print "Pretty: {}".format(float(priors[True])/total)
print "Ugly: {}".format(float(priors[False])/total)
print total, priors
