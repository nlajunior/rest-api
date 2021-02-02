from flask_restful import Resource, reqparse

from helper import *
import json

class Identifier(Resource):

    def get(self):
        with open('invalid_id.json') as file_json:
            dict_last_id = json.load(file_json)

            invalid_id = dict_last_id.get('id')
            last_id = invalid_id
            file_json.close()
        
        new_id = get_id_monitoring(1, last_id)
        dict_last_id = {"id": new_id}
       
        with open('invalid_id.json', 'w') as json_file:
            json.dump(dict_last_id, json_file, indent=4)
                        
        return {
            "id":new_id
            }