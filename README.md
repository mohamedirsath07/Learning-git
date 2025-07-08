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

### Professional Development Workflows

- **Feature branch development**: Complete professional development cycles
- **Code review processes**: Pull requests and collaboration patterns
- **CI/CD automation**: GitHub Actions for testing and deployment
- **Container deployment**: Docker for consistent environments and production deployment

## How to Use This Repository

### 1. Fork & Clone

#### What is Forking?

**Forking** creates your own copy of this repository on GitHub. Unlike simply downloading the code, a fork:

- **Creates your personal repository** - You'll have `github.com/YOUR_USERNAME/Learning-git`
- **Maintains connection to the original** - You can sync updates if needed
- **Enables independent development** - Make changes without affecting the original
- **Allows contribution back** - Submit pull requests to share improvements

Think of forking as getting your own laboratory to experiment in, while keeping a connection to the original research facility.

#### Why Fork This Learning Repository?

1. **Safe experimentation** - Break things, make mistakes, learn without consequences
2. **Personal progress tracking** - Your commits show your learning journey
3. **Portfolio development** - Your fork becomes a showcase of your Git skills
4. **Professional practice** - Forking mirrors real-world open source workflows

#### Step-by-Step Fork & Clone Process

1. **Fork the repository**:
   - Go to `https://github.com/ORIGINAL_OWNER/Learning-git` (this repository)
   - Click the **"Fork"** button in the top-right corner
   - Choose your GitHub account as the destination
   - GitHub creates `https://github.com/YOUR_USERNAME/Learning-git`

2. **Clone your fork locally**:

   ```bash
   # Replace YOUR_USERNAME with your actual GitHub username
   git clone https://github.com/YOUR_USERNAME/Learning-git.git
   cd Learning-git
   ```

3. **Verify your setup**:

   ```bash
   git remote -v
   # Should show:
   # origin  https://github.com/YOUR_USERNAME/Learning-git.git (fetch)
   # origin  https://github.com/YOUR_USERNAME/Learning-git.git (push)
   
   ls exercises/
   # Should show: 01-basic-commit  02-branching  03-merging  ...
   ```

#### Important: Work in Your Fork

- **All exercises** should be completed in your forked repository
- **All commits** will be saved to your GitHub account
- **All GitHub Actions** (Exercise 6) will run on your repository
- **All Docker deployment** (Exercise 7) will showcase your personal work

Your fork is your learning workspace and eventual portfolio piece!

**Bonus**: Your repository includes a beautiful celebration website (`index.html` and `app.py`) that you'll containerize in the final Docker exercise to celebrate your achievements! 🎉

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
├── 06-github-actions/        # Automate testing for your entire repository
├── 07-docker-deployment/     # Containerize and deploy your complete project
└── concepts/
    ├── docker-fundamentals.md    # Container theory and best practices
    └── cicd-principles.md         # CI/CD concepts and workflows
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
- Automate testing and deployment on your complete repository
- Deploy your learning portfolio as a containerized application

Think of this as your Git apprenticeship—learning through doing, not just reading.

### Final Achievement: Professional Portfolio

By the end, you'll have transformed your learning repository into a deployable web application that showcases all your work through an interactive interface, demonstrating both your Git mastery and modern DevOps skills.

## Getting Help

- Check `resources.md` for detailed external links
- Each `developer_todo.md` includes expected outcomes
- Git stuck? Use `git status` and `git log` to understand your current state
- GitHub stuck? Check your fork's branches and compare with upstream

Ready to level up your Git skills? Start with `exercises/01-basic-commit/developer_todo.md`.
