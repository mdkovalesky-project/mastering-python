from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


migrate = Migrate()
db = SQLAlchemy()

login_manager = LoginManager()
