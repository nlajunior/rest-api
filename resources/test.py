from flask_restful import Resource, reqparse
from models.test import TestModel
from models.device import DeviceModel
from flask_jwt_extended import jwt_required
from resources.filters import *
from config import *

import mysql.connector
from datetime import date

path_params = reqparse.RequestParser()

path_params.add_argument('fhr_value_min', type=float)
path_params.add_argument('fhr_value_max', type=float)
path_params.add_argument('limit', type=int)
path_params.add_argument('offset', type=int)

#Ok
class Tests(Resource):
    

    @jwt_required
    def get(self):
        data = path_params.parse_args()
        data_valid = {key:data[key] for key in data if data[key] is not None}
        parameters = normalize_path_params(**data_valid)
        
        conn = mysql.connector.connect(user=config.get('USERDB'), password= config.get('PASSWORD') , host=config.get('HOST'), database=config.get('DATABASE'))
        cursor=conn.cursor()
       
        tupla = tuple([parameters[chave] for chave in parameters])
        
        cursor.execute(query_test, tupla)
        result = cursor.fetchall()
       
        tests_list = []
        if result:
            for linha in result:
                tests_list.append({
                    'id': linha[0],
                    'duration': linha[1],
                    'fhr_value': linha[2],
                    'date_created':linha[3].strftime('%d/%m/%Y') ,
                    'identifier': linha[4],
                    'device_id': linha[5]
                })
            return {"tests": tests_list}
        
 
class Test(Resource):
    arguments_test = reqparse.RequestParser()
    arguments_test.add_argument('duration')
    arguments_test.add_argument('fhr_value')
    arguments_test.add_argument('identifier', type=str, required=True, help="This field 'identifier' cannot be left.")
    arguments_test.add_argument('date_created')
    arguments_test.add_argument('device_id', type=str, required=True, help="Every test to be linked with a device.")
       
    def get(self, id):
        test = TestModel.find_by_id(id)
        if test:
            return test.json()
        return {'message': 'Test not found'}, 404


    #@jwt_required
    def  post(self):
        #if TestModel.find_test(id):
         #   return {"message": "Test id '{}' already exists.".format(id)}, 400
        
        data = Test.arguments_test.parse_args()
        test = TestModel(**data)
        
        if not DeviceModel.find_by_mac(data['device_id']):
            return {'message': 'Device id invalid.'}, 400
        try:
            test.save()
        except:
            return {'message': 'An internal error ocurred trying to save test'}, 500
        
        return test.json(), 200
    
    
class TestsSession(Resource):
    
    @jwt_required
    def get(self, identifier):
        try:
            return {'tests':[test.json() for test in TestModel.find_by_identifier(identifier)]} 
        except:
            return {'message': 'Tests not found'}, 404