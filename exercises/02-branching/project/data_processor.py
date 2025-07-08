#!/usr/bin/env python3
"""
Data Processor - Enhanced with Validation

Main data processing pipeline with integrated validation.
"""

import json
import statistics
from typing import List, Dict, Any, Tuple


def load_mixed_dataset() -> List[Any]:
    """Load a dataset that may contain invalid entries."""
    return [
        23.5, 18.2, "invalid", 31.7, 45.1, None, 29.8, 
        16.4, 999999, 38.9, 52.3, 27.6, 41.2, "",
        19.8, 34.5, 28.1, 47.6, 22.9, "N/A", 36.7
    ]


def calculate_statistics(data: List[float]) -> Dict[str, float]:
    """Calculate statistical measures for clean numerical data."""
    if not data:
        return {
            "count": 0,
            "mean": 0.0,
            "median": 0.0,
            "std_dev": 0.0,
            "min": 0.0,
            "max": 0.0
        }
    
    return {
        "count": len(data),
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "std_dev": statistics.stdev(data) if len(data) > 1 else 0.0,
        "min": min(data),
        "max": max(data)
    }


def process_data() -> None:
    """Main data processing workflow."""
    print("Data Processor v2.0 - With Validation")
    print("="*50)
    
    # Load potentially messy data
    raw_data = load_mixed_dataset()
    print(f"Loaded {len(raw_data)} raw data points")
    print(f"Sample data: {raw_data[:10]}...")
    
    # TODO: Add validation here
    # This is where you'll integrate the validator module
    # For now, we'll just filter obvious non-numbers
    
    # Basic filtering (to be replaced with proper validation)
    numeric_data = []
    for item in raw_data:
        try:
            if item is not None and item != "":
                numeric_data.append(float(item))
        except (ValueError, TypeError):
            print(f"Filtered out invalid item: {item}")
    
    print(f"After basic filtering: {len(numeric_data)} valid points")
    
    # Calculate statistics
    if numeric_data:
        stats = calculate_statistics(numeric_data)
        
        # Display results
        print("\nStatistical Analysis:")
        print(f"Count:          {stats['count']}")
        print(f"Mean:           {stats['mean']:.2f}")
        print(f"Median:         {stats['median']:.2f}")
        print(f"Std Deviation:  {stats['std_dev']:.2f}")
        print(f"Range:          {stats['min']:.2f} - {stats['max']:.2f}")
        
        # Save results
        with open('validated_results.json', 'w') as f:
            json.dump(stats, f, indent=2)
        
        print("\nResults saved to 'validated_results.json'")
    else:
        print("No valid data points found after filtering!")


if __name__ == "__main__":
    process_data()
