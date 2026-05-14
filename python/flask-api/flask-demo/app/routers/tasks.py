# -*- coding: utf-8 -*-
"""
    @Time    : 2026/5/14/周四 7:25
    @Author  : Joe
    @Email   : RJian_work@outlook.com
    @File    : tasks.py
    @Purpose : 
"""
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


@task_bp.get("/tasks")
@jwt_required()
def get_tasks():
    result = []
    username = get_jwt_identity()
    # 分页参数
    page = request.args.get("page", 1, type=int)
    page_size = request.args.get("page_size", 10, type=int)
    # 筛选参数
    status = request.args.get("status", '', type=str)
    priority = request.args.get("priority", '', type=str)
    keyword = request.args.get("keyword", '', type=str)
    user = User.query.filter_by(username=username).first()
    query = Tasks.query.filter_by(
        user_id=user.id,
        is_deleted=0
    )
    if status:
        query = query.filter(Tasks.status == status)
    if priority:
        query = query.filter(Tasks.priority == priority)
    if keyword:
        query = query.filter(Tasks.title.like(f"%{keyword}%"))
    tasks = query.paginate(
        page=page,
        per_page=page_size,
        error_out=False
    )
    for task in tasks:
        result.append(task.to_dict())
    return success(result)


@task_bp.get("/tasks/<int:task_id>")
@jwt_required()
def get_task(task_id):
    user = User.query.filter_by(username=get_jwt_identity()).first()
    task = Tasks.query.filter_by(
        id=task_id,
        user_id=user.id,
        is_deleted=0
    ).first()
    if task:
        return success(task.to_dict())
    else:
        return fail("未查询到！")


@task_bp.put("/tasks/<int:task_id>")
@jwt_required()
def update_tasks(task_id: int):
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    task = Tasks.query.filter_by(
        id=task_id,
        user_id=user.id,
        is_deleted=0
    ).first()
    if not task:
        return fail(f"未查询到该用户下的id为{task_id}的任务")
    data = request.get_json()
    if not data.get("title"):
        return fail("标题不能为空！")
    if not data.get("priority") or data['priority'] not in ["low", "medium", "high"]:
        return fail("优先级只能是low、medium、high")
    if not data.get("status") or data["status"] not in ['pending', 'doing', 'done', 'cancelled']:
        return fail("状态只能是pending, doing, done, cancelled")
    if not datetime_verify(data['due_date']):
        return fail("日期形式为YYYY-MM-DD")
    task.title = data['title']
    task.description = data['description']
    task.priority = data['priority']
    task.status = data['status']
    task.due_date = data['due_date']
    db.session.commit()
    return success(task.to_dict())


@task_bp.delete("/tasks/<int:task_id>")
@jwt_required()
def delete_task(task_id):
    user = User.query.filter_by(username=get_jwt_identity()).first()
    task = Tasks.query.filter_by(
        id=task_id,
        is_deleted=0
    ).first()
    if not task:
        return fail("当前任务不存在！！！")
    if task.user_id != user.id:
        return fail("只能删除自己的任务")
    task.is_deleted = 1
    db.session.commit()
    return success(task.to_dict())
