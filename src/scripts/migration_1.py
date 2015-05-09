#!/usr/bin/env python
import sys, os, inspect
APP_DIRNAME = os.path.abspath(os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe()))))
sys.path.append(APP_DIRNAME)

from playhouse.migrate import *
from peewee import *

db = SqliteDatabase('../data/images.db')

migrator = SqliteMigrator(db)

model_score = FloatField(null=True)
generation_method = CharField(default="random")

with db.transaction():
    migrate(
        migrator.add_column('image', 'model_score', model_score),
        migrator.add_column('image', 'generation_method', generation_method)
    )


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


# def prune():
#     from models import Image
#     APP_DIRNAME = os.path.abspath(os.path.dirname(__file__))
#     for image in Image.select():
#         exists = os.path.isfile(APP_DIRNAME + '/images/' + image.filename)
#         if not exists:
#             image.delete()

#
# def setup_tables():
#     from models import Image
#     db.connect()
#     db.create_tables([Image])
