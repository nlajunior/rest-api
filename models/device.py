from sql_alchemy import db

class DeviceModel(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(100))
    date_created = db.Column(db.DateTime(6))
    status = db.Column(db.String(2))

    def __init__(self, id, mac, date_created, status):
        self.id = id
        self.mac = mac
        self.date_created = date_created
        self.status = status
    
    def json(self):
        return {
            'id': self.id,
            'mac': self.mac,
            'date_created': str(self.date_created),
            'status': self.status
        }
