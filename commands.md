# Git Cheatsheet

## One-time setup

```bash
# Clone YOUR fork (not the professor’s directly)
git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
cd REPO-NAME

# Add professor’s repo as upstream (only once)
git remote add upstream https://github.com/PROFESSOR-USERNAME/REPO-NAME.git

# Create branch for your solutions
git checkout -b my-work

# Push branch to your fork
git push -u origin my-work
```

---

## Weekly update (get professor’s new material)

```bash
# 1. Switch to main branch (clean copy of professor’s repo)
git checkout main

# 2. Fetch professor’s updates
git pull upstream main

# 3. Push them to your fork (optional, keeps fork up-to-date)
git push origin main

# 4. Switch back to your work branch
git checkout my-work

# 5. Merge new exercises into your work branch
git merge main
```

> If you prefer a cleaner history: replace `git merge main` with `git rebase main`

---

## Daily workflow (working on exercises)

```bash
# Stage all changes
git add .

# Commit with message
git commit -m "Solved exercise 3.2"

# Push to your fork
git push
```

---

## Useful commands

```bash
# Show current remotes (origin = your fork, upstream = professor’s repo)
git remote -v

# Show branches
git branch

# Show commit history
git log --oneline --graph --all

# Check status of your files
git status

# Undo last commit (keep changes staged)
git reset --soft HEAD~1

# Undo last commit (discard changes completely!)
git reset --hard HEAD~1
```