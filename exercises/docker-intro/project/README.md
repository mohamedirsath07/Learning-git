# Data Analyzer - Container Edition

## Overview

A containerized data analysis tool that demonstrates Docker best practices and integration with Git workflows.

## Features

- Statistical analysis of numerical datasets
- Configurable via environment variables
- Multiple output formats (JSON, CSV)
- Container-ready with Docker support
- Development and production configurations

## Quick Start

### Using Docker

```bash
# Build the container
docker build -t data-analyzer .

# Run with default settings
docker run data-analyzer

# Run with custom configuration
docker run -e ANALYSIS_MODE=advanced -e PRECISION=4 data-analyzer

# Development mode with volume mounting
docker run -v $(pwd):/app -it data-analyzer bash
```

### Using docker-compose

```bash
# Start the application
docker-compose up --build

# Run in detached mode
docker-compose up -d
```

## Configuration

Configure via environment variables:

- `ANALYSIS_MODE`: `standard`, `detailed`, or `advanced`
- `PRECISION`: Number of decimal places (default: 2)
- `OUTPUT_FORMAT`: `json` or `csv`
- `OUTPUT_DIR`: Output directory path
- `INCLUDE_OUTLIERS`: `true` or `false`

## Development

### Local Development with Docker

```bash
# Build development image
docker build -t data-analyzer:dev .

# Run interactive development environment
docker run -it -v $(pwd):/app data-analyzer:dev bash

# Run with live code reloading
docker run -v $(pwd):/app data-analyzer:dev python data_analyzer.py --mode advanced
```

### Without Docker

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python data_analyzer.py --help
```

## Project Structure

```
project/
├── data_analyzer.py      # Main application
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
├── docker-compose.yml   # Multi-service setup
├── .dockerignore        # Files to exclude from container
└── README.md           # This file
```

## Container Features

- **Base Image**: Python 3.9 slim for efficiency
- **Security**: Runs as non-root user
- **Optimization**: Multi-layer caching for fast builds
- **Development**: Volume mounting for live editing
- **Production**: Minimal attack surface and dependencies
