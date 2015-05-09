from peewee import *
from generators import *
import os, inspect

APP_DIRNAME = os.path.dirname(inspect.getfile(inspect.currentframe()))
MAX_IMAGES = 2000
MAX_RATINGS = 3

db = SqliteDatabase(os.path.join(APP_DIRNAME, 'images.db'))


class Image(Model):
    filename = CharField(unique=True)
    score = FloatField(default=0.0)
    num_ratings = IntegerField(default=0)
    model_score = FloatField(null=True) # log prob that image is pretty
    model_prediction = BooleanField(null=True) # whether P(pretty) > P(ugly)
    generation_method = CharField(default="random")

    class Meta:
        database = db

    @classmethod
    def get_random(self, recycle=True):
        num_images = Image.select(fn.Count(Image.id)).scalar()
        if num_images < MAX_IMAGES or not recycle:
            filename = generate_image()
            img = Image.create(filename=filename, generation_method='scored')
        else:
            img = Image.select().order_by(Image.num_ratings, fn.Random()).limit(1)[0]
        return img

    @classmethod
    def get_scored(self):
        filename, score = generate_pretty_image()
        img = Image.create(filename=filename, model_score=score, generation_method='scored', model_prediction=True)
        return img
