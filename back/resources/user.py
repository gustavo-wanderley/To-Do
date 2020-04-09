from flask_restful import Resource, reqparse
from models.user import User
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
    
