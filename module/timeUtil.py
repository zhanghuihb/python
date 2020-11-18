import time

def fotmatTime(longTime):
    '''
    格式化日期时间的函数
    longTime:要格式化的时间
    '''
    return time.strftime('%Y%m%d%H%M%S', time.localtime(longTime))
