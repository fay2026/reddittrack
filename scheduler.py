"""Scheduler for automated daily runs"""
import schedule
import time
from datetime import datetime
import os
import sys


def run_tracker():
    """Run the main tracker script"""
    print()
    print("=" * 70)
    print(f"⏰ Scheduled run started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Import here to avoid circular imports
    from main import main
    
    try:
        main()
    except Exception as e:
        print(f"❌ Error during scheduled run: {e}")
        import traceback
        traceback.print_exc()
    
    print()
    print("✅ Scheduled run completed")
    print("=" * 70)


def main():
    """Main scheduler function"""
    print("🤖 Reddit Tracker Scheduler Started")
    print("=" * 70)
    print()
    print("📅 Schedule: Every day at 8:00 AM")
    print()
    print("💡 Press Ctrl+C to stop the scheduler")
    print("=" * 70)
    print()
    
    # Schedule the job for 8:00 AM every day
    schedule.every().day.at("08:00").do(run_tracker)
    
    # Optionally run immediately on startup
    if "--now" in sys.argv:
        print("🚀 Running immediately (--now flag detected)...")
        run_tracker()
    
    print(f"⏳ Waiting for scheduled time (next run: {schedule.next_run()})...")
    print()
    
    # Keep running
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print()
        print("=" * 70)
        print("👋 Scheduler stopped by user")
        print("=" * 70)


if __name__ == "__main__":
    main()
