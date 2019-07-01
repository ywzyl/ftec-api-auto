# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI

class InstitutionProductSort_API(object):
    """机构产品排序(需登录)"""
    @PostBaseAPI("sql_script_request.ini","backstage_service_api","institutionProductSort")
    def institutionProductSort_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    InstitutionProductSort_API().institutionProductSort_api()

