from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from models import db
from resources import PowerUserResource
from schemas import ma

import config


server = Flask(__name__)

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_POOL_SIZE"] = config.SQLALCHEMY_POOL_SIZE
server.config["SQLALCHEMY_MAX_OVERFLOW"] = config.SQLALCHEMY_MAX_OVERFLOW

api = Api(server)

db.init_app(server)
db.app = server

ma.init_app(server)

api.add_resource(PowerUserResource, '/api/v1/users')


if __name__ == '__main__':
    server.run(debug=True)