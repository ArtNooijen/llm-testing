#!/usr/bin/env python3
"""Test script to verify Ollama connection."""

import requests
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.config import Config

def test_connection():
    """Test connection to Ollama instances."""
    config = Config()
    models = config.ollama_models
    
    print(f"Testing {len(models)} model(s) across different instances...")
    print()
    
    for model_config in models:
        model_name = model_config['name']
        instance_name = model_config['instance']
        url = config.get_ollama_instance_url(instance_name)
        
        print(f"Testing {model_name} on {instance_name} ({url})")
        
        try:
            # Test basic connectivity
            response = requests.get(f"{url}/api/tags", timeout=10)
            if response.status_code == 200:
                print("✓ Ollama is reachable!")
                
                # Check if model is available
                models_list = response.json().get('models', [])
                model_names = [model.get('name', '') for model in models_list]
                
                print(f"Available models: {model_names}")
                
                if any(model_name in name for name in model_names):
                    print(f"✓ Model {model_name} is available!")
                else:
                    print(f"✗ Model {model_name} not found")
                    print("Available models:")
                    for model in model_names:
                        print(f"  - {model}")
            else:
                print(f"✗ Ollama returned status code: {response.status_code}")
                
        except requests.exceptions.ConnectTimeout:
            print("✗ Connection timeout - Ollama might not be running")
        except requests.exceptions.ConnectionError:
            print("✗ Connection failed - Check if Ollama is running and accessible")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
        
        print()

if __name__ == "__main__":
    test_connection()
