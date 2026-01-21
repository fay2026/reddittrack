#!/bin/bash
# Create .env file with your credentials

cat > .env << 'EOF'
# Reddit API Credentials
# Get these from https://www.reddit.com/prefs/apps
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=

# User agent is auto-generated to look more human-like

# Subreddits to monitor (comma-separated)
SUBREDDITS=complaints,techsupport,ProductComplaints,apple,microsoft

# Keywords to track (comma-separated)
KEYWORDS=complaint,issue,problem,bug,demand,request,need,broken,not working,frustrating,terrible

# Number of posts to fetch per subreddit
POST_LIMIT=100

# Report output directory
REPORT_DIR=reports
EOF

echo "✅ .env file created successfully!"
