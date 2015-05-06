#!/usr/bin/env python
import sys, os
APP_DIRNAME = os.path.dirname(os.path.dirname(__name__))
sys.path.append(APP_DIRNAME)

from models import Image
from classifier import classifier, caffe
from app import IMAGES_DIR
from peewee import *

db = SqliteDatabase(os.path.join(APP_DIRNAME, '/data/images.db'))

# BATCH_SIZE = 32
#
# to_score = []
# for image in Image.select().where(Image.model_score == None or Image.model_prediction == None):
#     exists = os.path.isfile(APP_DIRNAME + '/data/images/' + image.filename)
#     if exists:
#         to_score.append(image)
#     else:
#         image.delete()
#
# for i in range(0, len(to_score), BATCH_SIZE):
#     batch = to_score[i:i+BATCH_SIZE]
#     images = [caffe.io.load_image(os.path.join(IMAGES_DIR, image.filename))
#                 for image in batch]
#     results = classifier.predict(images)
#     for x in range(results.shape[0]):
#         scores = results[x]
#         batch[x].model_prediction = scores[1] > scores[0]
#         batch[x].model_score = scores[1]
#         batch[x].save()

correct = 0
false_positive = 0
false_negative = 0
with open(APP_DIRNAME + '/data/val.txt', 'r') as f:
    for row in f:
        filename, rating = row.split()
        filename = filename[1:]
        image = Image.select().where(Image.filename == filename)
# for image in Image.select().where(Image.num_ratings > 0):
        if image.model_prediction and image.score > 0 or \
            not image.model_prediction and image.score == 0:
            correct += 1
        elif image.model_prediction and image.score == 0:
            false_positive += 1
        else:
            false_negative += 1
print correct, false_positive, false_negative
