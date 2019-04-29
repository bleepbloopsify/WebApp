from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from server.config import Config 

db = SQLAlchemy()
bootstrap = Bootstrap() 
login_manager = LoginManager()
login_manager.login_view = 'users.login'

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    from server.users.routes import users
    from server.posts.routes import posts
    from server.main.routes import main
    from server.errors.handlers import errors 
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app