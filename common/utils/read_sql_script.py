# -*-coding:utf-8 -*-
import configparser as cparser
import os

def read_sql_script(sql_script_path):
    base_dir = str(os.path.dirname(os.path.dirname(__file__)))
    base_dir = base_dir.replace('\\','/')
    file_path = base_dir+'/settings/%s'%sql_script_path
    #print(file_path)
    cf = cparser.ConfigParser()
    cf.read(file_path,encoding='UTF-8')
    return cf