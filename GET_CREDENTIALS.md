# 🔑 How to Get Your Reddit API Credentials

## ⚠️ IMPORTANT: You're on the WRONG page!

### ❌ DON'T USE THIS:
- **Devvit** (developers.reddit.com) - This is for building Reddit apps
- The page with "npm create devvit@latest"
- That's NOT what you need!

### ✅ USE THIS INSTEAD:
- **Reddit API Apps** (old.reddit.com/prefs/apps)
- This gives you API credentials to READ Reddit data
- This is what our Python tool needs!

---

## 📝 Step-by-Step Instructions

### Step 1: Open the Correct Page

**Copy and paste this URL into your browser:**

```
https://www.reddit.com/prefs/apps
```

OR

```
https://old.reddit.com/prefs/apps
```

### Step 2: Log In

Use your Reddit account to log in.

### Step 3: What You'll See

You'll see a page that says:
- **"authorized applications"** at the top
- A list of any apps you've authorized
- At the BOTTOM, a button that says **"create another app..."** or **"are you a developer? create an app..."**

### Step 4: Click "Create App" Button

Scroll all the way to the bottom and click:
- **"create another app..."** or
- **"are you a developer? create an app..."**

### Step 5: Fill in the Form

A form will appear. Fill it in EXACTLY like this:

```
┌─────────────────────────────────────────┐
│ name: Reddit Tracker                     │
│                                          │
│ App type:                                │
│  ⚪ web app                              │
│  ⚪ installed app                        │
│  🔘 script  ← SELECT THIS ONE!          │
│  ⚪ personal use                         │
│                                          │
│ description: (optional)                  │
│  Personal Reddit monitoring tool        │
│                                          │
│ about url: (optional)                    │
│  [leave blank]                          │
│                                          │
│ redirect uri: (required)                 │
│  http://localhost:8080                  │
│                                          │
│ [create app]  ← CLICK THIS              │
└─────────────────────────────────────────┘
```

**IMPORTANT**: Make sure you select **"script"** as the app type!

### Step 6: Get Your Credentials

After clicking "create app", you'll see:

```
┌────────────────────────────────────────────┐
│ Reddit Tracker                              │
│ personal use script by YourUsername         │
│ [icon]                                      │
│                                             │
│ AbCd12EfGh34Ij  ← THIS IS YOUR CLIENT ID  │
│                                             │
│ secret                                      │
│ 1a2B3c4D5e6F7g8H9i0J1k2L3m  ← SECRET     │
│ (click "secret" to reveal)                  │
│                                             │
│ redirect uri                                │
│ http://localhost:8080                      │
│                                             │
│ [edit] [delete]                            │
└────────────────────────────────────────────┘
```

**Copy these two values:**
1. **Client ID**: The string right under your app name (looks random, ~14 characters)
2. **Secret**: Click the word "secret" to see it, then copy it (~27 characters)

### Step 7: Create Your .env File

Open Terminal and run:

```bash
cd "/Users/zhangfan/Desktop/reddit track"
nano .env
```

Paste this, but **REPLACE** with your actual credentials:

```env
REDDIT_CLIENT_ID=paste_your_client_id_here
REDDIT_CLIENT_SECRET=paste_your_secret_here

SUBREDDITS=complaints,techsupport,ProductComplaints
KEYWORDS=complaint,issue,problem,bug,demand,request,need,broken,not working
POST_LIMIT=50
REPORT_DIR=reports
```

Save: Press `Ctrl+O`, Enter, then `Ctrl+X`

### Step 8: Run the Program!

```bash
python3 main.py
```

---

## 🆘 Still Confused?

### The Difference:

| Devvit (WRONG) | Reddit API (CORRECT) |
|----------------|----------------------|
| Creates apps that run ON Reddit | Gets data FROM Reddit |
| Uses npm/JavaScript | Uses Python |
| For building Reddit features | For reading Reddit posts |
| The screenshot you sent | The page you actually need |

### Quick Check:

**Are you on the right page?**
- ✅ URL contains "reddit.com/prefs/apps"
- ✅ You see "authorized applications"
- ✅ Button says "create another app..."

**Are you on the wrong page?**
- ❌ URL contains "developers.reddit.com"
- ❌ You see "npm create devvit"
- ❌ Mentions "Devvit" anywhere

---

## 📞 Need Help?

If you're still stuck, tell me:
1. What URL are you currently at?
2. What do you see on the page?
3. Can you take a screenshot of the CORRECT page?

The correct page looks completely different from what you showed me!
