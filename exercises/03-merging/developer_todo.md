# Exercise 3: Merging and Conflict Resolution

## Context

Your data validation feature is complete and tested. Now it's time to merge it back into the main branch. However, while you were working on validation, another team member made changes to the main branch, creating a merge conflict that you'll need to resolve.

## Your Mission

1. **Prepare for merging** by understanding current branch states
2. **Attempt a merge** and encounter a realistic conflict
3. **Resolve merge conflicts** manually using Git tools
4. **Complete the merge** with a proper merge commit
5. **Clean up branches** after successful integration

## Required Git Commands

You'll master these merging operations:

```bash
git merge <branch>          # Merge branch into current branch
git merge --no-ff <branch>  # Force merge commit even for fast-forward
git status                  # Check merge status and conflicts
git diff                    # See conflict details
git add <file>             # Mark conflicts as resolved
git merge --abort          # Cancel merge in progress
git branch -d <branch>     # Delete merged branch
git log --graph --oneline  # Visualize merge history
```

## Step-by-Step Instructions

### 1. Set Up the Merge Scenario

```bash
cd exercises/03-merging/project
git status
git log --oneline --graph --all
```

You should see two branches with divergent histories:
- `main`: Has updates to the configuration system
- `feature/advanced-stats`: Has new statistical functions

### 2. Examine Both Branches

Switch between branches to see the differences:

```bash
git switch main
cat data_analyzer.py
git switch feature/advanced-stats
cat data_analyzer.py
```

Notice how both branches modified the same file in different ways.

### 3. Attempt the Merge

From the `main` branch, try to merge the feature:

```bash
git switch main
git merge feature/advanced-stats
```

**Expected Result**: Git will report merge conflicts that need manual resolution.

### 4. Understand the Conflict

Examine the conflict:

```bash
git status
cat data_analyzer.py
```

Look for conflict markers:
```
<<<<<<< HEAD
# Code from main branch
=======
# Code from feature branch
>>>>>>> feature/advanced-stats
```

### 5. Resolve the Conflict

Open `data_analyzer.py` in your editor and manually resolve the conflicts by:

1. **Keeping the best parts from both branches**
2. **Ensuring the merged code makes logical sense**
3. **Removing all conflict markers** (`<<<<<<<`, `=======`, `>>>>>>>`)
4. **Testing that the merged code works**

The resolution should:
- Include the configuration updates from `main`
- Include the advanced statistics from `feature/advanced-stats`  
- Maintain compatibility between both features
- Follow consistent code style

### 6. Test the Merged Code

Before completing the merge:

```bash
python data_analyzer.py
```

Ensure the merged code runs without errors and combines both features correctly.

### 7. Complete the Merge

Mark the conflict as resolved and finish the merge:

```bash
git add data_analyzer.py
git status
git commit -m "Merge feature/advanced-stats into main

Resolved conflicts between configuration updates and new statistical functions:
- Integrated advanced statistics (correlation, percentiles) 
- Maintained configuration system updates
- Ensured compatibility between both feature sets
- Updated documentation for combined functionality"
```

### 8. Verify the Merge

Check your commit history:

```bash
git log --oneline --graph
git show HEAD
```

You should see a merge commit that combines both branch histories.

### 9. Clean Up Branches

Remove the merged feature branch:

```bash
git branch -d feature/advanced-stats
git branch
```

## Advanced Merge Scenarios

### Practice Different Merge Types

This exercise includes additional branches to practice with:

#### Fast-Forward Merge

```bash
git switch -c feature/simple-fix
# Make a simple change that doesn't conflict
echo "# Simple documentation update" >> README.md
git add README.md
git commit -m "Update documentation"

git switch main
git merge feature/simple-fix  # Should be fast-forward
git branch -d feature/simple-fix
```

#### No-Fast-Forward Merge

```bash
git switch -c feature/logging
# Add logging functionality
git commit -m "Add logging system"

git switch main
git merge --no-ff feature/logging  # Force merge commit
```

## Expected Outcomes

### Repository State

After completing this exercise:

- ✅ `main` branch contains merged functionality from both branches
- ✅ Merge conflicts have been properly resolved
- ✅ All code runs without errors
- ✅ Feature branch has been cleaned up
- ✅ Commit history shows clear merge structure

### Merge History Visualization

```
main    A---B---C-------F
             \         /
feature       D---E---
```

Where:
- A, B, C: Original commits on main
- D, E: Feature development commits  
- F: Merge commit combining both histories

### Skills Practiced

- Identifying merge conflicts with `git status`
- Understanding conflict markers and resolution strategies
- Manual conflict resolution in code editors
- Completing merges with `git commit`
- Visualizing merge history with `git log --graph`
- Branch cleanup with `git branch -d`

## Conflict Resolution Strategies

### When Conflicts Occur

1. **Don't Panic**: Conflicts are normal in collaborative development
2. **Understand Context**: Look at what each branch was trying to accomplish
3. **Communicate**: In real projects, discuss complex conflicts with team members
4. **Test Thoroughly**: Always test merged code before completing the merge

### Resolution Approaches

- **Keep Both Changes**: Integrate functionality from both branches
- **Choose One Side**: Sometimes one approach is clearly better
- **Create New Solution**: Occasionally, a third approach works best
- **Refactor**: Use conflicts as opportunities to improve code structure

## Troubleshooting

**If you make a mistake during conflict resolution:**
```bash
git merge --abort  # Start over
```

**If the merged code doesn't work:**
```bash
git reset --hard HEAD~1  # Undo merge (use carefully)
```

**If you accidentally delete content:**
```bash
git show HEAD:filename  # See file content from specific commit
```

## Next Steps

Once you've successfully completed this exercise:

1. You understand how to handle merge conflicts in real scenarios
2. You can choose appropriate merge strategies for different situations
3. You're ready for Exercise 4: Remote collaboration workflows

The conflict resolution skills you've developed here are essential for team collaboration and will serve you throughout your development career.
