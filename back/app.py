from flask import Flask
from flask_jwt_extended import JWTManager  
from flask_restful import Api
from database import db
from resources.note import Notes
from resources.user import Users
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///base.sql"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = ""
app.config['JWT_BLACKLIST_ENABLED'] = True
jwt = JWTManager(app)
db.init_app(app)
@app.before_first_request
def create_data():
    db.create_all()
    

api.add_resource(Users,"/api/user","/api/user/<int:id>")
api.add_resource(Notes, "/api/notes", "/api/notes/<int:id>")
if __name__ == '__main__':
    app.debug = True
    app.run()
    
