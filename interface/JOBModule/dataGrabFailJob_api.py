# -*- coding:utf-8 -*-
from common.utils.assertions import Assertions
from interface.base_api import Base_API

class DataGrabFailJob_API(object):
    @Base_API("sql_script_request.ini","sql_script_post_JOBModule","dataGrabFailJob")
    def dataGrabFailJob_api(obj):
        body = obj[1]
        assert Assertions().assert_body(body,'msg','请求成功')

    """
    def __call__(self, *args, **kwargs):
        #获取请求路径、请求体、请求头数据
        p = Post_request_sqlData()
        p.post_request_sqlData("sql_script_request.ini","sql_script_post_JOBModule","dataGrabFailJob")
        #发送请求
        req = BaseReq(p.path)
        r = req.post(data=p.data,headers=p.headers)
        self.status_code = req.get_status_code()
        return self.status_code
        """

if __name__=="__main__":
    d= DataGrabFailJob_API()
    d()