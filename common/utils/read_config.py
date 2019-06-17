# -*- coding:utf-8 -*-
import os,configparser as cparser

def read_config_ini():
    base_dir = str(os.path.dirname(os.path.dirname(__file__)))
    base_dir = base_dir.replace("\\","/")
    file_path = base_dir+"/settings/config.ini"
    #print(file_path)
    cf = cparser.ConfigParser()
    cf.read(file_path)
    return cf





