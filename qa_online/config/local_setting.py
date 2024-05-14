# 数据库连接参数
from datetime import timedelta

HOSTNAME = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = '2280139492'
DATABASE = 'qa_flask'

# 数据库配置
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# WTF表单密钥
# base替换为项目名
WTF_CSRF_SECRET_KEY = 'base_abc'
# 消息闪现密钥
SECRET_KEY = 'base_abc'

AUTH_COOKIE_NAME = 'base'

DEBUG_TB_INTERCEPT_REDIRECTS = False

SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)