"""
Jira Manager - A powerful CLI tool for Jira automation
"""

__version__ = "1.0.0"
__author__ = "Jeevi"
__license__ = "MIT"

from .core import JiraClient
from .config import Config
from .exceptions import JiraManagerError, AuthenticationError, ConnectionError

__all__ = [
    "JiraClient",
    "Config",
    "JiraManagerError",
    "AuthenticationError",
    "ConnectionError",
]
