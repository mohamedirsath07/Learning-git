# Exercise: GitHub Actions CI/CD

## Context

Your team wants to automate testing and deployment for the data analysis tool. You'll set up GitHub Actions workflows to automatically test your code when changes are pushed, ensuring quality and catching issues early in the development process.

## Your Mission

1. **Create automated testing workflows** that run on every push and pull request
2. **Set up container-based testing** using Docker for consistency
3. **Implement quality gates** that prevent broken code from being merged
4. **Practice workflow debugging** and optimization
5. **Understand CI/CD principles** through hands-on implementation

## Required Knowledge

You'll work with these GitHub Actions concepts:

```yaml
# Workflow triggers
on: [push, pull_request]

# Job definitions
jobs:
  test:
    runs-on: ubuntu-latest
    
# Action steps
steps:
  - uses: actions/checkout@v3
  - uses: actions/setup-python@v4
  - run: python -m pytest
```

## Step-by-Step Instructions

### 1. Examine the Project Structure

```bash
cd exercises/github-actions/project
ls -la
cat test_data_analyzer.py
cat data_analyzer.py
```

You have a complete application with tests ready for automation.

### 2. Create Your First Workflow

Create `.github/workflows/ci.yml`:

```yaml
name: Continuous Integration

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, "3.10"]
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    
    - name: Run tests
      run: |
        pytest test_data_analyzer.py -v --cov=data_analyzer
    
    - name: Run application smoke test
      run: |
        python data_analyzer.py --create-sample
        python data_analyzer.py --data data/sample_dataset.json --mode standard
```

### 3. Create Container-Based Testing

Create `.github/workflows/docker-test.yml`:

```yaml
name: Docker Testing

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  docker-test:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Build Docker image
      run: |
        docker build -t data-analyzer:test .
    
    - name: Test in container
      run: |
        docker run --rm data-analyzer:test python -m pytest test_data_analyzer.py -v
    
    - name: Run application in container
      run: |
        docker run --rm -e ANALYSIS_MODE=advanced data-analyzer:test
    
    - name: Check image size
      run: |
        docker images data-analyzer:test
        echo "Image size should be under 200MB for efficiency"
```

### 4. Add Code Quality Checks

Create `.github/workflows/quality.yml`:

```yaml
name: Code Quality

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.9
    
    - name: Install linting tools
      run: |
        pip install flake8 black isort mypy
    
    - name: Check code formatting with Black
      run: |
        black --check --diff data_analyzer.py test_data_analyzer.py
    
    - name: Check import sorting
      run: |
        isort --check-only --diff data_analyzer.py test_data_analyzer.py
    
    - name: Lint with flake8
      run: |
        flake8 data_analyzer.py test_data_analyzer.py --max-line-length=88
    
    - name: Type checking with mypy
      run: |
        mypy data_analyzer.py --ignore-missing-imports
```

### 5. Create Conditional Deployment

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    branches: [ main ]
    tags: [ 'v*' ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    needs: [test, docker-test, lint]  # Only deploy if all tests pass
    if: github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/tags/v')
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Build and tag Docker image
      run: |
        docker build -t data-analyzer:${{ github.sha }} .
        docker tag data-analyzer:${{ github.sha }} data-analyzer:latest
    
    - name: Log in to Container Registry
      run: |
        echo "Would log in to container registry here"
        echo "docker login ghcr.io -u ${{ github.actor }} -p ${{ secrets.GITHUB_TOKEN }}"
    
    - name: Push to registry
      run: |
        echo "Would push to registry here"
        echo "docker push data-analyzer:${{ github.sha }}"
        echo "docker push data-analyzer:latest"
    
    - name: Create deployment artifact
      run: |
        mkdir -p artifacts
        echo "data-analyzer:${{ github.sha }}" > artifacts/image-tag.txt
        echo "Deployed at $(date)" >> artifacts/deployment-log.txt
    
    - name: Upload deployment artifacts
      uses: actions/upload-artifact@v3
      with:
        name: deployment-info
        path: artifacts/
```

### 6. Test Your Workflows

#### Local Testing (Act)

If you have `act` installed, test workflows locally:

```bash
# Install act (GitHub Actions runner)
# brew install act  # macOS
# OR follow instructions at https://github.com/nektos/act

# Test the CI workflow
act push

# Test specific job
act -j test
```

#### Push and Monitor

```bash
# Commit your workflow files
git add .github/
git commit -m "Add GitHub Actions CI/CD workflows

- Create comprehensive testing pipeline
- Add Docker-based testing for consistency  
- Include code quality checks (linting, formatting)
- Set up conditional deployment workflow
- Enable matrix testing across Python versions"

# Push to trigger workflows
git push origin main
```

### 7. Monitor Workflow Execution

1. **Go to your GitHub repository**
2. **Click the "Actions" tab**
3. **Watch your workflows run**
4. **Examine logs for any failures**
5. **Debug and fix issues**

### 8. Create Workflow Status Badges

Add badges to your README.md:

```markdown
# Data Analyzer

[![CI](https://github.com/yourusername/Learning-git/workflows/Continuous%20Integration/badge.svg)](https://github.com/yourusername/Learning-git/actions)
[![Docker](https://github.com/yourusername/Learning-git/workflows/Docker%20Testing/badge.svg)](https://github.com/yourusername/Learning-git/actions)
[![Quality](https://github.com/yourusername/Learning-git/workflows/Code%20Quality/badge.svg)](https://github.com/yourusername/Learning-git/actions)

A data analysis tool with automated testing and deployment.
```

## Advanced Workflow Features

### Environment-Specific Workflows

```yaml
# .github/workflows/staging.yml
name: Staging Deployment

on:
  push:
    branches: [ develop ]

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Deploy to staging environment
        run: echo "Deploying to staging..."
```

### Secrets and Variables

Use repository secrets for sensitive data:

```yaml
- name: Deploy with secrets
  env:
    API_KEY: ${{ secrets.API_KEY }}
    DATABASE_URL: ${{ secrets.DATABASE_URL }}
  run: |
    echo "Deploying with secure configuration"
```

### Workflow Dependencies

```yaml
jobs:
  test:
    # Test job definition
    
  security-scan:
    needs: test
    # Only runs if test succeeds
    
  deploy:
    needs: [test, security-scan]
    # Only runs if both previous jobs succeed
```

## Expected Outcomes

### Automated Quality Gates

After completing this exercise:

- ✅ All code changes are automatically tested
- ✅ Multiple Python versions are tested via matrix strategy
- ✅ Container builds are validated on every change
- ✅ Code quality is enforced through automated checks
- ✅ Deployments only happen when all tests pass

### CI/CD Pipeline

```text
Code Push → Tests → Quality Checks → Build Container → Deploy
     ↓         ↓           ↓              ↓           ↓
   Trigger   Pass/Fail   Pass/Fail   Pass/Fail   Success
```

### Skills Practiced

- Writing GitHub Actions workflows
- Matrix testing across multiple environments
- Container-based CI/CD
- Conditional deployment logic
- Workflow status monitoring and debugging
- Integration with Git branching strategies

## Troubleshooting

**If workflows fail to trigger:**
- Check workflow file syntax with YAML validator
- Ensure files are in `.github/workflows/` directory
- Verify branch names match trigger conditions

**If tests fail in CI but pass locally:**
- Check for environment differences
- Verify all dependencies are specified
- Use container testing for consistency

**If Docker builds fail:**
- Check Dockerfile syntax
- Verify base image availability
- Review build context and .dockerignore

**If deployment fails:**
- Check job dependencies with `needs:`
- Verify secrets and permissions
- Review conditional logic in `if:` statements

## Security Best Practices

### Secrets Management
- Never commit secrets to repository
- Use GitHub Secrets for sensitive data
- Limit secret access to necessary workflows
- Rotate secrets regularly

### Workflow Security
- Pin action versions to specific commits
- Review third-party actions before use
- Limit workflow permissions with `permissions:`
- Use environments for production deployments

## Next Steps

Once you've successfully completed this exercise:

1. You understand modern CI/CD practices
2. You can automate testing and deployment for any project
3. You've experienced the full Git + GitHub + DevOps workflow

This completes your journey through Git, GitHub, and modern development practices. You now have the skills to contribute confidently to professional software projects!
