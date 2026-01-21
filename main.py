"""Main script to run the Reddit tracker"""
import sys
from datetime import datetime
from reddit_fetcher import RedditFetcher
from data_manager import DataManager
from analyzer import PostAnalyzer
from report_generator import ReportGenerator
import config


def main():
    """Main execution function"""
    print("=" * 60)
    print("🎯 Reddit Tracker - Complaints & Demands Collector")
    print("=" * 60)
    print()
    
    # Check if API credentials are set
    if not config.REDDIT_CLIENT_ID or not config.REDDIT_CLIENT_SECRET:
        print("❌ ERROR: Reddit API credentials not configured!")
        print("Please set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET in .env file")
        print("Get credentials from: https://www.reddit.com/prefs/apps")
        sys.exit(1)
    
    try:
        # Initialize components
        print("📡 Initializing Reddit API client...")
        fetcher = RedditFetcher()
        
        print("💾 Loading data manager...")
        data_manager = DataManager()
        
        print("🔍 Initializing analyzer...")
        analyzer = PostAnalyzer()
        
        print("📊 Initializing report generator...")
        report_gen = ReportGenerator()
        
        print()
        print(f"📥 Fetching posts from {len(config.SUBREDDITS)} subreddit(s)...")
        print(f"   Subreddits: {', '.join(config.SUBREDDITS)}")
        print()
        
        # Fetch all posts
        all_posts = fetcher.fetch_all_subreddits()
        print()
        print(f"✅ Fetched {len(all_posts)} posts matching keywords")
        
        # Filter for new posts only
        print("🆕 Filtering for new posts...")
        new_posts = data_manager.filter_new_posts(all_posts)
        print(f"   Found {len(new_posts)} new posts")
        
        if len(new_posts) == 0:
            print()
            print("✨ No new posts found! You're all caught up.")
            # Still generate a report with empty data
            date_str = datetime.now().strftime('%Y-%m-%d')
            report_path = report_gen.generate_report([], date_str)
            print(f"📄 Generated report: {report_path}")
            return
        
        # Analyze posts
        print()
        print("🧠 Analyzing posts (sentiment & categorization)...")
        analyzed_posts = analyzer.analyze_posts(new_posts)
        
        # Show summary
        high_priority = sum(1 for p in analyzed_posts if p.get('priority') == 'High')
        negative = sum(1 for p in analyzed_posts if p.get('sentiment') == 'negative')
        
        print(f"   High Priority: {high_priority}")
        print(f"   Negative Sentiment: {negative}")
        
        # Save data
        print()
        print("💾 Saving data...")
        date_str = datetime.now().strftime('%Y-%m-%d')
        data_manager.save_daily_data(analyzed_posts, date_str)
        data_manager.mark_as_seen(analyzed_posts)
        
        # Generate report
        print("📊 Generating HTML report...")
        report_path = report_gen.generate_report(analyzed_posts, date_str)
        
        print()
        print("=" * 60)
        print("✅ SUCCESS! Report generated:")
        print(f"📄 {report_path}")
        print("=" * 60)
        print()
        print("💡 TIP: Open the HTML file in your browser to view the report")
        
    except Exception as e:
        print()
        print("=" * 60)
        print(f"❌ ERROR: {str(e)}")
        print("=" * 60)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
