import yaml
import os
from typing import Dict, Any, Optional
from pathlib import Path


class Config:
    """Configuration manager for LLM testing setup."""
    
    def __init__(self, config_path: Optional[str] = None):
        if config_path is None:
            config_path = Path(__file__).parent / "config.yaml"
        
        self.config_path = Path(config_path)
        self._config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        try:
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML configuration: {e}")
    
    def get_model_config(self, model_name: str) -> Dict[str, Any]:
        """Get configuration for a specific model."""
        models = self._config.get('models', {})
        if model_name not in models:
            raise ValueError(f"Model '{model_name}' not found in configuration")
        return models[model_name]
    
    def get_available_models(self) -> list:
        """Get list of available model names."""
        return list(self._config.get('models', {}).keys())
    
    def get_default_model(self) -> str:
        """Get the default model name."""
        return self._config.get('default_model', 'mistral-local')
    
    def get_app_config(self) -> Dict[str, Any]:
        """Get application configuration."""
        return self._config.get('app', {})
    
    def validate_config(self) -> bool:
        """Validate the configuration structure."""
        required_keys = ['models']
        for key in required_keys:
            if key not in self._config:
                raise ValueError(f"Missing required configuration key: {key}")
        
        # Validate each model configuration
        for model_name, model_config in self._config['models'].items():
            required_model_keys = ['provider', 'url', 'model_name']
            for key in required_model_keys:
                if key not in model_config:
                    raise ValueError(f"Model '{model_name}' missing required key: {key}")
            
            # Validate provider
            if model_config['provider'] not in ['ollama', 'lmstudio']:
                raise ValueError(f"Model '{model_name}' has invalid provider: {model_config['provider']}")
        
        return True
    
    def reload(self):
        """Reload configuration from file."""
        self._config = self._load_config()
