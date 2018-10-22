import os
from flask import Flask, Blueprint
from flask_restful import Api

from instance import config



def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = os.getenv("SECRET_KEY")
    
    from .api.v1 import version1 as v1

    app.register_blueprint(v1)

    return app