import os

__author__ = 'nikosD'

DEBUG = False
ADMINS = frozenset([os.environ.get('MAILGUN_EMAIL')])