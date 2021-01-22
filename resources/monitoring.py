from flask_restful import Resource, reqparse
from models.monitoring import MonitoringModel

class  Monitoring(Resource):

    arguments_monitoring = reqparse.RequestParser()
    arguments_monitoring.add_argument('identifier', type=str, required=True, help="This field 'identifier' cannot be left.")
    arguments_monitoring.add_argument('status', type=bool)
    arguments_monitoring.add_argument('device_id', type=str)
    
    def get(self):
        try:
            return {'list': [monitoring.json() for monitoring in MonitoringModel.find__running(status=True)]}
        except:
            return {"message": "Not found."}, 400
         
    def post(self):
        data = Monitoring.arguments_monitoring.parse_args()
        monitoring = MonitoringModel(**data)
       
        if  monitoring.find_by_identifier(data['identifier']):
            return {"message": "The monitoring already exists."}, 400
        try:
            monitoring.save()
        except:
            return {"message": 'An internal error ocurred trying to create a new monitoring.'}, 500
        return monitoring.json()

    def put(self):
        data = Monitoring.arguments_monitoring.parse_args() 

        monitoring_find = MonitoringModel.find_by_identifier(data['identifier'])
        
        if monitoring_find:
            monitoring_find.update(status=False)
            monitoring_find.save()
            return monitoring_find.json(), 200

        monitoring = MonitoringModel(**data)
        try:
            monitoring.save()
        except:
            return {'message': 'An internal error ocurred trying to save monitoring'}, 500
        return monitoring, 201



