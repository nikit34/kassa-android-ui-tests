import os
from jira import JIRA


class JiraAPI:
    SERVER = 'https://jira.rambler-co.ru'
    USER = 'n.permyakov'

    def __init__(self, project_id='12718'):
        self.project_id = project_id
        self.jira = JIRA(
            options={'server': self.SERVER},
            basic_auth=(self.USER, os.environ['IOS_HOST_PASSWORD'])
        )
        self.issues = []

    def prepare_issue(self, summary, description, type, priority, sprint_id):
        self.issues.append({
            'project': self.project_id,
            'summary': summary,
            'description': description,
            'issuetype': {'name': type},
            'priority': {'name': priority},
            'components': [{'name': 'iOS'}],
            'labels': ['auto_created', 'auto_test'],
            'customfield_10101': sprint_id,
        })

    def create_issues(self):
        return self.jira.create_issues(self.issues)

    def get_permalink(self, issue):
        return issue.permalink()
