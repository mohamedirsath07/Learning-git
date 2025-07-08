#!/usr/bin/env python3
"""
Data Analyzer - GitHub Actions Edition

Enhanced data analysis tool with comprehensive testing support.
"""

import os
import json
import statistics
import argparse
from typing import List, Dict, Any, Optional
from pathlib import Path


class DataAnalyzer:
    """Main data analysis class with full testing support."""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or self.load_default_config()
        self.results = {}
    
    def load_default_config(self) -> Dict[str, Any]:
        """Load default configuration with environment variable overrides."""
        config = {
            "precision": int(os.getenv("PRECISION", "2")),
            "output_format": os.getenv("OUTPUT_FORMAT", "json"),
            "analysis_mode": os.getenv("ANALYSIS_MODE", "standard"),
            "include_outliers": os.getenv("INCLUDE_OUTLIERS", "true").lower() == "true",
            "output_dir": os.getenv("OUTPUT_DIR", "./output")
        }
        return config
    
    def load_dataset(self, file_path: Optional[str] = None) -> List[float]:
        """Load dataset from file or use sample data."""
        if file_path and Path(file_path).exists():
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    return [float(x) for x in data if isinstance(x, (int, float))]
            except (json.JSONDecodeError, ValueError, TypeError):
                print(f"Error loading data from {file_path}, using sample data")
        
        # Comprehensive sample dataset for testing
        return [
            23.5, 18.2, 31.7, 45.1, 29.8, 16.4, 38.9, 52.3, 27.6, 41.2,
            19.8, 34.5, 28.1, 47.6, 22.9, 36.7, 33.4, 26.8, 42.1, 30.5,
            15.3, 48.7, 35.9, 21.4, 39.6, 25.1, 44.8, 32.3, 17.9, 46.2,
            12.8, 55.1, 37.4, 24.7, 43.9, 18.6, 50.2, 29.3, 35.8, 41.7,
            14.2, 49.5, 33.7, 26.4, 40.8, 20.1, 45.6, 31.9, 38.3, 42.7
        ]
    
    def calculate_basic_stats(self, data: List[float]) -> Dict[str, float]:
        """Calculate basic statistical measures."""
        if not data:
            return {}
        
        precision = self.config["precision"]
        
        stats = {
            "count": len(data),
            "mean": round(statistics.mean(data), precision),
            "median": round(statistics.median(data), precision),
            "min": round(min(data), precision),
            "max": round(max(data), precision)
        }
        
        # Add standard deviation and variance for datasets with multiple points
        if len(data) > 1:
            stats["std_dev"] = round(statistics.stdev(data), precision)
            stats["variance"] = round(statistics.variance(data), precision)
        
        return stats
    
    def calculate_advanced_stats(self, data: List[float]) -> Dict[str, float]:
        """Calculate advanced statistical measures."""
        if len(data) < 4:
            return {}
        
        precision = self.config["precision"]
        sorted_data = sorted(data)
        n = len(data)
        
        # Calculate percentiles
        percentiles = {}
        for p in [25, 50, 75, 90, 95]:
            index = max(0, min(int(n * p / 100), n - 1))
            percentiles[f"p{p}"] = round(sorted_data[index], precision)
        
        # Interquartile range and outlier detection
        q1 = percentiles["p25"]
        q3 = percentiles["p75"]
        iqr = round(q3 - q1, precision)
        
        # Outlier detection using IQR method
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = [x for x in data if x < lower_bound or x > upper_bound]
        
        advanced_stats = {
            **percentiles,
            "iqr": iqr,
            "outlier_count": len(outliers),
            "outlier_percentage": round(len(outliers) / n * 100, precision)
        }
        
        return advanced_stats
    
    def analyze(self, data_file: Optional[str] = None) -> Dict[str, Any]:
        """Perform complete data analysis."""
        print(f"Data Analyzer v4.0 - CI/CD Edition")
        print(f"Configuration: {self.config}")
        print("=" * 60)
        
        # Load data
        dataset = self.load_dataset(data_file)
        print(f"Loaded {len(dataset)} data points")
        
        # Calculate basic statistics
        basic_stats = self.calculate_basic_stats(dataset)
        self.results.update(basic_stats)
        
        # Calculate advanced statistics if requested
        if self.config["analysis_mode"] in ["detailed", "advanced"]:
            advanced_stats = self.calculate_advanced_stats(dataset)
            self.results.update(advanced_stats)
        
        # Display and save results
        self.display_results()
        self.save_results()
        
        return self.results
    
    def display_results(self) -> None:
        """Display analysis results in formatted output."""
        if not self.results:
            print("No results to display")
            return
            
        print("\nAnalysis Results:")
        print("-" * 50)
        
        for key, value in self.results.items():
            formatted_key = key.replace('_', ' ').title()
            if isinstance(value, float):
                precision = self.config["precision"]
                print(f"{formatted_key:<20}: {value:>10.{precision}f}")
            else:
                print(f"{formatted_key:<20}: {value:>10}")
        
        print("-" * 50)
    
    def save_results(self) -> None:
        """Save results to file in specified format."""
        if not self.results:
            print("No results to save")
            return
            
        output_dir = Path(self.config["output_dir"])
        output_dir.mkdir(exist_ok=True)
        
        output_format = self.config["output_format"]
        
        if output_format == "json":
            output_file = output_dir / "analysis_results.json"
            with open(output_file, 'w') as f:
                json.dump(self.results, f, indent=self.config["precision"])
        
        elif output_format == "csv":
            output_file = output_dir / "analysis_results.csv"
            with open(output_file, 'w') as f:
                f.write("metric,value\n")
                for key, value in self.results.items():
                    f.write(f"{key},{value}\n")
        
        else:
            print(f"Unsupported output format: {output_format}")
            return
        
        print(f"Results saved to {output_file}")


def create_sample_data():
    """Create sample data file for testing and demonstrations."""
    sample_data = [
        23.5, 18.2, 31.7, 45.1, 29.8, 16.4, 38.9, 52.3, 27.6, 41.2,
        19.8, 34.5, 28.1, 47.6, 22.9, 36.7, 33.4, 26.8, 42.1, 30.5,
        15.3, 48.7, 35.9, 21.4, 39.6, 25.1, 44.8, 32.3, 17.9, 46.2
    ]
    
    os.makedirs("data", exist_ok=True)
    with open("data/sample_dataset.json", 'w') as f:
        json.dump(sample_data, f, indent=2)
    
    print("Sample data file created: data/sample_dataset.json")
    return sample_data


def validate_environment():
    """Validate that the environment is properly configured."""
    print("Environment Validation:")
    print(f"Python version: {os.sys.version}")
    
    # Check required directories
    required_dirs = ["output", "data"]
    for dir_name in required_dirs:
        if not Path(dir_name).exists():
            print(f"Creating directory: {dir_name}")
            Path(dir_name).mkdir(exist_ok=True)
    
    # Check environment variables
    env_vars = ["PRECISION", "OUTPUT_FORMAT", "ANALYSIS_MODE"]
    for var in env_vars:
        value = os.getenv(var)
        if value:
            print(f"{var}: {value}")
    
    print("Environment validation complete")


def main():
    """Main application entry point with comprehensive CLI support."""
    parser = argparse.ArgumentParser(
        description="Data Analyzer - CI/CD Edition",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python data_analyzer.py --create-sample
  python data_analyzer.py --data data/sample_dataset.json --mode advanced
  python data_analyzer.py --validate-env
        """
    )
    
    parser.add_argument("--data", help="Path to data file (JSON format)")
    parser.add_argument("--create-sample", action="store_true", 
                       help="Create sample data file")
    parser.add_argument("--validate-env", action="store_true",
                       help="Validate environment configuration")
    parser.add_argument("--mode", choices=["standard", "detailed", "advanced"], 
                       default=None, help="Analysis mode override")
    parser.add_argument("--output-format", choices=["json", "csv"],
                       help="Output format override")
    parser.add_argument("--precision", type=int, choices=range(0, 11),
                       help="Decimal precision override (0-10)")
    
    args = parser.parse_args()
    
    # Handle utility commands
    if args.create_sample:
        create_sample_data()
        return
    
    if args.validate_env:
        validate_environment()
        return
    
    # Build configuration with command line overrides
    config_overrides = {}
    if args.mode:
        config_overrides["analysis_mode"] = args.mode
    if args.output_format:
        config_overrides["output_format"] = args.output_format  
    if args.precision is not None:
        config_overrides["precision"] = args.precision
    
    # Initialize and run analyzer
    analyzer = DataAnalyzer(config_overrides if config_overrides else None)
    
    try:
        results = analyzer.analyze(args.data)
        print(f"\nAnalysis complete! Generated {len(results)} metrics.")
        
        # Return exit code based on success
        return 0 if results else 1
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
