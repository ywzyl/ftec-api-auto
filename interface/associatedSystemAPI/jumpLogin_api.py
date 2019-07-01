# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI
from common.utils.tokens import set_token

class JumpLogin_API(object):
    """云商跳转登录"""
    @PostBaseAPI("sql_script_request.ini","associated_system_api","jumpLogin")
    def jumpLogin_api(obj):
        body = obj[1]
        token = body['data']['token']
        set_token(token,"jumpLogin")
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    j = JumpLogin_API().jumpLogin_api()
