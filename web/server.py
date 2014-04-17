'''
Created on 6 Apr 2014

@author: ttaylor
'''
import os
from tornado.options import define, options
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

define("port", default="8080", help="Port to listen on")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    try:
        application.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()