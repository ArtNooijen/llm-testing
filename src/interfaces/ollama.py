"""Ollama inference interface implementation."""

import ollama
from typing import Optional, Dict, Any
from interfaces.base import BaseInferenceInterface
from config import Config


class OllamaInterface(BaseInferenceInterface):
    """Ollama inference interface implementation."""
    
    def __init__(self, config: Config, instance_name: str = "remote"):
        """
        Initialize Ollama interface.
        
        Args:
            config: Configuration object
            instance_name: Name of the Ollama instance to use
        """
        self.config = config
        self.instance_name = instance_name
        instance_config = config.get_ollama_instance_config(instance_name)
        self.host = instance_config['host']
        self.port = instance_config['port']
        self.timeout = instance_config['timeout']
        self.client = ollama.Client(host=config.get_ollama_instance_url(instance_name))
        self.model = config.ollama_model
    
    def generate(self, prompt: str) -> Dict[str, Any]:
        """
        Generate a response using Ollama.
        
        Args:
            prompt: The input prompt
            
        Returns:
            Dictionary containing response text and performance metrics
            
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
            
            # Extract performance metrics
            total_duration = response.get('total_duration', 0)
            load_duration = response.get('load_duration', 0)
            prompt_eval_count = response.get('prompt_eval_count', 0)
            prompt_eval_duration = response.get('prompt_eval_duration', 0)
            eval_count = response.get('eval_count', 0)
            eval_duration = response.get('eval_duration', 0)
            
            # Calculate tokens per second
            tokens_per_second = 0
            if eval_duration > 0:
                tokens_per_second = eval_count / (eval_duration / 1_000_000_000)
            
            # Calculate total time in seconds
            total_time_seconds = total_duration / 1_000_000_000 if total_duration > 0 else 0
            
            return {
                'response': response['response'],
                'metrics': {
                    'total_duration_ns': total_duration,
                    'total_duration_s': total_time_seconds,
                    'load_duration_ns': load_duration,
                    'load_duration_s': load_duration / 1_000_000_000 if load_duration > 0 else 0,
                    'prompt_eval_count': prompt_eval_count,
                    'prompt_eval_duration_ns': prompt_eval_duration,
                    'prompt_eval_duration_s': prompt_eval_duration / 1_000_000_000 if prompt_eval_duration > 0 else 0,
                    'eval_count': eval_count,
                    'eval_duration_ns': eval_duration,
                    'eval_duration_s': eval_duration / 1_000_000_000 if eval_duration > 0 else 0,
                    'tokens_per_second': tokens_per_second,
                    'model': response.get('model', self.model),
                    'created_at': response.get('created_at', ''),
                    'done': response.get('done', True)
                }
            }
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
