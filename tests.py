from tornado import testing
from os import environ

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
        self.assertIn("hello", response.body)