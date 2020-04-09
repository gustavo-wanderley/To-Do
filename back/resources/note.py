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
    
    def get(self):
        pass
    
    def put(self, id):
        pass
    
    def delete(self, id):
        pass