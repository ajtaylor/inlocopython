__author__ = 'ttaylor'

from domain import organisation
from tornado import gen
import tornado.web


class OrganisationHandler(tornado.web.RequestHandler):
    """
    classdocs
    """

    @gen.coroutine
    def post(self):
        # u = user.User(self.application.db)
        o = organisation.Organisation(self.application.db)
        # u.fullname = self.get_argument('fullname')
        # u.email_address = self.get_argument('email_address')
        # u.password = self.get_argument('password')
        # u.organisation_name = self.get_argument('organisation_name')
        o.name = self.get_argument('organisation_name')
        yield o.register(self.get_argument('fullname'), self.get_argument('email_address'), self.get_argument('password'))
        self.redirect('/thankyou')