from sql_alchemy import db
from sqlalchemy import desc, and_
from datetime import date


class MonitoringModel(db.Model):
    __tablename__ = 'monitoring'

    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(60), unique=True)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
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
            
            'identifier': self.identifier,
            'status':self.status,
            #'tests':[test.json() for test in self.tests]
        }
    
    @classmethod
    def find_by_identifier(cls, identifier):
        print(identifier)
        monitoring =  cls.query.filter_by(identifier=identifier).first()
        if monitoring:
            return monitoring
        return None
    
    @classmethod
    def find_by_id(cls, identifier):
        monitoring =  cls.query.filter_by(identifier=identifier).first()
       
        if monitoring:
            return monitoring
        return None
    
    @classmethod
    def find__running(cls, status=True):
        monitoring = cls.query.order_by(desc(cls.id)).filter(and_(cls.status==1,cls.date_created==str(date.today()))).limit(250).all()
        return monitoring
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, status=False):
        self.status = status
        
    def delete(self):
        [test.delete() for test in self.tests]
        db.session.delete(self)
        db.session.commit()
