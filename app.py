from flask import Flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db=SQLAlchemy(app)
bootstrap=Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:594695768@127.0.0.1:3306/db_demon1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.create_all()

@app.route('/')
def index():
    context={
        "username":"吕俊才"
    }
    return render_template("index.html",**context)


@app.route('/login/')
def Login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
