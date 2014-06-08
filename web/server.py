__author__ = 'ttaylor'

import os
import json
import momoko
from urllib.parse import urlparse
from tornado.options import define, options
import tornado.ioloop
import tornado.web
from web import handlers

root = os.path.dirname(__file__)

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    static_path=os.path.join(os.path.dirname(__file__), 'static'),
    cookie_secret='on#the#buses'
)

application = tornado.web.Application([
    (r'/', handlers.HomeHandler),
    (r'/features', handlers.FeaturesHandler),
    (r'/about', handlers.AboutHandler),
    (r'/register', handlers.RegisterHandler),
    (r'/login', handlers.LoginHandler),
    (r'/thankyou', handlers.ThankyouHandler),
    (r'/static/(.*)', tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
    (r'/api/organisation/register', handlers.OrganisationHandler),
    (r'/api/user/login', handlers.UserLoginHandler),
    (r'/app', handlers.AppHandler),
], **settings)

define('port', default='8080', help='Port to listen on')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    try:
        cred_file = open(os.environ['CRED_FILE'])
        credentials = json.load(cred_file)
        
        elephant_uri = urlparse(credentials['ELEPHANTSQL']['ELEPHANTSQL_URL'])
        
        db_config = {
            'database': elephant_uri.path[1:],
            'host': elephant_uri.hostname,
            'port': elephant_uri.port,
            'username': elephant_uri.username,
            'password': elephant_uri.password
        }
    
    except IOError:
        print('Could not load credentials file')
    
    try:
        application.db = momoko.Pool(
            dsn='dbname={0} user={1} password={2} host={3} port={4}'
                .format(db_config['database'],
                        db_config['username'],
                        db_config['password'],
                        db_config['host'],
                        db_config['port']),
            size=1)
    except Exception as ex:
        print('Could not instantiate momoko pool')
        print(type(ex))
    
    try:
        application.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()