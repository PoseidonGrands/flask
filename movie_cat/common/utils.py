from flask import jsonify, g, render_template

def response_json(code=200, msg='操作成功', data=None):
    if data is None:
        data = {}
    return jsonify({'code': code, 'msg': msg, 'data': data})

def response_error_json(msg='操作失败'):
    return response_json(code=-1, msg=msg, data={})


def ops_render(template_name, data=None):
    data = {}
    if 'current_user' in g:
        data['current_user'] = g.current_user
    # 最后要把字典展开
    return render_template(template_name, **data)


