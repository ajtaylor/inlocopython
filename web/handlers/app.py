__author__ = 'ttaylor'

from domain import user
import tornado.web


class AppHandler(tornado.web.RequestHandler):
    """
    classdocs
    """

    def get(self):
        self.render('app.html')