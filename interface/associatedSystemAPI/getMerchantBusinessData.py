# -*- coding:utf-8 -*-
from interface.base_api_post_data_time import DataTimePostBaseAPI
from common.utils.assertions import Assertions


class GetMerchantBusinessData_API(object):
    """获取商户经营数据"""
    @DataTimePostBaseAPI("sql_script_request.ini", "associated_system_api", "getMerchantBusinessData")
    def getMerchantBusinessData_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_body(body, "msg", "请求成功")


if __name__ == "__main__":
    GetMerchantBusinessData_API().getMerchantBusinessData_api()

