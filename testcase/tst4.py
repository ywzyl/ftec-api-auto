import os
from common.utils.read_catalina import read_catalina
def tst():
    """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = path+'\\common\\log\\catalina.out'
    i = open(path,'r',encoding='utf-8')
    """
    i = read_catalina()
    r = []


    for line in i:
        line = line.split()
        if 'url:http://jie2.test.jisucloud.cn/api/getapplication' in line:
            r.append(line[-1])
            res = r[0]
            if res.__contains__('13068281408'):
                print('name success write to database')

tst()