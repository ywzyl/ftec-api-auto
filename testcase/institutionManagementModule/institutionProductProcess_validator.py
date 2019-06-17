# -*- coding:utf-8 -*-
from common.validator.validator_post_value import Validator_post
import unittest
from validator import Equals,validate

class InstitutionProductValidator(unittest.TestCase):
    def test_institutionProductValidator(self):
        v = Validator_post
        #写入数据库的数据
        v.DB_w(self,"sql_script_validator.ini","sql_script_validator_institutionProduct","modifyInstitutionProduct")
        # 读取数据库结果
        v.DB_r(self,"sql_script_validator.ini","sql_script_validator_institutionProduct_DBTest","modifyInstitutionProduct")
        # 验证
        validation = {
            "name":Equals(v.validation['name'])
        }
        passes = {
            "name":v.passes['name']
        }
        validationResult = validate(validation,passes)
        print(validationResult)
        #self.assertEqual(validationResult,'')

if __name__=='__main__':
    unittest.main()

