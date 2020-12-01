from flask import Flask
from flask_restful import Api

from resources.test import Tests
from resources.test import Test

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']= 'tautomeria'

api = Api(app)

@app.before_first_request
def cria_banco():
    db.create_all()

api.add_resource(Tests, '/tests')
api.add_resource(Test, '/tests/<int:id>')

if __name__=='__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)

