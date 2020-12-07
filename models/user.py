from sql_alchemy import db

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    organization_key = db.Column(db.String(200))
    email = db.Column(db.String(100), nullable=False, unique=True)
    actived = db.Column(db.Boolean, default=False)

    def __init__(self, login, password, organization_key, email,actived):
        self.login = login
        self.password = password
        self.organization_key = organization_key  
        self.email = email
        self.actived= actived      
    
    def json(self):
        return {
            'login': self.login,
            'organization_key': self.organization_key,
            'email':self.email,
            'actived': self.actived           
        }

    @classmethod
    def find_user(cls, id):
        user = cls.query.filter_by(id=id).first()
        print(user.actived)
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, organization_key):
        user = cls.query.filter_by(organization_key=organization_key).first()
        if user:
            return user
        return None
    
    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        return None

    def save_user(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()