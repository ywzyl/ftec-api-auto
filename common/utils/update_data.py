from common.utils.time_utils import randomDate
from common.utils.SSH_connect import *
from common.utils.read_catalina import Read_Catalina
from common.utils.db_connect import connect_db
import time

def __get_sign():
    # 下载日志文件
    file_path = '/log/catalina_sign.out'
    download_catalina(file_path)
    # 读取日志记录
    catalina = Read_Catalina()
    log_info = catalina.read_catalina("catalina_sign.out")
    for line in log_info:
        line = line.split()
        if 'validateSign' in line:
            sign = []
            #print(line)
            str = line[-2].partition(':')[-1]
            sign.append(str)
    return sign[0]

def update_sign(api_name: str):
    sql = """select data from api_req_post where api_name='{}'""".format(api_name)
    res = connect_db(sql)
    new_sign = __get_sign()
    sign = res[0]['data'].split()[4].split('"')[1]
    res1 = res[0]['data']
    new_data = res1.replace(sign,new_sign)
    return new_data

def update_time(api_name: str) -> 'data':
    sql = """select data from api_req_post where api_name='{}'""".format(api_name)
    res = connect_db(sql)
    startTime = res[0]['data'].split()[-2].split('"')[1]
    res1 = res[0]['data']
    new_startTime = randomDate('2018-06-01','2018-08-01')
    new_data = res1.replace(startTime,new_startTime)
    print(new_data)
    return new_data

def update_time_sign(new_data: str) -> 'data':
    """第二次发送时，时间段要与第一次发送时一样，因为第一次生成的sign包含时间段，所以前后时间段要一致"""
    sign = new_data.split()[-4].split('"')[1]
    new_sign =  __get_sign()
    new_data2 = new_data.replace(sign,new_sign)
    return new_data2


