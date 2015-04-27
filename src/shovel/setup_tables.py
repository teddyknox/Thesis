#!/usr/bin/env python
import sys, os
sys.path.append(os.path.dirname(__name__))
from shovel import task

@task
def setup_tables():
    from peewee import *
    from models import *

    db.connect()
    db.create_tables([Image])
