# sys.setdefaultencoding('utf-8')

from handler.index import IndexHandler

url = [
    (r'/', IndexHandler),

]
