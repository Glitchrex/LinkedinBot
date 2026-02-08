# GitHub Push Guide for LinkedIn Bot

## Step 1: Create a GitHub Repository

1. Go to https://github.com/new
2. Create a new repository:
   - Name: `linkedin-bot` (or your preferred name)
   - Description: "Semi-automatic LinkedIn posting bot with AI-powered post generation"
   - Choose: **Public** (for open source)
   - Click "Create repository"

3. Copy the repository URL (e.g., `https://github.com/yourusername/linkedin-bot.git`)

---

## Step 2: Initialize Git in Your Project

Open terminal in your project directory and run:

```bash
# Navigate to project
cd d:\Projects\LinkedinBot

# Initialize git (if not already done)
git init

# Add all files
git add .

# Check status (optional but recommended)
git status
```

---

## Step 3: Configure Git (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@github.com"
```

---

## Step 4: Create Initial Commit

```bash
git commit -m "Initial commit: LinkedIn bot with AI post generation and Playwright automation"
```

---

## Step 5: Connect to Remote Repository

Replace `YOUR_USERNAME` and `REPO_NAME` with your GitHub details:

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

For example:
```bash
git remote add origin https://github.com/diptangshu/linkedin-bot.git
```

---

## Step 6: Push to GitHub

```bash
# Push to main branch (create it if needed)
git branch -M main
git push -u origin main
```

If you get authentication errors on Windows:
- GitHub requires **Personal Access Token (PAT)** for HTTPS
- Or use SSH (recommended)

### Option A: Use SSH (Recommended)

1. Generate SSH key:
   ```bash
   ssh-keygen -t ed25519 -C "your.email@github.com"
   ```
   - Press Enter to accept default location
   - Enter a passphrase (or leave blank)

2. Add SSH key to GitHub:
   - Copy key: `cat ~/.ssh/id_ed25519.pub | clip` (Windows) or `pbcopy` (Mac)
   - Go to https://github.com/settings/ssh/new
   - Paste the key

3. Update remote to SSH:
   ```bash
   git remote set-url origin git@github.com:YOUR_USERNAME/REPO_NAME.git
   ```

4. Push:
   ```bash
   git push -u origin main
   ```

### Option B: Use GitHub CLI (Easier)

```bash
# Install: https://cli.github.com/
# Then:
gh auth login
# Follow prompts, choose SSH or HTTPS

git push -u origin main
```

---

## Step 7: Verify Online

1. Go to `https://github.com/YOUR_USERNAME/REPO_NAME`
2. You should see all your files and a beautiful README

---

## Step 8: Add GitHub Workflows (Optional but Recommended)

Create `.github/workflows/lint.yml` for automatic code quality checks:

```bash
mkdir -p .github/workflows
```

See `.github/workflows/` directory for example workflow files.

---

## Step 9: Make it Discoverable

1. Add **topics** to your repo:
   - Go to repo → Settings → Topics
   - Add: `linkedin`, `automation`, `bot`, `python`, `playwright`, `openai`, `social-media`

2. Add **badges** to your README:
   - Example: `[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)`

3. Ensure README.md is comprehensive (already done!)

---

## Step 10: Future Updates

To push new changes:

```bash
git add .
git commit -m "Feature: Add scheduling support"
git push
```

---

## Troubleshooting

**Error: "remote origin already exists"**
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

**Error: "fatal: could not read from repository"**
- Check SSH keys are configured
- Or switch to HTTPS with PAT token
- Run: `ssh -T git@github.com` to test SSH connection

**Error: "Permission denied (publickey)"**
- SSH key not configured
- Use GitHub CLI: `gh auth login`
- Or use HTTPS with PAT

---

## Next Steps

1. Monitor Issues and PRs from the community
2. Add GitHub Actions for automated testing
3. Create releases/tags when reaching milestones
4. Document contribution guidelines (see CONTRIBUTING.md if needed)

---

Happy coding! 🚀
