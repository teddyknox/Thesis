from peewee import *

db = SqliteDatabase('data/images.db')


class Image(Model):
    filename = CharField(unique=True)
    score = FloatField(default=0.0)
    num_ratings = IntegerField(default=0)

    class Meta:
        database = db
