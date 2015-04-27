#!/usr/bin/env python
import sys, os
sys.path.append(os.path.dirname(__name__))
from shovel import task

@task
def import_from_manifest():
    from models import Image, db
    import peewee
    with open('../data/manifest.txt', 'r') as manifest:
        for record in manifest:
            filename, rating = record.split()
            image = Image.create(filename=filename, score=rating, num_ratings=1)
