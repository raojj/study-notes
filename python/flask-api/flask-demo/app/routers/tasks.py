# -*- coding: utf-8 -*-
"""
    @Time    : 2026/5/14/周四 7:25
    @Author  : Joe
    @Email   : RJian_work@outlook.com
    @File    : tasks.py
    @Purpose : 
"""
from datetime import datetime, UTC
from flask import Blueprint, request
from app.models import User, Tasks
from app.extension import db
from app.tools.tools import success, fail, datetime_verify
from flask_jwt_extended import jwt_required, get_jwt_identity

task_bp = Blueprint('task_bp', __name__)


@task_bp.post("/tasks")
@jwt_required()
def create_tasks():
    username = get_jwt_identity()
    print(username)
    data = request.get_json()
    if not data.get("title"):
        return fail("标题不能为空！")
    if not data.get("priority") or data['priority'] not in ["low", "medium", "high"]:
        return fail("优先级只能是low、medium、high")
    if not data.get("status") or data["status"] not in ['pending', 'doing', 'done', 'cancelled']:
        return fail("状态只能是pending, doing, done, cancelled")
    if not datetime_verify(data['due_date']):
        return fail("日期形式为YYYY-MM-DD")
    user = User.query.filter_by(username=username).first()
    task = Tasks(
        user_id=user.id,
        title=data['title'],
        description=data['description'],
        priority=data['priority'],
        status=data['status'],
        due_date=data['due_date']
    )

    db.session.add(task)
    db.session.commit()
    return success({
        "id": task.id,
    })
