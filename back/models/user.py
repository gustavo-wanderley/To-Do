from database import db
from sqlalchemy import Column, Integer, String, Boolean
class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    name = Column(String(90), nullable = False)
    login = Column(String(90), nullable = False)
    password = Column(String(80), nullable = False)
    
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    def serial(self):
        return {
            "name": self.name,
            "login": self.login,
            "password": self.password
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def check_password(self, password):
        return self.password == password:
            
    @classmethod
    def find_user(cls, login):
        user = cls.query.filter_by(login = login).first()
        if user:
            return user
        return None
