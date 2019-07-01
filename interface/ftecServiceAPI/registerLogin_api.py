# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI

class RegisterLogin_API(object):
    @PostBaseAPI("sql_script_request.ini","ftec_service_api","registerLogin")
    def registerLogin_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,"msg","请求成功")

if __name__=="__main__":
    RegisterLogin_API().registerLogin_api()
