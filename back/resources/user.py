from flask_restful import Resource, reqparse
from models.user import User
from flask_jwt_extended import jwt_required
class Users(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument("name", required = True, type = str)
    parse.add_argument("login", required = True, type = str) 
    parse.add_argument("password", required = True, type = str)

    def post(self):
        args = Users.parse.parse_args()
        user = User(**args)
        try:
            user.save()
            return user.serial(), 201
        except:
            return {"message":"error"}, 500
    @jwt_required
    def get(self, id):
        user = User.find_user(id)
        if user:
            return user.serial(), 200
        return {"message":"not found"}, 404
    @jwt_required
    def put(self, id):
        args = Users.parse.parse_args()
        user = User.find_user(id)
        if user:
            try:
                user.update(**args)
                user.save()
                return {"message": "atualizado"}, 200
            
            except:
                return {"message": "error intern"}, 500
        return {"message": "not found"}, 404
    
    def delete(self):
        """
        caso existisse um adm o usuario só seria desativado
        """
        return {"message": "not found"}, 404