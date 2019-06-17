# -*- coding:utf-8 -*-
import os,time,configparser
from ftplib import FTP
from common.utils.read_config import read_config_ini

class FTPOperate(object):
    def __init__(self):
        r = read_config_ini()
        self.host = r.get("ftp_config","ip")
        self.port = r.get("ftp_config","port")
        self.user = r.get("ftp_config","username")
        self.passwd = r.get("ftp_config","password")

    def connector(self):
        ftp = FTP()
        ftp.set_debuglevel(2)
        ftp.connect(self.host,int(self.port))
        ftp.login(self.user,self.passwd)
        ftp.set_pasv(False)  # 如果被动模式由于某种原因失败，请尝试使用活动模式
        print("已连接到： %s"%self.host)
        return ftp

    def list_files(self):
        ftp = self.connector()
        print(ftp.dir())

    def upload_file(self,local_file,target,filename):
        ftp = self.connector()
        try:
            ftp.cwd(target)  #设置FTP当前操作的路径
        except Exception as e:
            ftp.mkd(target)  #新建远程目录
            ftp.cwd(target)
        buf_size = 1024
        fp = open(local_file,'rb')
        ftp.storbinary('STOR %s'%os.path.basename(filename),fp,buf_size)  #上传文件
        ftp.set_debuglevel(0)
        print('okokokok')
        fp.close()  #关闭文件
        ftp.quit()

    def download_file(self,remotepath,localpath):
        ftp = self.connector()
        buf_size = 1024
        fp = open(localpath,'wb')
        ftp.retrbinary('RETR ' + remotepath,fp.write,buf_size)
        ftp.set_debuglevel(0)
        fp.close()
        ftp.quit()

def ftp_upload():
    sql_file = FTPOperate()
    sql_file.upload_file("D:\\qiang.sql","sqlback","D:\\qiang.sql")


def ftp_download():
    sql_file = FTPOperate()
    sql_file.download_file("/var/ftec/sqlback/qiang.sql","qiang.sql")

if __name__=='__main__':
    #ftp_upload()
    ftp_download()