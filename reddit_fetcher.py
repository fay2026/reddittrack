"""Reddit data fetcher for collecting complaints and demands"""
import praw
import json
import time
import random
from datetime import datetime
from typing import List, Dict
import config


class RedditFetcher:
    """Fetches and filters Reddit posts based on keywords"""
    
    def __init__(self):
        """Initialize Reddit API client"""
        self.reddit = praw.Reddit(
            client_id=config.REDDIT_CLIENT_ID,
            client_secret=config.REDDIT_CLIENT_SECRET,
            user_agent=config.REDDIT_USER_AGENT
        )
        self.keywords = [kw.lower().strip() for kw in config.KEYWORDS]
        
    def _human_delay(self, min_seconds=2, max_seconds=5):
        """Add random delay to simulate human browsing"""
        delay = random.uniform(min_seconds, max_seconds)
        time.sleep(delay)
        
    def fetch_posts(self, subreddit_name: str, limit: int = 100) -> List[Dict]:
        """
        Fetch recent posts from a subreddit (human-like behavior)
        
        Args:
            subreddit_name: Name of the subreddit
            limit: Number of posts to fetch
            
        Returns:
            List of post dictionaries
        """
        posts = []
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            
            # Simulate human browsing: mix different sorting methods
            sorting_methods = ['new', 'hot', 'rising']
            chosen_sort = random.choice(sorting_methods)
            
            # Split limit across different methods for more natural behavior
            posts_per_method = limit // 3
            
            print(f"  Browsing r/{subreddit_name} ({chosen_sort} posts)...")
            
            # Fetch from primary sorting method
            posts.extend(self._fetch_from_listing(subreddit, chosen_sort, posts_per_method))
            
            # Add small delay between different browsing patterns
            self._human_delay(1, 3)
            
            # Fetch from secondary method (like a human might scroll through different tabs)
            secondary_sort = random.choice([s for s in sorting_methods if s != chosen_sort])
            posts.extend(self._fetch_from_listing(subreddit, secondary_sort, posts_per_method))
            
        except Exception as e:
            print(f"  ⚠️  Error accessing r/{subreddit_name}: {str(e)}")
            if "429" in str(e):
                print(f"  Rate limited. Waiting 60 seconds...")
                time.sleep(60)
            
        return posts
    
    def _fetch_from_listing(self, subreddit, sort_method: str, limit: int) -> List[Dict]:
        """
        Fetch posts from a specific sorting method
        
        Args:
            subreddit: Subreddit object
            sort_method: 'new', 'hot', or 'rising'
            limit: Number of posts to fetch
            
        Returns:
            List of filtered post dictionaries
        """
        posts = []
        try:
            # Get the appropriate listing
            if sort_method == 'new':
                listing = subreddit.new(limit=limit)
            elif sort_method == 'hot':
                listing = subreddit.hot(limit=limit)
            else:  # rising
                listing = subreddit.rising(limit=limit)
            
            # Process posts with random delays (simulate reading)
            for idx, submission in enumerate(listing):
                post_data = self._extract_post_data(submission)
                if self._matches_keywords(post_data):
                    posts.append(post_data)
                
                # Add small random delay every few posts (like human scrolling/reading)
                if idx > 0 and idx % 10 == 0:
                    self._human_delay(0.5, 2)
                    
        except Exception as e:
            print(f"    Error fetching {sort_method} posts: {str(e)}")
            
        return posts
    
    def _extract_post_data(self, submission) -> Dict:
        """Extract relevant data from a Reddit submission"""
        return {
            'id': submission.id,
            'title': submission.title,
            'author': str(submission.author) if submission.author else '[deleted]',
            'subreddit': str(submission.subreddit),
            'created_utc': submission.created_utc,
            'created_date': datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
            'score': submission.score,
            'num_comments': submission.num_comments,
            'url': f"https://reddit.com{submission.permalink}",
            'selftext': submission.selftext[:500] if submission.selftext else '',
            'upvote_ratio': submission.upvote_ratio,
            'is_self': submission.is_self
        }
    
    def _matches_keywords(self, post_data: Dict) -> bool:
        """Check if post contains any of the target keywords"""
        text = f"{post_data['title']} {post_data['selftext']}".lower()
        return any(keyword in text for keyword in self.keywords)
    
    def fetch_all_subreddits(self) -> List[Dict]:
        """Fetch posts from all configured subreddits (human-like behavior)"""
        all_posts = []
        subreddits = [s.strip() for s in config.SUBREDDITS]
        
        # Randomize order (humans don't always check in the same order)
        random.shuffle(subreddits)
        
        for idx, subreddit in enumerate(subreddits):
            print(f"Fetching from r/{subreddit}...")
            
            # Vary the limit slightly for each subreddit (more natural)
            varied_limit = config.POST_LIMIT + random.randint(-10, 10)
            varied_limit = max(20, min(varied_limit, 150))  # Keep it reasonable
            
            posts = self.fetch_posts(subreddit, varied_limit)
            all_posts.extend(posts)
            print(f"  ✓ Found {len(posts)} relevant posts")
            
            # Add delay between subreddits (like switching between tabs)
            if idx < len(subreddits) - 1:  # Don't delay after the last one
                delay = random.uniform(3, 8)
                print(f"  Taking a {delay:.1f}s break before next subreddit...")
                time.sleep(delay)
        
        # Remove duplicates (same post in multiple subreddits)
        seen_ids = set()
        unique_posts = []
        for post in all_posts:
            if post['id'] not in seen_ids:
                seen_ids.add(post['id'])
                unique_posts.append(post)
        
        # Sort by date (newest first)
        unique_posts.sort(key=lambda x: x['created_utc'], reverse=True)
        
        if len(all_posts) != len(unique_posts):
            print(f"\n  🔍 Removed {len(all_posts) - len(unique_posts)} duplicate posts")
        
        return unique_posts
