'''
Created on 22 Apr 2014

@author: Owner
'''

import momoko
import psycopg2
from tornado import gen
import uuid

class User():
    '''
    classdocs
    '''


    def __init__(self, repository):
        '''
        Constructor
        '''
        self.repository = repository
    

    @gen.coroutine
    def register(self):
        try:
            sql = ' '.join(['SELECT user_id, organisation_id FROM public.register_organisation',
                            '(%(fullname)s, %(email_address)s, %(password)s, %(organisation_name)s, %(roomkey)s);'])
            values = {'fullname': self.fullname,
                      'email_address': self.email_address,
                      'password': self.password,
                      'organisation_name': self.organisation_name,
                      'roomkey': str(uuid.uuid4())}
                    
            cursor = yield momoko.Op(self.repository.execute, sql, values)
        except (psycopg2.Warning, psycopg2.Error) as error:
            print(str(error))
            return str(error)
        else:
            return cursor.fetchone()