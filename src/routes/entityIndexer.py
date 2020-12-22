from flask import Blueprint

entityIndexerApis = Blueprint('entityIndexerApis', __name__)

@entityIndexerApis.route('/')
def hello():
    return 'Hello, Little Search Navigator!'
