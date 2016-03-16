#-*-coding:utf8-*-

class User(object):
    def __init__(self,id,sex,age,post):
        self.id = id
        self.sex = sex
        self.age = age
        self.post = post

class Forums(object):
    def __init__(self,userid,name):
        self.userid = userid
        self.name = name

class Follow(object):
    def __init__(self,userid,followid):
        self.userid = userid
        self.followid = followid

class Fans(object):
    def __init__(self,userid,fansid):
        self.userid = userid
        self.fansid = fansid