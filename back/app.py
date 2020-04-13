from flask import Flask
from flask_jwt_extended import JWTManager  
from flask_restful import Api
from database import db
from resources.note import Notes
from resources.user import Users
from resources.acess import Login, Logout
from config import *
import black_list
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///base.sql"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = TRACK_MODIFICATIONS
app.config["JWT_SECRET_KEY"] = SECRET_KEY
app.config['JWT_BLACKLIST_ENABLED'] = JWT_ENABLE
jwt = JWTManager(app)
db.init_app(app)
@app.before_first_request
def create_data():
    db.create_all()


@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in black_list.BLACK_LIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return {'message': 'acess revogad'}, 401 

    
api.add_resource(Login, "/api/")
api.add_resource(Logout, "/api/exit")
api.add_resource(Users,"/api/user","/api/user/<int:id>")
api.add_resource(Notes, "/api/notes", "/api/notes/<int:id>")
if __name__ == '__main__':
    app.debug = True
    app.run()
    
