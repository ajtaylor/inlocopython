'''
Created on 6 Apr 2014

@author: ttaylor
'''
import os
import tornado.ioloop
import tornado.web
from handlers import *

root = os.path.dirname(__file__)

settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
)

application = tornado.web.Application([
    (r"/", home.HomeHandler),
    (r"/features", features.FeaturesHandler),
    (r"/about", about.AboutHandler),
    (r"/register", register.RegisterHandler),
    (r"/login", login.LoginHandler),
    (r'/static/(.*)', tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()