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

db = SQLAlchemy()
jwt = JWTManager()
