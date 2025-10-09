#!/usr/bin/env python3
"""Interactive CLI for LLM testing interface."""

import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.live import Live
from rich.spinner import Spinner
from rich import markdown
import time

from config import Config
from interfaces.ollama import OllamaInterface


class LLMChat:
    """Interactive chat interface for LLM testing."""
    
    def __init__(self):
        """Initialize the chat interface."""
        self.console = Console()
        self.config = Config()
        self.interface = OllamaInterface(self.config)
        self.cli_config = self.config.get_cli_config()
        
    def show_welcome(self):
        """Display welcome message and connection status."""
        welcome_msg = self.cli_config.get('welcome_message', 'Welcome to LLM Testing Interface!')
        
        # Check connection status
        if self.interface.is_available():
            status = "[green]✓ Connected[/green]"
            model_info = self.interface.get_model_info()
            if model_info:
                model_name = model_info.get('name', 'Unknown')
                status += f" to [bold]{model_name}[/bold]"
        else:
            status = "[red]✗ Not connected[/red]"
        
        panel = Panel(
            f"{welcome_msg}\n\nStatus: {status}\n\n"
            f"Host: {self.config.ollama_host}:{self.config.ollama_port}\n"
            f"Model: {self.config.ollama_model}\n\n"
            f"Commands: /exit to quit, /clear to clear screen",
            title="[bold blue]LLM Testing Interface[/bold blue]",
            border_style="blue"
        )
        
        self.console.print(panel)
        self.console.print()
    
    def clear_screen(self):
        """Clear the console screen."""
        self.console.clear()
        self.show_welcome()
    
    def show_typing_indicator(self):
        """Show typing indicator while generating response."""
        with Live(Spinner("dots", text="Thinking..."), console=self.console, refresh_per_second=10) as live:
            return live
    
    def format_response(self, response: str) -> str:
        """Format the model response for display."""
        # Try to format as markdown if it looks like markdown
        if any(marker in response for marker in ['#', '**', '*', '`', '```']):
            try:
                return markdown.Markdown(response)
            except:
                pass
        return response
    
    def run_comparison(self):
        """Run model comparison mode."""
        self.show_welcome()
        
        if not self.interface.is_available():
            self.console.print("[red]Error: Cannot connect to Ollama. Please check your connection.[/red]")
            self.console.print(f"Trying to connect to: {self.config.ollama_url}")
            return
        
        # Get prompt from user
        prompt_text = self.cli_config.get('prompt', 'Enter your prompt: ')
        user_prompt = Prompt.ask(prompt_text, console=self.console)
        
        if not user_prompt.strip():
            self.console.print("[yellow]No prompt provided. Exiting.[/yellow]")
            return
        
        # Get models to test
        models = self.config.ollama_models
        self.console.print(f"\n[bold]Testing {len(models)} models with the same prompt...[/bold]")
        self.console.print(f"Prompt: [italic]{user_prompt}[/italic]\n")
        
        results = []
        
        # Test each model
        for i, model_config in enumerate(models, 1):
            model_name = model_config['name']
            instance_name = model_config['instance']
            self.console.print(f"[bold blue]Testing Model {i}/{len(models)}: {model_name} (on {instance_name})[/bold blue]")
            
            # Create interface for this model and instance
            model_interface = OllamaInterface(self.config, instance_name)
            model_interface.model = model_name
            
            # Show typing indicator
            with self.show_typing_indicator():
                try:
                    response = model_interface.generate(user_prompt)
                    results.append({
                        'model': model_name,
                        'instance': instance_name,
                        'response': response,
                        'success': True
                    })
                except Exception as e:
                    results.append({
                        'model': model_name,
                        'instance': instance_name,
                        'response': f"Error: {e}",
                        'success': False
                    })
            
            self.console.print()
        
        # Display comparison results
        self.show_comparison_results(results)
    
    def show_comparison_results(self, results):
        """Display comparison results for all models."""
        self.console.print("[bold green]=== COMPARISON RESULTS ===[/bold green]\n")
        
        for i, result in enumerate(results, 1):
            model_name = result['model']
            instance_name = result['instance']
            response = result['response']
            success = result['success']
            
            # Create panel for each model result
            if success:
                panel = Panel(
                    response,
                    title=f"[bold blue]Model {i}: {model_name} ({instance_name})[/bold blue]",
                    border_style="green" if success else "red"
                )
            else:
                panel = Panel(
                    response,
                    title=f"[bold red]Model {i}: {model_name} ({instance_name}) - ERROR[/bold red]",
                    border_style="red"
                )
            
            self.console.print(panel)
            self.console.print()
    
    def run(self):
        """Run the application in comparison mode."""
        comparison_mode = self.cli_config.get('comparison_mode', False)
        
        if comparison_mode:
            self.run_comparison()
        else:
            # Original interactive mode (kept for backward compatibility)
            self.run_interactive()
    
    def run_interactive(self):
        """Run the interactive chat loop (original mode)."""
        self.show_welcome()
        
        if not self.interface.is_available():
            self.console.print("[red]Error: Cannot connect to Ollama. Please check your connection.[/red]")
            self.console.print(f"Trying to connect to: {self.config.ollama_url}")
            return
        
        exit_commands = self.cli_config.get('exit_commands', ['/exit', '/quit', '/q'])
        clear_commands = self.cli_config.get('clear_commands', ['/clear', '/cls'])
        prompt_text = self.cli_config.get('prompt', 'You: ')
        
        while True:
            try:
                user_input = Prompt.ask(prompt_text, console=self.console)
                
                # Handle commands
                if user_input.lower() in exit_commands:
                    self.console.print("[yellow]Goodbye![/yellow]")
                    break
                elif user_input.lower() in clear_commands:
                    self.clear_screen()
                    continue
                elif not user_input.strip():
                    continue
                
                # Generate response
                self.console.print()
                
                # Show typing indicator
                with self.show_typing_indicator():
                    try:
                        response = self.interface.generate(user_input)
                    except Exception as e:
                        self.console.print(f"[red]Error: {e}[/red]")
                        continue
                
                # Display response
                self.console.print()
                self.console.print("[bold blue]Assistant:[/bold blue]")
                
                formatted_response = self.format_response(response)
                if isinstance(formatted_response, markdown.Markdown):
                    self.console.print(formatted_response)
                else:
                    self.console.print(Panel(formatted_response, border_style="green"))
                
                self.console.print()
                
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Goodbye![/yellow]")
                break
            except EOFError:
                self.console.print("\n[yellow]Goodbye![/yellow]")
                break


def main():
    """Main entry point."""
    try:
        chat = LLMChat()
        chat.run()
    except Exception as e:
        console = Console()
        console.print(f"[red]Fatal error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
