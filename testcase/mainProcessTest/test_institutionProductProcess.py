# -*- coding:utf-8 -*-
from interface.institutionManagement_api.institutionProductSort_api import InstitutionProductSort_API
from interface.institutionManagement_api.createInstitutionProduct_api import CreateInstitutionProduct_API
from interface.institutionManagement_api.queryInstitutionProduct_api import QueryInstitutionProduct_API
from interface.institutionManagement_api.modifyInstitutionProduct_api import ModifyInstitutionProduct_API
from interface.adminLogin_api.adminLogin_api import AdminLogin_API
import pytest

@pytest.mark.IPP
def test_institutionProductProcess():
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
    """
    @pytest.fixture()
    def login():
        login = AdminLogin_API()
        login()
        assert login.msg == "请求成功"
    """
    """
    #create = CreateInstitutionProduct_API()
    #create()
    #assert create.msg == "请求成功"
    #assert create.status_code == 200
    #修改机构产品
    modify = ModifyInstitutionProduct_API()
    modify()
    assert modify.status_code == 200
    assert modify.msg == "请求成功"
    #机构产品排序
    sort = InstitutionProductSort_API()
    sort()
    assert sort.status_code == 200
    assert sort.msg == "请求成功"
    #机构产品查询
    query = QueryInstitutionProduct_API()
    query()
    assert query.status_code == 200
    assert query.msg == "请求成功"
"""

if __name__=="__main__":
    pytest.main()


