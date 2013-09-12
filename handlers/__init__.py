import tornado.web
import github3
import json

from os import environ

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
        for issue in r.iter_issues(state='open', labels='gs'):
            out.append({'id': issue.id,
                'body': issue.body_text,
                'num_subscribers': 5})
        self.write(json.dumps(out))
    def post(self):
        r = client.repository('rainforestapp', 'GitSatisfaction')
        print self.request.body
        new_issue = tornado.escape.json_decode(self.request.body)
        label = r.label('gs')
        if not label: label = r.create_label('gs', '#00ffff')
        r.create_issue(new_issue['title'], body=new_issue['body'], labels='[gs]')

class GithubCallbackHandler(tornado.web.RequestHandler):
    def post(self, q):
        print "GithubCallbackHandler:"
        payload = tornado.escape.json_decode(self.get_argument('payload'))
        print payload

        self.content_type = 'application/json'
        self.write(payload['after'])
