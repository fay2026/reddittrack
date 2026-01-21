# 🚀 Push to GitHub Guide

Your GitHub repository: https://github.com/fay2026/reddittrack

## 🔒 Security First!

Before pushing, let's make sure your credentials are safe:

### ✅ Your .gitignore is configured correctly:
- `.env` file will NOT be pushed ✅
- `data/` folder will NOT be pushed ✅
- `reports/` folder will NOT be pushed ✅
- `logs/` folder will NOT be pushed ✅

**Your secret credentials are safe!** 🛡️

## 🚀 Two Ways to Push

### Option 1: Use the Automated Script (Easiest)

Open Terminal and run:

```bash
cd "/Users/zhangfan/Desktop/reddit track"
chmod +x push_to_github.sh
./push_to_github.sh
```

The script will:
1. Initialize Git
2. Add your GitHub remote
3. Show you what will be committed
4. Ask for confirmation
5. Push everything to GitHub

### Option 2: Manual Commands

If you prefer to do it manually:

```bash
cd "/Users/zhangfan/Desktop/reddit track"

# Initialize git
git init

# Add your GitHub repository
git remote add origin https://github.com/fay2026/reddittrack.git

# Stage all files
git add .

# Check what will be committed (make sure .env is NOT listed)
git status

# Create initial commit
git commit -m "Initial commit: Reddit Tracker"

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

## 📋 What Will Be Pushed

### ✅ Files that WILL be pushed:
- All Python scripts (`.py` files)
- Documentation (`.md` files)
- Shell scripts (`.sh` files)
- `requirements.txt`
- `.gitignore`
- Configuration templates

### ❌ Files that will NOT be pushed:
- `.env` (your credentials) 🔒
- `data/` (collected posts)
- `reports/` (generated HTML reports)
- `logs/` (log files)
- `__pycache__/` (Python cache)

## 🔐 Double-Check Security

Before pushing, verify .env won't be committed:

```bash
cd "/Users/zhangfan/Desktop/reddit track"
git add .
git status
```

If you see `.env` in the list, **STOP** and run:
```bash
git rm --cached .env
```

## 📝 After Pushing

Once pushed, your repository will contain:
- Complete source code
- Full documentation
- Setup instructions
- Human-like behavior features
- Scheduling scripts

Others can clone it and use it with their own Reddit credentials!

## 🌟 Making Your README Stand Out

Your `README.md` is already comprehensive. After pushing, GitHub will display it automatically on your repository page.

## 🔄 Future Updates

To push future changes:

```bash
cd "/Users/zhangfan/Desktop/reddit track"
git add .
git commit -m "Description of your changes"
git push
```

## ⚠️ Important Reminders

1. **NEVER** commit your `.env` file
2. **NEVER** commit your `data/` or `reports/` folders
3. Always check `git status` before committing
4. Your `.gitignore` protects you, but always double-check

## 🆘 Troubleshooting

### "Permission denied (publickey)"

You need to authenticate with GitHub. Options:
1. Use HTTPS (will ask for username/password)
2. Set up SSH keys (more secure)

For HTTPS, the script already uses:
```
https://github.com/fay2026/reddittrack.git
```

### "Repository already exists"

If you've already pushed before:
```bash
git remote set-url origin https://github.com/fay2026/reddittrack.git
git push -f origin main
```

### Need to configure Git username?

```bash
git config --global user.name "Your Name"
git config --global user.email "fay@intallaga.com"
```

---

**Ready to push? Run the script or use manual commands above!** 🚀
