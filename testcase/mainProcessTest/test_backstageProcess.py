# -*- coding:utf-8 -*-
from interface.backstageServiceAPI.institutionProductSort_api import InstitutionProductSort_API
from interface.backstageServiceAPI.createInstitutionProduct_api import CreateInstitutionProduct_API
from interface.backstageServiceAPI.queryInstitutionProduct_api import QueryInstitutionProduct_API
from interface.backstageServiceAPI.modifyInstitutionProduct_api import ModifyInstitutionProduct_API
from interface.backstageServiceAPI.adminLogin_api import AdminLogin_API
from interface.backstageServiceAPI.queryClientInfo import QueryClientInfo_API
from interface.backstageServiceAPI.queryLoanEntry import QueryLoanEntry_API
from interface.backstageServiceAPI.queryLoanWithdraw import QueryLoanWithdraw_API
from common.utils.admin_init import *
import pytest

@pytest.fixture()
def before():
    admin_init()
    yield
    admin_clean()

@pytest.mark.MP
def test_institutionProductProcess(before):
    #管理员登录
    AdminLogin_API().adminLogin_api()
    #新增机构产品
    CreateInstitutionProduct_API().createInstitutionProduct_api()
    # 修改机构产品
    ModifyInstitutionProduct_API().modifyInstitutionProduct_api()
    # 机构产品排序
    InstitutionProductSort_API().institutionProductSort_api()
    # 机构产品查询
    QueryInstitutionProduct_API().queryInstitutionProduct_api()
    # 查询客户信息
    QueryClientInfo_API().queryClientInfo_api()
    # 查询贷款进件
    QueryLoanEntry_API().queryLoanEntry_api()
    # 查询贷款放款
    QueryLoanWithdraw_API().queryLoanWithdraw_api()

if __name__=="__main__":
    pytest.main()


