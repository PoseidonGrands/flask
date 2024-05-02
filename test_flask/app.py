import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from models import db
from views import index

app = Flask(__name__)

# 加载配置文件
app.config.from_pyfile(f'config/basic_setting.py')
# 根据环境变量的值来判断加载开发环境还是生产环境
if 'ops_config' in os.environ:
    app.config.from_pyfile(f'config/{os.environ["ops_config"]}_setting.py')

# 初始化数据库连接对象
db.init_app(app)

toolbar = DebugToolbarExtension(app)

# 注册蓝图
app.register_blueprint(index, url_prefix='/index/')


# 用命令行启动需要的代码
if __name__ == '__main__':
    app.run()