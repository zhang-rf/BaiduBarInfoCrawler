#-*-coding:utf8-*-
from service.DataSaver import DataSaver
from service.MainDataAnalysiser import MainDataAnalysiser
from tools.ConfigReader import ConfigReader

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

    def startAnslysisData(self,url):
        cfr = ConfigReader(self.xpath)
        mainAnalysis = MainDataAnalysiser(url,cfr.getDicts())
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
        # for f in fans:
        #     url =  "http://tieba.baidu.com/home/main?un="+ f + "&fr=ibaidu&ie=utf-8"


    def _saveFollows(self, follows):
        self.dbSaver.insertFollow(follows)


main = CrawlerMain()
main.startAnslysisData(main.startUrl)