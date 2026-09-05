#!/usr/bin/env python3
"""
FitLife Daily Facebook Auto-Poster
Posts: 2 Reels + 3 Image Posts Daily
Automatically shares all posts to Stories
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

# Post schedule: 2 reels + 3 images = 5 posts daily
POST_TYPES = ['reel', 'reel', 'image', 'image', 'image']  # 2 reels, 3 images

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
        subprocess.run(["git", "add", LOG_FILE, POSTS_FILE], capture_output=True)
        
        result = subprocess.run(["git", "diff", "--staged", "--quiet"], 
                               capture_output=True)
        
        if result.returncode != 0:
            subprocess.run(["git", "commit", "-m", f"📊 Update logs {datetime.now().strftime('%Y-%m-%d %H:%M')} [skip ci]"], 
                          capture_output=True)
            
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
# FACEBOOK POSTING FUNCTIONS
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

def get_next_post_by_type(posts, posted_ids, post_type):
    """
    Get the next unposted post of a specific type
    reel = has video_url
    image = has image_url
    """
    for post in posts:
        post_id = post.get('id', '')
        if post_id in posted_ids:
            continue
        
        if post_type == 'reel' and post.get('video_url', '').strip():
            return post
        elif post_type == 'image' and post.get('image_url', '').strip() and not post.get('video_url', '').strip():
            return post
    
    return None

def post_to_facebook(page_id, token, content, image_url=None, video_url=None):
    """
    Post to Facebook - handles text, image, and video
    Returns: (success, post_id)
    """
    try:
        if video_url:
            # Post as Reel/Video
            print("🎬 Posting as REEL...")
            url = f"{BASE_URL}/{page_id}/videos"
            payload = {
                "title": content[:60],
                "description": content,
                "file_url": video_url,
                "access_token": token,
                "published": "true",
                "content_category": "FITNESS"
            }
            response = requests.post(url, data=payload, timeout=60)
            
            if response.status_code == 200:
                post_id = response.json().get('id')
                print(f"✅ Reel posted! ID: {post_id}")
                return True, post_id
            else:
                error_msg = response.json().get('error', {}).get('message', 'Unknown error')
                print(f"❌ Reel failed: {error_msg}")
                return False, None
                
        elif image_url:
            # Post as Image
            print("🖼️ Posting as IMAGE...")
            url = f"{BASE_URL}/{page_id}/photos"
            payload = {
                "url": image_url,
                "caption": content,
                "access_token": token,
                "published": "true"
            }
            response = requests.post(url, data=payload, timeout=30)
            
            if response.status_code == 200:
                post_id = response.json().get('id')
                print(f"✅ Image posted! ID: {post_id}")
                return True, post_id
            else:
                error_msg = response.json().get('error', {}).get('message', 'Unknown error')
                print(f"❌ Image failed: {error_msg}")
                return False, None
        else:
            # Post as Text
            print("📝 Posting as TEXT...")
            url = f"{BASE_URL}/{page_id}/feed"
            payload = {
                "message": content,
                "access_token": token
            }
            response = requests.post(url, data=payload, timeout=30)
            
            if response.status_code == 200:
                post_id = response.json().get('id')
                print(f"✅ Text posted! ID: {post_id}")
                return True, post_id
            else:
                error_msg = response.json().get('error', {}).get('message', 'Unknown error')
                print(f"❌ Text failed: {error_msg}")
                return False, None
                
    except Exception as e:
        print(f"❌ Post error: {str(e)}")
        return False, None

def share_to_story(page_id, token, post_id):
    """
    Share a post to the page's Story
    """
    try:
        print(f"📱 Sharing post {post_id} to Story...")
        url = f"{BASE_URL}/{page_id}/stories"
        payload = {
            "media_id": post_id,
            "access_token": token,
            "story_type": "VIDEO" if "video" in str(post_id).lower() else "PHOTO"
        }
        
        response = requests.post(url, data=payload, timeout=30)
        
        if response.status_code == 200:
            print(f"✅ Post shared to Story! Story ID: {response.json().get('id')}")
            return True
        else:
            # Try alternative method if first fails
            print("🔄 Trying alternative story sharing method...")
            url = f"{BASE_URL}/{page_id}/feed"
            payload = {
                "message": "📱 Check out this post!",
                "access_token": token,
                "published": "false",
                "story_media_id": post_id
            }
            response = requests.post(url, data=payload, timeout=30)
            
            if response.status_code == 200:
                print(f"✅ Story share successful!")
                return True
            else:
                error_msg = response.json().get('error', {}).get('message', 'Unknown error')
                print(f"❌ Story share failed: {error_msg}")
                return False
                
    except Exception as e:
        print(f"❌ Story error: {str(e)}")
        return False

# ============================================
# MAIN EXECUTION
# ============================================

def run_poster():
    """Main execution function - 2 Reels + 3 Images daily"""
    print("🏋️ FitLife Daily - Auto-Poster")
    print("=" * 65)
    print(f"⏰ Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("📋 Schedule: 2 Reels + 3 Images daily")
    print("📱 Auto-share to Stories: Enabled")
    print()
    
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
    
    # Post 5 times daily: 2 Reels + 3 Images
    posts_scheduled = 0
    story_share_count = 0
    
    for post_type in POST_TYPES:
        print(f"\n{'='*50}")
        print(f"📤 Looking for {post_type.upper()} post...")
        
        # Get next unposted post of this type
        next_post = get_next_post_by_type(posts, posted_ids, post_type)
        
        if not next_post:
            print(f"⚠️ No {post_type} posts left! Skipping...")
            continue
        
        post_id = next_post.get('id', '')
        content = next_post.get('content', '').strip()
        image_url = next_post.get('image_url', '').strip()
        video_url = next_post.get('video_url', '').strip()
        
        print(f"📤 Post #{post_id}: {content[:50]}...")
        
        # Post to Facebook
        success, fb_post_id = post_to_facebook(PAGE_ID, ACCESS_TOKEN, content, image_url, video_url)
        
        if success and fb_post_id:
            # Mark as posted
            mark_as_posted(post_id)
            posts_scheduled += 1
            print(f"✅ {post_type.upper()} post {post_id} published!")
            
            # Share to Story
            print("📱 Attempting to share to Story...")
            if share_to_story(PAGE_ID, ACCESS_TOKEN, fb_post_id):
                story_share_count += 1
            else:
                print("⚠️ Story share failed, but post was successful.")
        else:
            print(f"❌ {post_type.upper()} post {post_id} failed.")
        
        # Wait between posts to avoid rate limiting
        if post_type != POST_TYPES[-1]:
            wait_time = random.randint(30, 60)
            print(f"⏳ Waiting {wait_time} seconds before next post...")
            time.sleep(wait_time)
    
    # Summary
    print(f"\n{'='*50}")
    print("📊 POSTING SUMMARY")
    print(f"   Total posts scheduled: {posts_scheduled} of 5")
    print(f"   Stories created: {story_share_count}")
    print(f"   Remaining posts: {len(posts) - len(posted_ids)}")
    
    # Push changes back to GitHub
    git_push()
    
    print("\n✨ Done!")

if __name__ == "__main__":
    run_poster()
