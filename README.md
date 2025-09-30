# jira-manager
A lightweight tool to streamline Jira project management through automation, integration, and custom workflows

# Jira Manager

Automate Jira issue creation and management using Python.

## Overview

This project provides an easy way to create, update, and manage Jira tickets programmatically using Python and the [`jira`](https://pypi.org/project/jira/) library. Configuration is handled via a simple `config.ini` file, making setup quick and straightforward.

## Features

- Create Jira issues from scripts
- Use configuration files for credentials and project info
- Easily extendable for updating issues, adding comments, and more

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Jeevi1990/jira-manager.git
   cd jira-manager
   ```

2. **Install Dependencies**

   ```bash
   pip install jira configparser
   ```

3. **Configure Credentials**

   Create a `config.ini` file in the project root:

   ```ini
   [jira]
   JIRA_URL = https://your-domain.atlassian.net
   JIRA_EMAIL = your-email@example.com
   JIRA_API_TOKEN = your_api_token
   JIRA_PROJECT_KEY = YOURPROJECT
   PROJECT_ISSUE_TYPE = Task
   ```

   - You can get your API token from [Atlassian's API token manager](https://id.atlassian.com/manage-profile/security/api-tokens).

## Usage

Run the main script to create a Jira issue:

```bash
python create_issue.py
```

You can modify the script to customize issue summaries, descriptions, or extend its functionality.

## Example

```python
import configparser
from jira import JIRA

# Load config
config = configparser.ConfigParser()
config.read('config.ini')

jira = JIRA(
    server=config['jira']['JIRA_URL'],
    basic_auth=(config['jira']['JIRA_EMAIL'], config['jira']['JIRA_API_TOKEN'])
)

issue_dict = {
    'project': {'key': config['jira']['JIRA_PROJECT_KEY']},
    'summary': 'Sample Issue',
    'description': 'Created via Python script.',
    'issuetype': {'name': config['jira']['PROJECT_ISSUE_TYPE']}
}

new_issue = jira.create_issue(fields=issue_dict)
print(f"Issue {new_issue.key} created.")
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## License

[MIT](LICENSE)
