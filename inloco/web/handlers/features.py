'''
Created on 6 Apr 2014

@author: Owner
'''
import tornado.web

class FeaturesHandler(tornado.web.RequestHandler):
    '''
    classdocs
    '''


    def get(self):
        self.render("features.html")