# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_token import TokenPostBaseAPI

class GetJumpInstitutionInfo_API(object):
    """获取跳转第三方机构登录信息（需登录）   关联登录token"""
    @TokenPostBaseAPI("sql_script_request.ini","ftec_service_api","getJumpInstitutionInfo","getJumpInstitutionInfo","jumpLogin")
    def getJumpInstitutionInfo_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body, 'msg', '请求成功')

if __name__=="__main__":
    GetJumpInstitutionInfo_API().getJumpInstitutionInfo_api()