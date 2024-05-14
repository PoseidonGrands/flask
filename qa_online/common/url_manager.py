from .release_manager import get_release

DOMAIN = 'http://127.0.0.1:5003'

class URLManager(object):
    @staticmethod
    def build_url( path ):
        return f'{DOMAIN}{path}'

    @staticmethod
    def build_static_url(path):
        return f'{DOMAIN}/static{path}?ves={get_release()}'

