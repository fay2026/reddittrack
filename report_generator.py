"""HTML report generator for easy viewing of collected data"""
from datetime import datetime
from typing import List, Dict
import os
import config


class ReportGenerator:
    """Generates beautiful HTML reports from analyzed posts"""
    
    HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reddit Complaints & Demands - {date}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header .subtitle {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
            border-bottom: 2px solid #e9ecef;
        }}
        
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        .stat-card .number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 5px;
        }}
        
        .stat-card .label {{
            color: #6c757d;
            font-size: 0.9em;
        }}
        
        .filters {{
            padding: 20px 30px;
            background: #f8f9fa;
            border-bottom: 1px solid #e9ecef;
        }}
        
        .filter-buttons {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }}
        
        .filter-btn {{
            padding: 8px 16px;
            border: 2px solid #667eea;
            background: white;
            color: #667eea;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: 500;
        }}
        
        .filter-btn:hover {{
            background: #667eea;
            color: white;
        }}
        
        .filter-btn.active {{
            background: #667eea;
            color: white;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .post {{
            background: white;
            border: 2px solid #e9ecef;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            transition: all 0.3s;
        }}
        
        .post:hover {{
            border-color: #667eea;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
        }}
        
        .post-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 16px;
            flex-wrap: wrap;
            gap: 10px;
        }}
        
        .post-title {{
            font-size: 1.4em;
            font-weight: 600;
            color: #212529;
            flex: 1;
            min-width: 300px;
        }}
        
        .post-title a {{
            color: #212529;
            text-decoration: none;
        }}
        
        .post-title a:hover {{
            color: #667eea;
        }}
        
        .priority {{
            padding: 6px 14px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85em;
            text-transform: uppercase;
        }}
        
        .priority-high {{
            background: #fee;
            color: #dc3545;
        }}
        
        .priority-medium {{
            background: #fff3cd;
            color: #856404;
        }}
        
        .priority-low {{
            background: #d1ecf1;
            color: #0c5460;
        }}
        
        .post-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            margin-bottom: 12px;
            font-size: 0.9em;
            color: #6c757d;
        }}
        
        .meta-item {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        
        .post-text {{
            color: #495057;
            line-height: 1.6;
            margin-bottom: 16px;
        }}
        
        .tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}
        
        .tag {{
            padding: 4px 12px;
            background: #e7f3ff;
            color: #0066cc;
            border-radius: 12px;
            font-size: 0.85em;
        }}
        
        .sentiment {{
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85em;
            font-weight: 500;
        }}
        
        .sentiment-positive {{
            background: #d4edda;
            color: #155724;
        }}
        
        .sentiment-negative {{
            background: #f8d7da;
            color: #721c24;
        }}
        
        .sentiment-neutral {{
            background: #e2e3e5;
            color: #383d41;
        }}
        
        .no-posts {{
            text-align: center;
            padding: 60px 20px;
            color: #6c757d;
        }}
        
        .no-posts h2 {{
            font-size: 2em;
            margin-bottom: 10px;
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 1.8em;
            }}
            
            .post-title {{
                font-size: 1.2em;
            }}
            
            .stats {{
                grid-template-columns: 1fr 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 Reddit Tracker Report</h1>
            <div class="subtitle">Complaints & Demands Analysis - {date}</div>
        </div>
        
        <div class="stats">
            {stats_html}
        </div>
        
        <div class="filters">
            <div class="filter-buttons">
                <button class="filter-btn active" data-filter="all">All Posts</button>
                <button class="filter-btn" data-filter="high">High Priority</button>
                <button class="filter-btn" data-filter="medium">Medium Priority</button>
                <button class="filter-btn" data-filter="negative">Negative Sentiment</button>
            </div>
        </div>
        
        <div class="content">
            {posts_html}
        </div>
    </div>
    
    <script>
        // Filter functionality
        const filterBtns = document.querySelectorAll('.filter-btn');
        const posts = document.querySelectorAll('.post');
        
        filterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                // Update active button
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                const filter = btn.dataset.filter;
                
                posts.forEach(post => {{
                    const priority = post.dataset.priority;
                    const sentiment = post.dataset.sentiment;
                    
                    if (filter === 'all') {{
                        post.style.display = 'block';
                    }} else if (filter === 'high' && priority === 'High') {{
                        post.style.display = 'block';
                    }} else if (filter === 'medium' && priority === 'Medium') {{
                        post.style.display = 'block';
                    }} else if (filter === 'negative' && sentiment === 'negative') {{
                        post.style.display = 'block';
                    }} else {{
                        post.style.display = 'none';
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>
"""
    
    def generate_report(self, posts: List[Dict], date_str: str = None) -> str:
        """
        Generate HTML report from posts
        
        Args:
            posts: List of analyzed post dictionaries
            date_str: Date string for the report
            
        Returns:
            Path to generated HTML file
        """
        if date_str is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
        
        # Generate stats
        stats_html = self._generate_stats_html(posts)
        
        # Generate posts HTML
        posts_html = self._generate_posts_html(posts)
        
        # Fill template
        html = self.HTML_TEMPLATE.format(
            date=date_str,
            stats_html=stats_html,
            posts_html=posts_html
        )
        
        # Save report
        report_path = os.path.join(config.REPORT_DIR, f'report_{date_str}.html')
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return report_path
    
    def _generate_stats_html(self, posts: List[Dict]) -> str:
        """Generate statistics cards HTML"""
        total = len(posts)
        high_priority = sum(1 for p in posts if p.get('priority') == 'High')
        negative = sum(1 for p in posts if p.get('sentiment') == 'negative')
        
        # Count unique subreddits
        subreddits = len(set(p['subreddit'] for p in posts)) if posts else 0
        
        return f"""
            <div class="stat-card">
                <div class="number">{total}</div>
                <div class="label">Total Posts</div>
            </div>
            <div class="stat-card">
                <div class="number">{high_priority}</div>
                <div class="label">High Priority</div>
            </div>
            <div class="stat-card">
                <div class="number">{negative}</div>
                <div class="label">Negative Sentiment</div>
            </div>
            <div class="stat-card">
                <div class="number">{subreddits}</div>
                <div class="label">Subreddits</div>
            </div>
        """
    
    def _generate_posts_html(self, posts: List[Dict]) -> str:
        """Generate posts HTML"""
        if not posts:
            return """
                <div class="no-posts">
                    <h2>🎉 No new posts found!</h2>
                    <p>Either there are no new complaints/demands, or you've already seen them all.</p>
                </div>
            """
        
        posts_html = []
        for post in posts:
            posts_html.append(self._generate_post_html(post))
        
        return '\n'.join(posts_html)
    
    def _generate_post_html(self, post: Dict) -> str:
        """Generate HTML for a single post"""
        priority = post.get('priority', 'Low')
        sentiment = post.get('sentiment', 'neutral')
        categories = post.get('categories', [])
        
        # Format text
        text = post['selftext'] if post['selftext'] else '[No text content]'
        if len(text) > 300:
            text = text[:300] + '...'
        
        # Categories tags
        tags_html = ''.join([f'<span class="tag">{cat}</span>' for cat in categories])
        
        return f"""
            <div class="post" data-priority="{priority}" data-sentiment="{sentiment}">
                <div class="post-header">
                    <div class="post-title">
                        <a href="{post['url']}" target="_blank">{post['title']}</a>
                    </div>
                    <span class="priority priority-{priority.lower()}">{priority}</span>
                </div>
                <div class="post-meta">
                    <div class="meta-item">📍 r/{post['subreddit']}</div>
                    <div class="meta-item">👤 {post['author']}</div>
                    <div class="meta-item">📅 {post['created_date']}</div>
                    <div class="meta-item">⬆️ {post['score']}</div>
                    <div class="meta-item">💬 {post['num_comments']}</div>
                </div>
                <div class="post-text">{text}</div>
                <div class="tags">
                    <span class="sentiment sentiment-{sentiment}">
                        {'😊' if sentiment == 'positive' else '😠' if sentiment == 'negative' else '😐'} {sentiment.title()}
                    </span>
                    {tags_html}
                </div>
            </div>
        """
