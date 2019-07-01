# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI

class QueryHelperStatus_API():
    """查询助手状态"""
    @PostBaseAPI("sql_script_request.ini","ftec_service_api","queryHelperStatus")
    def queryHelperStatus_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    QueryHelperStatus_API().queryHelperStatus_api()

