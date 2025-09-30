import configparser
from jira import JIRA

# Load config
config = configparser.ConfigParser()
config.read('config.ini')

JIRA_URL = config['jira']['JIRA_URL']
EMAIL = config['jira']['JIRA_EMAIL']
API_TOKEN = config['jira']['JIRA_API_TOKEN']
PROJECT_KEY = config['jira']['JIRA_PROJECT_KEY']
ISSUE_TYPE = config['jira']['PROJECT_ISSUE_TYPE']

ISSUE_SUMMARY = 'Example issue from Python script'
ISSUE_DESCRIPTION = 'This ticket was created using jira-manager with config.ini.'

jira = JIRA(server=JIRA_URL, basic_auth=(EMAIL, API_TOKEN))

issue_dict = {
    'project': {'key': PROJECT_KEY},
    'summary': ISSUE_SUMMARY,
    'description': ISSUE_DESCRIPTION,
    'issuetype': {'name': ISSUE_TYPE}
}

new_issue = jira.create_issue(fields=issue_dict)

print(f"Issue {new_issue.key} created: {JIRA_URL}/browse/{new_issue.key}")
