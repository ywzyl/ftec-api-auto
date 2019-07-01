# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_get import GetBaseAPI

class IsShowModule_API():
    """是否显示经销商认证模块（需登录）"""
    @GetBaseAPI("sql_script_request.ini","ftec_service_api","isShowModule")
    def isShowModule_api(obj):
        body = obj[0]  #get取0
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    IsShowModule_API().isShowModule_api()