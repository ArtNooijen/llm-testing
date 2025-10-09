import requests
import json
from typing import Iterator, Union
from ollama_interface import LLMInterface


class OllamaModel(LLMInterface):
    """Ollama model implementation with proper streaming support."""
    
    def __init__(self, url: str = "http://localhost:11434", model_name: str = "mistral:7b"):
        self.url = url.rstrip('/')
        self.model_name = model_name
        self._base_url = f"{self.url}/api"
    
    def generate(self, prompt: str, stream: bool = True) -> Union[Iterator[str], str]:
        """
        Generate a response from the Ollama model.
        
        Args:
            prompt: The input prompt
            stream: Whether to return streaming response or complete response
            
        Returns:
            Iterator[str] if stream=True, str if stream=False
        """
        try:
            payload = {
                "model": self.model_name,
                "prompt": prompt,
                "stream": stream,
                "options": {
                    "temperature": 0.7,
                    "num_predict": 200
                }
            }
            
            response = requests.post(
                f"{self._base_url}/generate",
                json=payload,
                stream=stream,
                timeout=30
            )
            response.raise_for_status()
            
            if stream:
                return self._stream_response(response)
            else:
                data = response.json()
                return data.get("response", "No response returned.")
                
        except requests.exceptions.RequestException as e:
            if stream:
                def error_generator():
                    yield f"Request failed: {e}"
                return error_generator()
            else:
                return f"Request failed: {e}"
    
    def _stream_response(self, response: requests.Response) -> Iterator[str]:
        """Handle streaming response from Ollama API."""
        try:
            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode('utf-8'))
                        if 'response' in data:
                            yield data['response']
                        if data.get('done', False):
                            break
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            yield f"Streaming error: {e}"
    
    def get_model_info(self) -> dict:
        """Get information about the current model."""
        try:
            response = requests.get(f"{self._base_url}/show", 
                                  params={"name": self.model_name},
                                  timeout=10)
            response.raise_for_status()
            data = response.json()
            return {
                "provider": "ollama",
                "model_name": self.model_name,
                "url": self.url,
                "details": data
            }
        except requests.exceptions.RequestException:
            return {
                "provider": "ollama",
                "model_name": self.model_name,
                "url": self.url,
                "status": "unavailable"
            }
    
    def is_available(self) -> bool:
        """Check if the Ollama server and model are available."""
        try:
            response = requests.get(f"{self._base_url}/tags", timeout=5)
            response.raise_for_status()
            data = response.json()
            available_models = [model['name'] for model in data.get('models', [])]
            return self.model_name in available_models
        except requests.exceptions.RequestException:
            return False
