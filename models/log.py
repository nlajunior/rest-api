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
