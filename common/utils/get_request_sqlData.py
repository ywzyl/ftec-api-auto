# -*- coding:utf-8 -*-
from common.utils.db_connect import connect_db
from common.utils.read_sql_script import read_sql_script

class Get_request_sqlData(object):
    def __call__(self,sql_script_path,sql_script_section,sql_script_name):
        # 获取请求数据
        s = read_sql_script(sql_script_path)
        sql = s.get(sql_script_section,sql_script_name)
        # 连接数据库
        sql_res = connect_db(sql)[0]
        try:
            # 获取路径
            self.path = sql_res["path"]
        except Exception as e:
            print(e)
