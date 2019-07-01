# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI

class AdminLogin_API(object):
    """管理员登录"""
    @PostBaseAPI("sql_script_request.ini","backstage_service_api","adminLogin")
    def adminLogin_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')


if __name__=="__main__":
    a= AdminLogin_API().adminLogin_api()