import os


CSRF_ENABLED = True
SECRET_KEY = 'grkeo564e5/*gr_+_=--=_3wr\dfs34/*-+*/qe2d'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


basedir = os.path.abspath(os.path.dirname(__file__))

# mail server settings. Test later somehow

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

ADMINS = ['rellik-the-great@mail.ru']