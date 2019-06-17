import time
from datetime import datetime


def set_timeStamp_flag():
    # 获取当前时间
    times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 转为时间数组
    timeArray = time.strptime(times,"%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp