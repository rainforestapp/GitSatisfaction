import tornado.web
import github3
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "main.html",
            page_title='user: %s, pass: %s' % (SETTINGS['github_user'], SETTINGS['github_pass']),
            google_analytics_id=SETTINGS['google_analytics_id'],
        )


class IssuesHandler(tornado.web.RequestHandler):
    def get(self):
    	r = github3.repository('rainforestapp', 'GitSatisfaction')
        out = []
        for issue in r.iter_issues(state='open', labels='gs'):
            out.append({'id': issue.id,
                'text': issue.body_text})
        self.write(json.dumps(out))
    def post(self):
    	r = github3.repository('rainforestapp', 'GitSatisfaction')
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