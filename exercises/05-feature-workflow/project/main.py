#!/usr/bin/env python3
"""
Data Processor - Ready for Export Feature

Base application ready for data export system implementation.
"""

import json
import statistics
from typing import List, Dict, Any, Optional


class DataProcessor:
    """Core data processing functionality."""
    
    def __init__(self):
        self.results = {}
    
    def load_data(self, file_path: Optional[str] = None) -> List[float]:
        """Load data from file or return sample data."""
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    return [float(x) for x in data if isinstance(x, (int, float))]
            except (FileNotFoundError, json.JSONDecodeError, ValueError):
                print(f"Could not load {file_path}, using sample data")
        
        # Sample dataset
        return [
            25.4, 31.7, 19.8, 42.1, 36.9, 28.3, 45.6, 33.2, 27.8, 39.4,
            22.7, 48.1, 34.5, 26.9, 41.3, 30.7, 37.8, 24.6, 43.9, 32.1,
            29.5, 46.2, 35.8, 23.4, 40.7, 31.6, 38.9, 25.1, 44.3, 33.7
        ]
    
    def analyze_data(self, data: List[float]) -> Dict[str, Any]:
        """Perform statistical analysis on the data."""
        if not data:
            return {"error": "No data provided"}
        
        self.results = {
            "count": len(data),
            "mean": round(statistics.mean(data), 2),
            "median": round(statistics.median(data), 2),
            "std_dev": round(statistics.stdev(data) if len(data) > 1 else 0, 2),
            "min": round(min(data), 2),
            "max": round(max(data), 2)
        }
        
        return self.results
    
    def display_results(self) -> None:
        """Display analysis results."""
        if not self.results:
            print("No results to display")
            return
        
        print("\n" + "="*40)
        print("       DATA ANALYSIS RESULTS")
        print("="*40)
        
        for key, value in self.results.items():
            print(f"{key.replace('_', ' ').title():<15}: {value:>10}")
        
        print("="*40)


def main():
    """Main application entry point."""
    print("Data Processor v1.5")
    print("Ready for export feature development!")
    
    processor = DataProcessor()
    
    # Process data
    data = processor.load_data()
    print(f"Loaded {len(data)} data points")
    
    results = processor.analyze_data(data)
    processor.display_results()
    
    # TODO: Add export functionality here
    # This is where the export feature will be integrated
    
    return results


if __name__ == "__main__":
    main()
