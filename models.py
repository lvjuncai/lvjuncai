from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Reporter(db.Model):
    __tablename__ = "Reporter"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title= db.Column(db.String(100),nullable=False)
    content =db.Column(db.Text,nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)#不加括号是调用函数 加了括号是调用值
    author_id=db.Column(db.Integer,db.ForeignKey('user.id'))

    author=db.relationship('User',backref=db.backref('reporters'))

class Comment(db.Model):
    __tablename__="Comment"
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    content=db.Column(db.Text,nullable=False)
    comment_time=db.Column(db.DateTime,default=datetime.now)
    reporter_id=db.Column(db.Integer,db.ForeignKey('Reporter.id'))
    author_id=db.Column(db.Integer,db.ForeignKey('user.id'))

    reporter=db.relationship('Reporter',backref=db.backref('comments'))
    author = db.relationship('User', backref=db.backref('comments'))