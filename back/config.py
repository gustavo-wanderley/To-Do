import json

with open('settings.json') as json_arq:
    config = json.load(json_arq)

DATABASE_URL = config.get('Data_base_uri')
SECRET_KEY = config.get("key_secret")
TRACK_MODIFICATIONS = config.get("track_modifications")
JWT_ENABLE = config.get("enable_jwt")
