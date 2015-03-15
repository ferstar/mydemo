#!/usr/bin/env python
#coding:utf-8

import sys
from imp import reload
#sys.setdefaultencoding('utf-8')

from handler.index import IndexHandler

url=[
    (r'/', IndexHandler),

    ]
