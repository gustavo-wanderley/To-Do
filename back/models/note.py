from database import db
from sqlalchemy import Column, Integer, String, ForeignKey
class Note(db.Model):
    __tablename__ = "notes"
    id_note = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(500))
    key_user = Column(Integer, ForeignKey("users.id"))
    def __init__(self, text, key_user):
        self.text = text
        self.key_user = key_user

    def serial(self):
        return {
            "id_note": self.id_note,
            "text": self.text
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, text):
        self.text = text

    @classmethod
    def find_note_key_user(cls, id):
        notes = cls.query.filter_by(key_user = id).all()
        if notes:
            return notes
        return None

    @classmethod
    def find_note(cls, id):
        note = cls.query.filter_by(id_note = id).first()
        if note:
            return note
        return None