import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from movie_cat.common.url_manager import URLManager
from movie_cat.controllers.account import account
from movie_cat.controllers.index import index
from movie_cat.models import db


app = Flask(__name__)

# 加载配置
app.config.from_pyfile('config/basic_setting.py')
if 'ops_config' in os.environ:
    app.config.from_pyfile(f'config/{os.environ["ops_config"]}_setting.py')

# 初始化调试工具
toolbar = DebugToolbarExtension(app)

# 初始化数据库连接对象
db.init_app(app)

# 蓝图注册
app.register_blueprint(account, url_prefix='/account/')
app.register_blueprint(index, url_prefix='/')

# 添加自定义模板函数
app.add_template_global(URLManager.build_url, 'build_url')
app.add_template_global(URLManager.build_static_url, 'build_static_url')

# 用命令行启动需要的代码
if __name__ == '__main__':
    app.run()