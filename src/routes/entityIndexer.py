from flask import request

from src.helpers.staticHelper import StaticHelper
from src.routes.interfaces.iEntityIndexerLogic import IEntityIndexerLogic

class EntityIndexer:
    def __init__(self, app, entityIndexerLogic):
        self.entityIndexerLogic = entityIndexerLogic
        StaticHelper.isInterfaceResloved(self.entityIndexerLogic, IEntityIndexerLogic)

        self.setRoutes(app)

    def setRoutes(self, app):
        app.add_url_rule('/create', 'Create Entity', self.create, methods = ['POST'])

    def create(self):
        self.entityIndexerLogic.createIndex(request.json)
        return '', 201
