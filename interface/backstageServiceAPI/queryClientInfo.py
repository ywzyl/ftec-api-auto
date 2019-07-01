# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI

class QueryClientInfo_API(object):
    """查询客户信息接口(需登录)"""
    @PostBaseAPI("sql_script_request.ini","backstage_service_api","queryClientInfo")
    def queryClientInfo_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    QueryClientInfo_API().queryClientInfo_api()