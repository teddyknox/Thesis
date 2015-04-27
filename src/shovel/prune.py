#!/usr/bin/env python
import sys, os
sys.path.append(os.path.dirname(__name__))
from shovel import task

@task
def prune():
    from models import Image
    import os
    APP_DIRNAME = os.path.abspath(os.path.dirname(__file__))
    for image in Image.select():
        exists = os.path.isfile(APP_DIRNAME + '/images/' + image.filename)
        if not exists:
            image.delete()
