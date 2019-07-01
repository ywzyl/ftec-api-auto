# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI

class QueryIndexInfo_API(object):
    """查询首页信息（需登录）"""
    @PostBaseAPI("sql_script_request.ini","ftec_service_api","queryIndexInfo")
    def queryIndexInfo_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body, "msg", "请求成功")

if __name__=="__main__":
    QueryIndexInfo_API().queryIndexInfo_api()