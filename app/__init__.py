from urllib.parse import quote_plus
import os
from flask import Flask
from flask_login import LoginManager
from flask_login.utils import login_user
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

template_dir = os.path.abspath('./templates')
static_dir = os.path.abspath('./static')

app = Flask(__name__,template_folder=template_dir,static_folder=static_dir)

print("printando template")
print(app.template_folder)

app.config.from_object('config')

import pandas as pd

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import main