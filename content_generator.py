#!/usr/bin/env python3
"""
Content Generator for Health & Fitness Auto-Poster
Pulls free, copyright-safe content from public APIs
No copyrighted material - uses royalty-free sources only
"""

import csv
import requests
import random
from datetime import datetime

# ============================================
# FREE CONTENT SOURCES (No Copyright Issues)
# ============================================

# 1. Text Content - General Health Tips (Not Copyrightable)
HEALTH_TIPS = [
    "💪 Start your day with 5 minutes of dynamic stretching to wake up your muscles!",
    "🥗 Add a handful of spinach to your morning smoothie for extra iron and fiber.",
    "💧 Drink 8 glasses of water daily. Set reminders every 2 hours!",
    "😴 Get 7-8 hours of sleep for optimal muscle recovery and hormone balance.",
    "🏃 Mix cardio and strength training: 3x strength + 2x cardio weekly.",
    "🧘 Take 5 deep breaths. Roll your shoulders back. Stress relief in 60 seconds!",
    "🎯 Write down one fitness goal this week. Make it realistic and specific.",
    "📱 Try a 7-minute workout app on busy days. Something beats nothing!",
    "🥑 Healthy snack: Avocado with sea salt and chili flakes. Delicious and filling!",
    "🔥 Quick HIIT: 20 sec work / 10 sec rest x 8 rounds. Done in 4 minutes!",
    "🚶 Walk 10 minutes after each meal to aid digestion and stabilize blood sugar.",
    "🧠 Train your brain: Learn a new skill or read 10 pages daily.",
    "🌿 Get outside: 15 minutes of sunlight boosts Vitamin D and mood.",
    "🍽️ Eat protein within 30 minutes post-workout for optimal muscle repair.",
    "📊 Track your progress weekly. What gets measured gets improved!",
    "🎵 Workout playlist: Upbeat music increases performance by 15%!",
    "👟 Replace workout shoes every 300-500 miles to prevent injury.",
    "🧖 Post-workout: Stretch and foam roll for faster recovery.",
    "🌙 Evening routine: Dim lights 1 hour before bed for better sleep.",
    "💪 Progressive overload: Increase weight or reps by 5% weekly."
]

MOTIVATIONAL_QUOTES = [
    "✨ 'The only bad workout is the one that didn't happen.'",
    "🌟 'Your body can do it. Your mind is the one that needs convincing.'",
    "🔥 'Discipline = Freedom. Show up every day.'",
    "💫 'Don't wish for it. Work for it.'",
    "⚡ 'Motivation gets you started. Habit keeps you going.'",
    "🎯 'Progress, not perfection. Every step counts.'",
    "🙌 'You are stronger than you think. Prove it to yourself.'",
    "🚀 'The pain you feel today is the strength you'll feel tomorrow.'",
    "💎 'Small daily improvements = massive results over time.'",
    "⭐ 'Your only competition is the person in the mirror.'"
]

FITNESS_FACTS = [
    "📊 Did you know? Walking 10,000 steps burns ~400-500 calories!",
    "📊 Fun fact: Your heart is a muscle. Cardio strengthens it!",
    "📊 Interesting: Muscle weighs more than fat but takes up less space.",
    "📊 Quick fact: Stretching increases blood flow to muscles by 30%.",
    "📊 True: Hydration boosts metabolism by up to 30% for 1 hour.",
    "📊 Surprising: Laughter burns calories! It's a mini-workout.",
    "📊 Did you know? It takes 21 days to form a new habit.",
    "📊 Fact: Protein needs increase as you age. Prioritize it!",
    "📊 Quick tip: Rest days prevent burnout and injury.",
    "📊 True: Consistency beats intensity. Show up daily!"
]

def get_random_text():
    """Generate random health/fitness text content"""
    all_texts = HEALTH_TIPS + MOTIVATIONAL_QUOTES + FITNESS_FACTS
    return random.choice(all_texts)

# 2. Free Images - Using Lorem Picsum (Free Stock Photos)
def get_random_image_url(width=800, height=600):
    """
    Get random free image from Lorem Picsum
    These are high-quality royalty-free images
    """
    # For fitness-themed images, we can use specific seed
    seed = random.randint(1, 1000)
    return f"https://picsum.photos/seed/{seed}/{width}/{height}"

# 3. Free Videos - Using Sample Videos
# These are public domain/CC0 sample videos that are safe to use
SAMPLE_VIDEOS = [
    "https://sample-videos.com/video321/mp4/240/big_buck_bunny_240p_1mb.mp4",
    "https://sample-videos.com/video321/mp4/240/big_buck_bunny_240p_2mb.mp4",
    "https://sample-videos.com/video321/mp4/240/big_buck_bunny_240p_3mb.mp4",
    "https://sample-videos.com/video321/mp4/240/big_buck_bunny_240p_4mb.mp4",
    "https://sample-videos.com/video321/mp4/240/big_buck_bunny_240p_5mb.mp4",
]

def get_random_video_url():
    """Get a random sample video URL (public domain content)"""
    return random.choice(SAMPLE_VIDEOS)

# 4. Generate Complete Posts
def generate_posts(count=30):
    """
    Generate a list of posts with text, image, and video options
    Mix of text-only, image, and video posts
    """
    posts = []
    
    for i in range(1, count + 1):
        post_type = random.choice(['text', 'image', 'video'])
        
        # Generate text content
        content = get_random_text()
        
        post = {
            'id': f'post{i:03d}',
            'content': content,
            'image_url': '',
            'video_url': ''
        }
        
        # Add image or video based on type
        if post_type == 'image':
            post['image_url'] = get_random_image_url()
        elif post_type == 'video':
            post['video_url'] = get_random_video_url()
        # Text-only posts have no media
        
        posts.append(post)
    
    return posts

def save_posts_to_csv(posts, filename='posts.csv'):
    """Save generated posts to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'content', 'image_url', 'video_url'])
        writer.writeheader()
        writer.writerows(posts)
    
    print(f"✅ Generated {len(posts)} posts saved to {filename}")

if __name__ == "__main__":
    print("🎨 Generating Health & Fitness Content...")
    print("=" * 50)
    
    posts = generate_posts(50)  # Generate 50 posts
    save_posts_to_csv(posts)
    
    print("\n📊 Sample post:")
    sample = random.choice(posts)
    print(f"ID: {sample['id']}")
    print(f"Content: {sample['content'][:60]}...")
    print(f"Image: {sample['image_url'] or 'None'}")
    print(f"Video: {sample['video_url'] or 'None'}")
    print("\n✨ Done! Run 'python fb_poster.py' to post.")
