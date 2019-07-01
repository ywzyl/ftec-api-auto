# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_get import GetBaseAPI

class GetBaseConfig_API():
    """获取基础配置"""
    @GetBaseAPI("sql_script_request.ini","ftec_service_api","getBaseConfig")
    def getBaseConfig_api(obj):
        body = obj[0]  #get取0
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    GetBaseConfig_API().getBaseConfig_api()