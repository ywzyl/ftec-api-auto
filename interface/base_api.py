# -*- coding:utf-8 -*-
from common.utils.post_request_sqlData import Post_request_sqlData
from common.request.base_req import BaseReq
import functools,json
from common.log.log import MyLog
from common.utils.set_timeStamp_flag import set_timeStamp_flag

class Base_API:
    def __init__(self,sql_script_path,sql_script_section,sql_script_name):
        self.sql_script_path = sql_script_path
        self.sql_script_section = sql_script_section
        self.sql_script_name = sql_script_name
        self.log = MyLog()
        self.timeStamp = set_timeStamp_flag()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            source = Post_request_sqlData()
            source(self.sql_script_path,self.sql_script_section,self.sql_script_name)
            req = BaseReq(source.path)
            res = req.post(data=source.data.encode("utf-8"),headers=source.headers)
            timeStamp = self.timeStamp
            self.log.info("{}接口的响应信息：{}，时间戳标记：{}".format(source.api_name,str(res),timeStamp))
            return  func(res) #返回值，给被装饰的函数调用
        return wrapper