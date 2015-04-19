import caffe
import os
import numpy as np
import pandas as pd
import time
import logging

loggingHandler = logging.FileHandler('results.log')
logger = logging.getLogger()
logger.addHandler(loggingHandler)


class Classifier(object):
    def __init__(self, model_def_file, pretrained_model_file, image_dim=256, raw_scale=255.0, gpu_mode=True):
        logging.info('Loading net and associated files...')
        if gpu_mode:
            caffe.set_mode_gpu()
        else:
            caffe.set_mode_cpu()
        self.net = caffe.Classifier(
            model_def_file, pretrained_model_file,
            image_dims=(image_dim, image_dim), raw_scale=raw_scale,
            # mean=np.load(mean_file).mean(1).mean(1),
            channel_swap=(2, 1, 0)
        )

        # with open(class_labels_file) as f:
        #     labels_df = pd.DataFrame([
        #         {
        #             'synset_id': l.strip().split(' ')[0],
        #             'name': ' '.join(l.strip().split(' ')[1:]).split(',')[0]
        #         }
        #         for l in f.readlines()
        #     ])
        # self.labels = labels_df.sort('synset_id')['name'].values
        #
        # self.bet = cPickle.load(open(bet_file))
        # # A bias to prefer children nodes in single-chain paths
        # # I am setting the value to 0.1 as a quick, simple model.
        # # We could use better psychological models here...
        # self.bet['infogain'] -= np.array(self.bet['preferences']) * 0.1

    def classify_image(self, image):
        try:
            starttime = time.time()
            scores = self.net.predict([image], oversample=True).flatten()
            logger.error(scores)
            endtime = time.time()

            # indices = (-scores).argsort()[:5]
            # predictions = self.labels[indices]


            # In addition to the prediction text, we will also produce
            # the length for the progress bar visualization.
            # meta = [
            #     (p, '%.5f' % scores[i])
            #     for i, p in zip(indices, predictions)
            # ]
            # logging.info('result: %s', str(meta))
            #
            # # Compute expected information gain
            # expected_infogain = np.dot(
            #     self.bet['probmat'], scores[self.bet['idmapping']])
            # expected_infogain *= self.bet['infogain']
            #
            # # sort the scores
            # infogain_sort = expected_infogain.argsort()[::-1]
            # bet_result = [(self.bet['words'][v], '%.5f' % expected_infogain[v])
            #               for v in infogain_sort[:5]]
            # logging.info('bet result: %s', str(bet_result))

            # return (True, meta, bet_result, '%.3f' % (endtime - starttime))
            return True
            # return (True, meta, None, '%.3f' % (endtime - starttime))

        except Exception as err:
            logging.info('Classification error: %s', err)
            return (False, 'Something went wrong when classifying the '
                           'image. Maybe try another one?')
