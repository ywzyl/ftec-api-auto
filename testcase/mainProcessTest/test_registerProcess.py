# -*- coding:utf-8 -*-
from interface.loginModule.sendAuthCode_api import SendAuthCode_API
from interface.loginModule.registerLogin_api import RegisterLogin_API
import pytest

def test_registerProcess():
    #1,发送验证码
    SendAuthCode_API().sendAuthCode_api()
    #2,注册登录
    RegisterLogin_API().registerLogin_api()
