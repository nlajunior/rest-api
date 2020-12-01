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
   
    def get(self, id):
        test = TestModel.find_test(id)
        if test:
            return test.json()
        return {'message': 'Test not found'}, 404

    def  post(self, id):
        if TestModel.find_test(id):
            return {"message": "Test id '{}' already exists.".format(id)}, 400
        
        data = Test.argumentos.parse_args()
        test = TestModel(id, **data)
        #new_test = test_object.json()
        #novo_test = { 'id':id, **data }
        #tests.append(new_test)
        test.save_test()

        return test.json(), 200
    
    def put(self, id):
        data = Test.argumentos.parse_args()
                
        test_find = TestModel.find_test(id)
        if test_find:
            test_find.update_test(**data)
            test_find.save_test()
            return test_find.json(), 200

        test = TestModel(id, **data)
        test.save_test()
        return test, 201

    def delete(self, id):
        global tests
        tests =[test for test in tests if test['id']!=id]
        return {'message':'Test deleted'}