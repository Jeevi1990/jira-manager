"""Core Jira operations"""

import logging
from typing import Optional, List, Dict, Any
from jira import JIRA, JIRAError
from .config import Config
from .exceptions import (
    AuthenticationError,
    ConnectionError,
    IssueNotFoundError,
    JiraManagerError,
)


logger = logging.getLogger(__name__)


class JiraClient:
    """Enhanced Jira client with additional features"""
    
    def __init__(self, config: Optional[Config] = None):
        """Initialize Jira client"""
        self.config = config or Config()
        self._jira = None
        self._connect()
    
    def _connect(self):
        """Establish connection to Jira"""
        try:
            self._jira = JIRA(
                server=self.config.jira_url,
                basic_auth=(self.config.jira_email, self.config.jira_api_token)
            )
            logger.info(f"Connected to Jira: {self.config.jira_url}")
        except JIRAError as e:
            if e.status_code == 401:
                raise AuthenticationError(
                    "Authentication failed. Please check your email and API token."
                ) from e
            raise ConnectionError(
                f"Failed to connect to Jira: {e}"
            ) from e
    
    @classmethod
    def from_env(cls) -> "JiraClient":
        """Create client from environment variables"""
        return cls(Config())
    
    def create_issue(
        self,
        summary: str,
        description: str = "",
        issue_type: Optional[str] = None,
        project_key: Optional[str] = None,
        priority: Optional[str] = None,
        assignee: Optional[str] = None,
        labels: Optional[List[str]] = None,
        **kwargs
    ) -> Any:
        """Create a new Jira issue"""
        project_key = project_key or self.config.project_key
        issue_type = issue_type or self.config.issue_type
        
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type},
        }
        
        if priority:
            issue_dict['priority'] = {'name': priority}
        
        if assignee:
            issue_dict['assignee'] = {'name': assignee}
        
        if labels:
            issue_dict['labels'] = labels
        
        # Add any additional fields
        issue_dict.update(kwargs)
        
        try:
            new_issue = self._jira.create_issue(fields=issue_dict)
            logger.info(f"Created issue: {new_issue.key}")
            return new_issue
        except JIRAError as e:
            raise JiraManagerError(f"Failed to create issue: {e}") from e
    
    def get_issue(self, issue_key: str) -> Any:
        """Get an issue by key"""
        try:
            return self._jira.issue(issue_key)
        except JIRAError as e:
            if e.status_code == 404:
                raise IssueNotFoundError(f"Issue {issue_key} not found") from e
            raise JiraManagerError(f"Failed to get issue: {e}") from e
    
    def update_issue(
        self,
        issue_key: str,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        assignee: Optional[str] = None,
        priority: Optional[str] = None,
        labels: Optional[List[str]] = None,
        **kwargs
    ) -> Any:
        """Update an existing issue"""
        issue = self.get_issue(issue_key)
        update_fields = {}
        
        if summary:
            update_fields['summary'] = summary
        if description:
            update_fields['description'] = description
        if assignee:
            update_fields['assignee'] = {'name': assignee}
        if priority:
            update_fields['priority'] = {'name': priority}
        if labels is not None:
            update_fields['labels'] = labels
        
        update_fields.update(kwargs)
        
        try:
            issue.update(fields=update_fields)
            logger.info(f"Updated issue: {issue_key}")
            return issue
        except JIRAError as e:
            raise JiraManagerError(f"Failed to update issue: {e}") from e
    
    def add_comment(self, issue_key: str, comment: str) -> Any:
        """Add a comment to an issue"""
        try:
            result = self._jira.add_comment(issue_key, comment)
            logger.info(f"Added comment to {issue_key}")
            return result
        except JIRAError as e:
            raise JiraManagerError(f"Failed to add comment: {e}") from e
    
    def transition_issue(self, issue_key: str, transition_name: str) -> None:
        """Transition an issue to a new status"""
        try:
            self._jira.transition_issue(issue_key, transition_name)
            logger.info(f"Transitioned {issue_key} to {transition_name}")
        except JIRAError as e:
            raise JiraManagerError(f"Failed to transition issue: {e}") from e
    
    def delete_issue(self, issue_key: str) -> None:
        """Delete an issue"""
        try:
            issue = self.get_issue(issue_key)
            issue.delete()
            logger.info(f"Deleted issue: {issue_key}")
        except JIRAError as e:
            raise JiraManagerError(f"Failed to delete issue: {e}") from e
    
    def search_issues(
        self,
        jql: str,
        max_results: int = 50,
        fields: Optional[List[str]] = None
    ) -> List[Any]:
        """Search issues using JQL"""
        try:
            issues = self._jira.search_issues(
                jql,
                maxResults=max_results,
                fields=fields or '*all'
            )
            logger.info(f"Found {len(issues)} issues")
            return issues
        except JIRAError as e:
            raise JiraManagerError(f"Failed to search issues: {e}") from e
    
    def list_issues(
        self,
        project_key: Optional[str] = None,
        assignee: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 20
    ) -> List[Any]:
        """List issues with filters"""
        project_key = project_key or self.config.project_key
        jql_parts = [f"project = {project_key}"]
        
        if assignee:
            jql_parts.append(f"assignee = {assignee}")
        if status:
            jql_parts.append(f"status = '{status}'")
        
        jql = " AND ".join(jql_parts)
        jql += " ORDER BY created DESC"
        
        return self.search_issues(jql, max_results=limit)
    
    def get_transitions(self, issue_key: str) -> List[Dict[str, Any]]:
        """Get available transitions for an issue"""
        try:
            transitions = self._jira.transitions(issue_key)
            return [{'id': t['id'], 'name': t['name']} for t in transitions]
        except JIRAError as e:
            raise JiraManagerError(f"Failed to get transitions: {e}") from e
    
    def assign_issue(self, issue_key: str, assignee: str) -> None:
        """Assign an issue to a user"""
        try:
            self._jira.assign_issue(issue_key, assignee)
            logger.info(f"Assigned {issue_key} to {assignee}")
        except JIRAError as e:
            raise JiraManagerError(f"Failed to assign issue: {e}") from e
