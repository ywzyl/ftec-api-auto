# -*- coding:utf-8 -*-
import pymysql
import os
from common.utils.read_config import read_config_ini

# ======== MySql base operating ===================
class DB:
    def __init__(self):
        r = read_config_ini()
        #数据库连接
        try:
            self.connection = pymysql.connect(host=r.get("mysql_config","db_host"),
                                              user=r.get("mysql_config","db_username"),
                                              passwd=r.get("mysql_config","db_passwd"),
                                              port=r.getint("mysql_config","db_port"),
                                              db=r.get("mysql_config","db_name"),
                                              charset='utf8',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("MySQL Error %d: %s"%(e.args[0],e.args[1]))

    #清空表数据
    def clear(self):
        r = read_config_ini()
        real_sql = r.get("db_sql_script","clear_script")
        with self.connection.cursor() as cursor:
            # cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    #创建必要数据
    def insert(self):
        r = read_config_ini()
        '''
        for key in table_data:
            table_data[key] = str(table_data[key])
            key  = ','.join(table_data.keys())
            value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " ("+ key +") VALUES ("+ value +")"
        '''
        real_sql = r.get("db_sql_script","insert_scrpit")
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()
        '''
        r = read_config_ini()
        #使用存储过程
        proc_name = r.get("db_sql_script","stored_procedure_script")
        with self.connection.cursor() as cursor:
            cursor.callproc(proc_name)
        self.connection.commit()
        '''

    #关闭数据库
    def close(self):
        self.connection.close()

    #初始化数据
    def init_data(self,datas):
        self.clear()
        for data in datas.items():
            self.insert(data)
        self.close()
"""
if __name__=='__main__':
    db = DB()
    r = read_config_ini()
    db.clear()
    '''
    if r.items("db_insert_table_name")==None:
        pass
    else:
        for keys in r.options("db_insert_table_name"):
            table_name = r.get("db_insert_table_name","%s"%keys)
            #if r.items("db_insert_data")==None:
                #pass
            #else:
                #for vals in r.options("db_insert_data"):
                    #data = r.get("db_insert_data","%s"%vals)
            data=dict([('name','km'),('text',"lol")])
            '''
    db.insert()
    db.close()
"""
