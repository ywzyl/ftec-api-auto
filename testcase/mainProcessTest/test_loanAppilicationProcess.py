# -*- coding:utf-8 -*-
import pytest
from interface.associatedSystemAPI.jumpLogin_api import JumpLogin_API
from interface.ftecServiceAPI.queryUserMerchant_api import QueryUserMerchant_API
from interface.ftecServiceAPI.cacheUserMerchant_api import CacheUserMerchant_API
from interface.ftecServiceAPI.queryIndexInfo_api import QueryIndexInfo_API
from interface.ftecServiceAPI.getJumpInstitutionInfo_api import GetJumpInstitutionInfo_API
from interface.ftecServiceAPI.queryHelperStatus_api import QueryHelperStatus_API
from interface.ftecServiceAPI.verifyRecommendCode import VerifyRecommendCode_API
from interface.ftecServiceAPI.dealerCodeCertification import DealerCodeCertification_API
from interface.ftecServiceAPI.queryRecommendCode import QueryRecommendCode_API

@pytest.mark.MP
def test_loanApplicationProcess():
    #1,云商跳转登录
    JumpLogin_API().jumpLogin_api()
    #2,查询用户关联商户
    QueryUserMerchant_API().queryUserMerchant_api()
    #3,缓存用户选择商户
    CacheUserMerchant_API().cacheUserMerchant_api()
    #4,查询索引信息、查询助手状态
    QueryIndexInfo_API().queryIndexInfo_api()
    QueryHelperStatus_API.queryHelperStatus_api()
    #5,获取跳转第三方登录信息
    GetJumpInstitutionInfo_API().getJumpInstitutionInfo_api()
    #6,经销商编码认证
    DealerCodeCertification_API().dealerCodeCertification_api()
    #7,查询推荐码
    QueryRecommendCode_API().queryRecommendCode_api()
    #8,验证推荐码
    VerifyRecommendCode_API().verifyRecommendCode_api()

if __name__=="__main__":
    pytest.main()

