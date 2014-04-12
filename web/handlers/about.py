'''
Created on 6 Apr 2014

@author: Owner
'''
import tornado.web

class AboutHandler(tornado.web.RequestHandler):
    '''
    classdocs
    '''


    def get(self):
        self.render("about.html")