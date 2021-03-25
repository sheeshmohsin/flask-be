from . import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, Sequence, VARCHAR, SmallInteger, UniqueConstraint, PrimaryKeyConstraint
from flask_sqlalchemy import BaseQuery


class MyQuery(BaseQuery):

    def infinite_paginate(self, before=None, after=None):
        if after:
            query = self.filter(PowerUser.id > after).order_by(PowerUser.id.asc())
        elif before:
            query = self.filter(PowerUser.id < before).order_by(PowerUser.id.desc())
        else:
            query = self
        return query


class PowerUser(db.Model):

    query_class = MyQuery
    __tablename__ = "poweruser"
    __tableargs__ = (
        UniqueConstraint('id', 'user_type', name='poweruser_id_user_type_key')
    )

    id = Column(Integer, Sequence('id_seq'), autoincrement=True, primary_key=True)
    username = Column(VARCHAR(length=40))
    password = Column(VARCHAR(length=40))
    user_type = Column(SmallInteger)

    @property
    def json(self):
        """ Define a base way to jsonify models
            Columns inside `to_json_filter` are excluded """
        return {
            column: value
            if not isinstance(value, datetime)
            else value.strftime("%Y-%m-%d")
            for column, value in self._to_dict().items()
            if column not in self.to_json_filter
        }
