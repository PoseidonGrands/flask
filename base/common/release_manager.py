import os

from movie_cat.common.date_helper import get_current_time_format

def get_release():
    """开发环境：用当前时间做版本号
    生产环境：读取配置文件的版本号"""
    time_fmt = '%Y%m%d%H%M%S'
    from movie_cat.app import app
    # get方法获取不到不会报错
    path = app.config.get('RELEASE_PATH')
    if path and os.path.exists(path):
        with open(path, 'r') as f:
            return f.read()
    else:
        return get_current_time_format(time_fmt)