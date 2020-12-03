import json

with open('credentials.json') as file_json:
    config = json.load(file_json)

PORT = config.get('PORT')
HOST = config.get('HOST')
USERDB = config.get('USERDB')
PASSWORD = config.get('PASSWORD')
DATABASE = config.get('DATABASE')
JWT_SECRET_KEY =config.get('JWT_SECRET_KEY')
