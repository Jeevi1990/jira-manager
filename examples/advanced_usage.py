"""Example: Advanced issue management"""

from src.jira_manager import JiraClient

# Initialize client
client = JiraClient()

# Create an issue with more details
issue = client.create_issue(
    summary="Implement user authentication feature",
    description="""
    # Requirements
    - Add login page
    - Implement JWT authentication
    - Add password reset functionality
    
    # Acceptance Criteria
    - Users can log in with email/password
    - JWT tokens expire after 24 hours
    - Password reset emails are sent successfully
    """,
    priority="High",
    labels=["feature", "authentication", "security"],
    assignee="username"  # Replace with actual Jira username
)

print(f"✅ Created issue: {issue.key}")

# Add a comment
client.add_comment(issue.key, "Starting work on this feature")

# List recent issues
print("\n📋 Recent issues in project:")
issues = client.list_issues(limit=5)
for i in issues:
    print(f"   {i.key}: {i.fields.summary}")

# Get available transitions
transitions = client.get_transitions(issue.key)
print(f"\n🔄 Available transitions for {issue.key}:")
for t in transitions:
    print(f"   - {t['name']}")
