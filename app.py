from flask import Flask
from flask import Flask, render_template,redirect,url_for
from flask_bootstrap3 import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import request
from models import User
from exts import db
import pymysql
import config
pymysql.install_as_MySQLdb()


app = Flask(__name__)
db=SQLAlchemy(app)
bootstrap=Bootstrap(app)
app.config.from_object(config)
db.init_app(app)
"""
class User(db.Model):
    __tablename__="user"
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),nullable=False)
    author_id =db.Column(db.Integer,db.ForeignKey("user.id"))
    password=db.Column(db.String(100),nullable=False)
class Message(db.Model):
    __tablename__ = "Message"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title= db.Column(db.String(100),nullable=False)
    content =db.Column(db.Text,nullable=False)
   
db.create_all()
"""
@app.route('/')
def index():
    context={
        "username":"吕俊才"
    }
   # return render_template('if.html')
    return render_template("index.html",**context)


@app.route('/login/',methods=['GET','POST'])
def Login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        pass
@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username=request.form.get("username")
        password1=request.form.get("password1")
        password2=request.form.get("password2")
        own_user=User.query.filter(User.username == username).first()
        if own_user:
            return "该账户已被注册"
        else:
            if password1!=password2:
                return '两次密码不一致！！'
            else:
                own_user =User(username=username,password=password1)
                db.session.add(own_user)
                db.session.commit()
                return redirect(url_for("Login"))

"""def insert_db():
    article1=Message(title='aaa',content='bbb')
    db.session.add(article1)
    db.session.commit()
def findout_db():
    article11 =Message.query.filter(Message.title=="aaa").first()
    print('name:%s'%article11.title)
    print('content:%s'%article11.content)
"""



if __name__ == '__main__':
    app.run(debug=True)
