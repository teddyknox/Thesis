from flask import render_template, send_file, request, abort, send_from_directory, Response
from peewee import fn
import os
from app import app

from generators import *
from models import *


@app.route('/')
def rating():
    num_ratings = Image.select(fn.Sum(Image.num_ratings)).scalar()
    num_images = Image.select(fn.Count(Image.id)).scalar()
    return render_template('rating.html', num_ratings=num_ratings, num_images=num_images)


@app.route('/image/<string:image_filename>')
def download_image(image_filename):
    return send_from_directory(IMAGES_DIR, image_filename)


@app.route('/image')
def image():
    """
    Responds with the path to a generated or retrieved image, optionally filtered as good.
    """
    mode = request.args.get('mode', 'random')
    if mode == 'random':
        img = Image.get_random()
    elif mode == 'scored':
        try:
            img = Image.get_scored()
        except CaffeImportError:
            img = Image.get_random()
    return ('/image/' + img.filename, 200, {})


@app.route('/image/<string:image_filename>', methods=['POST'])
def image_label(image_filename):
    rating = int(request.form['label'])
    image = Image.get(filename=image_filename)
    image.score = ((image.score * image.num_ratings) + rating) / (image.num_ratings + 1)
    image.num_ratings += 1
    image.save()
    return "", 200, {}


@app.route('/pretty')
def pretty_gallery():
    best = Image.select(Image.filename).order_by(Image.score.desc()).limit(300)
    best = map(lambda i: i.filename, best)
    return render_template('gallery.html', images=best)


@app.route('/ugly')
def ugly_gallery():
    worst = Image.select(Image.filename).order_by(Image.score.asc()).limit(300)
    worst = map(lambda i: i.filename, worst)
    return render_template('gallery.html', images=worst)


@app.route('/smart_pretty')
def smart_pretty_gallery():
    """
    Generates a gallery of images that are classified as pretty.
    """
    images = Image.select().where(Image.generation_method == "scored").limit(300)
    images = list(images)
    images.append([generate_pretty_image()[0] for i in xrange(300 - len(images))])
    return render_template('gallery.html', images=images)


@app.route('/comparison')
def comparison_gallery():
    pretty = (Image.select()
                .where(Image.generation_method == 'random' and Image.score > 0)
                .order_by(fn.Random())
                .limit(40))
    ugly = (Image.select()
                .where(Image.generation_method == 'random' and Image.score == 0)
                .order_by(fn.Random())
                .limit(40))
    smart_pretty = (Image.select()
                    .where(Image.generation_method == 'scored' and Image.model_score > 0.6)
                    .order_by(fn.Random())
                    .limit(40))
    image_sets = [('pretty', pretty), ('ugly', ugly), ('smart_pretty', smart_pretty)]
    return render_template('comparison.html', image_sets=image_sets)
