# Exercise 5: Feature Development Workflow

## Context

You've mastered the basics of Git. Now it's time to put it all together in a complete feature development workflow that mirrors professional software development. You'll work on adding a data export feature using proper Git practices from start to finish.

## Your Mission

1. **Plan and create a feature branch** following naming conventions
2. **Develop incrementally** with meaningful commits
3. **Handle interruptions** with Git stash and branch switching
4. **Collaborate with code review simulation**
5. **Complete the feature** with proper merge and cleanup

## Feature Requirements

You'll implement a **data export system** with these capabilities:

- Export analysis results to multiple formats (JSON, CSV, XML)
- Command-line interface for export options
- Configuration-driven export templates
- Error handling for file operations
- Unit tests for all export functionality

## Step-by-Step Workflow

### 1. Plan Your Feature

```bash
cd exercises/05-feature-workflow/project
git status
git log --oneline
```

Examine the existing codebase and understand what needs to be added.

### 2. Create Feature Branch

Use conventional naming:

```bash
git switch -c feature/data-export-system
git branch
```

### 3. Break Work into Logical Commits

#### Commit 1: Basic Export Infrastructure

Create `export_manager.py` with base classes:

```python
class ExportManager:
    def __init__(self, format_type="json"):
        self.format_type = format_type
    
    def export_data(self, data, filename):
        # Base implementation
        pass
```

```bash
git add export_manager.py
git commit -m "Add basic export manager infrastructure

- Create ExportManager base class
- Define interface for data export functionality
- Set up foundation for multiple export formats"
```

#### Commit 2: JSON Export Implementation

Implement JSON export functionality:

```bash
git add export_manager.py
git commit -m "Implement JSON export functionality

- Add complete JSON export with formatting options
- Include error handling for file operations
- Support custom indentation and encoding"
```

#### Commit 3: CSV Export Implementation

Add CSV export capability:

```bash
git add export_manager.py
git commit -m "Add CSV export with customizable formatting

- Implement CSV export with header options
- Support custom delimiters and quote characters
- Add validation for tabular data structures"
```

### 4. Handle Work Interruption (Stashing)

Simulate urgent bug fix while working:

```bash
# You're halfway through XML export implementation
echo "# Partial XML implementation" >> export_manager.py

# Urgent bug fix needed on main branch
git stash save "WIP: XML export implementation"
git switch main

# Fix urgent issue
echo "# Bug fix applied" >> data_processor.py
git add data_processor.py
git commit -m "Fix critical data loading bug

- Handle empty file gracefully
- Add proper error messages
- Prevent application crash"

# Return to feature work
git switch feature/data-export-system
git stash pop
```

### 5. Complete Feature Implementation

#### Commit 4: XML Export and CLI Integration

```bash
git add export_manager.py main.py
git commit -m "Complete XML export and integrate CLI options

- Finish XML export implementation with proper formatting
- Add command-line arguments for export format selection
- Integrate export manager with main application flow"
```

#### Commit 5: Configuration and Templates

```bash
git add export_config.py templates/
git commit -m "Add export configuration and templates

- Create configurable export templates
- Support user-defined output formatting
- Add template system for consistent exports"
```

#### Commit 6: Tests and Documentation

```bash
git add test_export_manager.py README.md
git commit -m "Add comprehensive tests and documentation

- Create unit tests for all export formats
- Test error handling and edge cases
- Update README with export feature documentation"
```

### 6. Prepare for Code Review

#### Review Your Work

```bash
git log --oneline feature/data-export-system
git diff main..feature/data-export-system
```

#### Create Summary

Document your changes:

```bash
echo "## Feature Summary: Data Export System

### Changes Made:
- Added ExportManager class with support for JSON, CSV, XML
- Integrated command-line export options
- Created configurable export templates
- Added comprehensive test coverage
- Updated documentation

### Files Modified:
- export_manager.py (new)
- export_config.py (new)
- main.py (modified)
- test_export_manager.py (new)
- README.md (updated)

### Testing:
- All existing tests pass
- New export functionality fully tested
- Command-line interface validated" > FEATURE_SUMMARY.md

git add FEATURE_SUMMARY.md
git commit -m "Add feature development summary for review"
```

### 7. Simulate Code Review Process

#### Self-Review Checklist

```bash
# Check code quality
git diff main..feature/data-export-system --name-only | xargs wc -l

# Review commit messages
git log --oneline main..feature/data-export-system

# Test the feature
python main.py --help
python main.py --export-format json
python main.py --export-format csv
```

#### Address Review Feedback (Simulation)

```bash
# Simulate reviewer feedback: "Add error handling for invalid formats"
# Make improvements
git add export_manager.py
git commit -m "Improve error handling for invalid export formats

Addresses review feedback:
- Add validation for supported export formats
- Provide helpful error messages for invalid input
- Add fallback to default format when appropriate"
```

### 8. Merge Feature

#### Update from Main

```bash
git switch main
git pull origin main  # In real workflow
git switch feature/data-export-system
git merge main  # Handle any conflicts
```

#### Merge to Main

```bash
git switch main
git merge --no-ff feature/data-export-system -m "Merge feature/data-export-system

Complete implementation of data export system:
- Multi-format export (JSON, CSV, XML)
- Command-line interface integration
- Configurable export templates
- Comprehensive test coverage
- Full documentation update

Resolves: #123 (hypothetical issue number)"
```

### 9. Clean Up and Tag

```bash
# Delete feature branch
git branch -d feature/data-export-system

# Tag the release
git tag -a v2.0.0 -m "Release v2.0.0: Data Export System

Major new features:
- Multi-format data export
- Enhanced CLI interface
- Configurable templates
- Improved documentation"

# Push everything (in real workflow)
# git push origin main --tags
```

## Expected Outcomes

### Professional Workflow Skills

After completing this exercise:

- ✅ You can plan and execute complex features using Git
- ✅ You understand incremental development with meaningful commits
- ✅ You can handle work interruptions with stashing
- ✅ You know how to prepare code for review
- ✅ You can perform clean merges and proper cleanup

### Git History Structure

```
main    A---B---C-------M---N
             \         /
feature       D---E---F---G---H
```

Where:
- A, B, C: Original commits
- D-H: Feature development commits  
- M: Merge commit
- N: Tag commit

### Skills Practiced

- Feature branch workflow
- Incremental development
- Git stash for work interruption
- Commit message best practices
- Code review preparation
- Merge strategies
- Branch cleanup
- Release tagging

## Best Practices Applied

### Commit Strategy
- **Atomic commits**: Each commit represents one logical change
- **Clear messages**: Descriptive commit messages following conventions
- **Incremental development**: Build feature step by step
- **Test integration**: Include tests with each major component

### Branch Management
- **Descriptive naming**: `feature/data-export-system`
- **Clean history**: Logical progression of changes
- **Proper merging**: Use `--no-ff` for feature integration
- **Cleanup**: Remove merged branches promptly

### Code Review Readiness
- **Self-review**: Check your own work first
- **Documentation**: Update relevant docs and README
- **Testing**: Ensure all tests pass
- **Summary**: Provide clear description of changes

## Troubleshooting

**If merge conflicts occur:**
```bash
git status  # See conflicted files
# Edit files to resolve conflicts
git add resolved_file.py
git commit -m "Resolve merge conflicts"
```

**If you make mistakes in commits:**
```bash
# Fix last commit message
git commit --amend -m "Better commit message"

# Interactive rebase to clean up history
git rebase -i HEAD~3
```

**If you need to reorganize commits:**
```bash
# Use interactive rebase
git rebase -i main
# Then reorder, squash, or edit commits as needed
```

## Next Steps

Once you've successfully completed this exercise:

1. You understand professional feature development workflows
2. You can manage complex Git operations with confidence
3. You're ready for Exercise 6: Advanced Git operations (rebasing)

The workflow you've practiced here is the foundation of collaborative software development and will serve you in any professional development environment.
