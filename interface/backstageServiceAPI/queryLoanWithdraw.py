# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI

class QueryLoanWithdraw_API(object):
    """查询贷款放款(需登录、支持分页)"""
    @PostBaseAPI("sql_script_request.ini","backstage_service_api","queryLoanWithdraw")
    def queryLoanWithdraw_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    QueryLoanWithdraw_API().queryLoanWithdraw_api()