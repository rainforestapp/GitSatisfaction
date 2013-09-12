import tornado.web
import github3
import json

from os import environ
from models.issue import Issue

env = environ.get('APP_ENV', 'development')
config = getattr(__import__("config.%s" % env), env)

SETTINGS = config.settings()
client = github3.login(SETTINGS['github_user'], SETTINGS['github_pass'])

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "main.html",
            page_title='GitSatisfaction',
            google_analytics_id=SETTINGS['google_analytics_id'],
        )


class IssuesHandler(tornado.web.RequestHandler):
    def get(self):
        r = client.repository('rainforestapp', 'GitSatisfaction')
        out = []
        for issue in r.iter_issues(state='open'):
            out.append(Issue(issue).to_json())
        self.write(json.dumps(out))

    def post(self):
        r = client.repository('rainforestapp', 'GitSatisfaction')
        new_issue = tornado.escape.json_decode(self.request.body)
        label = r.label('gs')
        if not label: label = r.create_label('gs', '#00ffff')
        issue = r.create_issue(new_issue['title'], body=new_issue['body'])
        issue.add_labels('gs')




class SubscribeHandler(tornado.web.RequestHandler):
    def post(self, issue_id):
        r = client.repository('rainforestapp', 'GitSatisfaction')
        issue = Issue(r.issue(issue_id))

        j = tornado.escape.json_decode(self.request.body)

        issue.add_subscriber(j["email"])

        self.write(issue.to_json())

class GithubCallbackHandler(tornado.web.RequestHandler):
    def post(self, q):
        print "GithubCallbackHandler:"
        payload = tornado.escape.json_decode(self.request.body)
        print payload

        self.content_type = 'application/json'
        self.write(payload['action'])
