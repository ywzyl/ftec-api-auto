# -*- coding:utf-8 -*-
import pytest
from interface.cloudBusinessModule.jumpLogin_api import JumpLogin_API
from interface.merchantModule.queryUserMerchant_api import QueryUserMerchant_API
from interface.merchantModule.cacheUserMerchant_api import CacheUserMerchant_API
from interface.indexModule.queryIndexInfo_api import QueryIndexInfo_API
from interface.loginModule.getJumpLoginInfo_api import GetJumpLoginInfo_API
from interface.merchantModule.queryHelperStatus_api import QueryHelperStatus_API

@pytest.mark.LAP
def test_loanApplicationProcess():
    #1,老用户云商跳转登录
    JumpLogin_API().jumpLogin_api()
    #2,查询用户关联商户
    QueryUserMerchant_API().queryUserMerchant_api()
    #3,缓存用户选择商户
    CacheUserMerchant_API().cacheUserMerchant_api()
    #4,查询索引信息、查询助手状态
    QueryIndexInfo_API().queryIndexInfo_api()
    QueryHelperStatus_API.queryHelperStatus_api()
    #5,获取跳转第三方登录信息
    GetJumpLoginInfo_API().getJumpLoginInfo_api()

if __name__=="__main__":
    pytest.main()

