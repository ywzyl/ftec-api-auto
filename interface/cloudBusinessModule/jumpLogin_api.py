# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api import Base_API

class JumpLogin_API():
    @Base_API("sql_script_request.ini","sql_script_post_cloudBusinessModule","jumpLogin")
    def jumpLogin_api(obj):
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')
        """
    def __call__(self, *args, **kwargs):
        source = Post_request_sqlData()
        source("sql_script_request.ini","sql_script_post_cloudBusinessModule","jumpLogin")
        req = BaseReq(source.path)
        r = req.post(data=source.data,headers=source.headers)
        self.msg = req.get_response_message()
        self.status_code = req.get_status_code()
        print(self.msg)
        return self.msg,self.status_code
        """

if __name__=="__main__":
    j = JumpLogin_API().jumpLogin_api()
