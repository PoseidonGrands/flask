from .release_manager import get_release

DOMAIN = 'http://127.0.0.1:5003'

class URLManager(object):
    @staticmethod
    def build_url( path, param_value='' ):
        url = f'{DOMAIN}{path}{param_value}'
        print('url is:' + url)
        return url

    @staticmethod
    def build_static_url(path):
        url = f'{DOMAIN}/static{path}?ves={get_release()}'
        # print('static_url is:' + url)
        return url

