#-*-coding:utf8-*-
from service.DataSaver import DataSaver
from service.MainDataAnalysiser import MainDataAnalysiser
from tools.ConfigReader import ConfigReader
from tools.ThreadPool import *


syspath = "G:\My project\PythonProjects\MyCrawler\config\SysConfig.ini"

scaned = []
threadPool = ThreadPool(200)

class CrawlerMain(object):
    def __init__(self):
        syscfr = ConfigReader(syspath)
        self.status = syscfr.readConfig('Config','status')
        self.startUrl = syscfr.readConfig('Config','url')
        self.dbPath = syscfr.readConfig('Path','db')
        self.xpath = syscfr.readConfig('Path','xpath')
        dbutil = DataSaver(self.dbPath).dbUtil
        dbutil._initDatabase()


    def startAnslysisData(self,url):
            if url in scaned:
                return ()

            print("开始分析",url)
            scaned.append(url)
            cfr = ConfigReader(self.xpath)
            mainAnalysis = MainDataAnalysiser(url,cfr.getDicts())

            urls = []
            try:
                for f in mainAnalysis.getFans():
                    try:
                        print("start thread",f.fansid)
                        u =  "http://tieba.baidu.com/home/main?un="+ f.fansid + "&fr=ibaidu&ie=utf-8"
                        urls.append(u)
                    except:
                        print("URL异常")
            except:
                print("Main : getFans None")

            try:
                for f in mainAnalysis.getFollows():
                    print("start thread",f.followid)
                    u =  "http://tieba.baidu.com/home/main?un="+ f.followid + "&fr=ibaidu&ie=utf-8"
                    urls.append(u)
            except:
                print("Main : getFollows None")
            print("分析URL结束",url)

            self.saveToDB(mainAnalysis)
            # dbThreadPol.addTask(self.saveToDB,[mainAnalysis])
            return  set(urls)

    def saveToDB(self,dataSource):
        print("---存储数据---")
        dbSaver = DataSaver(self.dbPath)
        try:
            dbSaver.insertUser(dataSource.getUser())
        except:
            print("存储用户信息失败")
        try:
            dbSaver.insertForums(dataSource.getForums())
        except:
            print("存储论坛信息失败")
        try:
            dbSaver.insertFans(dataSource.getFans())
        except:
            print("存储粉丝信息失败")
        try:
            dbSaver.insertFollow(dataSource.getFollows())
        except:
            print("存储关注信息失败")



def analysis(urls, function):
    for u in urls:
        urlSet = function(u)
        threadPool.addTask(analysis,[urlSet,function])

if __name__ == '__main__':
    main = CrawlerMain()
    urls = main.startAnslysisData(main.startUrl)
    analysis(urls,main.startAnslysisData)