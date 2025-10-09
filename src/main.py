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
    
    def run(self):
        """Run the interactive chat loop."""
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
