# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI

class QueryLoanEntry_API(object):
    """查询贷款进件(需登录、支持分页)"""
    @PostBaseAPI("sql_script_request.ini","backstage_service_api","queryLoanEntry")
    def queryLoanEntry_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    QueryLoanEntry_API().queryLoanEntry_api()