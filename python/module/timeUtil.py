import time

def fotmatTime(longTime):
    """
    格式化日期时间的函数
    longTime:要格式化的时间
    :param longTime:
    :return:
    """
    return time.strftime('%Y%m%d%H%M%S', time.localtime(longTime))

def fotmatCurrentTimeWithFormat(format):
    """
    格式化日期时间的函数
    :return:
    """
    return time.strftime(format, time.localtime())

def fotmatTimeWithFormat(format, longTime):
    """
    格式化日期时间的函数
    longTime:要格式化的时间
    :param longTime:
    :return:
    """
    return time.strftime(format, time.localtime(longTime))