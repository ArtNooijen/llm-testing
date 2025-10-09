# LLM Testing Framework

A flexible testing framework for comparing different Large Language Model (LLM) providers including Ollama, LMStudio, and more.

## Features

- **Multi-Provider Support**: Test models from different providers (Ollama, LMStudio, etc.)
- **Streaming Responses**: Real-time streaming output for better user experience
- **Interactive Mode**: Chat-like interface for testing prompts
- **Batch Testing**: Run multiple prompts against different models
- **Configuration Management**: YAML-based configuration for easy model management
- **Network Support**: Works with remote models via Tailscale or other networks

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd llm-testing
```

2. Install dependencies:
```bash
pip install -e .
```

Or using uv (recommended):
```bash
uv sync
```

## Configuration

The framework uses `config.yaml` to define available models. Here's an example:

```yaml
models:
  mistral-local:
    provider: ollama
    url: "http://localhost:11434"
    model_name: "mistral:7b"
    default_params:
      temperature: 0.7
      max_tokens: 200
  
  mistral-remote:
    provider: ollama
    url: "http://100.70.84.114:11434"  # Your Tailscale IP
    model_name: "mistral:7b"
    default_params:
      temperature: 0.7
      max_tokens: 200

default_model: "mistral-remote"
```

## Usage

### Interactive Mode

Start an interactive chat session:

```bash
python main.py interactive
```

Or specify a model:

```bash
python main.py interactive --model mistral-local
```

### Batch Testing

Test multiple prompts against all configured models:

```bash
python main.py batch prompts.txt
```

Create a `prompts.txt` file with one prompt per line:

```
What is the meaning of life?
Explain quantum computing in simple terms.
Write a haiku about programming.
```

### List Available Models

Check which models are configured and their availability:

```bash
python main.py list
```

## Supported Providers

### Ollama

Ollama is fully supported with streaming responses. Configure with:

```yaml
my-ollama-model:
  provider: ollama
  url: "http://localhost:11434"  # or your remote IP
  model_name: "mistral:7b"
```

### LMStudio

LMStudio support is planned. The framework includes a placeholder implementation that can be extended to support LMStudio's OpenAI-compatible API.

## Network Setup

### Using Tailscale

If you have Ollama running on a remote machine connected via Tailscale:

1. Find your Tailscale IP on the remote machine:
```bash
tailscale ip
```

2. Update your `config.yaml` with the Tailscale IP:
```yaml
mistral-remote:
  provider: ollama
  url: "http://YOUR_TAILSCALE_IP:11434"
  model_name: "mistral:7b"
```

3. Ensure Ollama is configured to accept connections from your Tailscale network.

## Development

### Project Structure

```
llm-testing/
├── main.py              # Main application entry point
├── config.py            # Configuration management
├── config.yaml          # Model configurations
├── ollama_interface.py  # Abstract base class
├── ollama_model.py      # Ollama implementation
├── lmstudio_model.py    # LMStudio placeholder
├── pyproject.toml       # Project dependencies
└── README.md           # This file
```

### Adding New Providers

1. Create a new model class inheriting from `LLMInterface`
2. Implement the required methods: `generate()`, `get_model_info()`, `is_available()`
3. Add the provider to the `ModelFactory.create_model()` method
4. Update the configuration schema documentation

### Example Provider Implementation

```python
from ollama_interface import LLMInterface
from typing import Iterator, Union

class MyProviderModel(LLMInterface):
    def __init__(self, url: str, model_name: str):
        self.url = url
        self.model_name = model_name
    
    def generate(self, prompt: str, stream: bool = True) -> Union[Iterator[str], str]:
        # Implement your provider's API calls here
        pass
    
    def get_model_info(self) -> dict:
        return {
            "provider": "myprovider",
            "model_name": self.model_name,
            "url": self.url
        }
    
    def is_available(self) -> bool:
        # Check if the model is available
        return True
```

## Troubleshooting

### Connection Issues

- **Ollama not responding**: Check if Ollama is running and accessible
- **Network timeout**: Verify the URL and network connectivity
- **Model not found**: Ensure the model is installed in Ollama (`ollama list`)

### Configuration Issues

- **Invalid YAML**: Check your `config.yaml` syntax
- **Missing models**: Verify all required fields are present in model configurations
- **Provider not supported**: Check that the provider is implemented in `ModelFactory`

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Roadmap

- [ ] Complete LMStudio implementation
- [ ] Add OpenAI API support
- [ ] Implement response comparison tools
- [ ] Add performance benchmarking
- [ ] Web interface for easier testing
- [ ] Docker support for easy deployment
