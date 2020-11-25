class TestModel:
    def __init__(self, id, duration, fhr_valeu, token, date_created, device_id):
        self.id = id
        self.duration = duration
        self.fhr_valeu = fhr_valeu
        self.token = token
        self.date_created =  date_created
        self.device_id = device_id
    
    def json(self):
        return {
            'id': self.id,
            'duration': self.duration,
            'fhr_valeu': self.fhr_valeu,
            'token': self.token,
            'date_created': self.date_created,
            'device_id': self.device_id
        }