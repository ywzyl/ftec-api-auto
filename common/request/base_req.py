# -*- coding:utf-8 -*-
import json,requests
from common.utils.read_config import read_config_ini

class BaseReq(object):
    r = read_config_ini()
    base_url = r.get("test_url","api_base_url")
    base_param = r.items("base_param")
    custom_param = r.items("custom_param")

    def __init__(self,url_params):#url_params='/xdd-finance-web/config/getBaseConfig'
        if not url_params:
            url_params=[]
        self.url_params = url_params
        self.response = None
        self.base_url = self.base_url

    # 拼接url
    def api_url(self):
        format_url = self.url_params
        return "{0}{1}".format(self.base_url,format_url)

    # 封装POST请求类型
    def post(self,data=None,headers=None):
        if not data:
            data = {}
            print("data is None")
        print(self.api_url())
        self.response = requests.post(url=self.api_url(),data=data,headers=eval(headers))
        self.res = self.response.json()
        return self.response,self.res

    # 封装GET请求类型
    def get(self,headers=None):
        if not headers:
            headers = {}
        print(self.api_url())
        self.response = requests.get(url=self.api_url(),headers=eval(headers))
        self.res = self.response.json()
        return self.res,self.response

    # 获取回参中状态码
    def get_code(self):
        if self.res:
            return self.res['code']

    # 获取HTTP状态码
    def get_status_code(self):
        if self.response:
            return self.response.status_code

    # 获取回参中message
    def get_response_message(self):
        if self.res:
            return self.res['msg']

    # 所有接口共有的入参，比如：version、token等
    def build_base_param(self):
        return self.base_param
    # 被测接口除公共参数外所需的其余参数
    def build_custom_param(self,data):
        return self.custom_param

