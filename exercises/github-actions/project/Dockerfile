FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first for Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Create output directory
RUN mkdir -p /app/output

# Expose port for future web interface
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import data_analyzer; print('healthy')" || exit 1

# Default command
CMD ["python", "data_analyzer.py", "--validate-env"]
