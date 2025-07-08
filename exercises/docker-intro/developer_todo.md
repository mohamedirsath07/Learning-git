# Docker & Containers: Hands-On Exercise

## Context

Now that you understand container concepts, it's time to get hands-on experience. You'll containerize the data analysis tool from previous exercises, learning practical Docker skills that complement your Git workflow.

## Your Mission

1. **Create a Dockerfile** for the data analysis application
2. **Build and run containers** locally
3. **Use Docker with Git** to ensure consistent environments
4. **Practice container best practices** for development workflows
5. **Integrate containers** with version control

## Required Docker Commands

You'll practice these essential Docker operations:

```bash
docker build -t <name> .        # Build image from Dockerfile
docker run <image>              # Run container from image
docker run -it <image> bash     # Interactive container with shell
docker ps                       # List running containers
docker images                   # List available images
docker exec -it <container> cmd # Execute command in running container
docker logs <container>         # View container logs
docker stop <container>         # Stop running container
docker rm <container>           # Remove stopped container
docker rmi <image>             # Remove image
```

## Step-by-Step Instructions

### 1. Examine the Project Structure

```bash
cd exercises/docker-intro/project
ls -la
cat requirements.txt
cat data_analyzer.py
```

You have a complete data analysis application ready for containerization.

### 2. Create a Dockerfile

Create a `Dockerfile` with these requirements:

- Use Python 3.9 slim base image
- Install system dependencies if needed
- Copy requirements and install Python packages
- Copy application code
- Set working directory
- Define default command

**Dockerfile Template:**
```dockerfile
# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Expose port if needed (for future web interface)
EXPOSE 8000

# Define default command
CMD ["python", "data_analyzer.py"]
```

### 3. Create .dockerignore

Create a `.dockerignore` file to exclude unnecessary files:

```
.git
.gitignore
README.md
Dockerfile
.dockerignore
__pycache__
*.pyc
.pytest_cache
.coverage
.env
```

### 4. Build Your First Container

```bash
docker build -t data-analyzer .
docker images
```

Check that your image was created successfully.

### 5. Run the Container

```bash
# Run container and see output
docker run data-analyzer

# Run interactively to explore
docker run -it data-analyzer bash
```

In the interactive session, explore the container environment:
```bash
pwd
ls -la
python --version
pip list
```

### 6. Test Different Run Modes

#### Mount Local Code for Development

```bash
# Mount current directory to container
docker run -v $(pwd):/app data-analyzer

# Interactive development mode
docker run -it -v $(pwd):/app data-analyzer bash
```

This allows you to edit code locally while running in the container.

#### Pass Environment Variables

```bash
# Run with custom configuration
docker run -e ANALYSIS_MODE=detailed data-analyzer

# Run with multiple environment variables
docker run -e PRECISION=4 -e OUTPUT_FORMAT=csv data-analyzer
```

### 7. Version Your Container Images

```bash
# Build with version tags
docker build -t data-analyzer:v1.0 .
docker build -t data-analyzer:latest .

# List all versions
docker images data-analyzer
```

### 8. Create docker-compose.yml

For more complex setups, create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  analyzer:
    build: .
    container_name: data-analyzer
    environment:
      - ANALYSIS_MODE=interactive
      - PRECISION=3
    volumes:
      - .:/app
      - ./data:/app/data
      - ./output:/app/output
    working_dir: /app
    
  # Future: Add database service
  # database:
  #   image: postgres:13
  #   environment:
  #     POSTGRES_DB: analytics
```

Test with docker-compose:
```bash
docker-compose up --build
```

### 9. Git Integration

#### Commit Your Container Configuration

```bash
git add Dockerfile .dockerignore docker-compose.yml
git commit -m "Add Docker containerization

- Create Dockerfile with Python 3.9 slim base
- Add .dockerignore for clean builds
- Include docker-compose.yml for development
- Enable consistent development environment across team"
```

#### Create Development Scripts

Create `scripts/dev-setup.sh`:
```bash
#!/bin/bash
# Development environment setup script

echo "Setting up development environment with Docker..."

# Build development image
docker build -t data-analyzer:dev .

# Run interactive development container
docker run -it \
  -v $(pwd):/app \
  -e PYTHONPATH=/app \
  data-analyzer:dev bash

echo "Development environment ready!"
```

Make it executable and commit:
```bash
chmod +x scripts/dev-setup.sh
git add scripts/
git commit -m "Add development setup script with Docker"
```

## Expected Outcomes

### Container Skills

After completing this exercise:

- ✅ You can write effective Dockerfiles
- ✅ You understand Docker layer caching and optimization
- ✅ You can run containers in different modes (interactive, detached, with volumes)
- ✅ You can integrate Docker with Git for consistent development environments

### Development Workflow

Your new workflow combines Git and Docker:

```text
1. git clone <repo>
2. docker build -t <app> .
3. docker run -v $(pwd):/app <app>
4. # Edit code locally, run in container
5. git add . && git commit -m "feature"
6. git push origin feature
```

### Skills Practiced

- Writing production-ready Dockerfiles
- Using .dockerignore for efficient builds
- Container security with non-root users
- Volume mounting for development
- Environment variable configuration
- Integration with docker-compose
- Version tagging for container images

## Best Practices Applied

### Security
- Use non-root user in container
- Use official base images
- Don't include sensitive data in images
- Scan images for vulnerabilities

### Efficiency
- Leverage Docker layer caching
- Use .dockerignore to reduce context size
- Multi-stage builds for production
- Minimize image size with slim base images

### Development Experience
- Mount code volumes for live editing
- Use environment variables for configuration
- Provide development scripts for team onboarding
- Document container usage in README

## Troubleshooting

**If build fails with permission errors:**
```bash
# Check file permissions
ls -la
# Make sure Dockerfile is readable
chmod 644 Dockerfile
```

**If container exits immediately:**
```bash
# Check logs
docker logs <container-name>
# Run interactively to debug
docker run -it <image> bash
```

**If code changes don't appear in container:**
```bash
# Rebuild the image
docker build -t <image> .
# Or use volume mount for live editing
docker run -v $(pwd):/app <image>
```

## Next Steps

Once you've successfully completed this exercise:

1. You can containerize any Python application
2. You understand how containers improve development consistency
3. You're ready for Exercise: GitHub Actions with containerized testing

The container skills you've learned provide a foundation for modern DevOps practices and ensure your applications run consistently across all environments.
