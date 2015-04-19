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
import sys

MAX_IMAGES = 2000
MAX_RATINGS = 3
APP_DIRNAME = os.path.abspath(os.path.dirname(__file__))
MODEL_DEF_FILE = '{}/model/deploy.prototxt'.format(APP_DIRNAME)
PRETRAINED_MODEL_FILE = '{}/model/bvlc_googlenet_cae_iter_116000.caffemodel'.format(APP_DIRNAME)
GPU_MODE = os.environ.get('GPU_MODE', 'true') == 'true'
DEBUG = os.environ.get('DEBUG', 'true') == 'true'
PORT = int(os.environ.get('PORT', '8080'))

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


@app.route('/')
def index():
    num_ratings = DBImage.select(fn.Sum(DBImage.num_ratings)).scalar()
    num_images = DBImage.select(fn.Count(DBImage.id)).scalar()
    return render_template('index.html', num_ratings=num_ratings, num_images=num_images)


@app.route('/image')
def image():
    """
    Returns the path to a generated or retrieved image.
    """
    num_images = DBImage.select(fn.Count(DBImage.id)).scalar()
    if num_images < MAX_IMAGES:
        filename = generate_image()
        DBImage.create(filename=filename)
    else:
        to_rate = (DBImage.select()
                          .order_by(DBImage.num_ratings, fn.Random())
                          .limit(1))
        filename = to_rate[0].filename
    return ('/image/' + filename, 200, {})


@app.route('/pretty_image')
def pretty_image():
    """
    Responds with the path to a generated image, classified as pretty.
    """
    filename = generate_pretty_image()
    return ('/image/' + filename, 200, {})


@app.route('/smart_pretty')
def smart_pretty_gallery():
    """
    Generates a gallery of images that are classified as pretty.
    """
    images = [generate_pretty_image() for i in xrange(60)]
    return render_template('gallery.html', images=images)


@app.route('/image/<string:image_filename>')
def download_image(image_filename):
    return send_from_directory(os.path.abspath('images'), image_filename)


@app.route('/image/<string:image_filename>', methods=['POST'])
def image_label(image_filename):
    rating = int(request.form['label'])
    image = DBImage.get(filename=image_filename)
    image.score = ((image.score * image.num_ratings) + rating) / (image.num_ratings + 1)
    image.num_ratings += 1
    image.save()
    return "", 200, {}


@app.route('/pretty')
def pretty_gallery():
    best = DBImage.select(DBImage.filename).order_by(DBImage.score.desc()).limit(300)
    best = map(lambda i: i.filename, best)
    return render_template('gallery.html', images=best)


@app.route('/ugly')
def ugly_gallery():
    worst = DBImage.select(DBImage.filename).order_by(DBImage.score.asc()).limit(300)
    worst = map(lambda i: i.filename, worst)
    return render_template('gallery.html', images=worst)


@app.route('/manifest.txt')
def generate_manifest():
    images = DBImage.select()
    def generate():
        for image in images:
            yield "/{}\t{:.2f}\n".format(image.filename,image.score)
    return Response(generate(), mimetype='text/plain')


def generate_image():
    bg = (uniform(0, 360), uniform(0, 1), uniform(0, 1))
    bg = tuple(map(lambda x: int(x*256), hls_to_rgb(*bg)))
    image = Image.new('RGB', (256, 256), bg)
    d = ImageDraw.Draw(image)
    for i in xrange(randint(3, 5)):
        xy = [(randint(0, 255), randint(0, 255)) for i in xrange(3)]
        fill = (uniform(0, 360), uniform(0, 1), uniform(0, 1))
        outline = (fill[0], min(fill[1] + .1, 1), fill[2])
        fill = tuple(map(lambda x: int(x*256), hls_to_rgb(*fill)))
        outline = tuple(map(lambda x: int(x*256), hls_to_rgb(*outline)))
        d.polygon(xy, fill=fill, outline=outline)
    filename = str(uuid.uuid4()) + '.png'
    image.save(os.path.abspath('images/' + filename))
    return filename


def generate_pretty_image():
    print "GENERATE PRETTY IMAGE"
    pretty = False
    filename = None
    while not pretty:
        if filename:
            delete_image(filename)
        filename = generate_image()
        caffeImage = caffe.io.load_image(APP_DIRNAME + '/images/' + filename)
        scores = app.clf.predict([caffeImage], oversample=False).flatten()
        pretty = bool((-scores).argsort()[0])
    return filename


def delete_image(filename):
    os.remove(APP_DIRNAME + '/images/' + filename)


if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
