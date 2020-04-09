from flask import Flask
from flask_restful import Api
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///base.sql"

if __name__ == '__main__':
    app.debug = True
    app.run()
    
