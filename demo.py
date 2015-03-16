#!/usr/bin/env python
import tornado.ioloop
import tornado.options
import tornado.httpserver
import multiprocessing

import os,sys

from application import application

if __name__ == '__main__':
    tornado.options.parse_command_line()
    def run(mid,port):
        print("Process", mid, "start,", "Server started at port", port)
        sys.stdout.flush()
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(port)
        tornado.ioloop.IOLoop.instance().start()
    jobs=list()
    for mid,port in enumerate(range(9010,9014)):
        p=multiprocessing.Process(target=run,args=(mid,port))
        jobs.append(p)
        p.start()
