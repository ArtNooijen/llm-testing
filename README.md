# LLM Testing Interface

A Python interface for testing different LLM inference backends with a focus on Ollama. This project provides a swappable interface architecture that allows you to easily switch between different inference backends.

## Features

- 🚀 **Interactive CLI**: Beautiful command-line interface with rich formatting
- 🔄 **Swappable Backends**: Easy to add new inference backends
- 🌐 **Remote Connection**: Connect to Ollama running on remote machines via Tailscale
- ⚙️ **Configurable**: YAML-based configuration
- 📦 **UV Managed**: Modern Python dependency management

## Prerequisites

- Python 3.10+
- [UV](https://docs.astral.sh/uv/) package manager
- Ollama running on a remote machine (accessible via Tailscale)
- Tailscale network access to the remote machine

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

The project uses `config.yaml` for configuration. The default configuration connects to:

- **Host**: 100.70.84.114 (drutus via Tailscale)
- **Port**: 11434 (default Ollama port)
- **Model**: mistral:7b

### Customizing Configuration

Edit `config.yaml` to change settings:

```yaml
# Ollama Configuration
ollama:
  host: "100.70.84.114"  # Your remote machine IP
  port: 11434
  model: "mistral:7b"     # Model to use
  timeout: 30            # Request timeout in seconds

# CLI Configuration
cli:
  welcome_message: "Welcome to LLM Testing Interface!"
  prompt: "You: "
  exit_commands: ["/exit", "/quit", "/q"]
  clear_commands: ["/clear", "/cls"]
```

## Usage

### Running the Interface

```bash
uv run python src/main.py
```

### Commands

- **Type your message**: Just type and press Enter to send a message
- **`/exit`**, **`/quit`**, **`/q`**: Exit the application
- **`/clear`**, **`/cls`**: Clear the screen
- **Ctrl+C**: Force exit

### Example Session

```
┌─ LLM Testing Interface ─────────────────────────────────────────┐
│ Welcome to LLM Testing Interface!                              │
│                                                                │
│ Status: ✓ Connected to mistral:7b                            │
│                                                                │
│ Host: 100.70.84.114:11434                                     │
│ Model: mistral:7b                                             │
│                                                                │
│ Commands: /exit to quit, /clear to clear screen              │
└────────────────────────────────────────────────────────────────┘

You: Hello, how are you today?

Thinking...

Assistant:
┌────────────────────────────────────────────────────────────────┐
│ Hello! I'm doing well, thank you for asking. I'm here and     │
│ ready to help you with any questions or tasks you might have. │
│ How can I assist you today?                                   │
└────────────────────────────────────────────────────────────────┘
```

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

1. **Check Tailscale connection**:
   ```bash
   ping 100.70.84.114
   ```

2. **Verify Ollama is running** on the remote machine:
   ```bash
   curl http://100.70.84.114:11434/api/tags
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
│   ├── main.py            # Interactive CLI entry point
│   ├── config.py          # Configuration management
│   └── interfaces/
│       ├── __init__.py
│       ├── base.py        # Abstract base interface
│       └── ollama.py      # Ollama implementation
└── README.md              # This file
```

### Dependencies

- `ollama`: Ollama Python client
- `pyyaml`: YAML configuration parsing
- `rich`: Beautiful terminal output

## License

This project is open source and available under the MIT License.
