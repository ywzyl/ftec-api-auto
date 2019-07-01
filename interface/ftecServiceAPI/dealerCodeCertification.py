# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_token import TokenPostBaseAPI

class DealerCodeCertification_API(object):
    """经销商编码认证（需登录）    关联登录token"""
    @TokenPostBaseAPI("sql_script_request.ini","ftec_service_api","dealerCodeCertification","dealerCodeCertification","jumpLogin")
    def dealerCodeCertification_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')

if __name__=="__main__":
    DealerCodeCertification_API().dealerCodeCertification_api()