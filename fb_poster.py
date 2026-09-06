#!/usr/bin/env python3
"""
FitLife Daily - Facebook Auto-Poster
Posts: 2 Reels + 3 Images daily
NO DUPLICATES - Each post only once
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

POST_TYPES = ['reel', 'reel', 'image', 'image', 'image']

# ============================================
# GIT HELPER
# ============================================

def git_safe_push():
    try:
        subprocess.run(["git", "config", "--local", "user.email", "action@github.com"], capture_output=True)
        subprocess.run(["git", "config", "--local", "user.name", "GitHub Action Bot"], capture_output=True)
        subprocess.run(["git", "fetch", "origin", "main"], capture_output=True)
        subprocess.run(["git", "add", LOG_FILE, POSTS_FILE], capture_output=True)
        
        result = subprocess.run(["git", "diff", "--staged", "--quiet"], capture_output=True)
        if result.returncode != 0:
            subprocess.run(["git", "commit", "-m", f"📊 Update logs [skip ci]"], capture_output=True)
            for attempt in range(3):
                push_result = subprocess.run(["git", "push", "origin", "main", "--force-with-lease"], capture_output=True)
                if push_result.returncode == 0:
                    print("✅ Git push successful")
                    return True
                subprocess.run(["git", "pull", "--rebase", "origin", "main"], capture_output=True)
                time.sleep(2)
        return True
    except Exception as e:
        print(f"❌ Git error: {e}")
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

def get_next_post(posts, posted_ids, post_type):
    for post in posts:
        if post['id'] in posted_ids:
            continue
        if post_type == 'reel' and post.get('video_url', '').strip():
            return post
        if post_type == 'image' and post.get('image_url', '').strip() and not post.get('video_url', '').strip():
            return post
    return None

def post_to_facebook(content, image_url=None, video_url=None):
    try:
        if video_url:
            print("🎬 Posting as REEL...")
            url = f"{BASE_URL}/{PAGE_ID}/videos"
            payload = {
                "title": content[:60],
                "description": content,
                "file_url": video_url,
                "access_token": ACCESS_TOKEN,
                "published": "true",
                "content_category": "FITNESS"
            }
        elif image_url:
            print("🖼️ Posting as IMAGE...")
            url = f"{BASE_URL}/{PAGE_ID}/photos"
            payload = {
                "url": image_url,
                "caption": content,
                "access_token": ACCESS_TOKEN,
                "published": "true"
            }
        else:
            print("📝 Posting as TEXT...")
            url = f"{BASE_URL}/{PAGE_ID}/feed"
            payload = {
                "message": content,
                "access_token": ACCESS_TOKEN
            }
        
        response = requests.post(url, data=payload, timeout=60)
        if response.status_code == 200:
            post_id = response.json().get('id')
            print(f"✅ Posted! ID: {post_id}")
            return True, post_id
        else:
            print(f"❌ Failed: {response.json().get('error', {}).get('message', 'Unknown')}")
            return False, None
    except Exception as e:
        print(f"❌ Error: {e}")
        return False, None

def share_to_story(post_id):
    try:
        url = f"{BASE_URL}/{PAGE_ID}/stories"
        payload = {
            "media_id": post_id,
            "access_token": ACCESS_TOKEN
        }
        response = requests.post(url, data=payload, timeout=30)
        if response.status_code == 200:
            print("✅ Shared to Story!")
            return True
        return False
    except:
        return False

# ============================================
# MAIN
# ============================================

def run_poster():
    print("🏋️ FitLife Daily - Auto-Poster")
    print("=" * 65)
    print(f"⏰ Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if not PAGE_ID or not ACCESS_TOKEN:
        print("❌ Missing FACEBOOK_PAGE_ID or FACEBOOK_PAGE_ACCESS_TOKEN")
        return
    
    posts = load_posts()
    if not posts:
        print("❌ No posts found! Run content_generator.py first.")
        return
    
    posted_ids = get_posted_ids()
    total = len(posts)
    remaining = total - len(posted_ids)
    
    print(f"📊 Posts: {len(posted_ids)} posted, {remaining} remaining")
    
    if remaining <= 0:
        print("🎉 ALL POSTS PUBLISHED!")
        return
    
    posts_to_post = min(5, remaining)
    posts_scheduled = 0
    story_count = 0
    
    for post_type in POST_TYPES[:posts_to_post]:
        post = get_next_post(posts, posted_ids, post_type)
        if not post:
            print(f"⚠️ No {post_type} posts left")
            continue
        
        print(f"\n📤 Post #{post['id']} ({post_type.upper()})")
        success, fb_id = post_to_facebook(
            post['content'],
            post.get('image_url', ''),
            post.get('video_url', '')
        )
        
        if success and fb_id:
            mark_as_posted(post['id'])
            posted_ids.add(post['id'])
            posts_scheduled += 1
            if share_to_story(fb_id):
                story_count += 1
        
        if posts_scheduled < posts_to_post:
            time.sleep(random.randint(30, 60))
    
    print(f"\n📊 Summary: {posts_scheduled} posts, {story_count} stories")
    git_safe_push()
    print("✨ Done!")

if __name__ == "__main__":
    run_poster()
