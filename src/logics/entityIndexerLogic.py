from src.helpers.staticHelper import StaticHelper
from src.routes.interfaces.iEntityIndexerLogic import IEntityIndexerLogic
from src.logics.interfaces.iIndexingAlgorithm import IIndexingAlgorithm
from src.logics.interfaces.iEntityData import IEntityData

class EntityIndexerLogic(IEntityIndexerLogic):
    def __init__(self, indexingAlgorithm, entityData):
        self.indexingAlgorithm = indexingAlgorithm
        StaticHelper.isInterfaceResloved(self.indexingAlgorithm, IIndexingAlgorithm)
        self.entityData = entityData
        StaticHelper.isInterfaceResloved(self.entityData, IEntityData)


    def createIndex(self, data):
        self.indexingAlgorithm.createIndex({}, 1, 1, '', '')
        #self.entityData.insertEntityNode()
        #self.entityData.setData(data)
        #dataNodeId = self.entityData.insertEntityNode()
        #print(rootId)
        #self.indexingAlgorithm.createIndex(data, rootId, dataNode.GetNodeId(), '', '')

