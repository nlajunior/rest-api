from sql_alchemy import db
from datetime import date


class DeviceModel(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(30), unique=True)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
    status = db.Column(db.String(3))
    #tests = db.relationship('TestModel') #lista de objetos tests
    #monitoring = db.relationship('MonitoringModel')

    def __init__(self, mac, status):
        self.mac = mac
        self.date_created = str(date.today())
        self.status = status
    
    def json(self):
        return {
            'id': self.id,
            'mac': self.mac,
            'status':self.status #,
            #'tests':[test.json() for test in self.tests]
        }
    
    @classmethod
    def find_by_mac(cls, mac):
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
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, status):
        self.status = status  
        
    def delete(self):
        [test.delete() for test in self.tests]
        db.session.delete(self)
        db.session.commit()