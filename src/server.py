from flask import render_template, send_file, request, abort, send_from_directory, url_for, Flask, Response
from PIL import Image, ImageDraw
import uuid
import os
from random import randint, uniform
from colorsys import hls_to_rgb
from models import Image as DBImage
from peewee import fn
import optparse
import logging
import caffe
import generators

MAX_IMAGES = 2000
MAX_RATINGS = 3
APP_DIRNAME = os.path.abspath(os.path.dirname(__file__))
MODEL_DEF_FILE = '{}/models/googlenet/deploy.prototxt'.format(APP_DIRNAME)
PRETRAINED_MODEL_FILE = '{}/models/googlenet/bvlc_googlenet_cae_iter_116000.caffemodel'.format(APP_DIRNAME)
GPU_MODE = os.environ.get('GPU_MODE', 'true') == 'true'
DEBUG = os.environ.get('DEBUG', 'true') == 'true'
PORT = int(os.environ.get('PORT', '8080'))
CONFIDENCE_THRESHOLD = 0.6
BATCH_SIZE = 30

if GPU_MODE:
    caffe.set_mode_gpu()
else:
    caffe.set_mode_cpu()

app = Flask(__name__)
app.clf = caffe.Classifier(
    MODEL_DEF_FILE, PRETRAINED_MODEL_FILE,
    image_dims=(255, 255), raw_scale=256.0,
    # mean=np.load(mean_file).mean(1).mean(1),
    channel_swap=(2, 1, 0)
)
app.clf.forward()


# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename=filename)
)

from views import *



if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
