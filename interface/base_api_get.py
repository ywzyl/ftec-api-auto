# -*- coding:utf-8 -*-
from common.utils.get_request_sqlData import  Get_request_sqlData
from common.request.base_req import BaseReq
import functools
from common.log.log import MyLog
from common.utils.time_utils import set_timeStamp_flag

class GetBaseAPI:
    def __init__(self,sql_script_path,sql_script_section,sql_script_name):
        self.sql_script_path = sql_script_path
        self.sql_script_section = sql_script_section
        self.sql_script_name = sql_script_name
        self.log = MyLog()
        self.timeStamp = set_timeStamp_flag()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            source = Get_request_sqlData()
            source(self.sql_script_path,self.sql_script_section,self.sql_script_name)
            req = BaseReq(source.path)
            res = req.get(headers=source.headers)
            timeStamp = self.timeStamp
            self.log.info("{}接口的响应信息：{}，时间戳标记：{}".format(source.api_name,str(res),timeStamp))
            return  func(res) #返回值，给被装饰的函数调用
        return wrapper