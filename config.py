import os
_basedir = os.path.abspath(os.path.dirname(__file__))

"""
_basedir is a trick for you to get the folder where the script runs
DEBUG indicates that it is a dev environment, you'll get the very helpful error page from flask when an error occured.
SECRET_KEY will be use to sign the cookies. Change it and all your users will have to login again.
ADMINS will be used if you need to email information to the site administrators.
SQLALCHEMY_DATABASE_URI and DATABASE_CONNECT_OPTIONS are SQLAlchemy connection options (hard to guess )
THREAD_PAGE my understanding was 2/core... might be wrong :)
CSRF_ENABLED and CSRF_SESSION_KEY are protecting against form post fraud
RECAPTCHA_* WTForms comes with a RecaptchaField ready to use... just need to go to recaptcha website and get your public and private key.
"""

DEBUG = True

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'SecretKeyForSessionSigning'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED=True
CSRF_SESSION_KEY="somethingimpossibletoguess"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = 'blahblahblahblahblahblahblahblahblah'
RECAPTCHA_PRIVATE_KEY = 'blahblahblahblahblahblahprivate'
RECAPTCHA_OPTIONS = {'theme': 'white'}