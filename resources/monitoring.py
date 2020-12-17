from flask_restful import Resource, reqparse
from models.monitoring import MonitoringModel

class  Monitoring(Resource):

    arguments = reqparse.RequestParser()
    
    arguments.add_argument('identifier', type=str, required=True, help="This field 'identifier' cannot be left.")
    arguments.add_argument('status', type=bool, required=True, help="This field 'status' cannot be left.")
    arguments.add_argument('device_id', type=str, required=True, help="This field 'device_id' cannot be left.")
    
    def get(self, identifier):

        monitoring= MonitoringModel.find_by_identifier(identifier)

        if monitoring:
            return monitoring.json()
        return {'message': 'Monitoring not found'}, 404
           
    def post(self):
        data = Monitoring.arguments.parse_args()
        monitoring = MonitoringModel(**data)
        print(data)

        if  monitoring.find_by_identifier(data['identifier']):
            return {"message": "The monitoring already exists."}, 400

        try:
            monitoring.save()
        except:
            return {"message": 'An internal error ocurred trying to create a new monitoring.'}, 500
        
        return monitoring.json()

    def put(self):
        pass 


