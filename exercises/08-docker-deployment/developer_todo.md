# Exercise 7: Docker - Package Your Success

## Context

Congratulations! You've learned Git and GitHub Actions. Now let's package everything into a container and celebrate your achievements with a fun website!

## Your Mission

Create a Docker container that serves a congratulations website celebrating your Git learning journey!

## What You'll Build

A Docker container that serves the celebration website we've prepared for you! 🎉

## What's Already Prepared

Your repository already contains:
- `index.html` - A beautiful congratulations website with animations
- `app.py` - A simple Python web server

**Your job**: Learn Docker by containerizing this celebration app!

## Step-by-Step Instructions

### 1. Explore the Website Files

Take a look at what's already in your repository:

```bash
ls -la
# You should see: index.html, app.py, and your exercises/ folder
```

Test the website locally (optional):
```bash
python app.py
# Visit http://localhost:8080 to see your celebration page!
# Press Ctrl+C to stop
```

### 2. Create a Dockerfile

Create `Dockerfile` in your repository root:

```dockerfile
# Use Python as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy our website files
COPY index.html .
COPY app.py .

# Expose port 8080
EXPOSE 8080

# Run our web server
CMD ["python", "app.py"]
```

### 3. Build and Run Your Container

```bash
# Build your Docker image
docker build -t git-champion .

# Run your container
docker run -p 8080:8080 git-champion
```

### 4. Celebrate

Open your browser to `http://localhost:8080` and see your celebration website! 🎉

## What You Just Accomplished

🐳 **You containerized an application!** You:

- Learned how Docker works
- Built a Docker image  
- Ran a container
- Served a web application

## Expected Outcome

- ✅ A beautiful congratulations website running in a Docker container
- ✅ Understanding of basic Docker concepts
- ✅ A celebration of your learning journey!

## Troubleshooting

**Docker command not found?**

- Make sure Docker is installed and running

**Can't access localhost:8080?**

- Check if port 8080 is available
- Try `docker run -p 3000:8080 git-champion` and visit `localhost:3000`

**Build failed?**

- Make sure all files (`index.html`, `app.py`, `Dockerfile`) are in your repository root

## 🎊 Final Celebration

You did it! You've learned:

- Git fundamentals
- GitHub collaboration
- GitHub Actions automation  
- Docker containerization

**You're now ready to tackle any development project!**

Keep coding, keep learning, and remember - every expert was once a beginner. You've just taken the first steps on an amazing journey! 🚀✨
