# Exercise 1: Basic Commit Workflow

## Context

You've just joined a team developing a CLI tool for data analysis. The tool currently has a basic structure, but needs a new feature to calculate statistical summaries. Your task is to implement this feature and commit your changes using proper Git workflow.

## Your Mission

1. **Explore the project structure** using `git status` and `ls` commands
2. **Implement the missing `calculate_stats()` function** in `main.py`
3. **Stage and commit your changes** using Git best practices
4. **Examine your commit history** with `git log`

## Required Git Commands

You'll practice these essential Git operations:

```bash
git status          # Check repository state
git add <file>      # Stage specific changes
git add .           # Stage all changes
git commit -m "message"  # Commit with descriptive message
git log             # View commit history
git log --oneline   # Condensed history view
git diff            # See unstaged changes
git diff --staged   # See staged changes
```

## Step-by-Step Instructions

### 1. Check Current Repository State

```bash
cd exercises/01-basic-commit/project
git status
```

**Expected Output**: You should see untracked files or a clean working directory.

### 2. Examine the Project

Look at the existing code structure:

```bash
ls -la
cat main.py
cat requirements.txt
```

### 3. Implement the Missing Feature

Open `main.py` and implement the `calculate_stats()` function. The function should:

- Calculate mean, median, and standard deviation
- Return results as a formatted dictionary
- Handle edge cases (empty lists, single values)

### 4. Test Your Implementation

```bash
python main.py
```

Ensure the program runs without errors and produces reasonable output.

### 5. Stage Your Changes

First, check what Git sees:

```bash
git status
git diff
```

Then stage your changes:

```bash
git add main.py
git status
```

Notice how the file moves from "Changes not staged" to "Changes to be committed".

### 6. Commit Your Work

Write a clear, descriptive commit message:

```bash
git commit -m "Implement statistical calculations in calculate_stats function

- Add mean, median, and standard deviation calculations
- Handle edge cases for empty and single-value datasets
- Include proper error handling and return formatting"
```

### 7. Verify Your Commit

Check your commit history:

```bash
git log
git log --oneline
git show HEAD
```

## Expected Outcomes

### Local Repository State

After completing this exercise:

- ✅ Your working directory should be clean (`git status` shows no changes)
- ✅ You should have at least one commit in your history
- ✅ The `calculate_stats()` function should be fully implemented
- ✅ The program should run successfully

### Skills Practiced

- Repository state inspection with `git status`
- Staging changes with `git add`
- Creating meaningful commits with `git commit`
- Reviewing history with `git log`
- Understanding the difference between working directory, staging area, and repository

## Troubleshooting

**If `git status` shows unexpected files:**
- Check your `.gitignore` file
- Use `git add <specific-file>` instead of `git add .`

**If your commit message is unclear:**
- Use `git commit --amend` to fix the last commit message
- Follow the format: brief summary, blank line, detailed description

**If you make a mistake:**
- Use `git diff` to see what changed
- Use `git checkout -- <file>` to discard unstaged changes
- Use `git reset HEAD <file>` to unstage changes

## Next Steps

Once you've successfully completed this exercise:

1. Your `main.py` should have a working `calculate_stats()` function
2. You should understand the basic Git workflow: modify → stage → commit
3. You're ready for Exercise 2: Branching workflows

The foundation you've built here—understanding Git's three-stage workflow—is crucial for all advanced Git operations.
