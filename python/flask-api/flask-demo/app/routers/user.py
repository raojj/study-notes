# -*- coding: utf-8 -*-
"""
    @Time    : 2026/5/13/周三 22:32
    @Author  : Joe
    @Email   : RJian_work@outlook.com
    @File    : user.py
    @Purpose : 
"""
from flask import Blueprint, request
from app.models import User
from app.extension import db
from app.tools.tools import encrypt_password, verify_password, success, fail
from flask_jwt_extended import create_access_token

user_bp = Blueprint('user_bp', __name__)


@user_bp.post('/register')
def register():
    data = request.get_json()
    user = User(
        username=data['username'],
        email=data['email'],
        password=encrypt_password(data['password']),
    )
    user_verify_username = User.query.filter_by(username=user.username).first()
    if user_verify_username:
        return fail("用户名已存在！")
    user_verify_email = User.query.filter_by(email=user.email).first()
    if user_verify_email:
        return fail("用户邮箱已存在！")
    db.session.add(user)
    db.session.commit()
    if user.id:
        return success({
            "user_id": user.id,
        })
    else:
        return fail("用户注册失败")


@user_bp.post('/login')
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User(
        email=email,
        password=password
    )
    user_verify_email = User.query.filter_by(email=user.email).first()
    if user_verify_email:
        if verify_password(user.password, user_verify_email.password):
            user_access_token = create_access_token(identity=user_verify_email.username)
            return success({
                "message": "登录成功",
                "token": user_access_token
            })
        else:
            return fail("用户密码错误！")
    else:
        return fail("用户不存在！")
