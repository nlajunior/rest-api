from flask import Flask, jsonify
from flask_restful import Api

from resources.test import Tests
from resources.test import Test
from resources.user import User, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://admindba:123456789@localhost:3306/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']= 'T@uT0m&r1@'
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
   db.create_all()

@jwt.token_in_blacklist_loader
def verify_token_blacklist(token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_invalid():
    return jsonify({'message':'You have been logged out.'}), 401

api.add_resource(Tests, '/tests')
api.add_resource(Test, '/tests/<int:id>')
api.add_resource(User, '/users/<int:id>')
api.add_resource(UserRegister, '/new')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__=='__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)

