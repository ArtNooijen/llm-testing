#!/usr/bin/env python3
"""Test script to verify Ollama connection."""

import requests
import json
from config import Config

def test_connection():
    """Test connection to Ollama instance."""
    config = Config()
    url = config.ollama_url
    
    print(f"Testing connection to: {url}")
    print(f"Model: {config.ollama_model}")
    print()
    
    try:
        # Test basic connectivity
        response = requests.get(f"{url}/api/tags", timeout=10)
        if response.status_code == 200:
            print("✓ Ollama is reachable!")
            
            # Check if model is available
            models = response.json().get('models', [])
            model_names = [model.get('name', '') for model in models]
            
            print(f"Available models: {model_names}")
            
            if any(config.ollama_model in name for name in model_names):
                print(f"✓ Model {config.ollama_model} is available!")
                return True
            else:
                print(f"✗ Model {config.ollama_model} not found")
                print("Available models:")
                for model in model_names:
                    print(f"  - {model}")
                return False
        else:
            print(f"✗ Ollama returned status code: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectTimeout:
        print("✗ Connection timeout - Ollama might not be running")
        return False
    except requests.exceptions.ConnectionError:
        print("✗ Connection failed - Check if Ollama is running and accessible")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    test_connection()
