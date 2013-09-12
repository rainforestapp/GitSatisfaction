from os import environ

def settings():
    return dict(
        github_user="",
        github_pass="",
        google_analytics_id=environ.get('GOOGLEANALYTICSID', False)
    )

