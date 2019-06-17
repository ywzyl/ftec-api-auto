# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api import Base_API

class GetJumpLoginInfo_API(object):
    @Base_API("sql_script_request.ini","sql_script_post_loginModule","getJumpLoginInfo")
    def getJumpLoginInfo_api(obj):
        body = obj[1]
        assert Assertions().assert_body(body, 'msg', '请求成功')

if __name__=="__main__":
    GetJumpLoginInfo_API().getJumpLoginInfo_api()