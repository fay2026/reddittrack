# 🎯 Reddit Tracker - Automated Complaints & Demands Collector

An intelligent agent that automatically collects and analyzes user complaints and demands from Reddit every morning, presenting them in a beautiful, easy-to-read HTML report.

## ✨ Features

- 🤖 **Automated Collection**: Fetches posts from multiple subreddits daily
- 🧠 **Smart Analysis**: Sentiment analysis and automatic categorization
- 📊 **Priority Scoring**: Identifies high-priority issues based on engagement and sentiment
- 🎨 **Beautiful Reports**: Interactive HTML reports with filtering capabilities
- 📝 **Tracking System**: Only shows new posts you haven't seen before
- ⏰ **Flexible Scheduling**: Multiple automation options (Python scheduler, cron, or manual)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 2. Get Reddit API Credentials

1. Go to https://www.reddit.com/prefs/apps
2. Click "Create App" or "Create Another App"
3. Fill in:
   - **name**: Reddit Tracker (or any name)
   - **type**: Choose "script"
   - **description**: Personal Reddit monitoring tool
   - **redirect uri**: http://localhost:8080 (required but not used)
4. Click "Create app"
5. Note your **client ID** (under the app name) and **secret**

### 3. Configure the Application

Create a `.env` file in the project directory:

```bash
# Copy the example file
cp .env.example .env

# Edit with your credentials
nano .env  # or use any text editor
```

Add your credentials:

```env
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=RedditTracker/1.0

# Customize which subreddits to monitor
SUBREDDITS=complaints,techsupport,ProductComplaints,apple,microsoft

# Customize keywords to track
KEYWORDS=complaint,issue,problem,bug,demand,request,need,broken,not working

# Number of posts to fetch per subreddit
POST_LIMIT=100
```

### 4. Run the Tracker

#### Manual Run (Test First!)

```bash
python3 main.py
```

This will:
- Fetch posts from configured subreddits
- Analyze sentiment and categorize them
- Generate an HTML report in the `reports/` directory
- Track seen posts to avoid duplicates

#### View the Report

Open the generated HTML file in your browser:

```bash
# macOS
open reports/report_YYYY-MM-DD.html

# Linux
xdg-open reports/report_YYYY-MM-DD.html

# Windows
start reports/report_YYYY-MM-DD.html
```

## ⏰ Automation Options

### Option 1: Python Scheduler (Recommended for macOS/Linux)

Run continuously in the background:

```bash
# Make scripts executable
chmod +x run_scheduler.sh stop_scheduler.sh

# Start the scheduler (runs at 8 AM daily)
./run_scheduler.sh

# Stop the scheduler
./stop_scheduler.sh

# Run immediately for testing
python3 scheduler.py --now
```

The scheduler will:
- Run every day at 8:00 AM
- Log output to `logs/scheduler.log`
- Continue running until stopped

### Option 2: Cron Job (macOS/Linux)

For system-level scheduling:

```bash
# Make script executable
chmod +x setup_cron.sh

# Setup cron job
./setup_cron.sh
```

This adds a cron job that runs daily at 8 AM.

To customize the time, edit your crontab:
```bash
crontab -e
```

Cron time format:
```
# Minute Hour Day Month DayOfWeek Command
0 8 * * *    # 8:00 AM daily
0 9 * * 1    # 9:00 AM every Monday
30 7 * * *   # 7:30 AM daily
```

### Option 3: Task Scheduler (Windows)

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger to "Daily" at 8:00 AM
4. Action: "Start a program"
5. Program: `python`
6. Arguments: `main.py`
7. Start in: `/path/to/reddit track/`

## 📊 Understanding the Report

The HTML report includes:

### Statistics Dashboard
- **Total Posts**: Number of new posts collected
- **High Priority**: Posts requiring immediate attention
- **Negative Sentiment**: Posts with negative tone
- **Subreddits**: Number of subreddits monitored

### Post Information
Each post shows:
- **Title**: Clickable link to original Reddit post
- **Priority**: High/Medium/Low based on engagement and sentiment
- **Metadata**: Subreddit, author, date, score, comments
- **Sentiment**: Positive/Negative/Neutral with polarity score
- **Categories**: Auto-assigned categories (Bug, Feature Request, etc.)
- **Text Preview**: First 300 characters of the post

### Interactive Filters
- **All Posts**: Show everything
- **High Priority**: Critical issues only
- **Medium Priority**: Important posts
- **Negative Sentiment**: Posts with complaints

## 🔧 Customization

### Monitor Different Subreddits

Edit `.env`:
```env
SUBREDDITS=yoursub1,yoursub2,yourproduct,techsupport
```

### Change Keywords

Edit `.env`:
```env
KEYWORDS=your,custom,keywords,here
```

### Adjust Schedule Time

Edit `scheduler.py` line 31:
```python
schedule.every().day.at("08:00").do(run_tracker)  # Change "08:00" to your preferred time
```

### Modify Categories

Edit `analyzer.py` to customize the `CATEGORIES` dictionary with your own keywords.

## 📁 Project Structure

```
reddit track/
├── main.py                 # Main execution script
├── reddit_fetcher.py       # Reddit API client
├── data_manager.py         # Data storage and tracking
├── analyzer.py             # Sentiment analysis & categorization
├── report_generator.py     # HTML report generator
├── scheduler.py            # Automated scheduling
├── config.py              # Configuration management
├── requirements.txt        # Python dependencies
├── .env                   # Your configuration (create this!)
├── .gitignore            # Git ignore rules
├── run_scheduler.sh       # Start scheduler script
├── stop_scheduler.sh      # Stop scheduler script
├── setup_cron.sh         # Cron setup script
├── data/                  # Stored data (auto-created)
│   ├── posts_*.json      # Daily post data
│   └── seen_posts.json   # Tracking file
├── reports/               # Generated reports (auto-created)
│   └── report_*.html     # Daily HTML reports
└── logs/                  # Logs (auto-created)
    └── scheduler.log     # Scheduler logs
```

## 🛠️ Troubleshooting

### "Reddit API credentials not configured"
- Make sure `.env` file exists in the project root
- Check that `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` are set correctly
- Verify no extra spaces or quotes around values

### "praw.exceptions.ResponseException: received 401 HTTP response"
- Your Reddit credentials are invalid
- Double-check your Client ID and Secret
- Make sure you created a "script" type app, not "web app"

### No posts found
- Try different subreddits in `.env`
- Adjust keywords to be less restrictive
- Increase `POST_LIMIT` (default: 100)
- Some subreddits may have little activity

### Report shows no new posts
- This is normal if you've already seen all posts
- The tracker only shows posts you haven't seen before
- Try deleting `data/seen_posts.json` to reset (you'll see all posts again)

### Scheduler not running
- Check logs: `cat logs/scheduler.log`
- Verify process is running: `ps aux | grep scheduler`
- Make sure scripts are executable: `chmod +x *.sh`

## 🔒 Privacy & Security

- Never commit your `.env` file to version control
- Your Reddit credentials are stored locally only
- The app only reads public Reddit data
- No data is sent to external services (except Reddit API)

## 📝 Tips

1. **Start Small**: Test with 2-3 subreddits first
2. **Review Reports**: Check reports daily to refine your keywords
3. **Adjust Priority**: Modify priority calculation in `analyzer.py` for your needs
4. **Backup Data**: The `data/` folder contains all collected posts
5. **Mobile Access**: HTML reports are mobile-responsive

## 🤝 Contributing

Feel free to:
- Add more analysis features
- Improve categorization logic
- Create new report templates
- Add support for other platforms

## 📄 License

This project is for personal use. Please respect Reddit's API terms of service and rate limits.

---

**Happy Tracking! 🎉**

For questions or issues, check the logs in `logs/scheduler.log` or review error messages in the terminal output.
