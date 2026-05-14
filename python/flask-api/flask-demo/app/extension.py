# -*- coding: utf-8 -*-
"""
    @Time    : 2026/5/13/周三 21:49
    @Author  : Joe
    @Email   : RJian_work@outlook.com
    @File    : extension.py
    @Purpose : 
"""
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.tools.tools import fail

db = SQLAlchemy()
jwt = JWTManager()


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return fail("请先登录"), 200


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return fail("登录已过期，请重新登录"), 200
