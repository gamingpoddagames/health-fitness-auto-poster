#!/usr/bin/env python3
"""
FitLife Daily - Facebook Auto-Poster
Posts text-only content - no external dependencies
"""

import os
import csv
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

POSTS_PER_RUN = 5

# ============================================
# GIT HELPER
# ============================================

def git_safe_push():
    try:
        subprocess.run(["git", "config", "--local", "user.email", "action@github.com"], capture_output=True)
        subprocess.run(["git", "config", "--local", "user.name", "GitHub Action Bot"], capture_output=True)
        subprocess.run(["git", "add", LOG_FILE, POSTS_FILE], capture_output=True)
        
        result = subprocess.run(["git", "diff", "--staged", "--quiet"], capture_output=True)
        if result.returncode != 0:
            subprocess.run(["git", "commit", "-m", "Update logs [skip ci]"], capture_output=True)
            for attempt in range(3):
                push_result = subprocess.run(["git", "push", "origin", "main"], capture_output=True)
                if push_result.returncode == 0:
                    print("Git push successful")
                    return True
                subprocess.run(["git", "pull", "--rebase", "origin", "main"], capture_output=True)
                time.sleep(2)
        return True
    except Exception as e:
        print(f"Git error: {e}")
        return False

# ============================================
# FACEBOOK POSTING
# ============================================

def load_posts():
    if not Path(POSTS_FILE).exists():
        return []
    with open(POSTS_FILE, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def get_posted_ids():
    if not Path(LOG_FILE).exists():
        return set()
    with open(LOG_FILE, 'r') as f:
        return {line.strip() for line in f.readlines()}

def mark_as_posted(post_id):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{post_id}\n")
        f.flush()

def get_next_post(posts, posted_ids):
    for post in posts:
        if post['id'] not in posted_ids:
            return post
    return None

def post_to_facebook(content):
    """Post text content to Facebook"""
    try:
        url = f"{BASE_URL}/{PAGE_ID}/feed"
        payload = {
            "message": content,
            "access_token": ACCESS_TOKEN
        }
        
        response = requests.post(url, data=payload, timeout=60)
        
        if response.status_code == 200:
            post_id = response.json().get('id')
            print(f"Posted! ID: {post_id}")
            return True, post_id
        else:
            error = response.json().get('error', {})
            error_msg = error.get('message', 'Unknown error')
            print(f"Failed: {error_msg}")
            return False, None
            
    except Exception as e:
        print(f"Error: {e}")
        return False, None

def share_to_story(post_id):
    """Try to share to story"""
    try:
        url = f"{BASE_URL}/{PAGE_ID}/stories"
        payload = {
            "media_id": post_id,
            "access_token": ACCESS_TOKEN
        }
        response = requests.post(url, data=payload, timeout=30)
        if response.status_code == 200:
            print("Shared to Story")
            return True
        return False
    except:
        return False

# ============================================
# MAIN
# ============================================

def run_poster():
    print("FitLife Daily - Auto-Poster")
    print("=" * 70)
    print(f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if not PAGE_ID or not ACCESS_TOKEN:
        print("Missing FACEBOOK_PAGE_ID or FACEBOOK_PAGE_ACCESS_TOKEN")
        print("Please add these as GitHub Secrets or environment variables")
        return
    
    posts = load_posts()
    if not posts:
        print("No posts found! Run content_generator.py first.")
        return
    
    posted_ids = get_posted_ids()
    total = len(posts)
    remaining = total - len(posted_ids)
    
    print(f"Posts: {len(posted_ids)} posted, {remaining} remaining")
    
    if remaining <= 0:
        print("ALL POSTS PUBLISHED!")
        return
    
    posts_to_post = min(POSTS_PER_RUN, remaining)
    posts_scheduled = 0
    story_count = 0
    
    for i in range(posts_to_post):
        print(f"\n{'-'*50}")
        
        post = get_next_post(posts, posted_ids)
        if not post:
            print("No more posts available")
            break
        
        print(f"Post #{post['id']}")
        content_preview = post['content'][:60] + "..."
        print(f"Content: {content_preview}")
        
        success, fb_id = post_to_facebook(post['content'])
        
        if success and fb_id:
            mark_as_posted(post['id'])
            posted_ids.add(post['id'])
            posts_scheduled += 1
            
            if share_to_story(fb_id):
                story_count += 1
        else:
            # Mark as posted anyway to avoid infinite loop
            mark_as_posted(post['id'])
            posted_ids.add(post['id'])
        
        if i < posts_to_post - 1:
            wait_time = random.randint(30, 60)
            print(f"Waiting {wait_time} seconds...")
            time.sleep(wait_time)
    
    print(f"\n{'='*50}")
    print("SUMMARY")
    print(f"Posts scheduled: {posts_scheduled}")
    print(f"Stories created: {story_count}")
    print(f"Remaining posts: {len(posts) - len(posted_ids)}")
    
    git_safe_push()
    print("Done!")

if __name__ == "__main__":
    run_poster()
