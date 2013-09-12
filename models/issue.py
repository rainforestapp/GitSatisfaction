import re

class Issue(object):
    def __init__(self, g3_issue):
        self.g3_issue = g3_issue

    def to_json(self):
        return  {
            'id': self.g3_issue.id,
            'body': self.g3_issue.body_text,
            'title': self.g3_issue.title, 
            'num_subscribers': len(self.get_listeners())
        }

    def get_listeners(self):
        start = "listeners: "
        for line in self.g3_issue.body_text.split("\n"):
            if line.startswith(start):
                return line[len(start):].split(",")

        return []


    def add_subscriber(self, email):
        listeners = self.get_listeners()
        listeners.append(email)

        body = self.g3_issue.body_text
        body = re.sub(r"^listeners:\s.*$", '', body, flags=re.MULTILINE)
        b = body + "\nlisteners: " + ",".join(listeners)
        self.g3_issue.body_text = b
        self.g3_issue.edit(body = b)

