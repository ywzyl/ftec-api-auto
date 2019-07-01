# -*- coding:utf-8 -*-
from interface.base_api_post_data import DataPostBaseAPI
from common.utils.assertions import Assertions


class AgencyCodeJumpLogin_API(object):
    """极速云跳转登录"""
    @DataPostBaseAPI("sql_script_request.ini", "associated_system_api", "agencyCodeJumpLogin")
    def agencyCodeJumpLogin_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body, "msg", "请求成功")


if __name__ == "__main__":
    AgencyCodeJumpLogin_API().agencyCodeJumpLogin_api()

