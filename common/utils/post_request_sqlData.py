# -*- coding:utf-8 -*-
from common.utils.read_sql_script import read_sql_script
from common.utils.db_connect import connect_db

class Post_request_sqlData(object):
    def __call__(self,sql_script_path,sql_script_section,sql_script_name):
        #获取请求数据
        s = read_sql_script(sql_script_path)
        sql = s.get(sql_script_section,sql_script_name)
        #连接数据库
        sql_res = connect_db(sql)
        try:
            #获取路径
            self.path = sql_res[0]["path"]
            #获取请求体数据
            self.data = sql_res[0]["data"]
            #获取请求头数据
            self.headers = sql_res[0]["headers"]
            #获取接口名称
            self.api_name = sql_res[0]["api_name"]
        except Exception as e:
            print(e)
