from flask import Flask
from flask import Flask, render_template
from flask_bootstrap3 import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import request
import config

app = Flask(__name__)
db=SQLAlchemy(app)
bootstrap=Bootstrap(app)
app.config.from_object(config)

"""class User(db.Model):
    __tablename__="user"
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(100),nullable=False)
    password=db.Column(db.String(100),nullable=False)
class Message(db.Model):
    __tablename__ = "Message"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title= db.Column(db.String(100),nullable=False)
    content =db.Column(db.Text,nullable=False)
    author_id =db.Column(db.Integer,db.ForeignKey("user.id"))

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
