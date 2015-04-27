from peewee import *

db = SqliteDatabase('data/images.db')


class Image(Model):
    filename = CharField(unique=True)
    score = FloatField(default=0.0)
    num_ratings = IntegerField(default=0)
    model_score = FloatField(null=True)
    generation_method = CharField(default="random")

    class Meta:
        database = db
