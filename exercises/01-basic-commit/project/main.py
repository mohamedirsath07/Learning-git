#!/usr/bin/env python3
"""
Data Analysis CLI Tool

A simple command-line tool for analyzing numerical datasets.
Currently supports basic data loading and statistical analysis.
"""

import json
import statistics
from typing import List, Dict, Any


def load_sample_data() -> List[float]:
    """Load sample dataset for analysis."""
    return [23.5, 18.2, 31.7, 45.1, 29.8, 16.4, 38.9, 52.3, 27.6, 41.2,
            19.8, 34.5, 28.1, 47.6, 22.9, 36.7, 33.4, 26.8, 42.1, 30.5]


def calculate_stats(data: List[float]) -> Dict[str, Any]:
    """
    Calculate statistical summary for numerical data.
    
    Args:
        data: List of numerical values
        
    Returns:
        Dictionary containing statistical measures
    """
    # TODO: Implement this function
    # Calculate mean, median, and standard deviation
    # Handle edge cases (empty lists, single values)
    # Return formatted results as a dictionary
    
    # Placeholder return - replace with actual implementation
    return {
        "count": 0,
        "mean": 0.0,
        "median": 0.0,
        "std_dev": 0.0,
        "min": 0.0,
        "max": 0.0
    }


def format_output(stats: Dict[str, Any]) -> None:
    """Display statistical results in a readable format."""
    print("\n" + "="*50)
    print("           STATISTICAL ANALYSIS RESULTS")
    print("="*50)
    print(f"Dataset Size:    {stats['count']:>10}")
    print(f"Mean:           {stats['mean']:>10.2f}")
    print(f"Median:         {stats['median']:>10.2f}")
    print(f"Std Deviation:  {stats['std_dev']:>10.2f}")
    print(f"Minimum:        {stats['min']:>10.2f}")
    print(f"Maximum:        {stats['max']:>10.2f}")
    print("="*50)


def main():
    """Main application entry point."""
    print("Data Analysis CLI Tool v1.0")
    print("Loading sample dataset...")
    
    # Load data
    dataset = load_sample_data()
    print(f"Loaded {len(dataset)} data points")
    
    # Calculate statistics
    results = calculate_stats(dataset)
    
    # Display results
    format_output(results)
    
    # Save results to file
    with open('analysis_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\nResults saved to 'analysis_results.json'")


if __name__ == "__main__":
    main()
