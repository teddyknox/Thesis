import sys, os, inspect
APP_DIRNAME = os.path.abspath(os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe()))))
sys.path.append(APP_DIRNAME)

MODEL_DEF_FILE = '{}/classifiers/googlenet/deploy.prototxt'.format(APP_DIRNAME)
PRETRAINED_MODEL_FILE = '{}/classifiers/googlenet/bvlc_googlenet_cae_iter_116000.caffemodel'.format(APP_DIRNAME)

# See if Caffe is available
try:
    import caffe
    GPU_MODE = os.environ.get('GPU_MODE', 'true') == 'true'

    if GPU_MODE:
        caffe.set_mode_gpu()
    else:
        caffe.set_mode_cpu()

    classifier = caffe.Classifier(
        MODEL_DEF_FILE, PRETRAINED_MODEL_FILE,
        image_dims=(255, 255), raw_scale=256.0,
        # mean=np.load(mean_file).mean(1).mean(1),
        channel_swap=(2, 1, 0)
    )
    classifier.forward()

except ImportError:
    caffe = None
    classifier = None

class CaffeImportError(Exception):
    pass
