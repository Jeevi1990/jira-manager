"""Example: Create a simple issue"""

from src.jira_manager import JiraClient

# Initialize client
client = JiraClient()

# Create a basic issue
issue = client.create_issue(
    summary="Sample issue from example script",
    description="This is a test issue created using the JiraClient library.",
    priority="Medium"
)

print(f"✅ Created issue: {issue.key}")
print(f"   URL: {client.config.jira_url}/browse/{issue.key}")
