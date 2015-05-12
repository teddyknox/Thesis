import sys, os, inspect
APP_DIRNAME = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())))

from random import randint, uniform
from colorsys import hls_to_rgb
import uuid
from PIL import Image, ImageDraw

BATCH_SIZE = 30
CONFIDENCE_THRESHOLD = 0.4
IMAGES_DIR = os.path.join(APP_DIRNAME, 'images')

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
    image.save(os.path.join(IMAGES_DIR, filename))
    return filename


def generate_pretty_image():
    from classifier import classifier
    import caffe
    iternum = 1
    while True:
        print iternum
        iternum += 1
        images = [generate_image() for i in xrange(BATCH_SIZE)]
        caffeImages = [caffe.io.load_image(os.path.join(IMAGES_DIR, filename)) for filename in images]
        results = classifier.predict(caffeImages, oversample=True)
        for x in range(results.shape[0]):
            scores = results[x]
            # prediction = (-scores).argsort()[0]
            # if prediction == 1 and scores[1] > CONFIDENCE_THRESHOLD:
            if scores[1]  > CONFIDENCE_THRESHOLD:
                return (images[x], scores[1])
            # else:
                # throw away image
                os.remove(os.path.join(IMAGES_DIR, images[x]))
