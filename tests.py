from tornado import testing
from os import environ
import json
import unittest
from models.issue import Issue

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


class Empty: pass

class TestIssueModel(unittest.TestCase):
    def test_add_subscripber(self):
        g3_issue = Empty()
        g3_issue.body_text = ""
        g3_issue.id = 1
        g3_issue.title = 5
        def empty(*args, **kwargs):
            pass
        g3_issue.edit = empty

        issue = Issue(g3_issue)
        issue.add_subscriber("foo1@bar.com")
        issue.add_subscriber("foo2@bar.com")
        b = issue.to_json()['body']
        self.assertIn("listeners: foo1@bar.com,foo2@bar.com", b)
