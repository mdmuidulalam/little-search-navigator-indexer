from src.helpers.staticHelper import StaticHelper
from src.routes.interfaces.iEntityIndexerLogic import IEntityIndexerLogic
from src.logics.interfaces.iIndexingAlgorithm import IIndexingAlgorithm
from src.logics.interfaces.iEntityData import IEntityData
from src.logics.interfaces.iIndexingData import IIndexingData

class EntityIndexerLogic(IEntityIndexerLogic):
    def __init__(self, indexingAlgorithm, entityData, indexingData):
        self.indexingAlgorithm = indexingAlgorithm
        StaticHelper.isInterfaceResloved(self.indexingAlgorithm, IIndexingAlgorithm)
        self.entityData = entityData
        StaticHelper.isInterfaceResloved(self.entityData, IEntityData)
        self.indexingData = indexingData
        StaticHelper.isInterfaceResloved(self.indexingData, IIndexingData)

    def createIndex(self, data):
        self.entityData.setData(data)
        #dataNodeId = self.entityData.insertEntityNode()
        #print(rootId)
        #self.indexingAlgorithm.createIndex(data, rootId, dataNode.GetNodeId(), '', '')

