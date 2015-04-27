#!/usr/bin/env python
import sys, os
sys.path.append(os.path.dirname(__name__))

from playhouse.migrate import *
from peewee import *
from models import Image

APP_DIRNAME = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

db = SqliteDatabase(os.path.join(APP_DIRNAME, '/data/images.db'))

for image in Image.select():
    if image.generation_method == "score":
        image.generation_method = "scored"
        image.save()
    exists = os.path.isfile(APP_DIRNAME + '/data/images/' + image.filename)        
    if not exists:
        image.delete()

# def export_to_manifest():
#     from random import random
#     from models import Image
#     val_fraction = 0.25
#     with open('data/train.txt', 'w') as train, open('data/val.txt', 'w') as val:
#         images = Image.select()
#         for image in images:
#             line = "/{}\t{}\n".format(image.filename,int(round(image.score)))
#             if random() > val_fraction:
#                 train.write(line)
#             else:
#                 val.write(line)


# def import_from_manifest():
#     from models import Image
#     with open('data/manifest.txt', 'r') as manifest:
#         for record in manifest:
#             filename, rating = record.split()
#             image = Image.create(filename=filename, score=rating, num_ratings=1)


#
# def setup_tables():
#     from models import Image
#     db.connect()
#     db.create_tables([Image])
