#-*-coding:utf8-*-
from service.DataSaver import DataSaver
from service.MainDataAnalysiser import MainDataAnalysiser
from tools.ConfigReader import ConfigReader
from tools.MultiProcessHelp import MultiProcessHelper

syspath = "G:\My project\PythonProjects\MyCrawler\config\SysConfig.ini"

class CrawlerMain(object):
    def __init__(self):
        self._initSys()

    def _initSys(self):
        syscfr = ConfigReader(syspath)
        self.status = syscfr.readConfig('Config','status')
        self.startUrl = syscfr.readConfig('Config','url')

        dbPath = syscfr.readConfig('Path','db')
        self.dbSaver = DataSaver(dbPath)

        self.xpath = syscfr.readConfig('Path','xpath')

        self._processHelper = MultiProcessHelper(4)

    def startAnslysisData(self,url):

        print(url)
        cfr = ConfigReader(self.xpath)
        mainAnalysis = MainDataAnalysiser(url,cfr.getDicts())

        for f in mainAnalysis.getFans():
            url =  "http://tieba.baidu.com/home/main?un="+ f.fansid + "&fr=ibaidu&ie=utf-8"
            self._processHelper.async(self.startAnslysisData,(url,))

        for f in mainAnalysis.getFollows():
            url =  "http://tieba.baidu.com/home/main?un="+ f.followid + "&fr=ibaidu&ie=utf-8"
            self._processHelper.async(self.startAnslysisData,(url,))

        self._saveUser(mainAnalysis.getUser())
        self._saveForums(mainAnalysis.getForums())
        self._saveFans(mainAnalysis.getFans())
        self._saveFollows(mainAnalysis.getFollows())

    def _saveUser(self, user):
        self.dbSaver.insertUser(user)

    def _saveForums(self, forums):
        self.dbSaver.insertForums(forums)

    def _saveFans(self, fans):
        self.dbSaver.insertFans(fans)


    def _saveFollows(self, follows):
        self.dbSaver.insertFollow(follows)


    def __del__(self):
        try:
            self._processHelper.join()
        except:
            self

if __name__ == '__main__':

    main = CrawlerMain()
    main.startAnslysisData(main.startUrl)