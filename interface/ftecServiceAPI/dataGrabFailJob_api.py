# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api_post import PostBaseAPI

class DataGrabFailJob_API(object):
    """数据抓取失败JOB"""
    @PostBaseAPI("sql_script_request.ini","ftec_service_api","dataGrabFailJob")
    def dataGrabFailJob_api(obj: list) -> None:
        body = obj[1]
        assert Assertions().assert_code(body['code'],200)

if __name__=="__main__":
    DataGrabFailJob_API().dataGrabFailJob_api()