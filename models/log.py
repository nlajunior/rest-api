from sql_alchemy import db

class LogModel(db.Model):
    __tablename__ = 'log_error'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(30))
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
    level_error =  db.Column(db.Integer)
    message = db.Column(db.String(100), nullable=False)
    
    def __init__(self, device_id, date_created, level_error, message):
        self.device_id = device_id
        self.date_created = date_created
        self.level_error = level_error  
        self.message = message

    def json(self):
        return {
            'device_id': self.device_id,
            'date_created': (self.date_created.strftime('%d/%m/%Y')),
            'level_error':self.level_error,
            'message': self.message           
        } 
    #db.session.query(Medicao).order_by(desc(Medicao.id)).filter(Medicao.date_created==str(date.today())).limit(limit).all()
    @classmethod
    def get_log(cls, device_id):
        log =  cls.query.filter_by(device_id=device_id).all()
        log2 = cls.query.order_by(cls.level_error).limit(2).all()
        return log2

    def save_log(self):
        db.session.add(self)
        db.session.commit()