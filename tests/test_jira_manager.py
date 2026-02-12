"""Tests for Jira Manager"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from src.jira_manager import JiraClient, Config
from src.jira_manager.exceptions import (
    AuthenticationError,
    ConnectionError,
    IssueNotFoundError,
    JiraManagerError,
    ConfigurationError
)


class TestConfig:
    """Test configuration management"""
    
    def test_config_from_dict(self):
        """Test creating config with dictionary"""
        config = Config()
        assert config is not None
    
    @patch.dict('os.environ', {
        'JIRA_URL': 'https://test.atlassian.net',
        'JIRA_EMAIL': 'test@example.com',
        'JIRA_API_TOKEN': 'test-token',
        'JIRA_PROJECT_KEY': 'TEST'
    })
    def test_config_from_env(self):
        """Test loading config from environment variables"""
        config = Config()
        assert config.jira_url == 'https://test.atlassian.net'
        assert config.jira_email == 'test@example.com'
        assert config.jira_api_token == 'test-token'
        assert config.project_key == 'TEST'


class TestJiraClient:
    """Test JiraClient functionality"""
    
    @patch('src.jira_manager.core.JIRA')
    def test_client_initialization(self, mock_jira):
        """Test client initialization"""
        with patch.dict('os.environ', {
            'JIRA_URL': 'https://test.atlassian.net',
            'JIRA_EMAIL': 'test@example.com',
            'JIRA_API_TOKEN': 'test-token',
            'JIRA_PROJECT_KEY': 'TEST'
        }):
            client = JiraClient()
            assert client is not None
            mock_jira.assert_called_once()
    
    @patch('src.jira_manager.core.JIRA')
    def test_create_issue(self, mock_jira):
        """Test creating an issue"""
        with patch.dict('os.environ', {
            'JIRA_URL': 'https://test.atlassian.net',
            'JIRA_EMAIL': 'test@example.com',
            'JIRA_API_TOKEN': 'test-token',
            'JIRA_PROJECT_KEY': 'TEST'
        }):
            # Setup mock
            mock_issue = MagicMock()
            mock_issue.key = 'TEST-123'
            mock_jira_instance = mock_jira.return_value
            mock_jira_instance.create_issue.return_value = mock_issue
            
            # Test
            client = JiraClient()
            issue = client.create_issue(
                summary="Test Issue",
                description="Test Description"
            )
            
            assert issue.key == 'TEST-123'
            mock_jira_instance.create_issue.assert_called_once()
    
    @patch('src.jira_manager.core.JIRA')
    def test_get_issue(self, mock_jira):
        """Test getting an issue"""
        with patch.dict('os.environ', {
            'JIRA_URL': 'https://test.atlassian.net',
            'JIRA_EMAIL': 'test@example.com',
            'JIRA_API_TOKEN': 'test-token',
            'JIRA_PROJECT_KEY': 'TEST'
        }):
            # Setup mock
            mock_issue = MagicMock()
            mock_issue.key = 'TEST-123'
            mock_jira_instance = mock_jira.return_value
            mock_jira_instance.issue.return_value = mock_issue
            
            # Test
            client = JiraClient()
            issue = client.get_issue('TEST-123')
            
            assert issue.key == 'TEST-123'
            mock_jira_instance.issue.assert_called_once_with('TEST-123')
    
    @patch('src.jira_manager.core.JIRA')
    def test_add_comment(self, mock_jira):
        """Test adding a comment to an issue"""
        with patch.dict('os.environ', {
            'JIRA_URL': 'https://test.atlassian.net',
            'JIRA_EMAIL': 'test@example.com',
            'JIRA_API_TOKEN': 'test-token',
            'JIRA_PROJECT_KEY': 'TEST'
        }):
            # Setup mock
            mock_comment = MagicMock()
            mock_jira_instance = mock_jira.return_value
            mock_jira_instance.add_comment.return_value = mock_comment
            
            # Test
            client = JiraClient()
            result = client.add_comment('TEST-123', 'Test comment')
            
            assert result is not None
            mock_jira_instance.add_comment.assert_called_once_with('TEST-123', 'Test comment')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
