#-*-coding:utf8-*-

import configparser

class ConfigReader(object):
    def __init__(self,path):
        self._cf = configparser.ConfigParser()
        self._cf.read(path, 'utf-8')

    def readConfig(self,section,item):
        return self._cf.get(section, item)

    def readFirstConfig(self,item):
        session = self._cf.sections()[0]
        return self._cf.get(session, item)

    def getDict(self,session):
        dict = {}
        items = self._cf.items(session)
        for k,v in items:
            dict[k] = v
        return dict

    def getDicts(self):
        dicts = {}
        for each in self._cf.sections():
            dicts[each] = self.getDict(each)
        return dicts
