from random import randint, uniform
from colorsys import hls_to_rgb
import uuid
from PIL import Image, ImageDraw
import os

BATCH_SIZE = 30
CONFIDENCE_THRESHOLD = 0.6


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


def pretty_image_generator():
    from classifier import classifier
    import caffe
    pretty_images = []
    while True:
        while len(pretty_images) == 0:
            images = [generate_image() for i in xrange(BATCH_SIZE)]
            caffeImages = [caffe.io.load_image(os.path.join(IMAGES_DIR, filename)) for filename in images]
            results = classifier.predict(caffeImages, oversample=True)
            for x in range(results.shape[0]):
                scores = results[x]
                prediction = (-scores).argsort()[0]
                if prediction == 1 and scores[1] > CONFIDENCE_THRESHOLD:
                    pretty_images.append((images[x], scores[1]))
                else:
                    # throw away image
                    os.remove(os.path.join(IMAGES_DIR, images[x]))
        yield pretty_images.pop(0)

pig = pretty_image_generator()
def generate_pretty_image():
    return next(pig)
