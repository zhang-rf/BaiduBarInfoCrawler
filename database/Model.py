#-*-coding:utf8-*-

"""在模型中定义好字段、类型和主键，以便自动创建表"""
class User(object):
    def __init__(self,id,sex,age,post):
        self.userid = id
        self.sex = sex
        self.age = age
        self.post = post

    @classmethod
    def getFields(cls):
        return ["userid","sex","age","post"]
    @classmethod
    def getTypes(cls):
        return ["varchar(50)","char(1)","int","float"]
    @classmethod
    def getKey(cls):
        return ["userid"]

class Forums(object):
    def __init__(self,userid,name):
        self.userid = userid
        self.name = name

    @classmethod
    def getFields(cls):
        return ["userid","name"]
    @classmethod
    def getTypes(cls):
        return ["varchar(50)","varchar(50)"]
    @classmethod
    def getKey(cls):
        return ["userid","name"]

class Follow(object):
    def __init__(self,userid,followid):
        self.userid = userid
        self.followid = followid

    @classmethod
    def getFields(cls):
        return ["userid","followid"]
    @classmethod
    def getTypes(cls):
        return ["varchar(50)","varchar(50)"]
    @classmethod
    def getKey(self):
        return ["userid","followid"]

class Fans(object):
    def __init__(self,userid,fansid):
        self.userid = userid
        self.fansid = fansid
    @classmethod
    def getFields(cls):
        return ["userid","fansid"]
    @classmethod
    def getTypes(cls):
        return ["varchar(50)","varchar(50)"]
    @classmethod
    def getKey(cls):
        return ["userid","fansid"]