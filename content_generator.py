#!/usr/bin/env python3
"""
Content Generator for Health & Fitness Auto-Poster
Pulls free, copyright-safe content from public sources
No copyrighted material - uses royalty-free sources only
"""

import csv
import random
from datetime import datetime

# ============================================
# FREE CONTENT SOURCES (No Copyright Issues)
# ============================================

# 1. Text Content - General Health Tips (Not Copyrightable)
HEALTH_TIPS = [
    "💪 Start your day with 5 minutes of dynamic stretching to wake up your muscles! #FitnessTips",
    "🥗 Add a handful of spinach to your morning smoothie for extra iron and fiber. #HealthyEating",
    "💧 Drink 8 glasses of water daily. Set reminders every 2 hours! #Hydration",
    "😴 Get 7-8 hours of sleep for optimal muscle recovery and hormone balance. #SleepWell",
    "🏃 Mix cardio and strength training: 3x strength + 2x cardio weekly. #FitnessJourney",
    "🧘 Take 5 deep breaths. Roll your shoulders back. Stress relief in 60 seconds! #MentalHealth",
    "🎯 Write down one fitness goal this week. Make it realistic and specific. #GoalSetting",
    "📱 Try a 7-minute workout app on busy days. Something beats nothing! #FitnessApp",
    "🥑 Healthy snack: Avocado with sea salt and chili flakes. Delicious and filling! #HealthySnacks",
    "🔥 Quick HIIT: 20 sec work / 10 sec rest x 8 rounds. Done in 4 minutes! #HIITWorkout",
    "🚶 Walk 10 minutes after each meal to aid digestion and stabilize blood sugar. #HealthyHabits",
    "🧠 Train your brain: Learn a new skill or read 10 pages daily. #MindBody",
    "🌿 Get outside: 15 minutes of sunlight boosts Vitamin D and mood. #VitaminD",
    "🍽️ Eat protein within 30 minutes post-workout for optimal muscle repair. #Nutrition",
    "📊 Track your progress weekly. What gets measured gets improved! #Progress",
    "🎵 Workout playlist: Upbeat music increases performance by 15%! #WorkoutMusic",
    "👟 Replace workout shoes every 300-500 miles to prevent injury. #FitnessGear",
    "🧖 Post-workout: Stretch and foam roll for faster recovery. #Recovery",
    "🌙 Evening routine: Dim lights 1 hour before bed for better sleep. #SleepHygiene",
    "💪 Progressive overload: Increase weight or reps by 5% weekly. #StrengthTraining",
    "🥦 Eat the rainbow: Different colored veggies = different nutrients! #EatClean",
    "🏋️ Compound exercises like squats and deadlifts burn more calories. #Workout",
    "🧘 Morning meditation: 5 minutes of silence sets the tone for the day. #Mindfulness",
    "📝 Keep a food journal for 3 days. See where you can improve! #FoodJournal",
    "🔄 Switch up your workout routine every 4-6 weeks to avoid plateaus. #FitnessVariety",
]

MOTIVATIONAL_QUOTES = [
    "✨ 'The only bad workout is the one that didn't happen.' #Motivation",
    "🌟 'Your body can do it. Your mind is the one that needs convincing.' #Mindset",
    "🔥 'Discipline equals freedom. Show up every day.' #Discipline",
    "💫 'Don't wish for it. Work for it.' #Grind",
    "⚡ 'Motivation gets you started. Habit keeps you going.' #Habits",
    "🎯 'Progress, not perfection. Every step counts.' #Progress",
    "🙌 'You are stronger than you think. Prove it to yourself.' #Strength",
    "🚀 'The pain you feel today is the strength you'll feel tomorrow.' #NoPainNoGain",
    "💎 'Small daily improvements equal massive results over time.' #Consistency",
    "⭐ 'Your only competition is the person in the mirror.' #SelfImprovement",
    "🏆 'Success is the sum of small efforts repeated day in and day out.' #Success",
    "💪 'Your health is an investment, not an expense.' #HealthIsWealth",
    "🌟 'Believe you can and you're halfway there.' #Believe",
    "🔥 'Push yourself because no one else is going to do it for you.' #PushHard",
    "🎯 'The secret of getting ahead is getting started.' #StartNow",
]

FITNESS_FACTS = [
    "📊 Did you know? Walking 10,000 steps burns ~400-500 calories! #FitnessFacts",
    "📊 Fun fact: Your heart is a muscle. Cardio strengthens it! #Cardio",
    "📊 Interesting: Muscle weighs more than fat but takes up less space. #BodyComposition",
    "📊 Quick fact: Stretching increases blood flow to muscles by 30%. #Stretching",
    "📊 True: Hydration boosts metabolism by up to 30% for 1 hour. #Hydration",
    "📊 Surprising: Laughter burns calories! It's a mini-workout. #Laughter",
    "📊 Did you know? It takes 21 days to form a new habit. #HabitFormation",
    "📊 Fact: Protein needs increase as you age. Prioritize it! #Protein",
    "📊 Quick tip: Rest days prevent burnout and injury. #RestDays",
    "📊 True: Consistency beats intensity. Show up daily! #Consistency",
    "📊 Did you know? 20 minutes of exercise = 2 hours of energy! #Energy",
    "📊 Fun fact: Your brain releases endorphins during exercise. #Endorphins",
    "📊 Interesting: 1 hour of exercise = 7 hours of better sleep! #Sleep",
    "📊 Quick fact: Walking after eating reduces blood sugar spikes. #BloodSugar",
    "📊 True: Strength training increases bone density. #BoneHealth",
]

# 2. Real Working Image URLs - Royalty Free from Pexels
REAL_IMAGES = [
    "https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg",  # Weights
    "https://images.pexels.com/photos/260447/pexels-photo-260447.jpeg",  # Running sunset
    "https://images.pexels.com/photos/1954524/pexels-photo-1954524.jpeg",  # Workout
    "https://images.pexels.com/photos/2581121/pexels-photo-2581121.jpeg",  # Gym minimalist
    "https://images.pexels.com/photos/3823039/pexels-photo-3823039.jpeg",  # Yoga
    "https://images.pexels.com/photos/414029/pexels-photo-414029.jpeg",  # Running
    "https://images.pexels.com/photos/3768911/pexels-photo-3768911.jpeg",  # Weights
    "https://images.pexels.com/photos/2294361/pexels-photo-2294361.jpeg",  # Gym
    "https://images.pexels.com/photos/317157/pexels-photo-317157.jpeg",  # Dumbbells
    "https://images.pexels.com/photos/1552249/pexels-photo-1552249.jpeg",  # Yoga
    "https://images.pexels.com/photos/2479216/pexels-photo-2479216.jpeg",  # Workout
    "https://images.pexels.com/photos/3764016/pexels-photo-3764016.jpeg",  # Training
    "https://images.pexels.com/photos/3727547/pexels-photo-3727547.jpeg",  # Running
    "https://images.pexels.com/photos/2681319/pexels-photo-2681319.jpeg",  # Healthy food
    "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg",  # Meditation
]

# ============================================
# CORE FUNCTIONS
# ============================================

def get_random_text():
    """Generate random health/fitness text content"""
    all_texts = HEALTH_TIPS + MOTIVATIONAL_QUOTES + FITNESS_FACTS
    return random.choice(all_texts)

def get_random_image_url():
    """Get a real working image URL from Pexels"""
    return random.choice(REAL_IMAGES)

def generate_posts(count=50):
    """
    Generate a list of posts with text and images
    Text-only: ~60% | Image posts: ~40%
    """
    posts = []
    
    for i in range(1, count + 1):
        # Generate content
        content = get_random_text()
        
        # Decide post type (text-only or with image)
        is_image_post = random.random() < 0.4  # 40% chance for image
        
        post = {
            'id': f'post{i:03d}',
            'content': content,
            'image_url': get_random_image_url() if is_image_post else '',
            'video_url': ''  # No videos to avoid issues
        }
        
        posts.append(post)
    
    return posts

def save_posts_to_csv(posts, filename='posts.csv'):
    """Save generated posts to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'content', 'image_url', 'video_url'])
        writer.writeheader()
        writer.writerows(posts)
    
    print(f"✅ Generated {len(posts)} posts saved to {filename}")

def print_stats(posts):
    """Print statistics about generated posts"""
    text_only = sum(1 for p in posts if not p['image_url'] and not p['video_url'])
    with_images = sum(1 for p in posts if p['image_url'])
    
    print(f"\n📊 Post Statistics:")
    print(f"   Total posts: {len(posts)}")
    print(f"   Text-only: {text_only} ({text_only/len(posts)*100:.0f}%)")
    print(f"   With images: {with_images} ({with_images/len(posts)*100:.0f}%)")
    print(f"   Videos: 0 (disabled for stability)")

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    print("🎨 Generating Health & Fitness Content...")
    print("=" * 60)
    print(f"⏰ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Generate 50 posts
    posts = generate_posts(50)
    
    # Save to CSV
    save_posts_to_csv(posts)
    
    # Show statistics
    print_stats(posts)
    
    # Show sample posts
    print("\n📌 Sample Posts:")
    print("-" * 40)
    for sample in random.sample(posts, min(3, len(posts))):
        print(f"ID: {sample['id']}")
        print(f"Content: {sample['content'][:70]}...")
        print(f"Image: {'✅ Yes' if sample['image_url'] else '❌ No'}")
        print("-" * 40)
    
    print("\n✨ Done! Run 'python fb_poster.py' to start posting.")
