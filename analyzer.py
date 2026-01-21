"""Sentiment analysis and categorization of posts"""
from textblob import TextBlob
from typing import List, Dict
import re


class PostAnalyzer:
    """Analyzes posts for sentiment and categorization"""
    
    # Category keywords
    CATEGORIES = {
        'Bug/Technical Issue': ['bug', 'error', 'crash', 'broken', 'not working', 'doesnt work', 
                                "doesn't work", 'glitch', 'issue', 'technical'],
        'Feature Request': ['request', 'feature', 'add', 'wish', 'would like', 'should have',
                           'need', 'want', 'demand', 'please add'],
        'Complaint': ['complaint', 'terrible', 'awful', 'worst', 'hate', 'disappointed',
                     'frustrating', 'annoying', 'poor', 'bad'],
        'Service Issue': ['support', 'service', 'customer service', 'help', 'response',
                         'refund', 'cancel', 'billing'],
        'Performance': ['slow', 'lag', 'performance', 'speed', 'fast', 'optimization',
                       'loading', 'timeout']
    }
    
    def analyze_sentiment(self, text: str) -> Dict:
        """
        Analyze sentiment of text
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary with sentiment info
        """
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        if polarity > 0.1:
            sentiment = 'positive'
        elif polarity < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {
            'sentiment': sentiment,
            'polarity': round(polarity, 3),
            'subjectivity': round(subjectivity, 3)
        }
    
    def categorize_post(self, post: Dict) -> List[str]:
        """
        Categorize post based on content
        
        Args:
            post: Post dictionary
            
        Returns:
            List of categories
        """
        text = f"{post['title']} {post['selftext']}".lower()
        categories = []
        
        for category, keywords in self.CATEGORIES.items():
            if any(keyword in text for keyword in keywords):
                categories.append(category)
        
        return categories if categories else ['General']
    
    def analyze_post(self, post: Dict) -> Dict:
        """
        Perform complete analysis on a post
        
        Args:
            post: Post dictionary
            
        Returns:
            Enhanced post dictionary with analysis
        """
        text = f"{post['title']} {post['selftext']}"
        
        sentiment_data = self.analyze_sentiment(text)
        categories = self.categorize_post(post)
        
        post_copy = post.copy()
        post_copy.update({
            'sentiment': sentiment_data['sentiment'],
            'polarity': sentiment_data['polarity'],
            'subjectivity': sentiment_data['subjectivity'],
            'categories': categories,
            'priority': self._calculate_priority(post, sentiment_data)
        })
        
        return post_copy
    
    def _calculate_priority(self, post: Dict, sentiment_data: Dict) -> str:
        """
        Calculate priority level (High/Medium/Low)
        
        Based on: engagement (score, comments), sentiment, and recency
        """
        score = post['score']
        comments = post['num_comments']
        polarity = sentiment_data['polarity']
        
        # High priority: negative sentiment + high engagement
        if polarity < -0.3 and (score > 50 or comments > 20):
            return 'High'
        
        # High priority: very high engagement
        if score > 100 or comments > 50:
            return 'High'
        
        # Medium priority: moderate engagement or negative sentiment
        if score > 20 or comments > 10 or polarity < -0.1:
            return 'Medium'
        
        return 'Low'
    
    def analyze_posts(self, posts: List[Dict]) -> List[Dict]:
        """Analyze a list of posts"""
        return [self.analyze_post(post) for post in posts]
