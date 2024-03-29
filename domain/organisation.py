__author__ = 'ttaylor'

from domain.domain_base import DomainBase
import momoko
import psycopg2
from tornado import gen
import uuid


class Organisation(DomainBase):
    """
    classdocs
    """

    @gen.coroutine
    def register(self, fullname, email_address, password):
        try:
            sql = ' '.join(['SELECT user_id, organisation_id FROM public.register_organisation',
                            '(%(fullname)s, %(email_address)s, %(password)s, %(organisation_name)s, %(roomkey)s);'])
            values = dict(fullname=fullname, email_address=email_address, password=password,
                          organisation_name=self.name, roomkey=str(uuid.uuid4()))

            cursor = yield momoko.Op(self.repository.execute, sql, values)
        except (psycopg2.Warning, psycopg2.Error) as error:
            raise error
        else:
            return cursor.fetchone()