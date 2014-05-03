'''
Created on 6 Apr 2014

@author: Owner
'''
import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    '''
    classdocs
    '''


    def get(self):
        self.render("login.html")