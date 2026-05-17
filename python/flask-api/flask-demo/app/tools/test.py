# -*- coding: utf-8 -*-
"""
    @Time    : 2026/5/17/周日 10:24
    @Author  : Joe
    @Email   : RJian_work@outlook.com
    @File    : test.py
    @Purpose : 
"""


def outer(fn):
    def inner(name):
        print(f"{name}是inner函数的参数")
        fn(name)

    return inner


@outer
def send(name):
    print("这是被装饰的函数")
    print(f"{name}这是被装饰函数的参数")


send("Joe")
