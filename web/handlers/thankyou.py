'''
Created on 27 Apr 2014

@author: Owner
'''
import tornado.web

class ThankyouHandler(tornado.web.RequestHandler):
    '''
    classdocs
    '''


    def get(self):
        self.render("thankyou.html")