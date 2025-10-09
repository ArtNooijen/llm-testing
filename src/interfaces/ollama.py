"""Ollama inference interface implementation."""

import ollama
from typing import Optional, Dict, Any
from interfaces.base import BaseInferenceInterface
from config import Config


class OllamaInterface(BaseInferenceInterface):
    """Ollama inference interface implementation."""
    
    def __init__(self, config: Config):
        """
        Initialize Ollama interface.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.client = ollama.Client(host=config.ollama_url)
        self.model = config.ollama_model
    
    def generate(self, prompt: str) -> str:
        """
        Generate a response using Ollama.
        
        Args:
            prompt: The input prompt
            
        Returns:
            Generated response text
            
        Raises:
            ConnectionError: If unable to connect to Ollama
            RuntimeError: If generation fails
        """
        try:
            response = self.client.generate(
                model=self.model,
                prompt=prompt,
                stream=False
            )
            return response['response']
        except ollama.ResponseError as e:
            raise RuntimeError(f"Ollama generation failed: {e}")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Ollama: {e}")
    
    def is_available(self) -> bool:
        """
        Check if Ollama is available and reachable.
        
        Returns:
            True if Ollama is available, False otherwise
        """
        try:
            # Try to list models to check if Ollama is reachable
            self.client.list()
            return True
        except Exception:
            return False
    
    def get_model_info(self) -> Optional[Dict[str, Any]]:
        """
        Get information about the current model.
        
        Returns:
            Model information dictionary or None if unavailable
        """
        try:
            models = self.client.list()
            for model in models.get('models', []):
                if model.get('name', '').startswith(self.model):
                    return {
                        'name': model.get('name'),
                        'size': model.get('size'),
                        'modified_at': model.get('modified_at'),
                        'family': model.get('details', {}).get('family'),
                        'parameter_size': model.get('details', {}).get('parameter_size'),
                        'quantization_level': model.get('details', {}).get('quantization_level')
                    }
            return None
        except Exception:
            return None
    
    def generate_streaming(self, prompt: str):
        """
        Generate a streaming response using Ollama.
        
        Args:
            prompt: The input prompt
            
        Yields:
            Response chunks as they are generated
            
        Raises:
            ConnectionError: If unable to connect to Ollama
            RuntimeError: If generation fails
        """
        try:
            response = self.client.generate(
                model=self.model,
                prompt=prompt,
                stream=True
            )
            for chunk in response:
                if 'response' in chunk:
                    yield chunk['response']
        except ollama.ResponseError as e:
            raise RuntimeError(f"Ollama streaming generation failed: {e}")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Ollama for streaming: {e}")
