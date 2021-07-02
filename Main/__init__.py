"""This is init module."""
from flask_restful import Api
from flask import Flask
from flask_bcrypt import Bcrypt
import os
from Main.Routes.routes import initialize_routes
from flask_jwt_extended import JWTManager
from config import Config

# Place where app is defined
app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ["DB"]
}
jwt = JWTManager(app)

from Main.DAC.config import initialize_db
initialize_db(app)
initialize_routes(api)
bcrypt = Bcrypt(app)

