from flask import Flask

from test_flask.views import index

app = Flask(__name__)
app.debug = True

# 注册蓝图
app.register_blueprint(index, url_prefix='/index/')