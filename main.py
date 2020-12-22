from flask import Flask
from src.routes.entityIndexer import entityIndexerApis

app = Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(entityIndexerApis)

app.run()