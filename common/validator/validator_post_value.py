# -*- coding:utf-8 -*-
from validator import validate,Equals
from common.utils.db_connect import connect_db
from common.utils.testDB_connect import connect_test_db
from validator import validate,Equals
import json
from common.utils.read_sql_script import read_sql_script

class Validator_post():
    def DB_w(self,sql_script_validator_path,sql_script_section,sql_script_name):
        #写入数据库的数据
        s = read_sql_script(sql_script_validator_path)
        sql1 = s.get(sql_script_section,sql_script_name)
        sql_res1 = connect_db(sql1)
        self.validation = json.loads(sql_res1[0]['data'])
        '''
        # 验证
        passes = {
            "name":r['name']
        }
        validation = {
            "name":[Equals(p['name'])]
        }
        '''
        #self.validationResult = validate(validation,passes)
        return self.validation
    def DB_r(self,sql_script_validator_path,sql_script_section,sql_script_name):
        # 读取数据库结果
        s = read_sql_script(sql_script_validator_path)
        sql2 = s.get(sql_script_section, sql_script_name)
        sql_res2 = connect_test_db(sql2)
        self.passes = sql_res2[0]
        return self.passes

