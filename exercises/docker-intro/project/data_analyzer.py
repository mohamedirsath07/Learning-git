#!/usr/bin/env python3
"""
Enhanced Data Analyzer - Container Ready

A comprehensive data analysis tool designed for containerized environments.
"""

import os
import json
import statistics
import argparse
from typing import List, Dict, Any, Optional
from pathlib import Path


class DataAnalyzer:
    """Main data analysis class with configurable options."""
    
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
            with open(file_path, 'r') as f:
                data = json.load(f)
                return [float(x) for x in data if isinstance(x, (int, float))]
        
        # Sample dataset for demonstration
        return [
            23.5, 18.2, 31.7, 45.1, 29.8, 16.4, 38.9, 52.3, 27.6, 41.2,
            19.8, 34.5, 28.1, 47.6, 22.9, 36.7, 33.4, 26.8, 42.1, 30.5,
            15.3, 48.7, 35.9, 21.4, 39.6, 25.1, 44.8, 32.3, 17.9, 46.2,
            12.8, 55.1, 37.4, 24.7, 43.9, 18.6, 50.2, 29.3, 35.8, 41.7
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
        
        # Percentiles
        percentiles = {}
        for p in [25, 50, 75, 90, 95]:
            index = int(n * p / 100)
            percentiles[f"p{p}"] = round(sorted_data[min(index, n-1)], precision)
        
        # Interquartile range
        q1 = percentiles["p25"]
        q3 = percentiles["p75"]
        iqr = round(q3 - q1, precision)
        
        # Outlier detection
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
        print(f"Data Analyzer v3.0 - Container Edition")
        print(f"Configuration: {self.config}")
        print("=" * 60)
        
        # Load data
        dataset = self.load_dataset(data_file)
        print(f"Loaded {len(dataset)} data points")
        
        # Calculate statistics
        basic_stats = self.calculate_basic_stats(dataset)
        self.results.update(basic_stats)
        
        if self.config["analysis_mode"] in ["detailed", "advanced"]:
            advanced_stats = self.calculate_advanced_stats(dataset)
            self.results.update(advanced_stats)
        
        # Display results
        self.display_results()
        
        # Save results
        self.save_results()
        
        return self.results
    
    def display_results(self) -> None:
        """Display analysis results."""
        print("\nAnalysis Results:")
        print("-" * 40)
        
        for key, value in self.results.items():
            if isinstance(value, float):
                print(f"{key.replace('_', ' ').title():<20}: {value:>10.{self.config['precision']}f}")
            else:
                print(f"{key.replace('_', ' ').title():<20}: {value:>10}")
        
        print("-" * 40)
    
    def save_results(self) -> None:
        """Save results to file."""
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
        
        print(f"Results saved to {output_file}")


def create_sample_data():
    """Create sample data file for testing."""
    sample_data = [
        23.5, 18.2, 31.7, 45.1, 29.8, 16.4, 38.9, 52.3, 27.6, 41.2,
        19.8, 34.5, 28.1, 47.6, 22.9, 36.7, 33.4, 26.8, 42.1, 30.5
    ]
    
    os.makedirs("data", exist_ok=True)
    with open("data/sample_dataset.json", 'w') as f:
        json.dump(sample_data, f, indent=2)
    
    print("Sample data file created: data/sample_dataset.json")


def main():
    """Main application entry point."""
    parser = argparse.ArgumentParser(description="Data Analyzer - Container Edition")
    parser.add_argument("--data", help="Path to data file")
    parser.add_argument("--create-sample", action="store_true", help="Create sample data file")
    parser.add_argument("--mode", choices=["standard", "detailed", "advanced"], 
                       default="standard", help="Analysis mode")
    
    args = parser.parse_args()
    
    if args.create_sample:
        create_sample_data()
        return
    
    # Override config with command line arguments
    config_overrides = {}
    if args.mode:
        config_overrides["analysis_mode"] = args.mode
    
    # Initialize analyzer
    analyzer = DataAnalyzer(config_overrides)
    
    # Run analysis
    results = analyzer.analyze(args.data)
    
    print(f"\nAnalysis complete! Found {len(results)} metrics.")


if __name__ == "__main__":
    main()
