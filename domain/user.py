__author__ = 'ttaylor'

import momoko
import psycopg2
from tornado import gen
import uuid


class User():
    """
    classdocs
    """

    def __init__(self, repository):
        """
        Constructor
        :type repository: application.repository
        """
        self.repository = repository

    @gen.coroutine
    def register(self):
        try:
            sql = ' '.join(['SELECT user_id, organisation_id FROM public.register_organisation',
                            '(%(fullname)s, %(email_address)s, %(password)s, %(organisation_name)s, %(roomkey)s);'])
            values = dict(fullname=self.fullname, email_address=self.email_address, password=self.password,
                          organisation_name=self.organisation_name, roomkey=str(uuid.uuid4()))
                    
            cursor = yield momoko.Op(self.repository.execute, sql, values)
        except (psycopg2.Warning, psycopg2.Error) as error:
            print(str(error))
            return str(error)
        else:
            return cursor.fetchone()

    @gen.coroutine
    def login(self, email_address, password):
        try:
            sql = ' '.join(['SELECT user_id, name, is_admin, organisation_id FROM public.login_user',
                            '(%(email_address)s, %(password)s);'])
            values = dict(email_address=email_address, password=password)

            cursor = yield momoko.Op(self.repository.execute, sql, values)
        except (psycopg2.Warning, psycopg2.Error) as error:
            print(str(error))
            return str(error)
        else:
            # print(cursor.description)
            # print(cursor.description[0][0])
            res = cursor.fetchone()
            description = cursor.description
            return {description[0][0]: res[0], description[3][0]: res[3]}