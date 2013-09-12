from tornado import testing
from os import environ
import json

environ['GITHUB_USER'] = 'gitsatisfaction'
environ['GITHUB_PASS'] = 'Password123'
environ['GITHUB_REPO'] = 'GitSatisfaction'

import server

class IssuesTest(testing.AsyncHTTPTestCase):
    def get_app(self):
        return server.Application()

    def test_issues(self):
        self.http_client.fetch(self.get_url('/issues/'), self.stop)
        response = self.wait()
        self.assertTrue(json.loads(response.body))

    def test_subscribe(self):
        self.http_client.fetch(self.get_url('/issues/1/subscribe'), self.stop,
                method="POST", body='{"email": "foo@bar.com"}')
        response = self.wait()
        j = json.loads(response.body)
        self.assertTrue(j)
        self.assertIn("foo@bar", j["body"])

