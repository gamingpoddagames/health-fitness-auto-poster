#!/usr/bin/env python3
"""
FitLife Daily - Facebook Auto-Poster (FIXED)
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

def get_file_url(file_path):
    """Convert local file path to URL or full path"""
    if not file_path:
        return None
    
    # If it's already a URL (starts with http), return it
    if file_path.startswith('http'):
        return file_path
    
    # If it's a local file, check if it exists
    if os.path.exists(file_path):
        # For GitHub Actions, we need absolute path
        return os.path.abspath(file_path)
    
    # If file doesn't exist, try to find it in images/ folder
    alt_path = f"images/{os.path.basename(file_path)}"
    if os.path.exists(alt_path):
        return os.path.abspath(alt_path)
    
    return None

def post_to_facebook(content, image_path=None, video_path=None):
    try:
        if video_path:
            print("🎬 Posting as REEL...")
            url = f"{BASE_URL}/{PAGE_ID}/videos"
            payload = {
                "title": content[:60],
                "description": content,
                "file_url": video_path,  # Can be URL or local path
                "access_token": ACCESS_TOKEN,
                "published": "true",
                # FIXED: Use correct Facebook category
                "content_category": "FITNESS"
            }
            
            # If video is local file, upload it
            if not video_path.startswith('http') and os.path.exists(video_path):
                print(f"📤 Uploading local video: {video_path}")
                with open(video_path, 'rb') as f:
                    files = {'source': f}
                    response = requests.post(
                        url,
                        data={
                            "title": content[:60],
                            "description": content,
                            "access_token": ACCESS_TOKEN,
                            "published": "true",
                            "content_category": "FITNESS"
                        },
                        files=files,
                        timeout=120
                    )
            else:
                response = requests.post(url, data=payload, timeout=120)
            
        elif image_path:
            print("🖼️ Posting as IMAGE...")
            url = f"{BASE_URL}/{PAGE_ID}/photos"
            
            # If image is local file
            if os.path.exists(image_path):
                print(f"📤 Uploading local image: {image_path}")
                with open(image_path, 'rb') as f:
                    files = {'source': f}
                    response = requests.post(
                        url,
                        data={
                            "caption": content,
                            "access_token": ACCESS_TOKEN,
                            "published": "true"
                        },
                        files=files,
                        timeout=60
                    )
            else:
                payload = {
                    "url": image_path,
                    "caption": content,
                    "access_token": ACCESS_TOKEN,
                    "published": "true"
                }
                response = requests.post(url, data=payload, timeout=60)
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
            error = response.json().get('error', {})
            error_msg = error.get('message', 'Unknown error')
            print(f"❌ Failed: {error_msg}")
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
        
        # Get file paths
        image_file = post.get('image_url', '').strip()
        video_file = post.get('video_url', '').strip()
        
        # Fix file paths
        if image_file:
            image_file = get_file_url(image_file)
            if not image_file:
                print(f"⚠️ Image file not found: {post.get('image_url', '')}")
                continue
        
        if video_file:
            video_file = get_file_url(video_file)
            if not video_file:
                print(f"⚠️ Video file not found: {post.get('video_url', '')}")
                continue
        
        print(f"\n📤 Post #{post['id']} ({post_type.upper()})")
        success, fb_id = post_to_facebook(
            post['content'],
            image_file,
            video_file
        )
        
        if success and fb_id:
            mark_as_posted(post['id'])
            posted_ids.add(post['id'])
            posts_scheduled += 1
            if share_to_story(fb_id):
                story_count += 1
        
        if posts_scheduled < posts_to_post:
            wait_time = random.randint(30, 60)
            print(f"⏳ Waiting {wait_time} seconds...")
            time.sleep(wait_time)
    
    print(f"\n📊 Summary: {posts_scheduled} posts, {story_count} stories")
    git_safe_push()
    print("✨ Done!")

if __name__ == "__main__":
    run_poster()
