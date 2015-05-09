#!/usr/bin/env python
import sys, os, inspect
APP_DIRNAME = os.path.abspath(os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe()))))
sys.path.append(APP_DIRNAME)

from playhouse.migrate import *
from peewee import *

db = SqliteDatabase('../data/images.db')

migrator = SqliteMigrator(db)

model_prediction = BooleanField(null=True)

with db.transaction():
    migrate(
        migrator.add_column('image', 'model_prediction', model_prediction),
    )
