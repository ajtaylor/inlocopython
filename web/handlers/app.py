__author__ = 'ttaylor'

from domain import user
from tornado import gen
import tornado.web


class AppHandler(tornado.web.RequestHandler):
    """
    classdocs
    """

    @gen.coroutine
    def get(self):
        u = user.User(self.application.db)
        user_info = yield u.getinfo(int(self.get_secure_cookie('user_id')))
        self.render('app.html', user_info = user_info)