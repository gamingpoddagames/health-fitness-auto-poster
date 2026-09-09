#!/usr/bin/env python3
"""
FitLife Daily - Content Generator
"""

import csv
import os
import random
import glob
from datetime import datetime

# ============================================
# HELPERS
# ============================================

def get_images():
    """Get all images from images/ folder"""
    images = glob.glob("images/*.png")
    if not images:
        print("No images found! Creating default images...")
        create_default_images()
        images = glob.glob("images/*.png")
    return images[:20]

def get_videos():
    """Get all videos from videos/ folder"""
    videos = glob.glob("videos/*.mp4")
    if not videos:
        print("No videos found! Creating default videos...")
        create_default_videos()
        videos = glob.glob("videos/*.mp4")
    return videos[:10]

def create_default_images():
    """Create fallback images"""
    os.makedirs("images", exist_ok=True)
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("PIL not installed, cannot create images")
        return
    
    titles = ["Morning Stretch", "HIIT Workout", "Healthy Tip", "Yoga Flow", "Motivation"]
    
    for i, title in enumerate(titles):
        img = Image.new('RGB', (800, 800), color="#1a237e")
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 60)
            font2 = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 30)
        except:
            font = ImageFont.load_default()
            font2 = ImageFont.load_default()
        
        draw.rectangle([0, 0, 800, 20], fill="#4fc3f7")
        draw.rectangle([0, 780, 800, 800], fill="#4fc3f7")
        
        bbox = draw.textbbox((0, 0), title, font=font)
        x = (800 - (bbox[2] - bbox[0])) // 2
        draw.text((x, 300), title, fill="#ffffff", font=font)
        
        brand = "FitLife Daily"
        bbox = draw.textbbox((0, 0), brand, font=font2)
        x = (800 - (bbox[2] - bbox[0])) // 2
        draw.text((x, 700), brand, fill="#4fc3f7", font=font2)
        
        filename = f"images/image_{i:03d}.png"
        img.save(filename)
        print(f"Created fallback: {filename}")

def create_default_videos():
    """Create fallback videos if moviepy is installed"""
    try:
        from moviepy.editor import ColorClip
        os.makedirs("videos", exist_ok=True)
        
        for i in range(3):
            clip = ColorClip(size=(1080, 1920), color=(26, 35, 126), duration=5)
            filename = f"videos/reel_{i:03d}.mp4"
            clip.write_videofile(filename, fps=24, verbose=False, logger=None)
            print(f"Created fallback: {filename}")
    except ImportError:
        print("moviepy not installed, cannot create videos")

# ============================================
# CONTENT
# ============================================

VIDEO_CONTENT = [
    "Intense Workout Session! Remember: The only bad workout is the one that didn't happen.\n\n#WorkoutMotivation #FitLifeDaily",
    "Master Your Squat Form! Feet apart, Chest up, Push through heels\n\n#SquatForm #FitLifeDaily",
    "4-Minute HIIT! 20 sec work / 10 sec rest x 8 rounds\n\n#HIIT #QuickWorkout #FitLifeDaily",
    "Morning Stretch Routine - 5 minutes to start your day!\n\n#MorningRoutine #FitLifeDaily",
    "Find Your Balance - Yoga flow for beginners\n\n#Yoga #Mindfulness #FitLifeDaily",
]

def generate_posts():
    """Generate posts with valid image and video paths"""
    posts = []
    
    images = get_images()
    videos = get_videos()
    
    print(f"Found {len(images)} images, {len(videos)} videos")
    
    # Image posts
    for i, img in enumerate(images, 1):
        content = f"FitLife Daily\n\nCheck out this fitness tip!\n\n#FitLifeDaily #Fitness #Health"
        posts.append({
            'id': f'post{i:03d}',
            'content': content,
            'image_url': os.path.abspath(img),
            'video_url': ''
        })
    
    # Video posts
    for i, vid in enumerate(videos, len(images) + 1):
        idx = i - len(images) - 1
        content = VIDEO_CONTENT[idx % len(VIDEO_CONTENT)]
        posts.append({
            'id': f'post{i:03d}',
            'content': content,
            'image_url': '',
            'video_url': os.path.abspath(vid)
        })
    
    random.shuffle(posts)
    
    for i, p in enumerate(posts, 1):
        p['id'] = f'post{i:03d}'
    
    return posts

def save_posts(posts):
    with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'content', 'image_url', 'video_url'])
        w.writeheader()
        w.writerows(posts)
    print(f"Generated {len(posts)} posts")

def print_stats(posts):
    total = len(posts)
    with_images = sum(1 for p in posts if p['image_url'])
    with_videos = sum(1 for p in posts if p['video_url'])
    print(f"Stats: {total} total, {with_images} images, {with_videos} videos")

if __name__ == "__main__":
    print("FitLife Daily - Content Generator")
    print("=" * 55)
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    posts = generate_posts()
    save_posts(posts)
    print_stats(posts)
    print("\nRun 'python fb_poster.py' to start posting")
