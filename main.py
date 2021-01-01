from flask import Flask
import json
import neo4j

from src.routes.entityIndexer import EntityIndexer

from src.logics.entityIndexerLogic import EntityIndexerLogic
from src.logics.suffixTreeIndexing import SuffixTreeIndexing
from src.logics.trie import Trie

from src.data.entityData import EntityData
from src.data.indexingData import IndexingData

with open("config.json") as jsonDataFile:
    config = json.load(jsonDataFile)
neo4jDriver = neo4j.GraphDatabase.driver(config["neo4j"]["url"], auth=(config["neo4j"]["user"], config["neo4j"]["password"]))

app = Flask(__name__)
app.config["DEBUG"] = True

EntityIndexer(
    app = app,
    entityIndexerLogic =  EntityIndexerLogic(
        indexingAlgorithm = SuffixTreeIndexing(
            trie = Trie()
        ),
        entityData = EntityData(neo4jDriver),
        indexingData = IndexingData(neo4jDriver)
    )
)

app.run()