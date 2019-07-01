# -*- coding:utf-8 -*-
from interface.ftecServiceAPI.sendAuthCode_api import SendAuthCode_API
from interface.ftecServiceAPI.registerLogin_api import RegisterLogin_API


def test_registerProcess():
    #1,发送验证码
    SendAuthCode_API().sendAuthCode_api()
    #2,注册登录
    RegisterLogin_API().registerLogin_api()
