from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import app
from exts import db
from models import User,Reporter,Comment

manager=Manager(app)#初始化以app为对象的Manager函数
migrate =Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__=="__main__":
    manager.run()

