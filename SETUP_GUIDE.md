# 🚀 Setup Guide - Get Your Reddit API Credentials

## Step-by-Step Instructions

### 1. Go to Reddit Apps Page
Open this link in your browser:
👉 **https://www.reddit.com/prefs/apps**

### 2. Log In
Use your Reddit account credentials:
- Email: fay@intallaga.com
- Password: intallaga188a

### 3. Create a New App
Scroll to the bottom and click **"Create App"** or **"Create Another App"**

### 4. Fill in the Form

```
Name: Reddit Tracker
App type: ⚪ web app  ⚪ installed app  🔘 script  ⚪ personal use
Description: Personal Reddit monitoring tool
About url: (leave blank)
Redirect uri: http://localhost:8080
```

**Important**: Select "**script**" as the app type!

### 5. Click "Create App"

### 6. Get Your Credentials

You'll see something like this:

```
┌─────────────────────────────────┐
│ Reddit Tracker                   │
│ personal use script by username  │
│                                  │
│ Ab12Cd34Ef56Gh  ← CLIENT ID     │
│ secret                           │
│ 1a2b3c4d5e6f7g8h ← SECRET       │
│                                  │
│ redirect uri                     │
│ http://localhost:8080            │
└─────────────────────────────────┘
```

**Copy these two values:**
- Client ID: The random string under your app name (14-ish characters)
- Secret: Click "secret" to see it, then copy (27-ish characters)

### 7. Create .env File

Open Terminal and run:

```bash
cd "/Users/zhangfan/Desktop/reddit track"
nano .env
```

Paste this and **replace with YOUR credentials**:

```env
REDDIT_CLIENT_ID=paste_your_client_id_here
REDDIT_CLIENT_SECRET=paste_your_secret_here
REDDIT_USER_AGENT=RedditTracker/1.0

SUBREDDITS=complaints,techsupport,ProductComplaints
KEYWORDS=complaint,issue,problem,bug,demand,request,need,broken,not working
POST_LIMIT=100
REPORT_DIR=reports
```

**Save**: Press `Ctrl+O`, Enter, then `Ctrl+X`

### 8. Test It!

```bash
python3 main.py
```

If it works, you'll see:
```
🎯 Reddit Tracker - Complaints & Demands Collector
============================================================

📡 Initializing Reddit API client...
💾 Loading data manager...
🔍 Initializing analyzer...
📊 Initializing report generator...

📥 Fetching posts from 3 subreddit(s)...
```

### 9. View Your Report

```bash
open reports/report_*.html
```

## 🎉 You're Done!

Now set up automation:

```bash
./run_scheduler.sh
```

---

## ❓ Troubleshooting

### "401 HTTP response"
- Your credentials are wrong
- Double-check Client ID and Secret
- Make sure you selected "script" type

### "No such file or directory: .env"
- Make sure you created the .env file in the correct folder
- Run: `ls -la .env` to verify it exists

### Still stuck?
Run the interactive setup:
```bash
python3 quick_start.py
```
