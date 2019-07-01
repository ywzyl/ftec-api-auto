# -*- coding:utf-8 -*-
from interface.base_api_post import PostBaseAPI
from common.utils.assertions import Assertions

class CreateInstitutionProduct_API(object):
    """创建机构产品(需登录)"""
    @PostBaseAPI("sql_script_request.ini","backstage_service_api","createInstitutionProduct")
    def createInstitutionProduct_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,"msg","请求成功")


if __name__=="__main__":
    CreateInstitutionProduct_API().createInstitutionProduct_api()
    
