#!/usr/bin/env python3
"""
Simple connection test script for debugging Ollama connectivity.
"""

import requests
import sys
from config import Config

def test_connection(url, model_name):
    """Test connection to an Ollama instance."""
    print(f"Testing connection to: {url}")
    print(f"Model: {model_name}")
    print("-" * 50)
    
    try:
        # Test basic connectivity
        print("1. Testing basic connectivity...")
        response = requests.get(f"{url}/api/tags", timeout=5)
        response.raise_for_status()
        print("✅ Basic connectivity: OK")
        
        # Check available models
        data = response.json()
        available_models = [model['name'] for model in data.get('models', [])]
        print(f"📋 Available models: {available_models}")
        
        if model_name in available_models:
            print(f"✅ Model '{model_name}' is available")
        else:
            print(f"❌ Model '{model_name}' not found")
            return False
        
        # Test a simple generation
        print("\n2. Testing model generation...")
        test_prompt = "Say hello in one word."
        payload = {
            "model": model_name,
            "prompt": test_prompt,
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_predict": 10
            }
        }
        
        response = requests.post(f"{url}/api/generate", json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        print(f"✅ Generation test: {data.get('response', 'No response')}")
        return True
        
    except requests.exceptions.ConnectTimeout:
        print("❌ Connection timeout - server not responding")
        return False
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Connection error: {e}")
        return False
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    """Main function."""
    if len(sys.argv) > 1:
        # Test specific URL
        url = sys.argv[1]
        model_name = sys.argv[2] if len(sys.argv) > 2 else "mistral:7b"
        test_connection(url, model_name)
    else:
        # Test all configured models
        config = Config()
        models = config.get_available_models()
        
        print("🔍 Testing all configured models...\n")
        
        for model_name in models:
            try:
                model_config = config.get_model_config(model_name)
                url = model_config['url']
                actual_model = model_config['model_name']
                
                print(f"\n🤖 Testing: {model_name}")
                success = test_connection(url, actual_model)
                
                if success:
                    print(f"✅ {model_name}: Working perfectly!")
                else:
                    print(f"❌ {model_name}: Failed")
                    
            except Exception as e:
                print(f"❌ {model_name}: Configuration error - {e}")
            
            print("\n" + "="*60)

if __name__ == "__main__":
    main()
