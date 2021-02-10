from sql_alchemy import db
from datetime import date
from sqlalchemy import asc, desc, and_

class TestModel(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Integer)
    fhr_value = db.Column(db.Float)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
    identifier = db.Column(db.String(60), db.ForeignKey('monitoring.identifier'))
    device_id = db.Column(db.String(30), db.ForeignKey('device.mac'))
    status = db.Column(db.Boolean, default=0)
    #device = bd.relationship('DeviceModel')

    def __init__(self, duration, fhr_value, date_created, identifier,  device_id):
               
        self.duration=duration
        self.fhr_value = fhr_value
        if date_created==None:
            self.date_created = date.today()
        else:
            self.date_created = date_created
        self.identifier = identifier
        self.device_id = device_id
        self.status=0
        
    def json(self):
        return {
            'duration': self.duration,
            'fhr_value': self.fhr_value,
            'identifier': self.identifier            
        }

    @classmethod
    def update_by_id(cls, id_list):
        if not len(id_list)==0:
            parametros = str(id_list)
            parametros = (parametros.replace("[", " ", 2)).replace("]", " ", 2)
                    
            update_sql=f'update db.test set status=1 where id in ({parametros})'
            try:
                db.session.execute(update_sql)
                db.session.commit()
                return True

            except Exception as e:
                db.session.rollback()
                return False
               
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
    
    @classmethod
    def find_by_list(cls, list_id, limit=None):
        if not limit==None:
            tests =  cls.query.order_by(asc(cls.identifier), cls.duration).filter(and_(cls.identifier.in_(list_id), cls.status==0, cls.date_created==str(date.today()))).limit(limit).all()
        else:
            tests =  cls.query.order_by(asc(cls.identifier), cls.duration).filter(and_(cls.identifier.in_(list_id), cls.status==0, cls.date_created==str(date.today()))).all()
                    
        return tests
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()