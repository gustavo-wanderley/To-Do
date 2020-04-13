from flask_restful import Resource, reqparse
from models.user import User
import black_list
from flask_jwt_extended import  create_access_token, jwt_required, get_raw_jwt
class Login(Resource):
    @classmethod
    def post(cls):
        parse = reqparse.RequestParser()
        parse.add_argument("login", type= str, required= True)
        parse.add_argument("password", type= str, required= True)
        login = parse.parse_args()["login"]
        password = parse.parse_args()["password"]
        user = User.find_user_login(login)
        if user:
            try:
                if user.check_password(password):
                    token =  create_access_token(identity = user.id)
                    return {
                        "id": user.id,
                        "token":token
                        }, 200
                else:
                    return {"message": "password incorrect"}, 401

            except:
                return {"message": "error login"}, 500
        
        return {"message", "user email not registrer"}, 404

class Logout(Resource):
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti'] 
        black_list.BLACK_LIST.add(jwt_id)
        return {'message': 'saiu com sucesso'}, 200