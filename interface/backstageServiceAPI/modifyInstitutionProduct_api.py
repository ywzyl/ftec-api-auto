# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI
from common.utils.clean_data import clean_product_data

class ModifyInstitutionProduct_API(object):
    """修改机构产品(需登录)"""
    @PostBaseAPI("sql_script_request.ini","backstage_service_api","modifyInstitutionProduct")
    def modifyInstitutionProduct_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')
        clean_product_data("modifyInstitutionProduct")
if __name__=="__main__":
    ModifyInstitutionProduct_API().modifyInstitutionProduct_api()