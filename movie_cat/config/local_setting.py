# 数据库连接参数
HOSTNAME = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = '2280139492'
DATABASE = 'movie_cat'

# 数据库配置
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# secret key
WTF_CSRF_SECRET_KEY = 'movie_cat_abc'
SECRET_KEY = 'movie_cat_abc'