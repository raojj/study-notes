# -*- coding: utf-8 -*-
"""
    @Time    : 2026/5/13/周三 21:52
    @Author  : Joe
    @Email   : RJian_work@outlook.com
    @File    : tasks.py
    @Purpose : 
"""
from datetime import datetime, UTC
from app.extension import db


class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    priority = db.Column(db.String(20))
    status = db.Column(db.String(20))
    due_date = db.Column(db.DateTime)
    is_deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now(UTC))
    updated_at = db.Column(db.DateTime, default=datetime.now(UTC))

    users = db.relationship('User', backref='tasks')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'due_date': self.due_date,
            'is_deleted': "已删除" if self.is_deleted == 1 else "未删除",
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
