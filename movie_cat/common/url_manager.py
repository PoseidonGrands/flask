DOMAIN = 'http://127.0.0.1:5002'

class URLManager(object):
    @staticmethod
    def buildUrl( path ):
        return f'{DOMAIN}{path}'

    @staticmethod
    def buildStaticUrl(path):
        return f'{DOMAIN}/static{path}'