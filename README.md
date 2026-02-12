# 🎯 Jira Manager

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Issues](https://img.shields.io/github/issues/Jeevi1990/jira-manager)
![Stars](https://img.shields.io/github/stars/Jeevi1990/jira-manager)
![Forks](https://img.shields.io/github/forks/Jeevi1990/jira-manager)
![Last Commit](https://img.shields.io/github/last-commit/Jeevi1990/jira-manager)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**A powerful, user-friendly CLI tool to streamline Jira project management through automation**

[Features](#-features) •
[Installation](#-installation) •
[Quick Start](#-quick-start) •
[Documentation](#-documentation) •
[Contributing](#-contributing)

</div>

---

## 🌟 Why Jira Manager?

Managing Jira tickets manually can be time-consuming and repetitive. **Jira Manager** brings the power of Jira to your command line with:

- 🚀 **Lightning-fast** issue creation, updates, and searches
- 🎨 **Beautiful CLI** with colorful output and interactive prompts
- 🔧 **Highly configurable** via config files or environment variables
- 📊 **Bulk operations** to handle multiple tickets at once
- 🔍 **Advanced search** with JQL support
- 🤖 **Automation-ready** for CI/CD pipelines and scripts

## ✨ Features

### Core Functionality
- ✅ **Create** issues with full field support
- 📋 **List & Search** issues with custom JQL queries
- ✏️ **Update** issue fields, assignees, and priorities
- 💬 **Add comments** and @mention team members
- 🔄 **Transition** issues through workflow states
- 🗑️ **Delete** issues (with confirmation prompts)
- 📎 **Attach files** to issues
- 🏷️ **Manage labels** and custom fields

### Advanced Features
- 📊 **Bulk operations** - Create/update multiple issues from CSV
- 🎯 **Templates** - Save and reuse issue configurations
- 🔔 **Notifications** - Get updates on issue changes
- 📈 **Reports** - Generate sprint and project reports
- 🔐 **Secure** - API token authentication
- 🌈 **Rich output** - Tables, colors, and formatted displays

## 📦 Installation

### Via pip (Recommended)
```bash
pip install jira-manager
```

### From Source
```bash
git clone https://github.com/Jeevi1990/jira-manager.git
cd jira-manager
pip install -e .
```

### Requirements
- Python 3.8 or higher
- Jira Cloud or Server instance
- API token ([Get yours here](https://id.atlassian.com/manage-profile/security/api-tokens))

## 🚀 Quick Start

### 1. Configure Credentials

Create a `.env` file or `config.ini`:

```bash
# .env file
JIRA_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your_api_token_here
JIRA_PROJECT_KEY=PROJ
```

Or use `config.ini`:
```ini
[jira]
JIRA_URL = https://your-domain.atlassian.net
JIRA_EMAIL = your-email@example.com
JIRA_API_TOKEN = your_api_token
JIRA_PROJECT_KEY = PROJ
PROJECT_ISSUE_TYPE = Task
```

### 2. Create Your First Issue

```bash
# Interactive mode
jira-manager create

# Command-line mode
jira-manager create --summary "Fix login bug" --type Bug --priority High

# From template
jira-manager create --template bug-template.json
```

### 3. Search and List Issues

```bash
# List recent issues in your project
jira-manager list

# Search with JQL
jira-manager search "assignee = currentUser() AND status = 'In Progress'"

# List with filters
jira-manager list --assignee john.doe --status "To Do" --limit 20
```

### 4. Update Issues

```bash
# Update single field
jira-manager update PROJ-123 --status "In Progress"

# Update multiple fields
jira-manager update PROJ-123 --assignee jane.doe --priority Critical --add-label urgent

# Add comment
jira-manager comment PROJ-123 "Working on this now"
```

## 📚 Documentation

### Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `create` | Create a new issue | `jira-manager create --summary "Task"` |
| `list` | List issues | `jira-manager list --limit 10` |
| `search` | Search with JQL | `jira-manager search "priority = High"` |
| `update` | Update an issue | `jira-manager update PROJ-123 --status Done` |
| `comment` | Add a comment | `jira-manager comment PROJ-123 "Fixed!"` |
| `transition` | Change issue status | `jira-manager transition PROJ-123 "In Progress"` |
| `delete` | Delete an issue | `jira-manager delete PROJ-123` |
| `show` | Show issue details | `jira-manager show PROJ-123` |
| `assign` | Assign an issue | `jira-manager assign PROJ-123 john.doe` |

### Configuration Options

The tool supports multiple configuration methods (in order of precedence):

1. **Command-line arguments** - Highest priority
2. **Environment variables** - `.env` file
3. **Configuration file** - `config.ini`
4. **Interactive prompts** - Fallback option

### Environment Variables

```bash
JIRA_URL              # Your Jira instance URL
JIRA_EMAIL            # Your email address
JIRA_API_TOKEN        # API token for authentication
JIRA_PROJECT_KEY      # Default project key
JIRA_ISSUE_TYPE       # Default issue type (Task, Bug, Story)
JIRA_LOG_LEVEL        # Logging level (DEBUG, INFO, WARNING, ERROR)
```

## 🎨 Usage Examples

### Bulk Create Issues from CSV

```bash
jira-manager bulk-create --from-csv issues.csv
```

CSV format:
```csv
summary,description,type,priority,assignee
"Setup CI/CD","Configure GitHub Actions",Task,High,john.doe
"Fix header","Header not responsive",Bug,Medium,jane.smith
```

### Create Issue with Template

```bash
# Save template
jira-manager create --summary "Bug template" --save-template bug.json

# Use template
jira-manager create --template bug.json --summary "New bug found"
```

### Advanced Searching

```bash
# Complex JQL query
jira-manager search "project = PROJ AND created >= -7d AND assignee in (john, jane)"

# Export results to JSON
jira-manager search "status = Done" --export results.json

# Display as table
jira-manager list --format table --fields key,summary,status,assignee
```

### Integration with Scripts

```python
from jira_manager import JiraClient

client = JiraClient.from_env()
issue = client.create_issue(
    summary="Automated issue",
    description="Created by script",
    issue_type="Task"
)
print(f"Created: {issue.key}")
```

## 🏗️ Project Structure

```
jira-manager/
├── src/
│   └── jira_manager/
│       ├── __init__.py
│       ├── cli.py           # CLI interface
│       ├── core.py          # Core Jira operations
│       ├── config.py        # Configuration management
│       ├── utils.py         # Helper functions
│       └── exceptions.py    # Custom exceptions
├── tests/
│   ├── test_core.py
│   ├── test_cli.py
│   └── test_config.py
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions
├── examples/
│   ├── create_issue.py
│   ├── bulk_update.py
│   └── templates/
├── .env.example
├── config.ini.example
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE
```

## 🤝 Contributing

We love contributions! Here's how you can help:

1. 🍴 **Fork** the repository
2. 🌱 **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. 📤 **Push** to the branch (`git push origin feature/amazing-feature`)
5. 🎉 **Open** a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

### Development Setup

```bash
# Clone the repo
git clone https://github.com/Jeevi1990/jira-manager.git
cd jira-manager

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/ tests/
isort src/ tests/

# Lint
flake8 src/ tests/
mypy src/
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=jira_manager --cov-report=html

# Run specific test
pytest tests/test_core.py::test_create_issue
```

## �� Troubleshooting

### Common Issues

**Authentication Failed**
- Verify your API token is correct
- Check if your email matches your Jira account
- Ensure your Jira URL includes `https://`

**Connection Timeout**
- Check your network connection
- Verify Jira instance is accessible
- Try increasing timeout: `--timeout 30`

**Permission Denied**
- Ensure you have permissions to create/edit issues
- Check project permissions in Jira settings

For more help, [open an issue](https://github.com/Jeevi1990/jira-manager/issues).

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes.

## 🛣️ Roadmap

- [ ] Web interface for visual management
- [ ] Support for Jira Data Center
- [ ] Slack/Teams integration
- [ ] Custom dashboard and analytics
- [ ] Plugin system for extensions
- [ ] Multi-project support
- [ ] Offline mode with sync

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [jira-python](https://github.com/pycontribs/jira)
- CLI powered by [Click](https://click.palletsprojects.com/)
- Beautiful output by [Rich](https://github.com/Textualize/rich)

## 📧 Contact

**Jeevi** - [@Jeevi1990](https://github.com/Jeevi1990)

Project Link: [https://github.com/Jeevi1990/jira-manager](https://github.com/Jeevi1990/jira-manager)

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ by the open source community

</div>
