# -*- coding: utf-8 -*-
"""
    @Time    : 2026/5/13/周三 22:06
    @Author  : Joe
    @Email   : RJian_work@outlook.com
    @File    : __init__.py.py
    @Purpose : 
"""
from flask import Flask
from app.extension import db, jwt
from app.routers.user import user_bp
from app.routers.tasks import task_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost:3306/flask_demo?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    jwt.init_app(app)
    app.config['JWT_SECRET_KEY'] = 'joe-task-manage-system-test'
    app.register_blueprint(user_bp, url_prefix='/api/auth')
    app.register_blueprint(task_bp, url_prefix='/api')
    from app import models

    with app.app_context():
        db.create_all()
    return app
