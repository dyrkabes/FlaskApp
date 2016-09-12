import os

from flask import Flask, g, render_template, flash, redirect, request, url_for, session


from forms import LoginForm, EditForm, RegisterForm, PostForm, PostHandForm, BuffForm

from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from flask.ext.bcrypt import check_password_hash
from flask.ext.openid import OpenID

import models



from config import basedir, ADMINS, MAIL_PASSWORD, MAIL_PORT, MAIL_SERVER, MAIL_USERNAME

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

open_id = OpenID(app, os.path.join(basedir, 'tmp'))


if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT),
                               'no-reply@' + MAIL_SERVER,
                               ADMINS,
                               'microblog failure',
                               credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)


# if not app.debug:
if True:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/blog.log',
                                       'a',
                                       1024*1024,
                                       10
                                       )
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))"
        )
    )

    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('Microblog start')


import views, models