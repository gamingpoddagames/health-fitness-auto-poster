#!/usr/bin/env python3
"""
Health & Fitness Facebook Auto-Poster
Runs on GitHub Actions - Fully Automatic
Uses Facebook Graph API for text, images, and videos
"""

import os
import csv
import json
import requests
import time
import random
from datetime import datetime
from pathlib import Path

# ============================================
# CONFIGURATION - Environment Variables
# ============================================

PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")
ACCESS_TOKEN = os.environ.get("FACEBOOK_PAGE_ACCESS_TOKEN")
POSTS_FILE = "posts.csv"
LOG_FILE = "posted_log.txt"

# Facebook API endpoints
BASE_URL = "https://graph.facebook.com/v19.0"
PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")
ACCESS_TOKEN = os.environ.get("FACEBOOK_PAGE_ACCESS_TOKEN")

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

def post_video(page_id, token, message, video_url):
    """Post a video/Reel to Facebook Page"""
    url = f"{BASE_URL}/{page_id}/videos"
    payload = {
        "title": message[:60],  # Facebook limits title
        "description": message,
        "file_url": video_url,   # Must be a public URL
        "access_token": token,
        "published": "true"
    }
    
    try:
        response = requests.post(url, data=payload, timeout=60)  # Longer timeout for video
        
        if response.status_code == 200:
            print(f"✅ Video post successful! Post ID: {response.json().get('id')}")
            return True
        else:
            error_msg = response.json().get('error', {}).get('message', 'Unknown error')
            print(f"❌ Video post failed: {error_msg}")
            
            # Check if it's a copyright issue
            if "copyright" in error_msg.lower():
                print("   ⚠️ This video may have been flagged for copyright.")
                print("   Try using a different video source or text-only post.")
            
            return False
    except Exception as e:
        print(f"❌ Video post error: {str(e)}")
        return False

def should_post_now():
    """Check if it's a good time to post (avoid spam detection)"""
    # Add small random delay to look human
    delay = random.randint(5, 30)
    time.sleep(delay)
    return True

def run_poster():
    """Main execution function"""
    print("🏋️ Health & Fitness Auto-Poster (GitHub Actions)")
    print("=" * 60)
    print(f"⏰ Run time: {datetime.now().isoformat()}")
    
    # Validate credentials
    if not PAGE_ID or not ACCESS_TOKEN:
        print("❌ Missing PAGE_ID or ACCESS_TOKEN in environment!")
        print("   Add these as GitHub Secrets.")
        print("   FACEBOOK_PAGE_ID: Your page ID")
        print("   FACEBOOK_PAGE_ACCESS_TOKEN: Your long-lived access token")
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
        print(f"   Generated {len(posts)} new posts? Run content_generator.py again.")
        return
    
    post_id = next_post.get('id', '')
    content = next_post.get('content', '').strip()
    image_url = next_post.get('image_url', '').strip()
    video_url = next_post.get('video_url', '').strip()
    
    print(f"\n📤 Post #{post_id}: {content[:50]}...")
    print(f"   Image: {'Yes' if image_url else 'No'}")
    print(f"   Video: {'Yes' if video_url else 'No'}")
    
    # Check posting time
    if not should_post_now():
        print("⏰ Skipping post (random delay check failed)")
        return
    
    # Choose the right posting method
    success = False
    
    try:
        if video_url:
            print("🎬 Posting as VIDEO/REEL...")
            success = post_video(PAGE_ID, ACCESS_TOKEN, content, video_url)
            
            # If video fails, try text-only fallback
            if not success:
                print("🔄 Video failed. Falling back to text-only post...")
                success = post_text(PAGE_ID, ACCESS_TOKEN, content)
        
        elif image_url:
            print("🖼️ Posting as IMAGE...")
            success = post_image(PAGE_ID, ACCESS_TOKEN, content, image_url)
            
            # If image fails, try text-only fallback
            if not success:
                print("🔄 Image failed. Falling back to text-only post...")
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
        print(f"📝 Logged to {LOG_FILE}")
    else:
        print("❌ Post failed. Will retry next time.")
        print("   Check your Facebook token and Page permissions.")
    
    print("\n✨ Done!")

if __name__ == "__main__":
    run_poster()
