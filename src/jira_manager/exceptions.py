"""Custom exceptions for Jira Manager"""


class JiraManagerError(Exception):
    """Base exception for all Jira Manager errors"""
    pass


class AuthenticationError(JiraManagerError):
    """Raised when authentication fails"""
    pass


class ConnectionError(JiraManagerError):
    """Raised when connection to Jira fails"""
    pass


class ConfigurationError(JiraManagerError):
    """Raised when configuration is invalid"""
    pass


class IssueNotFoundError(JiraManagerError):
    """Raised when an issue cannot be found"""
    pass


class PermissionError(JiraManagerError):
    """Raised when user doesn't have required permissions"""
    pass
