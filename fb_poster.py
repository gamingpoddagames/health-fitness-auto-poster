#!/usr/bin/env python3
"""
Health & Fitness Facebook Auto-Poster
Runs on GitHub Actions - Fully Automatic
"""

import os
import csv
import json
import requests
import time
import random
import subprocess
from datetime import datetime
from pathlib import Path

# ============================================
# CONFIGURATION
# ============================================

PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")
ACCESS_TOKEN = os.environ.get("FACEBOOK_PAGE_ACCESS_TOKEN")
POSTS_FILE = "posts.csv"
LOG_FILE = "posted_log.txt"
BASE_URL = "https://graph.facebook.com/v19.0"

# ============================================
# GIT HELPER FUNCTIONS
# ============================================

def git_pull():
    """Pull latest changes before making updates"""
    try:
        subprocess.run(["git", "pull", "--rebase", "origin", "main"], 
                      capture_output=True, check=False)
        print("✅ Git pull completed")
    except Exception as e:
        print(f"⚠️ Git pull error: {e}")

def git_push():
    """Push changes to GitHub"""
    try:
        # Add files
        subprocess.run(["git", "add", LOG_FILE, POSTS_FILE], capture_output=True)
        
        # Check if there are changes
        result = subprocess.run(["git", "diff", "--staged", "--quiet"], 
                               capture_output=True)
        
        if result.returncode != 0:
            # There are changes to commit
            subprocess.run(["git", "commit", "-m", f"📊 Update logs {datetime.now().strftime('%Y-%m-%d %H:%M')} [skip ci]"], 
                          capture_output=True)
            
            # Push with retry
            for attempt in range(3):
                push_result = subprocess.run(
                    ["git", "push", "origin", "main", "--force-with-lease"],
                    capture_output=True
                )
                if push_result.returncode == 0:
                    print("✅ Git push successful")
                    return True
                else:
                    print(f"⚠️ Push attempt {attempt + 1} failed. Retrying...")
                    # Pull latest before retry
                    git_pull()
                    time.sleep(2)
            
            print("❌ Git push failed after 3 attempts")
            return False
        
        print("ℹ️ No changes to commit")
        return True
        
    except Exception as e:
        print(f"❌ Git error: {e}")
        return False

# ============================================
# CORE FUNCTIONS
# ============================================

def load_posts():
    """Load posts from CSV file"""
    if not Path(POSTS_FILE).exists():
        print(f"❌ {POSTS_FILE} not found!")
        return []
    
    posts = []
    with open(POSTS_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            posts.append(row)
    
    print(f"✅ Loaded {len(posts)} posts from {POSTS_FILE}")
    return posts

def get_posted_ids():
    """Read which posts have been published"""
    if not Path(LOG_FILE).exists():
        return set()
    
    with open(LOG_FILE, 'r') as f:
        return {line.strip() for line in f.readlines()}

def mark_as_posted(post_id):
    """Record a post as published"""
    with open(LOG_FILE, 'a') as f:
        f.write(f"{post_id}\n")
        f.flush()

def post_text(page_id, token, message):
    """Post plain text to Facebook Page"""
    url = f"{BASE_URL}/{page_id}/feed"
    payload = {
        "message": message,
        "access_token": token
    }
    
    try:
        response = requests.post(url, data=payload, timeout=30)
        
        if response.status_code == 200:
            print(f"✅ Text post successful! Post ID: {response.json().get('id')}")
            return True
        else:
            error_msg = response.json().get('error', {}).get('message', 'Unknown error')
            print(f"❌ Text post failed: {error_msg}")
            return False
    except Exception as e:
        print(f"❌ Text post error: {str(e)}")
        return False

def post_image(page_id, token, message, image_url):
    """Post image with caption to Facebook Page"""
    url = f"{BASE_URL}/{page_id}/photos"
    payload = {
        "url": image_url,
        "caption": message,
        "access_token": token,
        "published": "true"
    }
    
    try:
        response = requests.post(url, data=payload, timeout=30)
        
        if response.status_code == 200:
            print(f"✅ Image post successful! Post ID: {response.json().get('id')}")
            return True
        else:
            error_msg = response.json().get('error', {}).get('message', 'Unknown error')
            print(f"❌ Image post failed: {error_msg}")
            return False
    except Exception as e:
        print(f"❌ Image post error: {str(e)}")
        return False

def should_post_now():
    """Check if it's a good time to post"""
    delay = random.randint(5, 30)
    time.sleep(delay)
    return True

def run_poster():
    """Main execution function"""
    print("🏋️ Health & Fitness Auto-Poster (GitHub Actions)")
    print("=" * 60)
    print(f"⏰ Run time: {datetime.now().isoformat()}")
    
    # Pull latest changes
    git_pull()
    
    # Validate credentials
    if not PAGE_ID or not ACCESS_TOKEN:
        print("❌ Missing PAGE_ID or ACCESS_TOKEN in environment!")
        return
    
    # Load content
    posts = load_posts()
    if not posts:
        print("❌ No posts found! Run content_generator.py first.")
        return
    
    # Check what's already posted
    posted_ids = get_posted_ids()
    print(f"📊 Already posted: {len(posted_ids)} of {len(posts)}")
    
    # Find next unposted post
    next_post = None
    for post in posts:
        post_id = post.get('id', '')
        if post_id and post_id not in posted_ids:
            next_post = post
            break
    
    if not next_post:
        print("🎉 All posts have been published!")
        return
    
    post_id = next_post.get('id', '')
    content = next_post.get('content', '').strip()
    image_url = next_post.get('image_url', '').strip()
    video_url = next_post.get('video_url', '').strip()
    
    print(f"\n📤 Post #{post_id}: {content[:50]}...")
    
    # Post
    success = False
    
    try:
        if image_url:
            print("🖼️ Posting as IMAGE...")
            success = post_image(PAGE_ID, ACCESS_TOKEN, content, image_url)
            if not success:
                print("🔄 Image failed. Falling back to text-only...")
                success = post_text(PAGE_ID, ACCESS_TOKEN, content)
        else:
            print("📝 Posting as TEXT...")
            success = post_text(PAGE_ID, ACCESS_TOKEN, content)
    
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        success = False
    
    # Log the result
    if success:
        mark_as_posted(post_id)
        print(f"✅ Post {post_id} marked as published")
    
    # Push changes back to GitHub
    git_push()
    
    print("\n✨ Done!")

if __name__ == "__main__":
    run_poster()
