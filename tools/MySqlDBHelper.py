#-*-coding:utf8-*-

#create by Raomengnan
import MySQLdb

from importlib import reload

class MySqlDBHelper(object):
    def __init__(self,host,user,password,db,port):
        self.connecter = self.getConnect(host,user,password,db,port)

    def __del__(self):
        try:
            self.connecter.close()
        except:
            print("connecter close ERROR")

    def getConnect(self,host,user,password,db,port):
        #python3.x之后，str字符集默认是Unicode，故没有了encode这个内置函数
        #将数据库的字符集设为utf8后，就不再发生 'latin-1' codec can't encode character '\u8d5e'
        con = MySQLdb.connect(host = host,user = user, passwd = password, db = db, port = port,charset= 'utf8')
        return con

    def query(self,sql,arg = None):
        """ Return the results(Tuples) after executing SQL statement """
        cur = self.connecter.cursor()
        cur.execute(sql,arg)
        result = cur.fetchall()
        cur.close()
        return result

    def insert(self,table,args):
        """ insert a row into the table,please make sure that the location of the parameter in the line is correct"""
        num = args.__len__()
        sql = 'insert into ' + table + " values(";
        i = 0
        while i< num:
            sql += '%s'
            i += 1
            if i == num:
                sql += ')'
            else:
                sql += ','
        cur = self.connecter.cursor()
        r = cur.execute(sql,args)
        self.connecter.commit()

        cur.close()
        return r

    def batchInsert(self, table, values):
        """ Batch insertions of row data into :table.Values must be a LIST of TUPLES """
        num = values[0].__len__()
        sql = 'insert into ' + table + " values(";
        i = 0
        while i< num:
            sql += '%s'
            i += 1
            if i == num:
                sql += ')'
            else:
                sql += ','
        cur = self.connecter.cursor()
        r = cur.executemany(sql,values)
        self.connecter.commit()
        cur.close()
        return

    def update(self,sql,args=None):
        """ Update or delete, args must be a list"""
        try:
            cur = self.connecter.cursor()
            r = cur.execute(sql,args)
            self.connecter.commit()
            cur.close()
            return r
        except:
            print("Update/Delete Error:"+sql)
            return 0

    def createDatabase(self,name):
        cursor = self.connecter.cursor()
        sql = "create database " + name
        cursor.execute(sql)
        return True


    def createTable(self,tableName):
        cursor = self.connecter.cursor()
        sql = "create database " + tableName
        cursor.execute(sql)
        return True

    def getAllDatabase(self):
       dbList = []
       cursor = self.connecter.cursor()
       cursor.execute("show databases")
       for db in cursor.fetchall():
           dbList.append(db[0])
       return dbList

    def getAllTables(self,database):

        cursor = self.connecter.cursor()
        cursor.execute("use "+database)
        cursor.execute("show tables")
        tables = []
        for tab in cursor.fetchall():
            tables.append(tab)
        return tables


    def createTable(self,db,tableName,fields,keys,types):
        """:db 数据库名, fields: 字段列表，keys: 主键列表，types:字段对应的类型"""

        if fields == None or fields.__len__() == 0 or fields.__len__() != types.__len__():
            return False
        if keys == None:
            keys = []

        self.connecter.cursor().execute("use "+db)
        if(tableName not in self.getAllTables(db)):
            sql = "create TABLE " + tableName;
            fs = "("
            i = 0
            while i < fields.__len__():
                if fs != "(":
                    fs +=","
                fs +=( fields[i]+" " + types[i] + " ")
                i += 1

            i = 0
            pk = ""
            if keys.__len__() != 0:
                while i < keys.__len__():
                    if pk == "":
                        pk += "primary key("+keys[i]
                    else:
                        pk += ","+keys[i]
                    i+=1
            pk+=")"
            if pk != "":
                fs+=","+pk
            fs += ")"
            sql += fs
            self.connecter.cursor().execute(sql)
            print("create_table Success")
            return True
        else:
            return False






if __name__ == '__main__':
    db = MySqlDBHelper("tx.atomicer.cn","root","Raomengnan766","test",3309)
    a = db.connecter

    # print(type("123"))
    # print(type(123))
    # print(type("123.12"))
    # print("\'")


    # tb = "tbtest"
    # def createTable(tableName,fields,keys,types):
    #         """:db 数据库名, fields: 字段列表，keys: 主键列表，types:字段对应的类型"""
    #         if True:
    #             sql = "create TABLE " + tableName;
    #             fs = "("
    #             i = 0
    #             while i < fields.__len__():
    #                 if fs != "(":
    #                     fs +=","
    #                 fs +=( fields[i]+" " + types[i] + " ")
    #                 i += 1
    #
    #             i = 0
    #             pk = ""
    #             if keys.__len__() != 0:
    #                 while i < keys.__len__():
    #                     if pk == "":
    #                         pk += "primary key("+keys[i]
    #                     else:
    #                         pk += ","+keys[i]
    #                     i+=1
    #             pk+=")"
    #             if pk != "":
    #                 fs+=","+pk
    #             fs += ")"
    #             sql += fs
    #         return sql
    #
    #
    # sql = "create TABLE " + tb;
    # fields = ["a","b","c"]
    # types = ["varchar(10)","int","float"]
    # keys = ["a"]
    #
    # print(createTable(tb,fields,keys,types))


