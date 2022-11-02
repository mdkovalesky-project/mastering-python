from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow


migrate = Migrate()
db = SQLAlchemy()
ma = Marshmallow()

login_manager = LoginManager()
