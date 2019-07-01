# -*- coding:utf-8 -*-
from common.utils.UseDatabase import UseDatabase

def connect_db(sql: str) -> 'result':
    """从config.ini文件中读取相关配置信息，连接接口数据库"""
    with UseDatabase("mysql_config","mysql") as cursor:
        cursor.execute(sql)
        res = cursor.fetchall()
    return res