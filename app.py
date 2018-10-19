from flask import Flask
from flask import Flask, render_template,redirect,url_for,session
from flask_bootstrap3 import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import request
from models import User,Reporter,db
from exts import db
import pymysql
import config
pymysql.install_as_MySQLdb()
from decorations import login_lim

app = Flask(__name__)
db=SQLAlchemy(app)
bootstrap=Bootstrap(app)
app.config.from_object(config)
db.init_app(app)

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
        username=request.form.get("username")
        password=request.form.get("password")
        user=User.query.filter(User.username==username,User.password==password).first()
        if user:
            session['user_id']=user.id
            session.permanent= True
            return redirect(url_for("index"))
        else:
            return u"账号或密码错误！"

@app.route('/logout/')
def logout():
    #session.pop('user_id')
    #del session["user_id"]
    session.clear()
    return redirect(url_for("Login"))
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
@app.route("/reporter/",methods=["GET","POST"])
@login_lim
def reporter():
    from models import db as thisdb
    if request.method=="GET":
        return render_template("reporter.html")
    else:
        title =request.form.get('title')
        content=request.form.get('content')
        reporter = Reporter(title=title,content=content)
        user_id=session.get('user_id')
        user=User.query.filter(User.id==user_id).first()
        reporter.author=user
        thisdb.session.add(reporter)
        thisdb.session.commit()
        return redirect(url_for('forum'))
@app.route('/detail/<reporter_id>')
def detail(reporter_id):
    reporter_model=Reporter.query.filter(Reporter.id==reporter_id).first()
    return render_template('detail.html',reporter=reporter_model)

@app.route('/comment/',methods=['POST'])
def add_comment():
    content=request.form.get('comment')
@app.route('/forum/')
def forum():
    context={
        'reporters':Reporter.query.order_by('-create_time').all()
    }
    return render_template('forum.html',**context)

@app.context_processor
def my_context_processor():
    user_id=session.get('user_id')
    if user_id:
        user=User.query.filter(User.id ==user_id).first()
        if user:
            return {'user':user}
    return {}



if __name__ == '__main__':
    app.run(debug=True)
