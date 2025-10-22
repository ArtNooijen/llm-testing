#!/usr/bin/env python3
"""Interactive CLI for LLM testing interface."""

import sys
import os
import hashlib
import difflib
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.live import Live
from rich.spinner import Spinner
from rich import markdown
from rich.table import Table
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
    
    def load_example_file(self) -> str:
        """Load content from the example.txt file."""
        example_path = os.path.join(os.path.dirname(__file__), 'code', 'example.txt')
        try:
            with open(example_path, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except FileNotFoundError:
            self.console.print(f"[red]Error: Example file not found at {example_path}[/red]")
            return None
        except Exception as e:
            self.console.print(f"[red]Error reading example file: {e}[/red]")
            return None
    
    def save_responses_to_files(self, results, user_prompt):
        """Save model responses to markdown files in the outputs directory."""
        # Create outputs directory if it doesn't exist
        outputs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'outputs')
        os.makedirs(outputs_dir, exist_ok=True)
        
        # Create timestamp for this session
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create a summary file with all responses
        summary_file = os.path.join(outputs_dir, f"comparison_{timestamp}.md")
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(f"# LLM Comparison Results\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Prompt:**\n```\n{user_prompt}\n```\n\n")
            f.write("---\n\n")
            
            for i, result in enumerate(results, 1):
                model_name = result['model']
                instance_name = result['instance']
                response = result['response']
                success = result['success']
                metrics = result.get('metrics')
                
                f.write(f"## Model {i}: {model_name} ({instance_name})\n\n")
                if success:
                    f.write(f"**Status:** ✅ Success\n\n")
                    if metrics:
                        f.write(f"**Performance Metrics:**\n")
                        f.write(f"- **Total Duration:** {metrics['total_duration_s']:.2f} seconds\n")
                        f.write(f"- **Tokens per Second:** {metrics['tokens_per_second']:.1f}\n")
                        f.write(f"- **Input Tokens:** {metrics['prompt_eval_count']}\n")
                        f.write(f"- **Output Tokens:** {metrics['eval_count']}\n")
                        f.write(f"- **Load Duration:** {metrics['load_duration_s']:.2f} seconds\n")
                        f.write(f"- **Prompt Eval Duration:** {metrics['prompt_eval_duration_s']:.2f} seconds\n")
                        f.write(f"- **Response Eval Duration:** {metrics['eval_duration_s']:.2f} seconds\n\n")
                    f.write(f"**Response:**\n\n{response}\n\n")
                else:
                    f.write(f"**Status:** ❌ Error\n\n")
                    f.write(f"**Error:** {response}\n\n")
                f.write("---\n\n")
        
        # Create individual files for each model
        for i, result in enumerate(results, 1):
            model_name = result['model'].replace(':', '_').replace('/', '_')
            instance_name = result['instance']
            response = result['response']
            success = result['success']
            metrics = result.get('metrics')
            
            individual_file = os.path.join(outputs_dir, f"model_{i}_{model_name}_{timestamp}.md")
            
            with open(individual_file, 'w', encoding='utf-8') as f:
                f.write(f"# {model_name} Response\n\n")
                f.write(f"**Model:** {model_name}\n")
                f.write(f"**Instance:** {instance_name}\n")
                f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"**Status:** {'✅ Success' if success else '❌ Error'}\n\n")
                
                if success and metrics:
                    f.write(f"**Performance Metrics:**\n")
                    f.write(f"- **Total Duration:** {metrics['total_duration_s']:.2f} seconds\n")
                    f.write(f"- **Tokens per Second:** {metrics['tokens_per_second']:.1f}\n")
                    f.write(f"- **Input Tokens:** {metrics['prompt_eval_count']}\n")
                    f.write(f"- **Output Tokens:** {metrics['eval_count']}\n")
                    f.write(f"- **Load Duration:** {metrics['load_duration_s']:.2f} seconds\n")
                    f.write(f"- **Prompt Eval Duration:** {metrics['prompt_eval_duration_s']:.2f} seconds\n")
                    f.write(f"- **Response Eval Duration:** {metrics['eval_duration_s']:.2f} seconds\n\n")
                
                f.write(f"**Prompt:**\n```\n{user_prompt}\n```\n\n")
                f.write("---\n\n")
                f.write("**Response:**\n\n")
                if success:
                    f.write(response)
                else:
                    f.write(f"Error: {response}")
                f.write("\n")
        
        return summary_file, outputs_dir
    
    def run_comparison(self):
        """Run model comparison mode."""
        self.show_welcome()
        
        if not self.interface.is_available():
            self.console.print("[red]Error: Cannot connect to Ollama. Please check your connection.[/red]")
            self.console.print(f"Trying to connect to: {self.config.ollama_url}")
            return
        
        # Ask user for input method
        self.console.print("\n[bold]Choose your input method:[/bold]")
        self.console.print("1. Type your own prompt")
        self.console.print("2. Use example file (code/example.txt)")
        self.console.print("3. Consistency test (run same model multiple times)")
        
        choice = Prompt.ask("Enter your choice (1, 2, or 3)", console=self.console, default="1")
        
        user_prompt = None
        
        if choice == "1":
            # Get prompt from user
            prompt_text = self.cli_config.get('prompt', 'Enter your prompt: ')
            user_prompt = Prompt.ask(prompt_text, console=self.console)
        elif choice == "2":
            # Load example file
            self.console.print("\n[blue]Loading example file...[/blue]")
            user_prompt = self.load_example_file()
            if user_prompt is None:
                self.console.print("[red]Failed to load example file. Exiting.[/red]")
                return
            self.console.print(f"[green]Loaded example content:[/green]")
            self.console.print(Panel(user_prompt, title="Example Content", border_style="blue"))
        elif choice == "3":
            # Run consistency test
            self.run_consistency_test()
            return
        else:
            self.console.print("[red]Invalid choice. Exiting.[/red]")
            return
        
        if not user_prompt or not user_prompt.strip():
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
                    result = model_interface.generate(user_prompt)
                    results.append({
                        'model': model_name,
                        'instance': instance_name,
                        'response': result['response'],
                        'metrics': result['metrics'],
                        'success': True
                    })
                except Exception as e:
                    results.append({
                        'model': model_name,
                        'instance': instance_name,
                        'response': f"Error: {e}",
                        'metrics': None,
                        'success': False
                    })
            
            self.console.print()
        
        # Display comparison results
        self.show_comparison_results(results)
        
        # Save responses to files
        self.console.print("\n[blue]Saving responses to files...[/blue]")
        summary_file, outputs_dir = self.save_responses_to_files(results, user_prompt)
        
        self.console.print(f"[green]✅ Responses saved successfully![/green]")
        self.console.print(f"[blue]Summary file:[/blue] {summary_file}")
        self.console.print(f"[blue]Output directory:[/blue] {outputs_dir}")
        self.console.print(f"[blue]Individual model files:[/blue] {len(results)} files created")
    
    def show_comparison_results(self, results):
        """Display comparison results for all models."""
        self.console.print("[bold green]=== COMPARISON RESULTS ===[/bold green]\n")
        
        for i, result in enumerate(results, 1):
            model_name = result['model']
            instance_name = result['instance']
            response = result['response']
            success = result['success']
            metrics = result.get('metrics')
            
            # Create panel for each model result
            if success and metrics:
                # Format performance metrics
                duration = f"{metrics['total_duration_s']:.2f}s"
                tokens_per_sec = f"{metrics['tokens_per_second']:.1f}"
                eval_count = metrics['eval_count']
                prompt_tokens = metrics['prompt_eval_count']
                
                metrics_text = f"Duration: {duration} | Tokens/sec: {tokens_per_sec} | Output tokens: {eval_count} | Input tokens: {prompt_tokens}"
                
                panel = Panel(
                    f"{metrics_text}\n\n{response}",
                    title=f"[bold blue]Model {i}: {model_name} ({instance_name})[/bold blue]",
                    border_style="green"
                )
            elif success:
                panel = Panel(
                    response,
                    title=f"[bold blue]Model {i}: {model_name} ({instance_name})[/bold blue]",
                    border_style="green"
                )
            else:
                panel = Panel(
                    response,
                    title=f"[bold red]Model {i}: {model_name} ({instance_name}) - ERROR[/bold red]",
                    border_style="red"
                )
            
            self.console.print(panel)
            self.console.print()
    
    def run_consistency_test(self):
        """Run consistency test on a single model multiple times."""
        self.show_welcome()
        
        if not self.interface.is_available():
            self.console.print("[red]Error: Cannot connect to Ollama. Please check your connection.[/red]")
            self.console.print(f"Trying to connect to: {self.config.ollama_url}")
            return
        
        # Get models to choose from
        models = self.config.ollama_models
        if not models:
            self.console.print("[red]No models configured. Exiting.[/red]")
            return
        
        # Let user select a model
        self.console.print("\n[bold]Select a model to test for consistency:[/bold]")
        for i, model_config in enumerate(models, 1):
            model_name = model_config['name']
            instance_name = model_config['instance']
            self.console.print(f"{i}. {model_name} (on {instance_name})")
        
        try:
            model_choice = int(Prompt.ask("Enter model number", console=self.console)) - 1
            if model_choice < 0 or model_choice >= len(models):
                self.console.print("[red]Invalid model choice. Exiting.[/red]")
                return
        except ValueError:
            self.console.print("[red]Invalid input. Exiting.[/red]")
            return
        
        selected_model = models[model_choice]
        model_name = selected_model['name']
        instance_name = selected_model['instance']
        
        # Get prompt
        self.console.print("\n[bold]Choose your input method:[/bold]")
        self.console.print("1. Type your own prompt")
        self.console.print("2. Use example file (code/example.txt)")
        
        prompt_choice = Prompt.ask("Enter your choice (1 or 2)", console=self.console, default="1")
        
        user_prompt = None
        
        if prompt_choice == "1":
            prompt_text = self.cli_config.get('prompt', 'Enter your prompt: ')
            user_prompt = Prompt.ask(prompt_text, console=self.console)
        elif prompt_choice == "2":
            self.console.print("\n[blue]Loading example file...[/blue]")
            user_prompt = self.load_example_file()
            if user_prompt is None:
                self.console.print("[red]Failed to load example file. Exiting.[/red]")
                return
            self.console.print(f"[green]Loaded example content:[/green]")
            self.console.print(Panel(user_prompt, title="Example Content", border_style="blue"))
        else:
            self.console.print("[red]Invalid choice. Exiting.[/red]")
            return
        
        if not user_prompt or not user_prompt.strip():
            self.console.print("[yellow]No prompt provided. Exiting.[/yellow]")
            return
        
        # Get repetition count
        repetition_count = self.config.repetition_count
        self.console.print(f"\n[bold]Running {model_name} {repetition_count} times with the same prompt...[/bold]")
        self.console.print(f"Prompt: [italic]{user_prompt}[/italic]\n")
        
        # Create interface for the selected model
        model_interface = OllamaInterface(self.config, instance_name)
        model_interface.model = model_name
        
        # Run the model multiple times
        results = []
        for i in range(repetition_count):
            self.console.print(f"[bold blue]Run {i+1}/{repetition_count}: {model_name} (on {instance_name})[/bold blue]")
            
            with self.show_typing_indicator():
                try:
                    result = model_interface.generate(user_prompt)
                    results.append({
                        'run_number': i + 1,
                        'model': model_name,
                        'instance': instance_name,
                        'response': result['response'],
                        'metrics': result['metrics'],
                        'success': True,
                        'timestamp': datetime.now()
                    })
                except Exception as e:
                    results.append({
                        'run_number': i + 1,
                        'model': model_name,
                        'instance': instance_name,
                        'response': f"Error: {e}",
                        'metrics': None,
                        'success': False,
                        'timestamp': datetime.now()
                    })
            
            self.console.print()
        
        # Analyze consistency
        analysis = self.analyze_consistency(results)
        
        # Display results
        self.show_consistency_results(results, analysis)
        
        # Save results to files
        self.console.print("\n[blue]Saving consistency test results to files...[/blue]")
        markdown_file, csv_file = self.save_consistency_results(results, analysis, user_prompt)
        
        self.console.print(f"[green]✅ Results saved successfully![/green]")
        self.console.print(f"[blue]Markdown file:[/blue] {markdown_file}")
        self.console.print(f"[blue]CSV file:[/blue] {csv_file}")
    
    def analyze_consistency(self, results):
        """Analyze consistency of multiple runs."""
        successful_results = [r for r in results if r['success']]
        
        if not successful_results:
            return {
                'total_runs': len(results),
                'successful_runs': 0,
                'failed_runs': len(results),
                'identical_outputs': 0,
                'different_outputs': 0,
                'unique_responses': 0,
                'similarity_matrix': [],
                'differences': [],
                'change_counts': []
            }
        
        # Calculate response hashes
        response_hashes = []
        for result in successful_results:
            response_hash = self.hash_response(result['response'])
            response_hashes.append(response_hash)
        
        # Count unique responses
        unique_hashes = set(response_hashes)
        unique_responses = len(unique_hashes)
        
        # Calculate similarity matrix and change counts
        similarity_matrix = []
        change_counts = []
        similarity_to_first = []
        
        for i, result1 in enumerate(successful_results):
            row = []
            changes_count = 0
            
            for j, result2 in enumerate(successful_results):
                if i == j:
                    row.append(1.0)
                else:
                    similarity = self.calculate_text_similarity(result1['response'], result2['response'])
                    row.append(similarity)
                    # Count actual differences (lines that differ)
                    changes = self.count_text_differences(result1['response'], result2['response'])
                    changes_count += changes
            
            similarity_matrix.append(row)
            
            # Calculate similarity to first run
            similarity_to_first_run = 1.0 if i == 0 else self.calculate_text_similarity(successful_results[0]['response'], result1['response'])
            similarity_to_first.append({
                'run_number': result1['run_number'],
                'similarity_to_first': similarity_to_first_run
            })
            
            change_counts.append({
                'run_number': result1['run_number'],
                'total_changes': changes_count,
                'avg_similarity': sum(row) / len(row) if row else 0,
                'similarity_to_first': similarity_to_first_run
            })
        
        # Find differences between runs
        differences = []
        for i in range(len(successful_results)):
            for j in range(i + 1, len(successful_results)):
                if response_hashes[i] != response_hashes[j]:
                    diff = self.generate_diff_html_style(
                        successful_results[i]['response'],
                        successful_results[j]['response'],
                        f"Run {successful_results[i]['run_number']}",
                        f"Run {successful_results[j]['run_number']}"
                    )
                    differences.append({
                        'run1': successful_results[i]['run_number'],
                        'run2': successful_results[j]['run_number'],
                        'similarity': similarity_matrix[i][j],
                        'diff': diff
                    })
        
        # Calculate overall accuracy metrics
        if len(similarity_to_first) > 1:
            avg_similarity_to_first = sum(s['similarity_to_first'] for s in similarity_to_first[1:]) / (len(similarity_to_first) - 1)
            min_similarity_to_first = min(s['similarity_to_first'] for s in similarity_to_first[1:])
            max_similarity_to_first = max(s['similarity_to_first'] for s in similarity_to_first[1:])
        else:
            avg_similarity_to_first = 1.0
            min_similarity_to_first = 1.0
            max_similarity_to_first = 1.0
        
        return {
            'total_runs': len(results),
            'successful_runs': len(successful_results),
            'failed_runs': len(results) - len(successful_results),
            'identical_outputs': len([h for h in response_hashes if response_hashes.count(h) > 1]),
            'different_outputs': len([h for h in response_hashes if response_hashes.count(h) == 1]),
            'unique_responses': unique_responses,
            'similarity_matrix': similarity_matrix,
            'differences': differences,
            'change_counts': change_counts,
            'similarity_to_first': similarity_to_first,
            'overall_accuracy': {
                'avg_similarity_to_first': avg_similarity_to_first,
                'min_similarity_to_first': min_similarity_to_first,
                'max_similarity_to_first': max_similarity_to_first
            }
        }
    
    def calculate_text_similarity(self, text1, text2):
        """Calculate similarity between two text strings."""
        return difflib.SequenceMatcher(None, text1, text2).ratio()
    
    def count_text_differences(self, text1, text2):
        """Count the number of different lines between two texts."""
        lines1 = text1.splitlines()
        lines2 = text2.splitlines()
        
        # Use difflib to find differences
        differ = difflib.unified_diff(lines1, lines2, lineterm='')
        diff_lines = list(differ)
        
        # Count lines that start with + or - (actual changes)
        changes = 0
        for line in diff_lines:
            if line.startswith('+') or line.startswith('-'):
                changes += 1
        
        return changes
    
    def generate_diff_html_style(self, text1, text2, label1, label2):
        """Generate a readable diff between two texts."""
        diff = difflib.unified_diff(
            text1.splitlines(keepends=True),
            text2.splitlines(keepends=True),
            fromfile=label1,
            tofile=label2,
            lineterm=''
        )
        return ''.join(diff)
    
    def hash_response(self, response):
        """Generate hash for response comparison."""
        return hashlib.md5(response.encode('utf-8')).hexdigest()
    
    def show_consistency_results(self, results, analysis):
        """Display consistency test results."""
        self.console.print("[bold green]=== CONSISTENCY TEST RESULTS ===[/bold green]\n")
        
        # Summary table
        table = Table(title="Consistency Summary")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        
        table.add_row("Total Runs", str(analysis['total_runs']))
        table.add_row("Successful Runs", str(analysis['successful_runs']))
        table.add_row("Failed Runs", str(analysis['failed_runs']))
        table.add_row("Unique Responses", str(analysis['unique_responses']))
        table.add_row("Identical Outputs", str(analysis['identical_outputs']))
        table.add_row("Different Outputs", str(analysis['different_outputs']))
        
        # Show change statistics if available
        if analysis.get('change_counts'):
            total_changes = sum(change['total_changes'] for change in analysis['change_counts'])
            avg_changes = total_changes / len(analysis['change_counts']) if analysis['change_counts'] else 0
            table.add_row("Total Changes", str(total_changes))
            table.add_row("Avg Changes per Run", f"{avg_changes:.1f}")
        
        # Show overall accuracy if available
        if analysis.get('overall_accuracy'):
            accuracy = analysis['overall_accuracy']
            table.add_row("Avg Similarity to First", f"{accuracy['avg_similarity_to_first']:.1%}")
            table.add_row("Min Similarity to First", f"{accuracy['min_similarity_to_first']:.1%}")
            table.add_row("Max Similarity to First", f"{accuracy['max_similarity_to_first']:.1%}")
        
        self.console.print(table)
        self.console.print()
        
        # Show individual results
        for result in results:
            run_num = result['run_number']
            model_name = result['model']
            instance_name = result['instance']
            response = result['response']
            success = result['success']
            metrics = result.get('metrics')
            
            # Get similarity to first run
            similarity_to_first = 100.0  # Default for first run
            for sim_data in analysis.get('similarity_to_first', []):
                if sim_data['run_number'] == run_num:
                    similarity_to_first = sim_data['similarity_to_first'] * 100
                    break
            
            if success and metrics:
                duration = f"{metrics['total_duration_s']:.2f}s"
                tokens_per_sec = f"{metrics['tokens_per_second']:.1f}"
                eval_count = metrics['eval_count']
                prompt_tokens = metrics['prompt_eval_count']
                
                metrics_text = f"Duration: {duration} | Tokens/sec: {tokens_per_sec} | Output tokens: {eval_count} | Input tokens: {prompt_tokens} | Similarity to First: {similarity_to_first:.1f}%"
                
                panel = Panel(
                    f"{metrics_text}\n\n{response}",
                    title=f"[bold blue]Run {run_num}: {model_name} ({instance_name})[/bold blue]",
                    border_style="green"
                )
            elif success:
                panel = Panel(
                    f"Similarity to First: {similarity_to_first:.1f}%\n\n{response}",
                    title=f"[bold blue]Run {run_num}: {model_name} ({instance_name})[/bold blue]",
                    border_style="green"
                )
            else:
                panel = Panel(
                    response,
                    title=f"[bold red]Run {run_num}: {model_name} ({instance_name}) - ERROR[/bold red]",
                    border_style="red"
                )
            
            self.console.print(panel)
            self.console.print()
    
    def save_consistency_results(self, results, analysis, user_prompt):
        """Save consistency test results to markdown and CSV files."""
        # Create outputs directory if it doesn't exist
        outputs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'outputs')
        os.makedirs(outputs_dir, exist_ok=True)
        
        # Create timestamp for this session
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Get model info from first successful result
        model_name = results[0]['model'] if results else "unknown"
        instance_name = results[0]['instance'] if results else "unknown"
        
        # Create markdown file
        markdown_file = os.path.join(outputs_dir, f"consistency_{model_name.replace(':', '_').replace('/', '_')}_{timestamp}.md")
        
        with open(markdown_file, 'w', encoding='utf-8') as f:
            f.write(f"# Model Consistency Test Results\n\n")
            f.write(f"**Model:** {model_name}\n")
            f.write(f"**Instance:** {instance_name}\n")
            f.write(f"**Number of Runs:** {analysis['total_runs']}\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## Summary\n")
            f.write(f"- **Total Runs:** {analysis['total_runs']}\n")
            f.write(f"- **Successful Runs:** {analysis['successful_runs']}\n")
            f.write(f"- **Failed Runs:** {analysis['failed_runs']}\n")
            f.write(f"- **Unique Responses:** {analysis['unique_responses']}\n")
            f.write(f"- **Identical Outputs:** {analysis['identical_outputs']}\n")
            f.write(f"- **Different Outputs:** {analysis['different_outputs']}\n")
            
            # Add change statistics if available
            if analysis.get('change_counts'):
                total_changes = sum(change['total_changes'] for change in analysis['change_counts'])
                avg_changes = total_changes / len(analysis['change_counts']) if analysis['change_counts'] else 0
                f.write(f"- **Total Changes:** {total_changes}\n")
                f.write(f"- **Average Changes per Run:** {avg_changes:.1f}\n")
            
            # Add overall accuracy if available
            if analysis.get('overall_accuracy'):
                accuracy = analysis['overall_accuracy']
                f.write(f"- **Average Similarity to First Run:** {accuracy['avg_similarity_to_first']:.1%}\n")
                f.write(f"- **Minimum Similarity to First Run:** {accuracy['min_similarity_to_first']:.1%}\n")
                f.write(f"- **Maximum Similarity to First Run:** {accuracy['max_similarity_to_first']:.1%}\n")
            
            f.write("\n")
            
            f.write("## Individual Runs\n")
            for result in results:
                run_num = result['run_number']
                response = result['response']
                success = result['success']
                metrics = result.get('metrics')
                timestamp_str = result['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                
                # Get similarity to first run
                similarity_to_first = 100.0  # Default for first run
                for sim_data in analysis.get('similarity_to_first', []):
                    if sim_data['run_number'] == run_num:
                        similarity_to_first = sim_data['similarity_to_first'] * 100
                        break
                
                f.write(f"### Run {run_num}\n\n")
                f.write(f"**Timestamp:** {timestamp_str}\n")
                f.write(f"**Status:** {'✅ Success' if success else '❌ Error'}\n")
                f.write(f"**Similarity to First Run:** {similarity_to_first:.1f}%\n")
                
                if success and metrics:
                    f.write(f"**Performance Metrics:**\n")
                    f.write(f"- **Total Duration:** {metrics['total_duration_s']:.2f} seconds\n")
                    f.write(f"- **Tokens per Second:** {metrics['tokens_per_second']:.1f}\n")
                    f.write(f"- **Input Tokens:** {metrics['prompt_eval_count']}\n")
                    f.write(f"- **Output Tokens:** {metrics['eval_count']}\n")
                    f.write(f"- **Load Duration:** {metrics['load_duration_s']:.2f} seconds\n")
                    f.write(f"- **Prompt Eval Duration:** {metrics['prompt_eval_duration_s']:.2f} seconds\n")
                    f.write(f"- **Response Eval Duration:** {metrics['eval_duration_s']:.2f} seconds\n\n")
                
                f.write(f"**Response:**\n\n{response}\n\n")
                f.write("---\n\n")
            
            # Add difference analysis if there are differences
            if analysis['differences']:
                f.write("## Difference Analysis\n")
                for diff in analysis['differences']:
                    f.write(f"### Comparison: Run {diff['run1']} vs Run {diff['run2']}\n")
                    f.write(f"**Similarity:** {diff['similarity']:.2%}\n\n")
                    f.write("**Diff:**\n```diff\n")
                    f.write(diff['diff'])
                    f.write("\n```\n\n")
            
            # Add overall test accuracy summary
            if analysis.get('overall_accuracy'):
                f.write("## Overall Test Accuracy Summary\n\n")
                accuracy = analysis['overall_accuracy']
                f.write(f"**Test Accuracy Metrics:**\n")
                f.write(f"- **Average Similarity to First Run:** {accuracy['avg_similarity_to_first']:.1%}\n")
                f.write(f"- **Minimum Similarity to First Run:** {accuracy['min_similarity_to_first']:.1%}\n")
                f.write(f"- **Maximum Similarity to First Run:** {accuracy['max_similarity_to_first']:.1%}\n")
                f.write(f"- **Consistency Range:** {accuracy['max_similarity_to_first'] - accuracy['min_similarity_to_first']:.1%}\n\n")
                
                # Add interpretation
                avg_sim = accuracy['avg_similarity_to_first']
                if avg_sim >= 0.95:
                    f.write("**Interpretation:** 🟢 **Excellent Consistency** - Model shows very high consistency across runs.\n\n")
                elif avg_sim >= 0.85:
                    f.write("**Interpretation:** 🟡 **Good Consistency** - Model shows good consistency with minor variations.\n\n")
                elif avg_sim >= 0.70:
                    f.write("**Interpretation:** 🟠 **Moderate Consistency** - Model shows moderate consistency with noticeable variations.\n\n")
                else:
                    f.write("**Interpretation:** 🔴 **Low Consistency** - Model shows significant variation across runs.\n\n")
        
        # Create CSV file
        csv_file = os.path.join(outputs_dir, f"consistency_{model_name.replace(':', '_').replace('/', '_')}_{timestamp}.csv")
        
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            f.write("Run,Model,Instance,Timestamp,Duration_s,Tokens,Response_Length,Total_Changes,Avg_Similarity,Similarity_to_First,Response_Text\n")
            for result in results:
                run_num = result['run_number']
                model_name = result['model']
                instance_name = result['instance']
                timestamp_str = result['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                response = result['response']
                response_length = len(response)
                
                if result['success'] and result.get('metrics'):
                    duration = result['metrics']['total_duration_s']
                    tokens = result['metrics']['eval_count']
                else:
                    duration = 0
                    tokens = 0
                
                # Get change count and similarity for this run
                change_count = 0
                avg_similarity = 0
                similarity_to_first = 1.0  # Default for first run
                for change_info in analysis.get('change_counts', []):
                    if change_info['run_number'] == run_num:
                        change_count = change_info['total_changes']
                        avg_similarity = change_info['avg_similarity']
                        similarity_to_first = change_info['similarity_to_first']
                        break
                
                # Escape quotes and newlines in response for CSV
                escaped_response = response.replace('"', '""').replace('\n', '\\n').replace('\r', '\\r')
                f.write(f"{run_num},{model_name},{instance_name},{timestamp_str},{duration:.2f},{tokens},{response_length},{change_count},{avg_similarity:.3f},{similarity_to_first:.3f},\"{escaped_response}\"\n")
            
            # Add summary row with totals
            f.write("\n")
            f.write("# SUMMARY STATISTICS\n")
            
            # Calculate totals
            total_duration = sum(result.get('metrics', {}).get('total_duration_s', 0) for result in results if result['success'])
            total_tokens = sum(result.get('metrics', {}).get('eval_count', 0) for result in results if result['success'])
            total_response_length = sum(len(result['response']) for result in results)
            total_changes = sum(change['total_changes'] for change in analysis.get('change_counts', []))
            avg_similarity_overall = sum(change['avg_similarity'] for change in analysis.get('change_counts', [])) / len(analysis.get('change_counts', [])) if analysis.get('change_counts') else 0
            avg_similarity_to_first = analysis.get('overall_accuracy', {}).get('avg_similarity_to_first', 0)
            
            f.write(f"TOTAL,{model_name},{instance_name},SUMMARY,{total_duration:.2f},{total_tokens},{total_response_length},{total_changes},{avg_similarity_overall:.3f},{avg_similarity_to_first:.3f},\"SUMMARY: {analysis['successful_runs']} successful runs, {analysis['unique_responses']} unique responses, {analysis['identical_outputs']} identical outputs\"\n")
        
        return markdown_file, csv_file
    
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
                        result = self.interface.generate(user_input)
                        response = result['response']
                        metrics = result.get('metrics')
                    except Exception as e:
                        self.console.print(f"[red]Error: {e}[/red]")
                        continue
                
                # Display response
                self.console.print()
                self.console.print("[bold blue]Assistant:[/bold blue]")
                
                # Show performance metrics if available
                if metrics:
                    duration = f"{metrics['total_duration_s']:.2f}s"
                    tokens_per_sec = f"{metrics['tokens_per_second']:.1f}"
                    eval_count = metrics['eval_count']
                    prompt_tokens = metrics['prompt_eval_count']
                    
                    metrics_text = f"[dim]Duration: {duration} | Tokens/sec: {tokens_per_sec} | Output: {eval_count} tokens | Input: {prompt_tokens} tokens[/dim]"
                    self.console.print(metrics_text)
                    self.console.print()
                
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
