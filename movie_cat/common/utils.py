import base64
import hashlib
import random
import string

from flask import jsonify
def response_json(code=200, msg='操作成功', data=None):
    if data is None:
        data = {}
    return jsonify({'code': code, 'msg': msg, 'data': data})

def response_error_json(msg='操作失败'):
    return response_json(code=-1, msg=msg, data={})

def gene_salt(length=6):
    # string.ascii_letters是a-z，string.digits是0-9
    salt = [ random.choice((string.ascii_letters + string.digits)) for _ in range(length)]
    return ''.join(salt)

def gene_pwd(pwd, salt):
    m = hashlib.md5()
    str = f'{base64.encodebytes(pwd.encode("utf-8"))}-{salt}'
    m.update(str.encode('utf-8'))
    return m.hexdigest()