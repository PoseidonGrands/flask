import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# 加载配置
app.config.from_pyfile('config/basic_setting.py')
# 从环境变量加载ops_config变量值（区分开发环境和生产环境的配置
if 'ops_config' in os.environ:
    app.config.from_pyfile(f'config/{os.environ["ops_config"]}_setting.py')

# 初始化调试工具
toolbar = DebugToolbarExtension(app)

# 初始化数据库连接对象
# db.init_app(app)

# 蓝图注册


# 添加自定义模板函数
# app.add_template_global(URLManager.build_url, 'build_url')
# app.add_template_global(URLManager.build_static_url, 'build_static_url')

# 拦截器代码引入
# from interceptors.auth import *

# 初始化命令行解析器
from jobs.launcher import *
# app.cli.add_command(job_cli)

