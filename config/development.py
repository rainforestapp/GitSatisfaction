from os import environ

def settings():
    return dict(
        github_user=environ['GITHUB_USER'],
        github_pass=environ['GITHUB_PASS'],
        google_analytics_id=environ.get('GOOGLEANALYTICSID', False)
    )
