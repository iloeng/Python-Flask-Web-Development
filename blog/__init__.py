#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    __init__.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.25   10:00
-------------------------------------------------------------------------------
   @Change:   2020.08.25
-------------------------------------------------------------------------------
"""
import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler

from flask import Flask

from blog.blueprints.admin import admin_bp
from blog.blueprints.auth import auth_bp
from blog.blueprints.blog import blog_bp
from blog.extensions import bootstrap, db, ckeditor, mail, moment, migrate
from blog.settings import config

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask('Blog')
    app.config.from_object(config[config_name])

    register_blueprints(app)

    register_extensions(app)

    return app


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')


if __name__ == '__main__':
    app = create_app()
    app.run()
