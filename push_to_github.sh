#!/bin/bash
# Script to push Reddit Tracker to GitHub

echo "🚀 Pushing Reddit Tracker to GitHub..."
echo ""

# Navigate to project directory
cd "/Users/zhangfan/Desktop/reddit track"

# Initialize git repository
echo "📦 Initializing Git repository..."
git init

# Add remote repository
echo "🔗 Adding remote repository..."
git remote add origin https://github.com/fay2026/reddittrack.git

# Check if .env exists and warn user
if [ -f ".env" ]; then
    echo ""
    echo "⚠️  WARNING: .env file detected!"
    echo "   This file contains your secret credentials."
    echo "   It will NOT be pushed (protected by .gitignore)"
    echo ""
fi

# Add all files (except those in .gitignore)
echo "📝 Adding files to git..."
git add .

# Show what will be committed
echo ""
echo "Files to be committed:"
git status --short

echo ""
read -p "Do you want to continue? (y/n) " -n 1 -r
echo

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

# Create initial commit
echo ""
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Reddit Tracker - Automated complaints and demands collector

Features:
- Automated Reddit post collection
- Sentiment analysis and categorization
- Beautiful HTML reports
- Human-like behavior to avoid detection
- Scheduled daily runs
- Priority scoring for posts"

# Set default branch to main
echo "🌿 Setting default branch to main..."
git branch -M main

# Push to GitHub
echo "⬆️  Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Successfully pushed to GitHub!"
echo "🔗 Your repository: https://github.com/fay2026/reddittrack"
echo ""
echo "⚠️  IMPORTANT: Make sure you never commit your .env file!"
echo "   It's protected by .gitignore, but always double-check."
