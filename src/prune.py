#!/usr/bin/env python

from models import Image
import os

APP_DIRNAME = os.path.abspath(os.path.dirname(__file__))

for image in Image.select():
    exists = os.path.isfile(APP_DIRNAME + '/images/' + image.filename)
    print exists
