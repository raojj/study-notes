# -*- coding: utf-8 -*-
"""
    @Time    : 2026/5/13/周三 22:36
    @Author  : Joe
    @Email   : RJian_work@outlook.com
    @File    : tools.py
    @Purpose : 
"""
import hashlib
from datetime import date
from typing import Any
PASSWORD_SALT = "joe"


def encrypt_password(password: str) -> str:
    """
    加密密码，MD5+盐值
    :param password: 原密码
    :return: 加密后的密码
    """
    salted_password = password + PASSWORD_SALT
    return hashlib.md5(salted_password.encode()).hexdigest()


def verify_password(password: str, encrypted_password: str) -> bool:
    """
    验证密码
    :param password: 用户输出的原密码
    :param encrypted_password: 加密后的密码
    :return: 验证结果
    """
    return encrypt_password(password) == encrypted_password


def success(data: Any) -> dict:
    return {
        "code": 0,
        "status": "success",
        "data": data
    }


def fail(message: str) -> dict:
    return {
        "code": 404,
        "status": "fail",
        "data": {
            "message": message
        }
    }


def datetime_verify(data: str) -> bool:
    if not isinstance(data, str):
        return False
    try:
        date.fromisoformat(data)
        return True
    except ValueError:
        return False
