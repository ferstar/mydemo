#!/usr/bin/env python
#-*-encodeing:utf-8-*-
#import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import multiprocessing

import os,sys

from application import application

from tornado.options import define,options

define("port", default=9010, help="run on the given port", type=int)
 
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print 'Development server is running at http://127.0.0.1:%s/' % options.port
    print 'Quit the server with Control-C'
    tornado.ioloop.IOLoop.instance().start()
     
if __name__ == '__main__':
    main()
    tornado.options.parse_command_line()
    def run(mid,port):
        print "Process %d start" % mid
        sys.stdout.flush()
        app.listen(port)
        tornado.ioloop.IOLoop.instance().start()
    jobs=list()
    for mid,port in enumerate(range(9010,9014)):
        p=multiprocessing.Process(target=run,args=(mid,port))
        jobs.append(p)
        p.start()
