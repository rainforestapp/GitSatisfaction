#!/usr/bin/env python
import os.path
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options

import json
import handlers

from tornado.options import define

define("port", default=5000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        urls = [
            (r"/issues/?", handlers.IssuesHandler),
            (r"/?", handlers.MainHandler),
            (r"/(callbacks/github)?", handlers.GithubCallbackHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, urls, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
