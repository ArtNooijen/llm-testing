"""Configuration management for the LLM testing interface."""

import yaml
from pathlib import Path
from typing import Dict, Any, Optional


class Config:
    """Configuration manager for the application."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize configuration.
        
        Args:
            config_path: Path to config file. If None, uses default config.yaml
        """
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config.yaml"
        
        self.config_path = Path(config_path)
        self._config: Dict[str, Any] = {}
        self.load()
    
    def load(self) -> None:
        """Load configuration from YAML file."""
        try:
            with open(self.config_path, 'r') as f:
                self._config = yaml.safe_load(f) or {}
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in configuration file: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value by key.
        
        Args:
            key: Configuration key (supports dot notation like 'ollama.host')
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        keys = key.split('.')
        value = self._config
        
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
    
    def get_ollama_config(self) -> Dict[str, Any]:
        """Get Ollama-specific configuration."""
        return self.get('ollama', {})
    
    def get_cli_config(self) -> Dict[str, Any]:
        """Get CLI-specific configuration."""
        return self.get('cli', {})
    
    @property
    def ollama_host(self) -> str:
        """Get Ollama host."""
        return self.get('ollama.host', 'localhost')
    
    @property
    def ollama_port(self) -> int:
        """Get Ollama port."""
        return self.get('ollama.port', 11434)
    
    @property
    def ollama_models(self) -> list:
        """Get list of models to test with their instances."""
        models = self.get('models', [])
        if not models:
            return [{'name': 'mistral:7b', 'instance': 'remote'}]
        return models
    
    @property
    def ollama_model(self) -> str:
        """Get first Ollama model (for backward compatibility)."""
        models = self.ollama_models
        return models[0]['name'] if models else 'mistral:7b'
    
    @property
    def ollama_timeout(self) -> int:
        """Get Ollama timeout."""
        return self.get('ollama.timeout', 30)
    
    @property
    def ollama_url(self) -> str:
        """Get full Ollama URL."""
        return f"http://{self.ollama_host}:{self.ollama_port}"
    
    def get_ollama_instance_config(self, instance_name: str) -> Dict[str, Any]:
        """Get configuration for a specific Ollama instance."""
        instances = self.get('ollama_instances', {})
        return instances.get(instance_name, {
            'host': 'localhost',
            'port': 11434,
            'timeout': 30
        })
    
    def get_ollama_instance_url(self, instance_name: str) -> str:
        """Get URL for a specific Ollama instance."""
        config = self.get_ollama_instance_config(instance_name)
        return f"http://{config['host']}:{config['port']}"
    
    @property
    def repetition_count(self) -> int:
        """Get number of repetitions for consistency testing."""
        return self.get('cli.repetition_count', 10)