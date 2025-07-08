#!/usr/bin/env python3
"""
UI Components for Data Analyzer

Simple user interface components for the data analysis tool.
"""

from typing import List, Dict, Any, Optional
import json


class DataInputHandler:
    """Handle user input for data analysis parameters."""
    
    def __init__(self):
        self.supported_formats = ["csv", "json", "txt"]
    
    def get_file_input(self) -> str:
        """Get file path from user input."""
        while True:
            file_path = input("Enter data file path: ").strip()
            if file_path:
                return file_path
            print("Please enter a valid file path.")
    
    def get_analysis_options(self) -> Dict[str, Any]:
        """Get analysis configuration from user."""
        options = {}
        
        # Get statistics to calculate
        print("\nSelect statistics to calculate:")
        stats_options = ["mean", "median", "std_dev", "percentiles"]
        for i, stat in enumerate(stats_options, 1):
            print(f"{i}. {stat}")
        
        selected = input("Enter numbers separated by commas (default: all): ").strip()
        if selected:
            indices = [int(x.strip()) - 1 for x in selected.split(",")]
            options["statistics"] = [stats_options[i] for i in indices if 0 <= i < len(stats_options)]
        else:
            options["statistics"] = stats_options
        
        # Get output format
        print(f"\nOutput formats: {', '.join(self.supported_formats)}")
        output_format = input("Select output format (default: json): ").strip()
        options["output_format"] = output_format if output_format in self.supported_formats else "json"
        
        return options


class ResultsDisplay:
    """Display analysis results in various formats."""
    
    def __init__(self, format_type: str = "table"):
        self.format_type = format_type
    
    def display_summary(self, results: Dict[str, Any]) -> None:
        """Display results summary."""
        print("\n" + "="*50)
        print("           ANALYSIS SUMMARY")
        print("="*50)
        
        for key, value in results.items():
            if isinstance(value, (int, float)):
                print(f"{key.replace('_', ' ').title():<20}: {value:>10.2f}")
            else:
                print(f"{key.replace('_', ' ').title():<20}: {value}")
        
        print("="*50)
    
    def display_detailed(self, results: Dict[str, Any], dataset: List[float]) -> None:
        """Display detailed analysis results."""
        self.display_summary(results)
        
        print(f"\nDataset Preview (first 10 values):")
        preview = dataset[:10] if len(dataset) > 10 else dataset
        print(f"{preview}")
        
        if len(dataset) > 10:
            print(f"... and {len(dataset) - 10} more values")


class ConfigurationUI:
    """User interface for managing analysis configuration."""
    
    def __init__(self, config_file: str = "ui_config.json"):
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Load UI configuration."""
        default_config = {
            "theme": "default",
            "precision": 2,
            "show_charts": False,
            "auto_save": True
        }
        
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                return {**default_config, **config}
        except FileNotFoundError:
            return default_config
    
    def interactive_setup(self) -> Dict[str, Any]:
        """Interactive configuration setup."""
        print("\n=== Configuration Setup ===")
        
        # Precision setting
        try:
            precision = int(input(f"Decimal precision (current: {self.config['precision']}): ") or self.config['precision'])
            self.config['precision'] = max(0, min(10, precision))
        except ValueError:
            pass
        
        # Auto-save setting
        auto_save = input(f"Auto-save results? [y/n] (current: {'y' if self.config['auto_save'] else 'n'}): ").lower()
        if auto_save in ['y', 'n']:
            self.config['auto_save'] = auto_save == 'y'
        
        # Save configuration
        self.save_config()
        return self.config
    
    def save_config(self) -> None:
        """Save current configuration."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
        print(f"Configuration saved to {self.config_file}")


def create_interactive_session():
    """Create an interactive analysis session."""
    print("Welcome to Data Analyzer Interactive Mode!")
    
    # Initialize components
    input_handler = DataInputHandler()
    display = ResultsDisplay()
    config_ui = ConfigurationUI()
    
    # Setup configuration
    config = config_ui.interactive_setup()
    
    # Get analysis parameters
    options = input_handler.get_analysis_options()
    
    print(f"\nConfiguration: {config}")
    print(f"Analysis options: {options}")
    
    return config, options


if __name__ == "__main__":
    # Demo the UI components
    config, options = create_interactive_session()
    print("\nUI components ready for integration!")
