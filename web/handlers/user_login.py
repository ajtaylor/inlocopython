__author__ = 'ttaylor'

from domain import user
from tornado import gen
import tornado.web


class UserLoginHandler(tornado.web.RequestHandler):
    """
    classdocs
    """

    @gen.coroutine
    def post(self):
        u = user.User(self.application.db)
        try:
            res = yield u.login(self.get_argument('email_address'), self.get_argument('password'))
            self.set_secure_cookie('user_id', str(res.user_id))
            self.set_secure_cookie('organisation_id', str(res.organisation_id))
            self.redirect('/app')
        except Exception as ex:
            self.send_error(500)