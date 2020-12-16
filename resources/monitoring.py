from flask_restful import Resource, reqparse
from models.monitoring import MonitoringModel

class  Monitoring(Resource):

    arguments = reqparse.RequestParser()
    
    arguments.add_argument('identifier', type=str, required=True, help="This field 'token' cannot be left.")
    
    def get(self, identifier):

        monitoring= MonitoringModel.find_by_identifier(identifier)
        if monitoring:
            return monitoring.json()
        return {'message': 'Monitoring not found'}, 404
           



