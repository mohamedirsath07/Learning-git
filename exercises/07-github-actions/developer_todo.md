# Exercise 6: GitHub Actions - Your First Automation

## Context

You've mastered Git basics! Now let's add some automation magic. GitHub Actions will automatically run checks whenever you push code to your repository.

## Your Mission

Create a simple GitHub Actions workflow that:
1. **Runs automatically** when you push code
2. **Tests your Python files** to make sure they work
3. **Shows you're learning automation** like a pro!

## What You'll Build

A basic workflow that says "Hello!" and checks your Python code works.

## Step-by-Step Instructions

### 1. Create the Workflow Directory

In your repository root, create the GitHub Actions folder:

```bash
mkdir -p .github/workflows
```

### 2. Create Your First Workflow

Create `.github/workflows/hello.yml`:

```yaml
name: Hello Learning Git!

# Run this workflow when you push to main branch
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  say-hello:
    runs-on: ubuntu-latest
    
    steps:
    - name: Check out your code
      uses: actions/checkout@v4
    
    - name: Say hello
      run: |
        echo "🎉 Hello from GitHub Actions!"
        echo "🚀 Your automation is working!"
        echo "📚 You're learning Git like a champion!"
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Test your Python files
      run: |
        echo "Testing your Python projects..."
        find exercises/ -name "*.py" -exec python -m py_compile {} \;
        echo "✅ All Python files are valid!"
```

### 3. Commit and Push

```bash
git add .github/workflows/hello.yml
git commit -m "Add GitHub Actions workflow"
git push origin main
```

### 4. Watch the Magic Happen

1. Go to your GitHub repository
2. Click the **"Actions"** tab
3. Watch your workflow run!
4. See the green checkmark when it succeeds

## What Just Happened?

🎯 **You created automation!** Every time you push code, GitHub will:
- Check out your code
- Say hello to you
- Test that your Python files work
- Give you a green checkmark of success

## Expected Outcome

- ✅ Green checkmark in your repository's Actions tab
- ✅ Automated testing every time you push
- ✅ You've learned the basics of CI/CD!

## Troubleshooting

**Workflow failed?** 
- Check the Actions tab for error messages
- Make sure your `.yml` file is properly indented
- Python errors? Check your Python file syntax

**Can't see Actions tab?**
- Make sure you pushed to your forked repository
- The workflow only runs after you push the `.github/workflows/hello.yml` file

## Next Steps

Ready for Exercise 7? Time to learn Docker and create something awesome! 🐳
