from flask_restful import Resource, reqparse
from models.test import TestModel

class Tests(Resource):
    def get(self):
        return {'tests':[test.json() for test in TestModel.query.all()]}

class Test(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('duration')
    argumentos.add_argument('fhr_valeu')
    argumentos.add_argument('token', type=str, required=True, help="This field 'token' cannote be left ")
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
        try:
            test.save_test()
        except:
            return {'message': 'An internal error ocurred trying to save test'}, 500
        
        return test.json(), 200
    
    def put(self, id):
        data = Test.argumentos.parse_args()
                
        test_find = TestModel.find_test(id)
        if test_find:
            test_find.update_test(**data)
            test_find.save_test()
            return test_find.json(), 200

        test = TestModel(id, **data)
        try:
            test.save_test()
        except:
            return {'message': 'An internal error ocurred trying to save test'}, 500
        
        return test, 201

    def delete(self, id):
        test = TestModel.find_test(id)
        if test:
            try:
                test.delete_test()
            except:
                return {'message': 'An internal error ocurred trying to delete test'}, 500
            return {'message': 'Test deleted.'}

        return {'message': 'Test not deleted'}, 404