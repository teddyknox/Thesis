from flask import render_template, send_file, request, abort, send_from_directory
from app import app
from PIL import Image, ImageDraw
import uuid
from os import path
from random import randint, uniform
from colorsys import hls_to_rgb

manifest_filename = './app/manifest.txt'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/image')
def generate_image():
    """
    Generates a new image and redirects the client to it.
    """
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
    image.save(path.abspath('./app/images/' + filename))
    return ('/image/' + filename, 200, {})


@app.route('/image/<string:image_filename>')
def download_image(image_filename):
    return send_from_directory(path.abspath('./app/images'), image_filename)


@app.route('/image/<string:image_filename>', methods=['POST'])
def image_label(image_filename):
    try:
        label = request.form['label']
    except KeyError:
        abort(500)
    with open(manifest_filename, 'a+') as manifest:
        manifest.write(image_filename + "\t" + label + "\n")
    return "", 200, {}
