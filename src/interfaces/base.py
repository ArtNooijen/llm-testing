"""Abstract base interface for inference backends."""

from abc import ABC, abstractmethod
from typing import Optional


class BaseInferenceInterface(ABC):
    """Abstract base class for inference backends."""
    
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response for the given prompt.
        
        Args:
            prompt: The input prompt to generate a response for
            
        Returns:
            The generated response text
            
        Raises:
            ConnectionError: If unable to connect to the inference backend
            RuntimeError: If generation fails
        """
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """
        Check if the inference backend is available and reachable.
        
        Returns:
            True if the backend is available, False otherwise
        """
        pass
    
    @abstractmethod
    def get_model_info(self) -> Optional[dict]:
        """
        Get information about the current model.
        
        Returns:
            Dictionary with model information or None if unavailable
        """
        pass
