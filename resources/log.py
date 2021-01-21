from flask_restful import Resource, reqparse
from models.log import LogModel

class  Logs(Resource):

    def get(self):
        try:
            return {'logs': [log.json() for log in LogModel.get_log('80:7D:3A:DA:D9:F5')]}
        except:
            return {'message':'Device not found.'}, 404 

class Log(Resource):
    arguments_log = reqparse.RequestParser()
    arguments_log.add_argument('device_id', type=str, required=True, help="This field MAC cannot be left.")
    arguments_log.add_argument('date_created', type=str, required=False, help="This field 'date' cannot be left.")
    arguments_log.add_argument('level_error', type=int, required=True, help="This field 'level' cannot be left.")
    arguments_log.add_argument('message', type=str, required=False, help="This field 'message' cannot be left.")

    
    def post(self):
        data = Log.arguments_log.parse_args()
        log = LogModel(**data)
        try:
            log.save_log()
        except:
            return {'message': 'An internal error ocurred trying to save log'}, 500
                
        return log.json(), 200
       