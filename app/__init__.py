from flask import Flask
from flask_login import LoginManager # type: ignore


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


from . import routes