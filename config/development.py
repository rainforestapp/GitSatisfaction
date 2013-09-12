from os import environ

def settings():
    return dict(
        github_user=environ['GITHUB_USER'],
        github_pass=environ['GITHUB_PASS'],
        #github_repo_name=environ['GITHUB_REPO_NAME'],
        #github_repo_owner=environ['GITHUB_REPO_OWNER'],
        google_analytics_id=environ.get('GOOGLEANALYTICSID', False)
    )
