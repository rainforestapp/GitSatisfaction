#!/usr/bin/env python
import os.path
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from os import environ

import json

from tornado.options import define
define("port", default=5000, help="run on the given port", type=int)

env = environ.get('APP_ENV', 'development')
config = getattr(__import__("config.%s" % env), env)

SETTINGS = config.settings()

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/issues/?", Issues),
            (r"/?", MainHandler),
            (r"/(callbacks/github)?", GithubCallbackHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "main.html",
            page_title='user: %s, pass: %s' % (SETTINGS['github_user'], SETTINGS['github_pass']),
            google_analytics_id=SETTINGS['google_analytics_id'],
        )

class Issues(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")

class GithubCallbackHandler(tornado.web.RequestHandler):
    def post(self, q):
        print "GithubCallbackHandler:"
        print json.loads(self.request.body)
        self.write("test")

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
