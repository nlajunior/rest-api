from flask_restful import Resource, reqparse

from helper import *
import json

class Identifier(Resource):

    def get(self):
        with open('invalid_id.json') as file_json:
            dict_last_id = json.load(file_json)

            invalid_id = dict_last_id.get('id')
            print(invalid_id)
            last_id = invalid_id
            file_json.close()
        
        new_id = get_id_monitoring(1, last_id)
        
        dict_last_id = {"id": new_id}
        print(dict_last_id)

        with open('invalid_id.json', 'w') as json_file:
            json.dump(dict_last_id, json_file, indent=4)
                        
        return {
            "id":new_id
            }


            
            

          
        


        
        #list_value = []
        
        #value_id = str(Identifier.get_id_json())
        #old_id = get_invalid_id()

        #new_id = get_id_monitoring(1, old_id)
        #save(new_id)

        #return {"new_id": new_id}

        #identifier = Identifier(list_value)
        #identifier.save()

        #id_obj = uuid.uuid4()
        #valor =  id_obj.time_mid
        #BLACKLIST.add(valor)
        #id = Identifier(valor)
        #with open('blacklist.json', 'w') as json_file:
        #    json.dump(id.json(), json_file, indent=4) DAZZEABG

        #return identifier.json()