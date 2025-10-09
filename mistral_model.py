import requests
from ollama_interface import OllamaModel

class MistralModel(OllamaModel):
    def __init__(self, url: str = "http://100.70.84.114:11434", model_name: str = "mistral:7b"):
        self.url = url
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        try:
            response = requests.post(
                f"{self.url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "temperature": 0.7,
                    "max_tokens": 200
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            return data.get("completion", "No completion returned.")
        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"
