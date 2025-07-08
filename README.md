# Learning Git & GitHub Through Practice

A hands-on repository for software engineering and machine learning students to master Git, GitHub, and DevOps fundamentals through realistic mini-projects.

## What This Repo Is

This isn't another Git tutorial with toy examples. Instead, you'll work with real project scenarios—building CLI tools, processing datasets, managing configurations, and automating workflows. Each exercise simulates common development tasks where Git becomes essential for collaboration and version control.

## What You'll Learn

### Git Fundamentals

- **Repository Management**: `git status`, `git add`, `git commit`
- **Branching & Navigation**: `git switch`, `git branch`, `git checkout`
- **History & Inspection**: `git log`, `git diff`, `git show`
- **Remote Operations**: `git push`, `git pull`, `git fetch`
- **Collaboration**: `git merge`, `git rebase`, merging conflicts
- **Recovery**: `git revert`, `git reset`, undoing changes

### DevOps Essentials

- **Containerization**: Docker concepts, container workflows
- **CI/CD**: GitHub Actions for automated testing and deployment
- **Collaboration**: Pull requests, code reviews, issue tracking

## How to Use This Repository

### 1. Fork & Clone

```bash
# Fork this repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/Learning-git.git
cd Learning-git
```

### 2. Work Through Exercises

Each exercise in `/exercises/` contains:

- `developer_todo.md` - Your mission and required Git operations
- `project/` - Real code to work with
- Clear expected outcomes for local and remote repositories

### 3. Follow the Sequence

Start with `01-basic-commit` and progress through each numbered exercise. Each builds on previous concepts while introducing new Git workflows.

```text
exercises/
├── 01-basic-commit/          # Git basics: status, add, commit
├── 02-branching/             # Creating and switching branches
├── 03-merging/               # Merge workflows and conflicts
├── 04-remote-collaboration/  # Push, pull, fetch operations
├── 05-feature-workflow/      # Complete feature development cycle
├── 06-rebasing/              # Interactive rebase and history cleanup
├── 07-advanced-merging/      # Complex merge scenarios
├── 08-recovery/              # Fixing mistakes with revert and reset
├── docker-intro/             # Container concepts and workflows
└── github-actions/           # Automated testing and CI/CD
```

## External Learning Resources

Master these concepts with top-tier resources:

### Git Mastery

- **[Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)** - Comprehensive guides with visual explanations
- **[Pro Git Book](https://git-scm.com/book)** - The definitive Git reference (free online)
- **[Oh My Git!](https://ohmygit.org/)** - Visual, interactive Git learning game
- **[Learn Git Branching](https://learngitbranching.js.org/)** - Interactive branching visualization

### DevOps & Collaboration

- **[GitHub Docs](https://docs.github.com/)** - Official GitHub guides and references
- **[Docker Documentation](https://docs.docker.com/)** - Container concepts and best practices
- **[GitHub Actions Docs](https://docs.github.com/en/actions)** - Workflow automation and CI/CD

## Repository Philosophy

Every exercise here reflects real development scenarios. You'll:

- Fix bugs in existing codebases
- Add features across multiple files
- Resolve meaningful merge conflicts
- Collaborate on shared repositories
- Automate testing and deployment

Think of this as your Git apprenticeship—learning through doing, not just reading.

## Getting Help

- Check `resources.md` for detailed external links
- Each `developer_todo.md` includes expected outcomes
- Git stuck? Use `git status` and `git log` to understand your current state
- GitHub stuck? Check your fork's branches and compare with upstream

Ready to level up your Git skills? Start with `exercises/01-basic-commit/developer_todo.md`.
