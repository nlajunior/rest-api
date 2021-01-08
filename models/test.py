from sql_alchemy import db
from datetime import date


class TestModel(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Integer)
    fhr_value = db.Column(db.Float)
    date_created = db.Column(db.DateTime(6))
    identifier = db.Column(db.String(60), db.ForeignKey('monitoring.identifier'))
    device_id = db.Column(db.String(30), db.ForeignKey('device.mac'))
    #device = bd.relationship('DeviceModel')

    def __init__(self, duration, fhr_value, date_created, identifier,  device_id):
        
        self.duration = duration
        self.fhr_value = fhr_value
        if date_created==None:
            self.date_created = date.today()
        else:
            self.date_created = date_created
        self.identifier = identifier
        self.device_id = device_id
    
    def json(self):
        return {
            'id': self.id,
            'duration': self.duration,
            'fhr_value': self.fhr_value,
            'date_created': (self.date_created.strftime('%d/%m/%Y')),
            'monitor_id': self.identifier,            
            'device_id': self.device_id
        }

    @classmethod
    def find_by_id(cls, id):
        test = cls.query.filter_by(id=id).first()
        if test:
            return test
        return None
    
    @classmethod
    def find_by_date(cls, date_created):
        test = cls.query.filter_by(date_created=date_created).all()
        if test:
            return test
        return None
    
    @classmethod
    def find_by_identifier(cls, identifier):
        test = cls.query.filter_by(identifier=identifier).all()
        if test:
            return test
        return None
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, duration, fhr_value, date_created, identifier, device_id):
        self.duration = duration
        self.fhr_valeu = fhr_value
        self.date_created =  date_created
        self.identifier = identifier
        self.device_id = device_id
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

