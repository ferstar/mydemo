import multiprocessing
import sys

import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application


if __name__ == '__main__':
    tornado.options.parse_command_line()

    def run(mid, port):
        print("Process %d started, Server started at port %d." % (mid, port))
        sys.stdout.flush()
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(port)
        tornado.ioloop.IOLoop.instance().start()

    jobs = list()
    for mid, port in enumerate(range(9010, 9014)):
        p = multiprocessing.Process(target=run, args=(mid, port))
        jobs.append(p)
        p.start()
