# -*- coding:utf-8 -*-
from common.utils.post_request_sqlData import Post_request_sqlData
from common.request.base_req import BaseReq
import functools
from common.log.log import MyLog
from common.utils.time_utils import set_timeStamp_flag
from common.utils.update_data import *

class DataTimePostBaseAPI:
    """sql_script_path：sql脚本文件位置，sql_script_section：sql脚本块，sql_script_name：sql脚本名，api_name：接口名，token_source：token源"""
    def __init__(self,sql_script_path: str,sql_script_section: str,sql_script_name: str) -> None:
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
            #第一次发送请求，更新时间
            self.data1 = update_time(source.api_name)
            print(self.data1)
            res1 = req.post(data=self.data1,headers=source.headers)
            print(res1)
            self.data = update_time_sign(self.data1)
            #第二次发送请求，更新签名
            res2 = req.post(data=self.data,headers=source.headers)
            print(res2)
            timeStamp = self.timeStamp
            self.log.info("{}接口的响应信息：{}，时间戳标记：{}".format(source.api_name,str(res2),timeStamp))
            return  func(res2) #返回值，给被装饰的函数调用
        return wrapper