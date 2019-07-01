# -*-  coding:utf-8 -*-
from common.utils.read_catalina import Read_Catalina
from common.log.log import MyLog
from common.utils.SSH_connect import *
import pytest,os,zipfile,csv
from urllib.request import urlretrieve
from common.utils.ERP_DB_connect import connect_ERP_db
from common.utils.testDB_connect import connect_test_db


def test_applicationInformationSecondStep():
    #下载并解压文件
    download_zip_file()
    #读取文件并与ERP数据进行比对
    read_csv()

def __get_download_url():
    #下载日志文件
    file_path = '/log/catalina_AISS.out'
    download_catalina(file_path)
    # 读取日志记录
    catalina = Read_Catalina()

    log_info = catalina.read_catalina()
    for line in log_info:
        line = line.split()
        if "businessDataDownloadNotify" in line:
            if "c.x.f.s.r.l.UserLoanServiceRemoteImpl" in line:
                result = line[-1]  #str类型
                par = result.partition('url":"')[2]
                par2 = par.partition('"')
                url = par2[0]
    #print(url)
    return url

def download_zip_file():
    log = MyLog()
    data_url = __get_download_url()
    #回调函数 a:已经下载的数据块,b:数据块的大小,c:远程文件的大小
    def reporthook(a,b,c):
       print("\rdownloading: %5.1f%%" % (a * b * 100.0 / c), end="")
    path = os.path.dirname(os.path.abspath(__file__))
    data_path = path + "\\DataSource"
    file_path = path + "\\DataSource\\OperatingData.zip"
    if not os.path.isfile(file_path):
        log.info("begin downloading")
        urlretrieve(data_url,file_path,reporthook=reporthook)
        log.info("download is finished")
        # 解压文件
        zipFile = zipfile.ZipFile(file_path)
        zipFile.extractall(data_path)
        zipFile.close()
        # 获取文件大小
        filesize = os.path.getsize(file_path)
        # 文件大小默认以Bytes计， 转换为Mb
        log.info('File size = %.2f Mb' % (filesize / 1024 / 1024))
    else:
        log.info('File already exsits!')
        path = os.path.dirname(os.path.abspath(__file__))
        data_path = path + "\\DataSource"
        for i in os.listdir(data_path):
            path_file = os.path.join(data_path,i)
            if os.path.isfile(path_file):
                os.remove(path_file)
        log.info("begin downloading")
        urlretrieve(data_url, file_path, reporthook=reporthook)
        log.info("download is finished")
        # 解压文件
        zipFile = zipfile.ZipFile(file_path)
        zipFile.extractall(data_path)
        zipFile.close()
        # 获取文件大小
        filesize = os.path.getsize(file_path)
        # 文件大小默认以Bytes计， 转换为Mb
        log.info('File size = %.2f Mb' % (filesize / 1024 / 1024))

# 读取csv文件
def read_csv():
    log = MyLog()
    path = os.path.dirname(os.path.abspath(__file__))
    file = path+"\\DataSource\\PRODUCT.csv"
    res_list = []
    with open(file,'r',encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        while True:
            try:
                csv_next_row = next(csv_reader)
            except:
                break
            else:
                res_list.append(csv_next_row)
    res = res_list[1] #此处仍是list
    qpctext = res[5]
    item_no = res[3]
    #print(item_no)
    sql = "select item_size from bi_t_item_info where item_no = '{}';".format(item_no)
    res = connect_ERP_db(sql)
    item_size = ''.join(res)
    #比对csv文件与ERP数据库的数据是否一致，可以多表多数据比对
    if item_size == qpctext:
        log.info("applicationInformation is correct")
    else:
        raise RuntimeError("applicationInformation is incorrect!")
    #获取商户贷款申请的open_id
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    log_path = path + "\\common\\log\\log.log"
    #print(log_path)
    with open(log_path,'r',encoding='utf-8') as log_info:
        for line in log_info:
            line = line.split()
            if "AIFS" in line:
                result = line
                open_id = result[7]

    #校验测试数据库中f_user_loan表，loan_status为0
    sql = "select loan_status from f_user_loan where open_id = '{}'".format(open_id)
    res = connect_test_db(sql)
    loan_status = res[0]['loan_status']
    if loan_status == 1:
        log.info("The status of loan is correct at the second step")
    else:
        log.error("The status of loan is incorrect at the second step")
#read_csv()


if __name__=="__main__":
    pytest.main()