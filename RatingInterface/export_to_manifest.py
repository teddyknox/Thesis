#!/usr/bin/env python
from models import Image
import peewee

with open('manifest.txt', 'w') as manifest:
    # ratings = Rating.select().join(Image).order_by(Image.filename.desc())
    images = Image.select()
    for image in images:
        manifest.write("{}\t{:.2f}\n".format(image.filename,image.score))
