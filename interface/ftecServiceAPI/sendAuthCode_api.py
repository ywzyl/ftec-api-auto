# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI

class SendAuthCode_API(object):
    """发送验证码"""
    @PostBaseAPI("sql_script_request.ini","ftec_service_api","sendAuthCode")
    def sendAuthCode_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    s = SendAuthCode_API().sendAuthCode_api()
