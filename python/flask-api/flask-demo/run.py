# -*- coding: utf-8 -*-
"""
    @Time    : 2026/5/13/周三 21:21
    @Author  : Joe
    @Email   : RJian_work@outlook.com
    @File    : run.py
    @Purpose : 
"""
from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
