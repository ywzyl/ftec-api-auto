# -*-  coding:utf-8 -*-
from common.utils.db_connect import connect_db

def set_token(token: str,api_name: str) -> None:
    """从接口数据库中存取token"""
    sql = """update api_req_post set token='{}' where api_name='{}'""".format(token,api_name)
    connect_db(sql)

def get_token(api_name: str) -> 'token(str)':
    sql = """select token from api_req_post where api_name='{}'""".format(api_name)
    res = connect_db(sql)
    return res[0]['token']

def update_token(api_name: str,token_source) -> 'new_headers':
    """根据api_name从接口数据库中取出headers，将userCookiesName的token值替换成新的token值"""
    sql1 = """select headers from api_req_post where api_name='{}'""".format(api_name)
    res = connect_db(sql1)
    token = res[0]['headers'].split()[4].split('"')[1]
    new_token = get_token(token_source)
    res1 = res[0]['headers']
    new_headers = res1.replace(token,new_token)
    return new_headers

