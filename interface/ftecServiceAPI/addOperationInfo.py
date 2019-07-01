# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI

class AddOperationInfo_API(object):
    """添加运营信息"""
    @PostBaseAPI("sql_script_request.ini","ftec_service_api","addOperationInfo")
    def addOperationInfo_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    AddOperationInfo_API().addOperationInfo_api()