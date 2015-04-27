import sys, os
sys.path.append(os.path.dirname(__name__))
from shovel import task

from playhouse.migrate import *
from peewee import *

db = SqliteDatabase('data/images.db')


@task
def migration_1():

    migrator = SqliteMigrator(db)

    model_score = FloatField(null=True)
    generation_method = CharField(default="random")

    with db.transaction():
        migrate(
            migrator.add_column('image', 'model_score', model_score),
            migrator.add_column('image', 'generation_method', generation_method)
        )


@task
def export_to_manifest():
    from random import random
    from models import Image
    val_fraction = 0.25
    with open('data/train.txt', 'w') as train, open('data/val.txt', 'w') as val:
        images = Image.select()
        for image in images:
            line = "/{}\t{}\n".format(image.filename,int(round(image.score)))
            if random() > val_fraction:
                train.write(line)
            else:
                val.write(line)


# @task
# def import_from_manifest():
#     from models import Image
#     with open('data/manifest.txt', 'r') as manifest:
#         for record in manifest:
#             filename, rating = record.split()
#             image = Image.create(filename=filename, score=rating, num_ratings=1)


# @task
# def prune():
#     from models import Image
#     APP_DIRNAME = os.path.abspath(os.path.dirname(__file__))
#     for image in Image.select():
#         exists = os.path.isfile(APP_DIRNAME + '/images/' + image.filename)
#         if not exists:
#             image.delete()


@task
def setup_tables():
    from models import Image
    db.connect()
    db.create_tables([Image])
