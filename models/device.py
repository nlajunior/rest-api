from sql_alchemy import db


class DeviceModel(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(100))
    date_created = db.Column(db.DateTime(6))
    status = db.Column(db.String(2))
    tests = db.relationship('TestModel') #lista de objetos tests

    def __init__(self, mac, date_created, status):
        self.mac = mac
        self.date_created = date_created
        self.status = status
    
    def json(self):
        return {
            'id': self.id,
            'mac': self.mac,
            #'date_created': str(self.date_created),
            #'status': self.status,
            'tests':[test.json() for test in self.tests]
        }
    
    @classmethod
    def find_device(cls, mac):
        device =  cls.query.filter_by(mac=mac).first()
        if device:
            return device
        return None
    
    @classmethod
    def find_by_id(cls, id):
        device =  cls.query.filter_by(id=id).first()
        if device:
            return device
        return None
    
    @classmethod
    def find_device_online(cls, status='ON'):
        device = cls.query.filter_by(status=status).all()
        if device:
            return device
        return None
    
    def save_device(self):
        db.session.add(self)
        db.session.commit()

    def update_device(self, mac, status):
        self.duration = duration
        self.fhr_valeu = fhr_valeu
        self.token = token
        self.date_created =  date_created
        self.device_id = device_id
    
    def delete_device(self):
        [test.delete() for test in self.tests]
        db.session.delete(self)
        db.session.commit()
