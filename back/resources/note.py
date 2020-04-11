from flask_restful import Resource,reqparse
from models.note import Note

class Notes(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument("text", required=True, type=str)
    parse.add_argument("key_user", required= False, type=int)

    def post(self):
        arqs = Notes.parse.parse_args()
        note = Note(**arqs)
        try:
            note.save()
            return note.serial(), 201
        except:
            return {"message": "error"}, 500
    
    def get(self, id):
        notes = Note.find_note_key_user(id)
        if notes:
            return [n.serial() for n in notes], 200
        return {"message": "not found"}, 404
    
    def put(self, id):
        note = Note.find_note(id)
        text = Notes.parse.parse_args()["text"]
        if note:
            try:
                note.update(text)
                note.save()
                return {"message": "ok"}, 200
            except:
                return {"message": "error intern"}, 500
        return {"message": "not found"}, 404 
            
    
    def delete(self, id):
        note = Note.find_note(id)
        if note:
            try:
                note.delete()
                return {"message": "delete note"}, 200
            except:
                return {"message": "error intern"}, 500
        return {"message":"not found"}, 404