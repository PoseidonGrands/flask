from flask import Flask

from test_flask.models import db
from test_flask.views import index

app = Flask(__name__)
# 添加调试模式
app.debug = True
# 数据库连接参数
HOSTNAME = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = '2280139492'
DATABASE = 'test_flask'
# 配置mysql连接字符串
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
db.init_app(app)

# 注册蓝图
app.register_blueprint(index, url_prefix='/index/')