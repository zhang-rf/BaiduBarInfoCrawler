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
        try:
            #python3.x之后，str字符集默认是Unicode，故没有了encode这个内置函数
            #将数据库的字符集设为utf8后，就不再发生 'latin-1' codec can't encode character '\u8d5e'
            con = MySQLdb.connect(host = host,user = user, passwd = password, db = db, port = port,charset= 'utf8')
            return con
        except MySQLdb.Error:
            print("Connect Error")
            return None

    def query(self,sql,arg = None):
        """ Return the results(Tuples) after executing SQL statement """
        try:
            cur = self.connecter.cursor()
            cur.execute(sql,arg)
            result = cur.fetchall()
            cur.close()
            return result
        except:
            print("Query Error:"+sql)
            return ()

    def insert(self,table,args):
        """ insert a row into the table,please make sure that the location of the parameter in the line is correct"""
        try:
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
        except:
            print("Insert Error-Table:"+table)
            return 0

    def batchInsert(self, table, values):
        """ Batch insertions of row data into :table.Values must be a LIST of TUPLES """
        try:
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
            return r
        except:
            print("Insert Error-Table:"+table)
            return 0

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

