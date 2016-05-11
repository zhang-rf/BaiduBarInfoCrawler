#-*-coding:utf8-*-
from database.Database import Database


class DataSaver(object):
    def __init__(self,dbPath):
        self.db = Database(dbPath).db

    def insertUser(self,user):
        user_info = [user.userid,user.sex,user.age,user.post]
        res = self.db.insert('user',user_info)
        return res

    def insertForums(self,forums):
        forumList = []
        for forum in forums:
            forumList.append([forum.userid,forum.name])
        res = self.db.batchInsert('forums', forumList)
        return res

    def insertFans(self,fans):
        fansList = []
        for fansInfo in fans:
            fansList.append( [fansInfo.userid,fansInfo.fansid] )
        res = self.db.batchInsert('fans', fansList)
        return res

    def insertFollow(self,follows):
        followList = []
        for follow in follows:
           followList.append( [follow.userid,follow.followid] )
        res = self.db.batchInsert('follow', followList)
        return res