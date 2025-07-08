#!/usr/bin/env python3
"""
Test suite for Data Analyzer

Comprehensive tests for the data analysis functionality.
"""

import pytest
import json
import os
import tempfile
from pathlib import Path
from data_analyzer import DataAnalyzer


class TestDataAnalyzer:
    """Test cases for DataAnalyzer class."""

    def setup_method(self):
        """Set up test environment before each test."""
        self.config = {
            "precision": 2,
            "output_format": "json", 
            "analysis_mode": "standard",
            "include_outliers": True,
            "output_dir": "./test_output"
        }
        self.analyzer = DataAnalyzer(self.config)
        
        # Sample test data
        self.test_data = [10.0, 20.0, 30.0, 40.0, 50.0]
        self.empty_data = []
        self.single_data = [42.0]

    def teardown_method(self):
        """Clean up after each test."""
        # Remove test output directory if it exists
        test_output = Path("./test_output")
        if test_output.exists():
            for file in test_output.glob("*"):
                file.unlink()
            test_output.rmdir()

    def test_load_default_config(self):
        """Test default configuration loading."""
        analyzer = DataAnalyzer()
        config = analyzer.config
        
        assert "precision" in config
        assert "output_format" in config
        assert "analysis_mode" in config
        assert isinstance(config["precision"], int)

    def test_load_dataset_sample(self):
        """Test loading sample dataset."""
        data = self.analyzer.load_dataset()
        
        assert len(data) > 0
        assert all(isinstance(x, (int, float)) for x in data)

    def test_load_dataset_from_file(self):
        """Test loading dataset from JSON file."""
        # Create temporary JSON file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(self.test_data, f)
            temp_file = f.name
        
        try:
            data = self.analyzer.load_dataset(temp_file)
            assert data == self.test_data
        finally:
            os.unlink(temp_file)

    def test_calculate_basic_stats_normal(self):
        """Test basic statistics calculation with normal data."""
        stats = self.analyzer.calculate_basic_stats(self.test_data)
        
        assert stats["count"] == 5
        assert stats["mean"] == 30.0
        assert stats["median"] == 30.0
        assert stats["min"] == 10.0
        assert stats["max"] == 50.0
        assert "std_dev" in stats
        assert "variance" in stats

    def test_calculate_basic_stats_empty(self):
        """Test basic statistics with empty dataset."""
        stats = self.analyzer.calculate_basic_stats(self.empty_data)
        assert stats == {}

    def test_calculate_basic_stats_single(self):
        """Test basic statistics with single data point."""
        stats = self.analyzer.calculate_basic_stats(self.single_data)
        
        assert stats["count"] == 1
        assert stats["mean"] == 42.0
        assert stats["median"] == 42.0
        assert stats["min"] == 42.0
        assert stats["max"] == 42.0

    def test_calculate_advanced_stats(self):
        """Test advanced statistics calculation."""
        # Use larger dataset for meaningful percentiles
        large_data = list(range(1, 101))  # 1 to 100
        stats = self.analyzer.calculate_advanced_stats(large_data)
        
        assert "p25" in stats
        assert "p50" in stats
        assert "p75" in stats
        assert "iqr" in stats
        assert "outlier_count" in stats
        assert "outlier_percentage" in stats

    def test_calculate_advanced_stats_small_dataset(self):
        """Test advanced statistics with small dataset."""
        stats = self.analyzer.calculate_advanced_stats(self.test_data[:3])
        assert stats == {}  # Should return empty for datasets < 4 items

    def test_precision_configuration(self):
        """Test that precision configuration is respected."""
        config = {"precision": 4}
        analyzer = DataAnalyzer(config)
        
        # Test with data that would have many decimal places
        test_data = [1/3, 2/3, 1.0]
        stats = analyzer.calculate_basic_stats(test_data)
        
        # Check that values are rounded to 4 decimal places
        mean_str = str(stats["mean"])
        decimal_places = len(mean_str.split(".")[-1]) if "." in mean_str else 0
        assert decimal_places <= 4

    def test_analysis_modes(self):
        """Test different analysis modes."""
        # Standard mode
        config = {"analysis_mode": "standard"}
        analyzer = DataAnalyzer(config)
        analyzer.results = {}
        analyzer.load_dataset = lambda x=None: list(range(1, 21))  # Mock data
        
        results = analyzer.analyze()
        
        # Should have basic stats
        assert "mean" in results
        assert "median" in results
        assert "count" in results

    def test_save_results_json(self):
        """Test saving results in JSON format."""
        self.analyzer.results = {"test": 123.45, "count": 10}
        self.analyzer.save_results()
        
        output_file = Path(self.config["output_dir"]) / "analysis_results.json"
        assert output_file.exists()
        
        with open(output_file, 'r') as f:
            saved_data = json.load(f)
        
        assert saved_data["test"] == 123.45
        assert saved_data["count"] == 10

    def test_save_results_csv(self):
        """Test saving results in CSV format."""
        config = self.config.copy()
        config["output_format"] = "csv"
        analyzer = DataAnalyzer(config)
        analyzer.results = {"mean": 25.0, "count": 5}
        analyzer.save_results()
        
        output_file = Path(config["output_dir"]) / "analysis_results.csv"
        assert output_file.exists()
        
        with open(output_file, 'r') as f:
            content = f.read()
        
        assert "metric,value" in content
        assert "mean,25.0" in content
        assert "count,5" in content

    def test_environment_variable_config(self):
        """Test configuration via environment variables."""
        # Set environment variables
        os.environ["PRECISION"] = "3"
        os.environ["ANALYSIS_MODE"] = "advanced"
        os.environ["OUTPUT_FORMAT"] = "csv"
        
        try:
            analyzer = DataAnalyzer()
            config = analyzer.config
            
            assert config["precision"] == 3
            assert config["analysis_mode"] == "advanced"
            assert config["output_format"] == "csv"
        finally:
            # Clean up environment variables
            for var in ["PRECISION", "ANALYSIS_MODE", "OUTPUT_FORMAT"]:
                if var in os.environ:
                    del os.environ[var]

    def test_outlier_detection(self):
        """Test outlier detection in advanced statistics."""
        # Create data with clear outliers
        data_with_outliers = [1, 2, 3, 4, 5, 100, 200]  # 100, 200 are outliers
        stats = self.analyzer.calculate_advanced_stats(data_with_outliers)
        
        assert stats["outlier_count"] >= 1
        assert stats["outlier_percentage"] > 0

    def test_display_results(self, capsys):
        """Test results display functionality."""
        self.analyzer.results = {"mean": 25.5, "count": 10}
        self.analyzer.display_results()
        
        captured = capsys.readouterr()
        assert "Analysis Results:" in captured.out
        assert "Mean" in captured.out
        assert "25.50" in captured.out


class TestDataAnalyzerIntegration:
    """Integration tests for complete workflows."""

    def test_complete_analysis_workflow(self):
        """Test complete analysis from start to finish."""
        config = {
            "precision": 2,
            "output_format": "json",
            "analysis_mode": "detailed",
            "output_dir": "./integration_test_output"
        }
        
        analyzer = DataAnalyzer(config)
        
        # Mock the load_dataset to return known data
        test_data = list(range(1, 51))  # 1 to 50
        analyzer.load_dataset = lambda x=None: test_data
        
        try:
            results = analyzer.analyze()
            
            # Verify results
            assert results["count"] == 50
            assert results["mean"] == 25.5
            assert results["min"] == 1
            assert results["max"] == 50
            
            # Verify output file was created
            output_file = Path(config["output_dir"]) / "analysis_results.json"
            assert output_file.exists()
            
        finally:
            # Clean up
            output_dir = Path(config["output_dir"])
            if output_dir.exists():
                for file in output_dir.glob("*"):
                    file.unlink()
                output_dir.rmdir()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
