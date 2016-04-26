#-*-coding:utf8-*-
from service.DataSaver import DataSaver
from service.MainDataAnalysiser import MainDataAnalysiser
from tools.ConfigReader import ConfigReader
from tools.MultiProcessHelp import MultiProcessHelper
import time

syspath = "G:\My project\PythonProjects\MyCrawler\config\SysConfig.ini"

class CrawlerMain(object):
    def __init__(self):
        syscfr = ConfigReader(syspath)
        self.status = syscfr.readConfig('Config','status')
        self.startUrl = syscfr.readConfig('Config','url')
        dbPath = syscfr.readConfig('Path','db')
        # self.dbSaver = DataSaver(dbPath)
        self.xpath = syscfr.readConfig('Path','xpath')

    def startAnslysisData(self,url):
            print("开始分析",url)
            cfr = ConfigReader(self.xpath)
            mainAnalysis = MainDataAnalysiser(url,cfr.getDicts())

            processHelper = MultiProcessHelper(4)
            print("进入分析",url)
            for f in mainAnalysis.getFans():
                try:
                    print("start process",f.fansid)
                    u =  "http://tieba.baidu.com/home/main?un="+ f.fansid + "&fr=ibaidu&ie=utf-8"
                    processHelper.apply_async(self.startAnslysisData, u);
                except:
                    print("URL异常")

            for f in mainAnalysis.getFollows():
                print("start process",f.followid)
                u =  "http://tieba.baidu.com/home/main?un="+ f.followid + "&fr=ibaidu&ie=utf-8"
                processHelper.apply_async(self.startAnslysisData, u);

            print("分析URL结束",url)

            self.dbSaver.insertUser(mainAnalysis.getUser())
            self.dbSaver.insertForums(mainAnalysis.getForums())
            self.dbSaver.insertFans(mainAnalysis.getFans())
            self.dbSaver.insertFollow(mainAnalysis.getFollows())

if __name__ == '__main__':

    main = CrawlerMain()
    main.startAnslysisData(main.startUrl)
