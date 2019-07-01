import time
from datetime import datetime
import random


def set_timeStamp_flag():
    # 获取当前时间
    times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 转为时间数组
    timeArray = time.strptime(times,"%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

def __strTimeProp(start, end, prop, frmt):
    """将输入时间转换成时间戳格式，进行加减，得出随机时间戳后再转换成需要的日期格式"""
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + prop * (etime - stime)
    return int(ptime)

def randomDate(start, end, frmt='%Y-%m-%d'):
    """获取两个时间点间的随机时间"""
    return time.strftime(frmt, time.localtime(__strTimeProp(start, end, random.random(), frmt)))

