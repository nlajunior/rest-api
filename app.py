from flask import Flask
from flask_restful import Api
from resources.test import Tests, Test

app = Flask(__name__)
api = Api(app)
    
api.add_resource(Tests, '/tests')
api.add_resource(Test, '/tests/<int:id>')

if __name__=='__main__':
    app.run(debug=True)
