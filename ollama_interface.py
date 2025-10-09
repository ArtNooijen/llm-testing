from abc import ABC, abstractmethod
from typing import Iterator, Union


class LLMInterface(ABC):
    """Abstract base class for all LLM model implementations."""
    
    @abstractmethod
    def generate(self, prompt: str, stream: bool = True) -> Union[Iterator[str], str]:
        """
        Generate a response from the model.
        
        Args:
            prompt: The input prompt
            stream: Whether to return streaming response (Iterator) or complete response (str)
            
        Returns:
            Iterator[str] if stream=True, str if stream=False
        """
        pass
    
    @abstractmethod
    def get_model_info(self) -> dict:
        """
        Get information about the current model.
        
        Returns:
            Dictionary containing model information (name, provider, etc.)
        """
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """
        Check if the model is available and accessible.
        
        Returns:
            True if model is available, False otherwise
        """
        pass
