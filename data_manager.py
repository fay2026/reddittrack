"""Data management for tracking seen posts and storing new ones"""
import json
import os
from datetime import datetime
from typing import List, Dict, Set
import config


class DataManager:
    """Manages post data storage and tracking"""
    
    def __init__(self):
        self.seen_posts_file = config.SEEN_POSTS_FILE
        self.seen_posts = self._load_seen_posts()
    
    def _load_seen_posts(self) -> Set[str]:
        """Load the set of previously seen post IDs"""
        if os.path.exists(self.seen_posts_file):
            try:
                with open(self.seen_posts_file, 'r') as f:
                    data = json.load(f)
                    return set(data.get('seen_ids', []))
            except Exception as e:
                print(f"Error loading seen posts: {e}")
                return set()
        return set()
    
    def _save_seen_posts(self):
        """Save the set of seen post IDs"""
        try:
            with open(self.seen_posts_file, 'w') as f:
                json.dump({
                    'seen_ids': list(self.seen_posts),
                    'last_updated': datetime.now().isoformat()
                }, f, indent=2)
        except Exception as e:
            print(f"Error saving seen posts: {e}")
    
    def filter_new_posts(self, posts: List[Dict]) -> List[Dict]:
        """
        Filter out posts that have already been seen
        
        Args:
            posts: List of post dictionaries
            
        Returns:
            List of new posts only
        """
        new_posts = [post for post in posts if post['id'] not in self.seen_posts]
        return new_posts
    
    def mark_as_seen(self, posts: List[Dict]):
        """Mark posts as seen"""
        for post in posts:
            self.seen_posts.add(post['id'])
        self._save_seen_posts()
    
    def save_daily_data(self, posts: List[Dict], date_str: str = None):
        """
        Save daily collected data to a JSON file
        
        Args:
            posts: List of post dictionaries
            date_str: Date string for filename (defaults to today)
        """
        if date_str is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
        
        filename = os.path.join(config.DATA_DIR, f'posts_{date_str}.json')
        
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'date': date_str,
                    'total_posts': len(posts),
                    'posts': posts
                }, f, indent=2)
            print(f"Saved {len(posts)} posts to {filename}")
        except Exception as e:
            print(f"Error saving daily data: {e}")
