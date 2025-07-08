#!/usr/bin/env python3
"""
Data Analyzer - Main Branch Version

Configuration-driven data analysis tool with enhanced settings management.
"""

import json
import statistics
from typing import List, Dict, Any, Optional


class AnalysisConfig:
    """Configuration management for data analysis."""
    
    def __init__(self, config_file: str = "analysis_config.json"):
        self.config_file = config_file
        self.settings = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file."""
        default_config = {
            "data_sources": ["sample_data.json"],
            "output_format": "json",
            "precision": 2,
            "include_outliers": True,
            "statistics": ["mean", "median", "std_dev"]
        }
        
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                # Merge with defaults
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
        except FileNotFoundError:
            return default_config
    
    def save_config(self) -> None:
        """Save current configuration to file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=2)


def load_dataset() -> List[float]:
    """Load sample dataset for analysis."""
    return [
        23.5, 18.2, 31.7, 45.1, 29.8, 16.4, 38.9, 52.3, 27.6, 41.2,
        19.8, 34.5, 28.1, 47.6, 22.9, 36.7, 33.4, 26.8, 42.1, 30.5,
        15.3, 48.7, 35.9, 21.4, 39.6, 25.1, 44.8, 32.3, 17.9, 46.2
    ]


def calculate_basic_statistics(data: List[float], config: AnalysisConfig) -> Dict[str, float]:
    """Calculate basic statistical measures based on configuration."""
    if not data:
        return {}
    
    stats = {}
    enabled_stats = config.settings.get("statistics", [])
    precision = config.settings.get("precision", 2)
    
    if "mean" in enabled_stats:
        stats["mean"] = round(statistics.mean(data), precision)
    
    if "median" in enabled_stats:
        stats["median"] = round(statistics.median(data), precision)
    
    if "std_dev" in enabled_stats:
        stats["std_dev"] = round(statistics.stdev(data) if len(data) > 1 else 0.0, precision)
    
    # Always include basic info
    stats["count"] = len(data)
    stats["min"] = round(min(data), precision)
    stats["max"] = round(max(data), precision)
    
    return stats


def format_results(stats: Dict[str, float], config: AnalysisConfig) -> None:
    """Display results according to configuration."""
    print("\n" + "="*60)
    print("           DATA ANALYSIS RESULTS")
    print("="*60)
    
    for key, value in stats.items():
        if isinstance(value, float):
            precision = config.settings.get("precision", 2)
            print(f"{key.replace('_', ' ').title():<15}: {value:.{precision}f}")
        else:
            print(f"{key.replace('_', ' ').title():<15}: {value}")
    
    print("="*60)


def main():
    """Main analysis workflow with configuration support."""
    print("Data Analyzer v2.1 - Configuration Enhanced")
    
    # Initialize configuration
    config = AnalysisConfig()
    print(f"Loaded configuration: {config.settings}")
    
    # Load and analyze data
    dataset = load_dataset()
    print(f"\nLoaded {len(dataset)} data points")
    
    # Calculate statistics
    results = calculate_basic_statistics(dataset, config)
    
    # Display results
    format_results(results, config)
    
    # Save results based on configuration
    output_format = config.settings.get("output_format", "json")
    if output_format == "json":
        output_file = "analysis_results.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=config.settings.get("precision", 2))
        print(f"\nResults saved to {output_file}")


if __name__ == "__main__":
    main()
