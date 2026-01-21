"""Configuration management for Reddit Tracker"""
import os
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Reddit API Configuration
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID', '')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET', '')

# Use more natural user agent (looks like a regular browser)
# Format: platform:app_name:version (by /u/username)
_base_user_agent = os.getenv('REDDIT_USER_AGENT', 'RedditTracker/1.0')

# Make user agent more realistic by varying it slightly
_platforms = ['MacOS', 'Windows', 'Linux']
_browsers = ['Chrome', 'Firefox', 'Safari', 'Edge']
_versions = ['91.0', '92.0', '93.0', '94.0', '95.0']

REDDIT_USER_AGENT = f"{random.choice(_platforms)}:{_base_user_agent}:v{random.choice(_versions)} (by /u/tracker_bot)"

# Monitoring Configuration
SUBREDDITS = os.getenv('SUBREDDITS', 'complaints,techsupport,ProductComplaints').split(',')
KEYWORDS = os.getenv('KEYWORDS', 'complaint,issue,problem,bug,demand,request,need,broken,not working').split(',')
POST_LIMIT = int(os.getenv('POST_LIMIT', '100'))

# Storage Configuration
DATA_DIR = 'data'
REPORT_DIR = os.getenv('REPORT_DIR', 'reports')
SEEN_POSTS_FILE = os.path.join(DATA_DIR, 'seen_posts.json')

# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)
