"""Quick start setup script for Reddit Tracker"""
import os
import sys


def print_header():
    """Print welcome header"""
    print("=" * 70)
    print("🎯 Reddit Tracker - Quick Start Setup")
    print("=" * 70)
    print()


def check_env_file():
    """Check if .env file exists"""
    if os.path.exists('.env'):
        print("✅ .env file found")
        return True
    else:
        print("❌ .env file not found")
        return False


def create_env_file():
    """Guide user through creating .env file"""
    print()
    print("Let's create your .env configuration file!")
    print()
    print("First, you need Reddit API credentials:")
    print("1. Go to: https://www.reddit.com/prefs/apps")
    print("2. Click 'Create App' or 'Create Another App'")
    print("3. Fill in:")
    print("   - name: Reddit Tracker")
    print("   - type: script")
    print("   - redirect uri: http://localhost:8080")
    print()
    
    input("Press Enter when you have your credentials ready...")
    print()
    
    # Get credentials
    client_id = input("Enter your Reddit Client ID: ").strip()
    client_secret = input("Enter your Reddit Client Secret: ").strip()
    
    print()
    print("Great! Now let's configure what to track...")
    print()
    
    default_subs = input("Subreddits to monitor (comma-separated) [complaints,techsupport]: ").strip()
    if not default_subs:
        default_subs = "complaints,techsupport"
    
    default_keywords = input("Keywords to track (comma-separated) [complaint,issue,problem]: ").strip()
    if not default_keywords:
        default_keywords = "complaint,issue,problem,bug,demand,request"
    
    # Create .env file
    env_content = f"""# Reddit API Credentials
REDDIT_CLIENT_ID={client_id}
REDDIT_CLIENT_SECRET={client_secret}
REDDIT_USER_AGENT=RedditTracker/1.0

# Subreddits to monitor (comma-separated)
SUBREDDITS={default_subs}

# Keywords to track (comma-separated)
KEYWORDS={default_keywords}

# Number of posts to fetch per subreddit
POST_LIMIT=100

# Report output directory
REPORT_DIR=reports
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print()
    print("✅ .env file created successfully!")


def check_dependencies():
    """Check if dependencies are installed"""
    print()
    print("Checking dependencies...")
    
    missing = []
    required = ['praw', 'dotenv', 'pandas', 'textblob', 'schedule', 'jinja2']
    
    for package in required:
        try:
            if package == 'dotenv':
                __import__('dotenv')
            else:
                __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package}")
            missing.append(package)
    
    return missing


def main():
    """Main setup function"""
    print_header()
    
    # Check dependencies
    missing = check_dependencies()
    
    if missing:
        print()
        print("⚠️  Missing dependencies detected!")
        print()
        response = input("Install missing packages now? (y/n): ").lower()
        if response == 'y':
            print()
            print("Installing dependencies...")
            os.system(f"{sys.executable} -m pip install -r requirements.txt")
            print()
            print("✅ Dependencies installed!")
        else:
            print()
            print("Please install dependencies manually:")
            print(f"  {sys.executable} -m pip install -r requirements.txt")
            sys.exit(1)
    
    # Check .env file
    print()
    if not check_env_file():
        response = input("Create .env file now? (y/n): ").lower()
        if response == 'y':
            create_env_file()
        else:
            print()
            print("You can create .env file later using env_template.txt as reference")
            sys.exit(0)
    
    # Test run option
    print()
    print("=" * 70)
    print("✅ Setup complete!")
    print("=" * 70)
    print()
    print("Next steps:")
    print("1. Run a test: python3 main.py")
    print("2. View report: open reports/report_*.html")
    print("3. Set up automation: ./run_scheduler.sh")
    print()
    
    response = input("Would you like to run a test now? (y/n): ").lower()
    if response == 'y':
        print()
        print("Running test...")
        print()
        os.system(f"{sys.executable} main.py")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print()
        print("Setup cancelled by user")
        sys.exit(0)
