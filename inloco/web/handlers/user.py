'''
Created on 22 Apr 2014

@author: Owner
'''
from domain import user
from tornado import gen
import tornado.web

class UserHandler(tornado.web.RequestHandler):
    '''
    classdocs
    '''

    
    @gen.coroutine
    def post(self):
        u = user.User(self.application.db)
        u.fullname = self.get_argument('fullname')
        u.email_address = self.get_argument('email_address')
        u.password = self.get_argument('password')
        u.organisation_name = self.get_argument('organisation_name')
        yield u.register()
        self.redirect('/thankyou')