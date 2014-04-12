'''
Created on 6 Apr 2014

@author: Owner
'''
import tornado.web

class RegisterHandler(tornado.web.RequestHandler):
    '''
    classdocs
    '''


    def get(self):
        self.render("register.html")