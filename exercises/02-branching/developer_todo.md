# Exercise 2: Branching Workflow

## Context

Your team uses feature branches for all new development. You've been assigned to add a data validation module to the CLI tool. This feature needs to be developed in isolation before merging back to the main branch, following standard Git branching practices.

## Your Mission

1. **Create a feature branch** for the validation module
2. **Switch between branches** and understand branch isolation
3. **Implement data validation functionality** across multiple files
4. **Use Git commands to track branch changes** and differences

## Required Git Commands

You'll master these branching operations:

```bash
git branch                    # List all branches
git branch <name>            # Create new branch
git switch <branch>          # Switch to branch (modern)
git checkout <branch>        # Switch to branch (traditional)
git switch -c <branch>       # Create and switch in one command
git log --oneline --graph    # Visualize branch history
git diff <branch1>..<branch2> # Compare branches
```

## Step-by-Step Instructions

### 1. Start from a Clean State

```bash
cd exercises/02-branching/project
git status
git log --oneline
```

### 2. Create and Switch to Feature Branch

Create a branch for the validation feature:

```bash
git branch feature/data-validation
git branch
git switch feature/data-validation
git branch
```

Notice how the `*` indicates your current branch.

### 3. Examine the Project Structure

Look at the existing codebase:

```bash
ls -la
cat data_processor.py
cat validator.py
```

The `validator.py` file has placeholder functions that need implementation.

### 4. Implement Data Validation

Edit `validator.py` to implement these functions:

- `validate_numeric_data()`: Check if data contains only numbers
- `validate_data_range()`: Ensure values are within acceptable bounds
- `clean_dataset()`: Remove invalid entries and handle edge cases

The implementation should handle common data quality issues like:
- Non-numeric values
- Outliers beyond reasonable ranges
- Empty or None values
- Duplicate entries

### 5. Update the Main Processor

Edit `data_processor.py` to integrate the validation module:

- Import the validator functions
- Add validation calls before statistical calculations
- Handle validation errors gracefully

### 6. Test Your Changes

```bash
python data_processor.py
```

Test with various inputs to ensure validation works correctly.

### 7. Stage and Commit Your Changes

```bash
git status
git add validator.py data_processor.py
git commit -m "Implement data validation module

- Add numeric data validation functions
- Include range checking and outlier detection
- Integrate validation into main data processing pipeline
- Handle edge cases and error conditions gracefully"
```

### 8. Compare Branches

Switch back to main and compare:

```bash
git switch main
cat validator.py    # Should show the original placeholder
git switch feature/data-validation
cat validator.py    # Should show your implementation

git diff main..feature/data-validation
git log --oneline --graph main feature/data-validation
```

### 9. Work with Multiple Commits

Make an additional improvement on your feature branch:

```bash
# Still on feature/data-validation
# Add a configuration file for validation settings
```

Create `validation_config.py` with customizable validation parameters, then commit this addition.

## Expected Outcomes

### Local Repository State

After completing this exercise:

- ✅ You should have a `main` branch with the original code
- ✅ You should have a `feature/data-validation` branch with new functionality
- ✅ Both branches should have different commit histories
- ✅ You should understand how branches isolate changes

### Branch Structure

```
main                    A---B
                         \
feature/data-validation   C---D
```

Where:
- A, B: Original commits on main
- C: Your validation implementation commit
- D: Your configuration addition commit

### Skills Practiced

- Creating branches with `git branch`
- Switching branches with `git switch`
- Understanding branch isolation
- Comparing branches with `git diff`
- Visualizing branch history with `git log --graph`
- Working with multiple commits on a branch

## Files You'll Modify

1. **`validator.py`**: Implement the validation functions
2. **`data_processor.py`**: Integrate validation into the main workflow
3. **`validation_config.py`**: Create configuration for validation parameters

## Troubleshooting

**If you're on the wrong branch:**
- Use `git branch` to see where you are
- Use `git switch <branch-name>` to move to the correct branch

**If you commit to the wrong branch:**
- Note the commit hash with `git log --oneline`
- Switch to the correct branch
- Use `git cherry-pick <commit-hash>` to copy the commit

**If you lose track of changes:**
- Use `git diff` to see current changes
- Use `git log --oneline --graph --all` to see all branch histories

## Next Steps

Once you've successfully completed this exercise:

1. You'll have a working feature branch with data validation
2. You'll understand how Git isolates changes between branches
3. You'll be ready for Exercise 3: Merging branches back together

The branching workflow you've learned here is fundamental to collaborative development and feature management in professional Git workflows.
