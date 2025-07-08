# Exercise 4: Remote Collaboration

## Context

Your team works across multiple locations, collaborating through a shared GitHub repository. You need to learn how to synchronize your work with remote repositories, handle updates from teammates, and contribute your changes back to the shared codebase.

## Your Mission

1. **Set up remote repository connections** and understand remote tracking
2. **Fetch updates** from the remote repository without merging
3. **Pull changes** from teammates and handle integration
4. **Push your contributions** to the shared repository
5. **Work with multiple remotes** (origin and upstream patterns)

## Required Git Commands

You'll master these remote operations:

```bash
git remote                    # List configured remotes
git remote -v                # Show remote URLs
git remote add <name> <url>  # Add new remote
git fetch <remote>           # Download remote changes
git pull <remote> <branch>   # Fetch and merge remote changes
git push <remote> <branch>   # Upload local changes
git push -u <remote> <branch> # Set upstream tracking
git branch -r                # List remote branches
git branch -a                # List all branches (local + remote)
```

## Step-by-Step Instructions

### 1. Understand Current Remote Setup

```bash
cd exercises/04-remote-collaboration/project
git remote -v
git branch -a
git log --oneline --graph --all
```

Examine your current remote configuration and branch structure.

### 2. Check Remote Repository Status

Fetch the latest information from remote:

```bash
git fetch origin
git status
git log --oneline --graph --all
```

This shows you if your local repository is ahead, behind, or diverged from remote.

### 3. Simulate Teammate Updates

Your teammate has pushed changes to the remote repository. Examine what's new:

```bash
git fetch origin
git diff HEAD origin/main
git log HEAD..origin/main --oneline
```

This shows you what changes are waiting to be integrated.

### 4. Handle Different Pull Scenarios

#### Scenario A: Fast-Forward Pull

When you're behind but haven't made local changes:

```bash
git switch main
git status  # Should be clean
git pull origin main
```

#### Scenario B: Merge Pull

When both you and teammates have made changes:

```bash
git switch feature/data-export
# Make some local changes first
echo "# Local changes" >> export_utils.py
git add export_utils.py
git commit -m "Add local export improvements"

# Now pull remote changes that conflict
git pull origin feature/data-export
# Resolve any conflicts that arise
```

### 5. Push Your Contributions

#### Push New Branch

Create and push a new feature branch:

```bash
git switch -c feature/user-interface
# Implement UI improvements in ui_components.py
git add ui_components.py
git commit -m "Add basic user interface components"

git push -u origin feature/user-interface
```

The `-u` flag sets up tracking so future `git push` commands know where to go.

#### Push Updates to Existing Branch

```bash
# Make additional changes
git add .
git commit -m "Enhance UI with input validation"
git push  # No need to specify remote/branch due to tracking
```

### 6. Work with Fork Workflow

Simulate working with a forked repository:

```bash
# Add upstream remote (the original repository you forked)
git remote add upstream https://github.com/original-owner/Learning-git.git
git remote -v

# Fetch updates from upstream
git fetch upstream
git switch main
git pull upstream main

# Push updates to your fork
git push origin main
```

### 7. Handle Push Conflicts

When remote has changes you don't have locally:

```bash
# This will fail if remote is ahead
git push origin main

# Fix by pulling first
git pull origin main
# Resolve any merge conflicts
git push origin main
```

### 8. Examine Remote Tracking

Understand how branches track remotes:

```bash
git branch -vv  # Show tracking information
git remote show origin  # Detailed remote information
```

## Advanced Remote Scenarios

### Multiple Remotes

```bash
# Working with multiple remotes (e.g., fork + upstream)
git remote add upstream https://github.com/upstream/repo.git
git fetch upstream
git checkout -b feature/new-feature upstream/main
git push origin feature/new-feature
```

### Pushing to Different Remotes

```bash
# Push feature to your fork
git push origin feature/awesome-feature

# Later, push to upstream via pull request
# (Done through GitHub interface)
```

## Expected Outcomes

### Remote Configuration

After completing this exercise:

- ✅ You understand the difference between `fetch`, `pull`, and `push`
- ✅ You can work with remote tracking branches
- ✅ You can handle merge conflicts during pulls
- ✅ You understand upstream/origin workflow patterns

### Repository Synchronization

```
Local:     A---B---C---D
                   \
Remote:    A---B---E---F
                   \
Merged:    A---B---C---D---M
                   \     /
                    E---F
```

### Skills Practiced

- Fetching remote updates with `git fetch`
- Integrating changes with `git pull`
- Contributing changes with `git push`
- Setting up branch tracking with `-u` flag
- Working with multiple remotes
- Understanding remote branch relationships

## Files You'll Work With

1. **`ui_components.py`**: Create user interface components
2. **`export_utils.py`**: Enhance data export functionality
3. **`config_manager.py`**: Improve configuration management
4. **`README.md`**: Update project documentation

## Troubleshooting

**If push is rejected:**
```bash
git pull origin <branch>  # Get remote changes first
# Resolve conflicts if any
git push origin <branch>
```

**If you lose track of remotes:**
```bash
git remote -v  # See configured remotes
git branch -r  # See remote branches
```

**If you push to wrong remote:**
```bash
# You can't "undo" a push, but you can push corrections
git push <correct-remote> <branch>
```

**If you have unstaged changes during pull:**
```bash
git stash  # Temporarily save changes
git pull
git stash pop  # Restore changes
```

## Common Remote Workflows

### Feature Branch Workflow

1. `git switch -c feature/new-feature`
2. Make changes and commit
3. `git push -u origin feature/new-feature`
4. Create pull request on GitHub
5. After merge: `git switch main && git pull origin main`

### Fork-based Workflow

1. Fork repository on GitHub
2. `git clone` your fork
3. `git remote add upstream <original-repo>`
4. `git fetch upstream && git pull upstream main`
5. Create feature branch and push to your fork
6. Create pull request to upstream

## Next Steps

Once you've successfully completed this exercise:

1. You understand how Git enables distributed collaboration
2. You can contribute to shared repositories confidently
3. You're ready for Exercise 5: Complete feature development workflow

The remote collaboration skills you've learned are essential for contributing to open source projects and working on distributed teams.
