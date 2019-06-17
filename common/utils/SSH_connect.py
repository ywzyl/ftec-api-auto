# -*- coding:utf-8 -*-
import paramiko
from common.settings.host_dict import *
from datetime import datetime
import os

class SSHConnection(object):
    def __init__(self):
        self.host = host
        self.username = username
        self.pwd = pwd
        self.port = port
        self.__k = None

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def run_cmd(self,command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        #执行命令
        stdin,stdout,stderr = ssh.exec_command(command)
        #获取命令结果
        result = stdout.read()
        return result

    def upload(self,local_path,target_path):
        # 连接，上传
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将本地文件上传至服务器
        sftp.put(local_path,target_path,confirm=True)
        # 增加权限
        # 注意这里的权限是八进制的，八进制需要使用0o作为前缀
        sftp.chmod(target_path,0o755)

    def download(self,target_path,local_path):
        # 连接，下载
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将服务器文件下载至本地
        sftp.get(target_path,local_path)

    # 销毁
    def __del__(self):
        self.close()

#下载provider中logs的catalina.out日志文件
def download_catalina(file_path):
    dl = SSHConnection()
    dl.connect()
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    local_path = path + file_path #'/log/catalina.out'
    dl.download("/xdd/application/tomcat_finance_provider/logs/catalina.out", local_path)

if __name__=="__main__":
    dl = SSHConnection()
    dl.connect()
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    local_path = path+'/log/catalina.out'
    dl.download("/xdd/application/tomcat_finance_provider/logs/catalina.out",local_path)

