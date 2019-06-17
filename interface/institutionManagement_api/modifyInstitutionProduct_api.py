# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api import Base_API

class ModifyInstitutionProduct_API(object):
    @Base_API("sql_script_request.ini","sql_script_post_institutionModule","modifyInstitutionProduct")
    def modifyInstitutionProduct_api(obj):
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')

    """
    def __call__(self, *args, **kwargs):
        #获取请求路径、请求体、请求头数据
        source = Post_request_sqlData()
        source("sql_script_request.ini","sql_script_post_institutionModule","modifyInstitutionProduct")
        #发送请求
        req = BaseReq(source.path)
        r = req.post(data=source.data.encode("utf-8"),headers=source.headers)
        self.status_code = req.get_status_code()
        self.msg = req.get_response_message()
        return self.msg,self.status_code
        """

if __name__=="__main__":
    m = ModifyInstitutionProduct_API()
    m()