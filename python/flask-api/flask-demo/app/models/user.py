# -*- coding: utf-8 -*-
"""
    @Time    : 2026/5/13/周三 21:48
    @Author  : Joe
    @Email   : RJian_work@outlook.com
    @File    : user.py
    @Purpose : user表模型
"""
from app.extension import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
