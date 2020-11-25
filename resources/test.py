from flask_restful import Resource, reqparse
from models.test import TestModel

tests = [
    {
        'id': 1,
        'duration': 12,
        'fhr_valeu':132,
        'token': 'AA:BB:CC:DD:EE:901',
        'date_created': '2020-11-25',
        'device_id': 1 
    },
    {
        'id': 2,
        'duration': 19,
        'fhr_valeu':132,
        'token': 'AA:BB:CC:DD:EE:901',
        'date_created': '2020-11-25',
        'device_id': 1 
    }
  
]

class Tests(Resource):
    def get(self):
        return {'tests':tests}

class Test(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('duration')
    argumentos.add_argument('fhr_valeu')
    argumentos.add_argument('token')
    argumentos.add_argument('date_created')
    argumentos.add_argument('device_id')
   
    def find_test(id):
        for test in tests:
            if test['id']==id:
                return test
        return None
    
    def get(self, id):
        test = Test.find_test(id)
        if test:
            return test
        return {'message': 'Test not found'}, 404

    def  post(self, id):
        data = Test.argumentos.parse_args()
        test_object = TestModel(id, **data)
        new_test = test_object.json()
        #novo_test = { 'id':id, **data }
  
        tests.append(new_test)
        return new_test, 200
    
    def put(self, id):
        data = Test.argumentos.parse_args()
        test_object = TestModel(id, **data)
        new_test = test_object.json()
        #novo_test = { 'id':id, **data }

        test = Test.find_test(id)
        if test:
            test.update(new_test)
            return new_test, 200

        tests.append(new_test)
        return new_test, 201

    def delete(self, id):
        global tests
        tests =[test for test in tests if test['id']!=id]
        return {'message':'Test deleted'}