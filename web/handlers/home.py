'''
Created on 6 Apr 2014

@author: Owner
'''
import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    '''
    classdocs
    '''

    
    def get(self):
        self.render("home.html")