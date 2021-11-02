import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String, unique=True)
    group_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('groups.id'))


class Lecture(Base):
    __tablename__ = 'lectures'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    lesson = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.Date)
    group_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('groups.id', ondelete='CASCADE'))


class Group(Base):
    __tablename__ = 'groups'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    users = relationship('User', backref='groups')
    number = sqlalchemy.Column(sqlalchemy.Integer, unique=True)

