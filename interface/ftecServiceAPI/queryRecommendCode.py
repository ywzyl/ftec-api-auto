# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_token import TokenPostBaseAPI

class QueryRecommendCode_API(object):
    """查询推荐码    关联登录token"""
    @TokenPostBaseAPI("sql_script_request.ini","ftec_service_api","queryRecommendCode","queryRecommendCode","jumpLogin")
    def queryRecommendCode_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body, 'msg', '请求成功')

if __name__=="__main__":
    QueryRecommendCode_API().queryRecommendCode_api()