# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_token import TokenPostBaseAPI

class VerifyRecommendCode_API(object):
    """验证推荐码    关联登录token"""
    @TokenPostBaseAPI("sql_script_request.ini","ftec_service_api","verifyRecommendCode","verifyRecommendCode","jumpLogin")
    def verifyRecommendCode_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body, 'msg', '请求成功')

if __name__=="__main__":
    VerifyRecommendCode_API().verifyRecommendCode_api()