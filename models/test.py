from sql_alchemy import db

class TestModel(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Integer)
    fhr_valeu = db.Column(db.Integer)
    token = db.Column(db.String(100))
    date_created = db.Column(db.DateTime(6))
    device_id = db.Column(db.Integer)

    def __init__(self, id, duration, fhr_valeu, token, date_created, device_id):
        self.id = id
        self.duration = duration
        self.fhr_valeu = fhr_valeu
        self.token = token
        self.date_created = date_created
        self.device_id = device_id
    
    def json(self):
        return {
            'id': self.id,
            'duration': self.duration,
            'fhr_valeu': self.fhr_valeu,
            'token': self.token,
            'date_created': str(self.date_created),
            'device_id': self.device_id
        }

    @classmethod
    def find_test(cls, id):
        test = cls.query.filter_by(id=id).first()
        if test:
            return test
        return None
    
    def save_test(self):
        db.session.add(self)
        db.session.commit()

    def update_test(self, duration, fhr_valeu, token, date_created, device_id):
        self.duration = duration
        self.fhr_valeu = fhr_valeu
        self.token = token
        self.date_created =  date_created
        self.device_id = device_id
    
    def delete_test(self):
        db.session.delete(self)
        db.session.commit()

