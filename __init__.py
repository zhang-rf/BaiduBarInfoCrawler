#-*-coding:utf8-*-
from MyCrawlerLib.service.DataSaver import DataSaver
from MyCrawlerLib.service.MainDataAnalysiser import MainDataAnalysiser
from MyCrawlerLib.tools.ConfigReader import ConfigReader
from MyCrawlerLib.tools.ThreadPool import *
import threading
import time
from MyCrawlerLib.tools.LogTool import LogTool
import sys

scaned = []
threadPool = ThreadPool(200)

mutex = threading.Lock()
class RecycleThread(threading.Thread):
    def run(self):
        while(True):
            mutex.acquire()
            print("--------回收Scaned--------:"+str(scaned.__len__()))
            scaned.clear()
            mutex.release()
            time.sleep(3600)


class CrawlerMain(object):
    def __init__(self,syspath):
        syscfr = ConfigReader(syspath)
        try:
            self.status = syscfr.readConfig('Config','status')
            self.startUrl = syscfr.readConfig('Config','url')
            self.dbPath = syscfr.readConfig('Path','db')
            self.xpath = syscfr.readConfig('Path','xpath')

        except:
            print("配置文件读取出错:"+str(sys.exc_info()[0])+str(sys.exc_info()[1]))
        #日志工具
        logpath = syscfr.readConfig('Path','logpath')
        self.logTool = LogTool(logpath)

        dbutil = DataSaver(self.dbPath).dbUtil
        try:
            dbutil._initDatabase()
        except:
            self.logTool.writeErrorLog("创建表失败:"+str(sys.exc_info()[0])+str(sys.exc_info()[1]))


    def startAnslysisData(self,url):
            if url in scaned:
                return ()
            print("开始分析",url)
            self.logTool.writeLog("开始分析:"+url)
            scaned.append(url)
            cfr = ConfigReader(self.xpath)
            mainAnalysis = MainDataAnalysiser(url,cfr.getDicts())

            urls = []
            try:
                for f in mainAnalysis.getFans():
                    print("start thread",f.fansid)
                    self.logTool.writeLog("start thread"+str(f.fansid))
                    u =  "http://tieba.baidu.com/home/main?un="+ f.fansid + "&fr=ibaidu&ie=utf-8"
                    urls.append(u)

            except:
                print("Main : getFans None")
                self.logTool.writeErrorLog("Main : getFans None:"+url+"|fans"+str(sys.exc_info()[0])+str(sys.exc_info()[1]))

            try:
                for f in mainAnalysis.getFollows():
                    print("start thread",f.followid)
                    u =  "http://tieba.baidu.com/home/main?un="+ f.followid + "&fr=ibaidu&ie=utf-8"
                    urls.append(u)
            except:
                print("Main : getFollows None")
                self.logTool.writeErrorLog("Main : getFollows None:"+url+"|follows:"+str(sys.exc_info()[0])+str(sys.exc_info()[1]))

            print("分析URL结束",url)
            self.logTool.writeLog("分析URL结束:"+url)

            self.saveToDB(mainAnalysis)
            return  set(urls)

    def saveToDB(self,dataSource):
        print("---存储数据---")
        self.logTool.writeLog("---存储数据---")
        dbSaver = DataSaver(self.dbPath)
        try:
            dbSaver.insertUser(dataSource.getUser())
        except:
            print("存储用户信息失败")
            self.logTool.writeErrorLog("存储用户信息失败:"+str(sys.exc_info()[0])+str(sys.exc_info()[1]))
        try:
            dbSaver.insertForums(dataSource.getForums())
        except:
            print("存储论坛信息失败")
            self.logTool.writeErrorLog("存储论坛信息失败"+str(sys.exc_info()[0])+str(sys.exc_info()[1]))
        try:
            dbSaver.insertFans(dataSource.getFans())
        except:
            print("存储粉丝信息失败")
            self.logTool.writeErrorLog("存储粉丝信息失败"+str(sys.exc_info()[0])+str(sys.exc_info()[1]))
        try:
            dbSaver.insertFollow(dataSource.getFollows())
        except:
            print("存储关注信息失败")
            self.logTool.writeErrorLog("存储关注信息失败"+str(sys.exc_info()[0])+str(sys.exc_info()[1]))



def analysis(urls, function):
    for u in urls:
        urlSet = function(u)
        threadPool.addTask(analysis,[urlSet,function])

def beginCrawler(spath):
    recycleThread = RecycleThread()
    recycleThread.start()
    main = CrawlerMain(spath)
    analysis([main.startUrl],main.startAnslysisData)

if __name__ == '__main__':
    beginCrawler("G:\My project\PythonProjects\MyCrawler\config\SysConfig.ini")