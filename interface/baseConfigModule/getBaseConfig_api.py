# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api import Base_API

class GetBaseConfig_API():
    @Base_API("sql_script_request.ini","sql_script_get_baseConfigModule","getBaseConfig")
    def getBaseConfig_api(obj):
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')
        """
    def __call__(self, *args, **kwargs):
        #获取请求路径数据
        source =Get_request_sqlData()
        source("sql_script_request.ini","sql_script_get_baseConfigModule","getBaseConfig")
        #发送请求
        req = BaseReq(source.path)
        r = req.get()
        self.msg = req.get_response_message()
        self.status_code = req.get_status_code()
        #print(self.msg)
        return self.msg,self.status_code
        """

if __name__=="__main__":
    g = GetBaseConfig_API()
    g()