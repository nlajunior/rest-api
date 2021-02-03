import json

class Identifier:

    def __init__(self, last_id):
        self._last_id = None
        self._new_id = None

    @property
    def last_id(self):
        return self._last_id

    
            
    def json(self):
        return {
            'last_id': self._last_id,
          } 
  