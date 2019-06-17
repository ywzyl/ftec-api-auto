# -*-  coding:utf-8 -*-
from common.utils.read_catalina import Read_Catalina
from common.log.log import MyLog
from common.utils.testDB_connect import connect_test_db
from common.utils.SSH_connect import *
import pytest,os

def test_applicationInformationFirstStep():
    #下载日志文件
    file_path = '/log/catalina_AIFS.out'
    download_catalina(file_path)
    #读取日志记录，ugly code
    log = MyLog()
    catalina = Read_Catalina()
    log_info = catalina.read_catalina()
    for line in log_info:
        line = line.split()
        if 'url:http://jie2.test.jisucloud.cn/api/getapplication' in line:
            result = line[-1]
            open_id = catalina.get_open_id(line)
            #将open_id写入日志，用于下一步的loan_status校验使用
            log.info("The flag of open_id : {} is AIFS".format(open_id))
            #f_user_info表数据校验
            sql = "select * from f_user_info where open_id='{}'".format(open_id)
            res = connect_test_db(sql)  #此处res类型为list
            res = res[0]  #此处res类型为dict
            keys = ('name','idcard','mobile','home_province','home_city','home_area','home_address','family_contact',
                    'family_relationship','family_mobile','work_contact','work_relationship','work_mobile',
                    'other_contact','other_relationship','other_mobile')
            for key in res:
                if res['open_id'] == open_id:
                    if res['idcard_front_image'] != None and res['idcard_back_image'] != None and res['create_time'] != None:
                        if key in keys:  #判断在极速云返回的数据中需要写入数据库存储的字段是否成功写入
                            val = res[key]
                            if result.__contains__(str(val)):  #判断数据库存储的数据与极速云返回数据是否一致
                                log.info('{} is written to database successfully'.format(key))
                            else:
                                log.error('{} is not written to database '.format(key))
                                raise RuntimeError('Database write failed:{} is not written to database'.format(key))
                    else:
                        log.error("Database write failed")
                        raise RuntimeError('Database write failed:{} is not written to database'.format('idcard_front_image or idcard_back_image or create_time'))
                else:
                    log.error('open_id is not the same')
                    raise RuntimeError('open_id is not the same')

            #f_user_loan表数据校验，loan_status为0
            sql = "select * from f_user_loan where open_id='{}'".format(open_id)
            res = connect_test_db(sql)
            res = res[0]
            keys = ('purpose','amount','duration')
            for key in keys:
                if res['open_id'] == open_id:
                    if res['loan_status'] == 0:
                        if key in keys:
                            val = res[key]
                            if result.__contains__(str(val)):
                                log.info('{} is written to database successfully'.format(key))
                            else:
                                log.error('{} is not written to database '.format(key))
                                raise RuntimeError('Database write failed:{} is not written to database'.format(key))
                        else:
                            log.error("Database write failed")
                            raise RuntimeError('Database write failed:{} is not written to database'.format(
                                'idcard_front_image or idcard_back_image or create_time'))
                    else:
                        log.error('The status of loan is incorrect at the first step')
                        raise RuntimeError('The status of loan is incorrect at the first step')
                else:
                    log.error('open_id is not the same')
                    raise RuntimeError('open_id is not the same')





if __name__=="__main__":
    pytest.main()