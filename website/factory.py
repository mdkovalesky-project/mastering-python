from flask import Flask
from .ext import db, migrate, login_manager, ma # <- import extension (.ext)

from .models import User


DB_NAME = "database.db"


def create_app(): # <- aplikasi factory (configurasi dalam aplikasi inti)
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from .views import views
    from .auth import auth
    from .api.routes import api_blueprint

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(api_blueprint)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)


    return app
