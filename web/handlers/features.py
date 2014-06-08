__author__ = 'ttaylor'

import tornado.web


class FeaturesHandler(tornado.web.RequestHandler):
    """
    classdocs
    """

    def get(self):
        self.render('features.html')