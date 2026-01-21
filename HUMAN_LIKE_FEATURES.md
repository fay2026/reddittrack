# 🕵️ Human-Like Behavior Features

Your Reddit tracker now behaves like a real human to avoid detection and rate limiting!

## ✨ What Was Changed

### 1. **Random Delays Between Requests** ⏱️
- Waits 2-5 seconds between actions (like a human reading)
- Longer breaks (3-8 seconds) between different subreddits
- Small pauses every 10 posts (simulating scrolling)

### 2. **Mixed Browsing Patterns** 🔀
- Randomly browses "new", "hot", and "rising" posts
- Switches between different sorting methods (like using tabs)
- Randomizes the order of subreddit checks

### 3. **Varied Request Amounts** 📊
- Slightly varies the number of posts fetched each time (±10)
- Not always fetching the exact same amount (more natural)
- Keeps limits reasonable (20-150 posts)

### 4. **Realistic User Agent** 🌐
- Uses browser-like user agent strings
- Varies platform and version slightly
- Looks like: "MacOS:RedditTracker/1.0:v93.0 (by /u/tracker_bot)"

### 5. **Smart Error Handling** 🛡️
- Detects rate limiting (HTTP 429)
- Automatically waits 60 seconds if rate limited
- Continues gracefully on errors

### 6. **Duplicate Removal** 🔍
- Removes posts that appear in multiple subreddits
- Prevents looking at the same content twice

## 📈 How It Works

### Before (Robotic):
```
→ Fetch 100 posts from r/complaints (new)
→ Fetch 100 posts from r/techsupport (new)
→ Fetch 100 posts from r/ProductComplaints (new)
→ Done in 5 seconds
```

### After (Human-like):
```
→ Shuffle subreddit order
→ Fetch 95 posts from r/techsupport (hot & rising)
   ⏱️ Pause 0.5s every 10 posts
→ Wait 5.3 seconds (switching tabs)
→ Fetch 108 posts from r/complaints (new & hot)
   ⏱️ Pause 1.2s every 10 posts
→ Wait 3.7 seconds (switching tabs)
→ Fetch 102 posts from r/ProductComplaints (rising & new)
→ Remove 3 duplicate posts
→ Done in 45 seconds
```

## ⚙️ Timing Breakdown

| Action | Delay | Purpose |
|--------|-------|---------|
| Between API calls | 2-5 seconds | Simulate reading posts |
| Every 10 posts | 0.5-2 seconds | Simulate scrolling |
| Between subreddits | 3-8 seconds | Simulate tab switching |
| After rate limit | 60 seconds | Comply with Reddit limits |

## 🎯 Benefits

### ✅ Avoids Detection
- Looks like normal browsing activity
- Respects Reddit's rate limits
- Less likely to trigger bot detection

### ✅ Better Success Rate
- Automatically handles rate limiting
- Continues even if one subreddit fails
- More reliable long-term

### ✅ More Natural Data
- Gets posts from multiple sorting methods
- Catches trending posts you might miss
- Better coverage of complaints/demands

## 🔧 Customization

You can adjust the timing in `reddit_fetcher.py`:

### Make it Slower (More Cautious)
```python
self._human_delay(5, 10)  # Wait 5-10 seconds instead of 2-5
```

### Make it Faster (More Aggressive)
```python
self._human_delay(1, 2)  # Wait 1-2 seconds
```

**Note**: Being too fast may trigger rate limits!

## 📊 Expected Performance

With human-like behavior:
- **Time per subreddit**: ~15-30 seconds
- **3 subreddits**: ~1-2 minutes total
- **Success rate**: Much higher
- **Detection risk**: Much lower

## 🛡️ Rate Limit Protection

Reddit's official limits:
- **60 requests per minute** for authenticated apps
- **600 requests per 10 minutes**

Our approach:
- ~10-15 requests per minute (well under limit)
- Automatic 60s cooldown if limited
- Natural browsing patterns

## 💡 Tips

1. **Don't check too frequently**: Once per day is ideal
2. **Monitor logs**: Watch for rate limit warnings
3. **Adjust delays**: If you get rate limited, increase delays
4. **Use fewer subreddits**: Start with 2-3, expand later
5. **Be patient**: Slower = safer and more reliable

## 🎭 The Result

Your tracker now looks like:
- Someone browsing Reddit casually
- Checking different tabs and sorting options
- Reading posts at a natural pace
- Taking breaks between sections

**Not like**:
- A bot hitting the API rapidly
- Automated script with fixed timing
- Mass data scraper

---

**Stay under the radar! 🥷**
