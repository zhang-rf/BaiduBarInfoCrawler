#-*-coding:utf8-*-

import configparser
#读取配置文件
class ConfigReader(object):
    def __init__(self,path):
        self._cf = configparser.ConfigParser()
        self._cf.read(path, 'utf-8')
    def readConfig(self,section,item):
        return self._cf.get(section, item)

    def readFirstConfig(self,item):
        session = self._cf.sections()[0]
        return self._cf.get(session, item)
    #获取指定section的配置信息的数据字典
    def getDict(self,section):
        dict = {}
        items = self._cf.items(section)
        for k,v in items:
            dict[k] = v
        return dict

    #遍历获取整个配置文件的数据字典
    def getDicts(self):
        dicts = {}
        for each in self._cf.sections():
            dicts[each] = self.getDict(each)
        return dicts
