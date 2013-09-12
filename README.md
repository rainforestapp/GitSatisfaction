# GitStatisfaction

Use github issues for customer facing problems.

## Development Envrionment

Install virtual env

    pip install virtualenv

    virtualenv .

    source bin/activate

    pip install -r requirements.txt

## Running the server

    GITHUB_USER=gitsatisfaction GITHUB_PASS=Password123 ./server.py

## Setup the issues hook

    curl -X POST -d '{"name": "web", "config": {"url": "http://YOUR_DOMAIN/callbacks/github", "content_type": "json"}, "events": ["issues", "issue_comment"]}'  https://api.github.com/repos/REPO_OWNER/REPO_NAME/hooks?access_token=ACCESS_TOKEN 

## Test callback

    curl -d "payload=`cat _github_sample.json`" http://localhost:5000/callbacks/github


