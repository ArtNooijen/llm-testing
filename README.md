# LLM Testing Interface

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-green.svg)](https://docs.astral.sh/uv/)
[![Ollama](https://img.shields.io/badge/Ollama-Compatible-orange.svg)](https://ollama.ai)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Rich](https://img.shields.io/badge/Rich-Terminal%20UI-red.svg)](https://rich.readthedocs.io)

A Python interface for testing and comparing different LLM models across multiple Ollama instances. 

## Prerequisites

- Python 3.10+
- [UV](https://docs.astral.sh/uv/) package manager
- Ollama running on one or more machines:
  - Remote machine (accessible via Tailscale) - optional
  - Local machine (localhost) - optional
- Tailscale network access (if using remote Ollama)

## Installation

1. **Install UV** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and setup the project**:
   ```bash
   cd llm-testing
   uv sync
   ```

## Configuration

The project uses `config.yaml` for configuration. You can configure multiple Ollama instances and specify which models run on which instance.

### Default Configuration

```yaml
# Ollama Instances
ollama_instances:
  remote:
    host: "your-remote-server.com"  # Your remote machine
    port: 11434
    timeout: 30
  local:
    host: "localhost"  # Local machine
    port: 11434
    timeout: 30

# Models to test (specify which instance each model runs on)
models:
  - name: "mistral:7b"
    instance: "remote"
  - name: "llama3.1:8b"
    instance: "local"
  - name: "codellama:7b"
    instance: "remote"

# CLI Configuration
cli:
  welcome_message: "Welcome to LLM Testing Interface!"
  prompt: "Enter your prompt: "
  comparison_mode: true  # Run all models and compare responses
```

### Customizing Configuration

**Add more models:**
```yaml
models:
  - name: "mistral:7b"
    instance: "remote"
  - name: "llama3.1:8b"
    instance: "local"
  - name: "phi:2.7b"
    instance: "local"
  - name: "codellama:7b"
    instance: "remote"
```

**Add more Ollama instances:**
```yaml
ollama_instances:
  remote:
    host: "your-remote-server.com"
    port: 11434
    timeout: 30
  local:
    host: "localhost"
    port: 11434
    timeout: 30
  cloud:
    host: "your-cloud-instance.com"
    port: 11434
    timeout: 60
```

## Usage

### Running the Interface

```bash
uv run python src/main.py
```

### Comparison Mode (Default)

The application runs in comparison mode by default. You enter a single prompt and it tests all configured models:

```
┌─ LLM Testing Interface ─────────────────────────────────────────┐
│ Welcome to LLM Testing Interface!                              │
│                                                                │
│ Status: ✓ Connected                                            │
│                                                                │
│ Host: your-remote-server.com:11434, localhost:11434           │
│ Models: mistral:7b, llama3.1:8b, codellama:7b                 │
└────────────────────────────────────────────────────────────────┘

Enter your prompt: Explain quantum computing in simple terms

Testing 3 models with the same prompt...
Prompt: Explain quantum computing in simple terms

Testing Model 1/3: mistral:7b (on remote)
Thinking...

Testing Model 2/3: llama3.1:8b (on local)
Thinking...

Testing Model 3/3: codellama:7b (on remote)
Thinking...

=== COMPARISON RESULTS ===

┌─ Model 1: mistral:7b (remote) ──────────────────────────────────┐
│ Quantum computing is like having a computer that can be in     │
│ multiple states at once, unlike regular computers that are     │
│ either on or off...                                            │
└────────────────────────────────────────────────────────────────┘

┌─ Model 2: llama3.1:8b (local) ───────────────────────────────┐
│ Think of quantum computing like having a coin that can be       │
│ both heads and tails at the same time until you look at it...   │
└────────────────────────────────────────────────────────────────┘

┌─ Model 3: codellama:7b (remote) ──────────────────────────────┐
│ Quantum computing uses quantum bits (qubits) that can exist     │
│ in superposition, allowing for parallel processing...         │
└────────────────────────────────────────────────────────────────┘
```

### Interactive Mode

To switch to interactive mode (chat with one model), set in `config.yaml`:

```yaml
cli:
  comparison_mode: false
```

### Commands (Interactive Mode)

- **Type your message**: Just type and press Enter to send a message
- **`/exit`**, **`/quit`**, **`/q`**: Exit the application
- **`/clear`**, **`/cls`**: Clear the screen
- **Ctrl+C**: Force exit

## Architecture

### Interface System

The project uses an abstract base class pattern for easy backend swapping:

```
src/
├── interfaces/
│   ├── base.py          # Abstract base interface
│   └── ollama.py        # Ollama implementation
├── config.py            # Configuration management
└── main.py             # Interactive CLI
```

### Adding New Backends

To add a new inference backend:

1. **Create a new interface class** in `src/interfaces/`:

```python
from .base import BaseInferenceInterface

class MyBackendInterface(BaseInferenceInterface):
    def generate(self, prompt: str) -> str:
        # Implementation here
        pass
    
    def is_available(self) -> bool:
        # Check availability
        pass
    
    def get_model_info(self) -> Optional[dict]:
        # Return model info
        pass
```

2. **Update the main application** to use your new backend
3. **Add configuration** for your backend in `config.yaml`

## Troubleshooting

### Connection Issues

1. **Check network connection**:
   ```bash
   ping your-remote-server.com
   ```

2. **Verify Ollama is running** on the remote machine:
   ```bash
   curl http://your-remote-server.com:11434/api/tags
   ```

3. **Check firewall settings** on the remote machine

### Common Issues

- **"Cannot connect to Ollama"**: Verify the remote machine is accessible and Ollama is running
- **"Model not found"**: Ensure the model is pulled on the remote Ollama instance
- **Timeout errors**: Increase the timeout value in `config.yaml`

## Development

### Project Structure

```
llm-testing/
├── pyproject.toml          # UV project configuration
├── config.yaml            # Runtime configuration
├── .gitignore             # Git ignore rules
├── src/
│   ├── __init__.py
│   ├── main.py            # Main application (comparison & interactive modes)
│   ├── config.py          # Configuration management
│   └── interfaces/
│       ├── __init__.py
│       ├── base.py        # Abstract base interface
│       └── ollama.py      # Ollama implementation
├── tests/
│   ├── __init__.py
│   └── test_connection.py # Connection testing utilities
└── README.md              # This file
```

### Dependencies

- `ollama`: Ollama Python client
- `pyyaml`: YAML configuration parsing
- `rich`: Beautiful terminal output
- `requests`: HTTP client for connection testing



## License

This project is open source and available under the MIT License.
