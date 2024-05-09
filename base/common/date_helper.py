from datetime import datetime


def get_current_time_format(fmt):
    """将当前时间转换成目标字符串"""
    now = datetime.now()
    return now.strftime(fmt)
