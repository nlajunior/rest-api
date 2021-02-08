from flask_restful import Resource, reqparse
from models.device import DeviceModel

class  Devices(Resource):

    def get(self):
        try:
            return {'devices': [device.json() for device in DeviceModel.find_device_online()]}
        except:
            return {'message':'Device not found.'}, 404       

class Device(Resource):

    arguments_device = reqparse.RequestParser()
    arguments_device.add_argument('mac', type=str, required=True, help="This field MAC cannot be left.")
    arguments_device.add_argument('status', type=str, required=False, help="This field 'status' cannot be left.")
    
    def get(self):
        data = Device.arguments_device.parse_args()
        device = DeviceModel.find_by_mac(data['mac'])
        if device:
            return device.json()
        return {'message':'Device not found.'}, 404

    def post(self):
        data =  Device.arguments_device.parse_args()
        if DeviceModel.find_by_mac(data['mac']):
            return {"message": "The device {} already exists."}, 400

        device = DeviceModel(data['mac'], "ON")
        try:
            device.save()
        except:
            return {"message": 'An internal error ocurred trying to create a new device.'}, 500
        return device.json()

    def put(self):
        data = Device.arguments_device.parse_args() 

        device_find = DeviceModel.find_by_mac(data['mac'])
        if device_find:
            device_find.update(data['status'])
            device_find.save()
            return device_find.json(), 200

        device = DeviceModel(**data)
       
        try:
            device.save()
        except:
            return {'message': 'An internal error ocurred trying to save device'}, 500
        return device, 201

   
