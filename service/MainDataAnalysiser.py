#-*-coding:utf8-*-
import re

from MyCrawlerLib.database.Model import *
from MyCrawlerLib.service.AnalysiserCreater import AnalysiserCreater

#可能会抛出数据解析错误的异常
class MainDataAnalysiser(object):
    def __init__(self,url,xpath_dict):
        self.analysiser = AnalysiserCreater(url).analysiser
        self.initDatas(xpath_dict)

    def getUser(self):
        try:
            id = self.datas['user']['userid'][0] +""
            sex = self.datas['user']['sex'][0] +""
            age = self.datas['user']['age'][0]
            post = self.datas['user']['post'][0]
            return User(id,sex,age,post)
        except:
            print("MainDataAnalysiser:getUser Error")
            return None

    def getForums(self):
        try:
            userid = self.datas['user']['userid'][0]
            forums = []
            items = self.datas['forums']['name']
            for name in items:
                forums.append(Forums(userid,name))
            return forums
        except:
            print("MainDataAnalysiser:getForums Error")
            return None

    def getFans(self):
        try:
            userid = self.datas['user']['userid'][0]
            fans = []
            items = self.datas['fans']['fansid']
            for fansid in items:
                fans.append(Fans(userid,fansid))
            return fans
        except:
            print("MainDataAnalysiser:getFans Error")
            return None

    def getFollows(self):
        try:
            userid = self.datas['user']['userid'][0]
            follows = []
            items = self.datas['follow']['followid']
            for followid in items:
                follows.append(Follow(userid,followid))
            return follows
        except:
            print("MainDataAnalysiser:getFollows Error")
            return None


    def initDatas(self,xpath_dict):
        """ Initialized Data by analysiser,use xpath_dict"""
        self.datas = self.analysiser.getDatas(xpath_dict)
        self.correctDatas()
        return self.datas

    def correctDatas(self):
        try:
            """Correct the data that you need"""
            # 修正年龄

            ageStr = self.datas['user']['age'][0]
            age = re.findall('吧龄:(.*?)年',ageStr,re.S)[0]
            self.datas['user']['age'][0] = float(age)

            # 修正发帖数量
            postStr = self.datas['user']['post'][0]
            post = postStr.split(':')[1]
            if '万' in postStr:
                post = float(post.split('万')[0])*10000
                self.datas['user']['post'][0] = post
            else:
                self.datas['user']['post'][0] = float(post)

            # 修正性别
            if self.datas['user']['sex'][0].find('male') < 0:
                self.datas['user']['sex'][0] = 'f'
            else:
                self.datas['user']['sex'][0] = 'm'

            # 修正关注id
            items = self.datas['follow']['followid']
            i = 0
            while i < items.__len__():
                id = re.findall('/home/main\?un=(.*?)&fr=home',items[i],re.S)[0]
                items[i] = id
                if id == '':
                    items.remove('')
                    continue
                i += 1
            # 修正粉丝id
            items = self.datas['fans']['fansid']
            i = 0
            while i < items.__len__():
                id = re.findall('/home/main\?un=(.*?)&fr=home',items[i],re.S)[0]
                items[i] = id
                if id == '':
                    items.remove('')
                i += 1
        except:
            print("MainDataAnalysiser:correctDatas Error")