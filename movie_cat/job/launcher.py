import sys, argparse
import importlib
import click

from flask.cli import AppGroup, FlaskGroup
job_cli = AppGroup('runjob')

"""
统一job入口，通过不同的路径文件名解析不同的文件
flask runjob run -m test
flask runjob run -m test
"""
@job_cli.command('run')
@click.option('-n', '--name', metavar='name', help='指定job名', required=True)
@click.option('-a', '--act', metavar='act', help='job动作')
@click.option('-p', '--param', multiple=True, type=int, metavar='param', help='业务参数')
@click.pass_context
def run(ctx, name, act, param):
    """函数的参数要对应装饰器配置的参数个数（ctx必填）"""
    # 找到文件并引入
    print(param)
    try:
        if name:
            module_name = name.replace('/', '.')
            import_string = f'job.tasks.{module_name}'
            # 根据导入路径字符串导入文件
            target = importlib.import_module(import_string)
            target.run(name)
    except Exception as e:
        print(e)
