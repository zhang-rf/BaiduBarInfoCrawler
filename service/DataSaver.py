#-*-coding:utf8-*-
from database.Database import Database


class DataSaver(object):
    def __init__(self,dbPath):
        self.db = Database(dbPath).db

    def insertUser(self,user):
        user_info = [user.id,user.sex,user.age,user.post]
        res = self.db.insert('user',user_info)
        return res

    def insertForums(self,forums):
        forumList = []
        for forum in forums:
            forumList.append((forum.name,forum.userid))
        res = self.db.batchInsert('forums', forumList)
        return res

    def insertFans(self,fans):
        fansList = []
        for fansInfo in fans:
            fansList.append( (fansInfo.fansid,fansInfo.userid) )
        res = self.db.batchInsert('fans', fansList)
        return res

    def insertFollow(self,follows):
        followList = []
        for follow in follows:
           followList.append( (follow.followid,follow.userid) )
        res = self.db.batchInsert('follow', followList)
        return res