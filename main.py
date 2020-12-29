from flask import Flask

from src.routes.entityIndexer import EntityIndexer

from src.logics.entityIndexerLogic import EntityIndexerLogic

app = Flask(__name__)
app.config["DEBUG"] = True

EntityIndexer(
    app = app,
    entityIndexerLogic =  EntityIndexerLogic()
)

app.run()