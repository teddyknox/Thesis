#!/usr/bin/env python
from models import Image, db
import peewee

with open('manifest.txt', 'r') as manifest:
    for record in manifest:
        filename, rating = record.split()
        image = Image.create(filename=filename, score=rating, num_ratings=1)
