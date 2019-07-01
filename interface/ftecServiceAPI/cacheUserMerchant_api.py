# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_token import TokenPostBaseAPI

class CacheUserMerchant_API(object):
    """缓存用户选择商户      关联登录token"""
    @TokenPostBaseAPI("sql_script_request.ini","ftec_service_api","cacheUserMerchant","cacheUserMerchant","jumpLogin")
    def cacheUserMerchant_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    CacheUserMerchant_API().cacheUserMerchant_api()