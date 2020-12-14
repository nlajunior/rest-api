from flask_restful import Resource, reqparse
from models.test import TestModel
from models.device import DeviceModel
from flask_jwt_extended import jwt_required
#from filtros import *
import mysql.connector
from datetime import date

path_params = reqparse.RequestParser()
path_params.add_argument('session_id', type=str)
path_params.add_argument('fhr_value_min', type=float)
path_params.add_argument('fhr_value_max', type=float)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)

#Ok
class Tests(Resource):
    @jwt_required
    def get(self):
        try:
            return {'tests':[test.json() for test in TestModel.find_by_date(date.today())]} 
        except:
            return {'message': 'Tests not found'}, 404
   

class Test(Resource):
    arguments_test = reqparse.RequestParser()
    arguments_test.add_argument('duration')
    arguments_test.add_argument('fhr_value')
    arguments_test.add_argument('session_id', type=str, required=True, help="This field 'token' cannot be left.")
    arguments_test.add_argument('date_created')
    arguments_test.add_argument('device_id', type=int, required=True, help="Every test to be linked with a device.")
       
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
        
        if not DeviceModel.find_by_id(data['device_id']):
            return {'message': 'Device id invalid.'}, 400
        try:
            test.save()
        except:
            return {'message': 'An internal error ocurred trying to save test'}, 500
        
        return test.json(), 200
    
    
class TestsSession(Resource):
    
    @jwt_required
    def get(self, session_id):
        try:
            return {'tests':[test.json() for test in TestModel.find_by_session(session_id)]} 
        except:
            return {'message': 'Tests not found'}, 404
