#!/usr/bin/env python3
"""
LLM Testing Framework
Interactive and batch testing for different LLM providers (Ollama, LMStudio, etc.)
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

from config import Config
from ollama_model import OllamaModel
from lmstudio_model import LMStudioModel
from ollama_interface import LLMInterface


class ModelFactory:
    """Factory class to create model instances based on configuration."""
    
    @staticmethod
    def create_model(model_config: dict) -> LLMInterface:
        """Create a model instance based on configuration."""
        provider = model_config['provider']
        url = model_config['url']
        model_name = model_config['model_name']
        
        if provider == 'ollama':
            return OllamaModel(url=url, model_name=model_name)
        elif provider == 'lmstudio':
            return LMStudioModel(url=url, model_name=model_name)
        else:
            raise ValueError(f"Unsupported provider: {provider}")


class LLMTester:
    """Main testing application."""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config = Config(config_path)
        self.config.validate_config()
    
    def interactive_mode(self, model_name: Optional[str] = None):
        """Run interactive CLI mode."""
        if model_name is None:
            model_name = self.config.get_default_model()
        
        try:
            model_config = self.config.get_model_config(model_name)
            model = ModelFactory.create_model(model_config)
            
            print(f"🤖 Using model: {model_name}")
            print(f"📍 Provider: {model_config['provider']}")
            print(f"🌐 URL: {model_config['url']}")
            print(f"📝 Model: {model_config['model_name']}")
            print("\n" + "="*50)
            print("Interactive mode - Type 'quit' or 'exit' to stop")
            print("="*50)
            
            # Check if model is available
            if not model.is_available():
                print(f"⚠️  Warning: Model '{model_name}' may not be available")
                print("Continuing anyway...\n")
            
            while True:
                try:
                    prompt = input("\n💬 Enter your prompt: ").strip()
                    
                    if prompt.lower() in ['quit', 'exit', 'q']:
                        print("👋 Goodbye!")
                        break
                    
                    if not prompt:
                        continue
                    
                    print(f"\n🤖 Response:")
                    print("-" * 30)
                    
                    # Generate streaming response
                    response_stream = model.generate(prompt, stream=True)
                    full_response = ""
                    
                    for chunk in response_stream:
                        print(chunk, end='', flush=True)
                        full_response += chunk
                    
                    print("\n" + "-" * 30)
                    
                except KeyboardInterrupt:
                    print("\n\n⏹️  Interrupted by user")
                    break
                except EOFError:
                    print("\n\n👋 Goodbye! (EOF detected)")
                    break
                except Exception as e:
                    print(f"\n❌ Error: {e}")
                    break
                    
        except Exception as e:
            print(f"❌ Failed to start interactive mode: {e}")
            sys.exit(1)
    
    def batch_mode(self, prompts_file: str, output_dir: Optional[str] = None):
        """Run batch testing mode."""
        prompts_path = Path(prompts_file)
        if not prompts_path.exists():
            print(f"❌ Prompts file not found: {prompts_file}")
            sys.exit(1)
        
        # Load prompts
        with open(prompts_path, 'r') as f:
            prompts = [line.strip() for line in f if line.strip()]
        
        if not prompts:
            print("❌ No prompts found in file")
            sys.exit(1)
        
        # Setup output directory
        if output_dir is None:
            output_dir = self.config.get_app_config().get('batch_output_dir', 'outputs')
        
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        print(f"📁 Output directory: {output_path}")
        print(f"📝 Found {len(prompts)} prompts")
        
        # Get available models
        available_models = self.config.get_available_models()
        print(f"🤖 Available models: {', '.join(available_models)}")
        
        # Test each model
        for model_name in available_models:
            print(f"\n🧪 Testing model: {model_name}")
            
            try:
                model_config = self.config.get_model_config(model_name)
                model = ModelFactory.create_model(model_config)
                
                if not model.is_available():
                    print(f"⚠️  Model '{model_name}' not available, skipping...")
                    continue
                
                # Create output file for this model
                output_file = output_path / f"{model_name}_responses.txt"
                
                with open(output_file, 'w') as f:
                    f.write(f"Model: {model_name}\n")
                    f.write(f"Provider: {model_config['provider']}\n")
                    f.write(f"URL: {model_config['url']}\n")
                    f.write("="*50 + "\n\n")
                    
                    for i, prompt in enumerate(prompts, 1):
                        print(f"  Processing prompt {i}/{len(prompts)}...")
                        
                        f.write(f"Prompt {i}: {prompt}\n")
                        f.write("-" * 30 + "\n")
                        
                        try:
                            response = model.generate(prompt, stream=False)
                            f.write(f"Response: {response}\n")
                        except Exception as e:
                            f.write(f"Error: {e}\n")
                        
                        f.write("\n" + "="*50 + "\n\n")
                
                print(f"✅ Results saved to: {output_file}")
                
            except Exception as e:
                print(f"❌ Error testing model '{model_name}': {e}")
        
        print(f"\n🎉 Batch testing completed! Check {output_path} for results.")
    
    def list_models(self):
        """List all available models."""
        models = self.config.get_available_models()
        default_model = self.config.get_default_model()
        
        print("🤖 Available Models:")
        print("=" * 50)
        
        for model_name in models:
            try:
                model_config = self.config.get_model_config(model_name)
                model = ModelFactory.create_model(model_config)
                status = "✅ Available" if model.is_available() else "❌ Unavailable"
                default_marker = " (default)" if model_name == default_model else ""
                
                print(f"{model_name}{default_marker}")
                print(f"  Provider: {model_config['provider']}")
                print(f"  URL: {model_config['url']}")
                print(f"  Model: {model_config['model_name']}")
                print(f"  Status: {status}")
                print()
                
            except Exception as e:
                print(f"{model_name}: ❌ Error - {e}")
                print()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="LLM Testing Framework")
    parser.add_argument("--config", help="Path to configuration file")
    parser.add_argument("--model", help="Model name to use (interactive mode)")
    
    subparsers = parser.add_subparsers(dest="mode", help="Available modes")
    
    # Interactive mode
    interactive_parser = subparsers.add_parser("interactive", help="Run interactive mode")
    interactive_parser.add_argument("--model", help="Model name to use")
    
    # Batch mode
    batch_parser = subparsers.add_parser("batch", help="Run batch testing mode")
    batch_parser.add_argument("prompts_file", help="File containing prompts to test")
    batch_parser.add_argument("--output-dir", help="Output directory for results")
    
    # List models
    list_parser = subparsers.add_parser("list", help="List available models")
    
    args = parser.parse_args()
    
    # Create tester instance
    try:
        tester = LLMTester(args.config)
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        sys.exit(1)
    
    # Execute based on mode
    if args.mode == "interactive" or args.mode is None:
        tester.interactive_mode(args.model)
    elif args.mode == "batch":
        tester.batch_mode(args.prompts_file, args.output_dir)
    elif args.mode == "list":
        tester.list_models()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
