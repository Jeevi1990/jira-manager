"""Configuration management for Jira Manager"""

import os
import configparser
from typing import Optional, Dict, Any
from pathlib import Path
from dotenv import load_dotenv
from .exceptions import ConfigurationError


class Config:
    """Manages configuration from multiple sources"""
    
    def __init__(self, config_file: Optional[str] = None):
        self.config_file = config_file or "config.ini"
        self._config = {}
        self._load_configuration()
    
    def _load_configuration(self):
        """Load configuration from .env, config.ini, and environment variables"""
        # Load .env file if it exists
        env_file = Path(".env")
        if env_file.exists():
            load_dotenv(env_file)
        
        # Load from config.ini
        if Path(self.config_file).exists():
            parser = configparser.ConfigParser()
            parser.read(self.config_file)
            if 'jira' in parser:
                self._config.update(dict(parser['jira']))
        
        # Override with environment variables (highest priority)
        env_vars = {
            'JIRA_URL': 'url',
            'JIRA_EMAIL': 'email',
            'JIRA_API_TOKEN': 'api_token',
            'JIRA_PROJECT_KEY': 'project_key',
            'PROJECT_ISSUE_TYPE': 'issue_type',
            'JIRA_LOG_LEVEL': 'log_level',
        }
        
        for env_var, config_key in env_vars.items():
            value = os.getenv(env_var)
            if value:
                self._config[config_key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        # Try direct key first
        if key in self._config:
            return self._config[key]
        
        # Try uppercase version
        upper_key = key.upper()
        if upper_key in self._config:
            return self._config[upper_key]
        
        # Try from config.ini naming
        ini_mappings = {
            'url': 'JIRA_URL',
            'email': 'JIRA_EMAIL',
            'api_token': 'JIRA_API_TOKEN',
            'project_key': 'JIRA_PROJECT_KEY',
            'issue_type': 'PROJECT_ISSUE_TYPE',
        }
        
        if key in ini_mappings and ini_mappings[key] in self._config:
            return self._config[ini_mappings[key]]
        
        return default
    
    def get_required(self, key: str) -> str:
        """Get required configuration value or raise error"""
        value = self.get(key)
        if value is None:
            raise ConfigurationError(
                f"Required configuration '{key}' is not set. "
                f"Please set it in {self.config_file} or as an environment variable."
            )
        return value
    
    @property
    def jira_url(self) -> str:
        """Get Jira URL"""
        return self.get_required('url')
    
    @property
    def jira_email(self) -> str:
        """Get Jira email"""
        return self.get_required('email')
    
    @property
    def jira_api_token(self) -> str:
        """Get Jira API token"""
        return self.get_required('api_token')
    
    @property
    def project_key(self) -> str:
        """Get default project key"""
        return self.get('project_key', 'PROJ')
    
    @property
    def issue_type(self) -> str:
        """Get default issue type"""
        return self.get('issue_type', 'Task')
    
    def to_dict(self) -> Dict[str, Any]:
        """Return configuration as dictionary"""
        return self._config.copy()
