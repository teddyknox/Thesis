#!/usr/bin/env python
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__name__)))

from playhouse.migrate import *
from peewee import *

db = SqliteDatabase('../data/images.db')

migrator = SqliteMigrator(db)

model_prediction = BooleanField(null=True)

with db.transaction():
    migrate(
        migrator.add_column('image', 'model_prediction', model_prediction),
    )
