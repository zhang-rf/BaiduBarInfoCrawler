from tools.MySqlDBHelper import MySqlDBHelper
from tools.ConfigReader import ConfigReader
from database.Model import *

class Database(object):
    def __init__(self,path):
        self._cfr = ConfigReader(path)
        self.db = None
        self._readDBConfig()

    def _readDBConfig(self):
        host = self._cfr.readFirstConfig('host')
        user = self._cfr.readFirstConfig('user')
        password = self._cfr.readFirstConfig('password')
        db = self._cfr.readFirstConfig('db')
        port = self._cfr.readFirstConfig('port')
        self.db = MySqlDBHelper(host,user,password,db,int(port))
        # self._initDatabase()

    def _initDatabase(self):
        dbName = self._cfr.readFirstConfig('db')
        models = [User,Forums,Fans,Follow]
        for m in models:
           if m.__name__ not in self.db.getAllTables(dbName) or self.db.getAllTables(dbName) is None:
                self.db.createTable(dbName,m.__name__,m.getFields(),m.getKey(),m.getTypes())


