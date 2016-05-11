from MyCrawlerLib.tools.MySqlDBHelper import MySqlDBHelper
from MyCrawlerLib.tools.ConfigReader import ConfigReader
from MyCrawlerLib.database.Model import *

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

    def _initDatabase(self):
        dbName = self._cfr.readFirstConfig('db')
        models = [User,Forums,Fans,Follow]
        tables = self.db.getAllTables(dbName)
        for m in models:
            #BUG:这里暂时无法判断表是否已创建
           if [set(str.lower(m.__name__))] not in self.db.getAllTables(dbName) or self.db.getAllTables(dbName) is None:
                self.db.createTable(dbName,m.__name__,m.getFields(),m.getKey(),m.getTypes())


