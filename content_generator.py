#!/usr/bin/env python3
"""
FitLife Daily - Money-Making Content Generator
Creates posts that drive traffic and generate revenue
"""

import csv
import random
from datetime import datetime

# ============================================
# YOUR MONETIZATION LINKS
# ============================================

YOUR_WEBSITE = "https://yourblog.com"
YOUR_AFFILIATE_LINK = "https://amzn.to/your-affiliate-id"
YOUR_PRODUCT_LINK = "https://gumroad.com/your-product"
YOUR_EMAIL_LIST = "https://yourwebsite.com/free-plan"

# ============================================
# MONEY-MAKING POSTS
# ============================================

MONEY_POSTS = [
    # Type 1: Traffic to Blog (Ad Revenue)
    {
        "content": "⚡ 4-Minute HIIT for Busy People!\n\n20 seconds work / 10 seconds rest\n8 rounds - only 4 minutes!\n\n🔹 Jump Squats\n🔹 Burpees\n🔹 Mountain Climbers\n🔹 High Knees\n\n👉 Full guide: {blog_link}\n\n#HIIT #FitLifeDaily",
        "link_type": "blog"
    },
    {
        "content": "💪 5-Minute Morning Stretch Routine!\n\n✅ Neck rolls\n✅ Arm circles\n✅ Torso twists\n✅ Leg swings\n\n👉 Full routine: {blog_link}\n\n#MorningRoutine #FitLifeDaily",
        "link_type": "blog"
    },
    
    # Type 2: Affiliate Products (Commission)
    {
        "content": "💪 Best Protein Powder for Muscle Growth!\n\n✅ 25g protein per scoop\n✅ No artificial sweeteners\n✅ Mixes perfectly\n\n👉 Get 30% OFF: {affiliate_link}\n\n#Fitness #Protein #FitLifeDaily",
        "link_type": "affiliate"
    },
    {
        "content": "🏋️ Must-Have Home Gym Equipment!\n\n✅ Adjustable Dumbbells\n✅ Resistance Bands\n✅ Yoga Mat\n\n👉 Shop here: {affiliate_link}\n\n#HomeGym #Fitness #FitLifeDaily",
        "link_type": "affiliate"
    },
    {
        "content": "👟 Best Running Shoes 2026!\n\n✅ Maximum comfort\n✅ Injury prevention\n✅ 5-star reviews\n\n👉 Check price: {affiliate_link}\n\n#Running #FitnessGear #FitLifeDaily",
        "link_type": "affiliate"
    },
    
    # Type 3: Own Products (Direct Sales)
    {
        "content": "🔥 30-Day Home Workout Challenge!\n\nTransform your body:\n✅ No equipment\n✅ 15 min daily\n✅ Beginner-friendly\n\n📘 Get plan: {product_link}\n\n#FitnessChallenge #FitLifeDaily",
        "link_type": "product"
    },
    {
        "content": "🥗 Complete Meal Prep Guide!\n\n✅ 50+ recipes\n✅ Shopping lists\n✅ Macro breakdowns\n\n📘 Download: {product_link}\n\n#MealPrep #HealthyEating #FitLifeDaily",
        "link_type": "product"
    },
    
    # Type 4: Email List Building (Free Lead Magnet)
    {
        "content": "💪 FREE 7-Day Workout Plan!\n\n✅ Daily 15-min workouts\n✅ No equipment needed\n✅ Printable PDF\n\n👉 Download FREE: {email_link}\n\n#FreeWorkout #Fitness #FitLifeDaily",
        "link_type": "email"
    },
    {
        "content": "🥗 FREE Healthy Meal Plan!\n\n✅ 7 days of meals\n✅ Shopping list included\n✅ Beginner-friendly\n\n👉 Get FREE: {email_link}\n\n#FreeMealPlan #HealthyEating #FitLifeDaily",
        "link_type": "email"
    },
]

def replace_links(content, link_type):
    """Replace link placeholders with actual URLs"""
    if link_type == "blog":
        return content.replace("{blog_link}", YOUR_WEBSITE)
    elif link_type == "affiliate":
        return content.replace("{affiliate_link}", YOUR_AFFILIATE_LINK)
    elif link_type == "product":
        return content.replace("{product_link}", YOUR_PRODUCT_LINK)
    elif link_type == "email":
        return content.replace("{email_link}", YOUR_EMAIL_LIST)
    return content

def generate_posts(count=50):
    """Generate money-making posts"""
    posts = []
    
    for i in range(count):
        template = MONEY_POSTS[i % len(MONEY_POSTS)]
        content = replace_links(template['content'], template['link_type'])
        
        posts.append({
            'id': f'post{i+1:03d}',
            'content': content,
            'image_url': '',
            'video_url': ''
        })
    
    return posts

def save_posts(posts, filename='posts.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'content', 'image_url', 'video_url'])
        writer.writeheader()
        writer.writerows(posts)
    print(f"Generated {len(posts)} money-making posts")

if __name__ == "__main__":
    print("FitLife Daily - Money-Making Content Generator")
    print("=" * 55)
    
    posts = generate_posts(50)
    save_posts(posts)
    
    print(f"\nSample post:")
    print(posts[0]['content'][:200])
    print("\nRun 'python fb_poster.py' to post")
