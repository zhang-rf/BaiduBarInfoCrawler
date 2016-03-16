from tools.MySqlDBHelper import MySqlDBHelper
from tools.ConfigReader import ConfigReader

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

