from sql_alchemy import db
from datetime import date


class MonitoringModel(db.Model):
    __tablename__ = 'monitoring'

    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(60), unique=True)
    date_created = db.Column(db.DateTime(6), nullable=True)
    status = db.Column(db.Boolean)
    device_id = db.Column(db.String(30))
    tests = db.relationship('TestModel') 

    def __init__(self, identifier, status, device_id):
        self.identifier = identifier
        self.device_id = device_id
        self.date_created=date.today()
        self.status = status
    
    def json(self):
        return {
            #'id': self.id,
            'monitor_id': self.identifier,
            'status':self.status,
            'tests':[test.json() for test in self.tests]
        }
    
    @classmethod
    def find_by_identifier(cls, identifier):
        print(identifier)
        monitoring =  cls.query.filter_by(identifier=identifier).first()
        if monitoring:
            return monitoring
        return None
    
    @classmethod
    def find_by_id(cls, id):
        monitoring =  cls.query.filter_by(id=id).first()
        if monitoring:
            return monitoring
        return None
    
    @classmethod
    def find__running(cls, status=True):
        monitoring = cls.query.filter_by(status=status).all()
        if monitoring:
            return monitoring
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
