#!/usr/bin/env python3
"""
FitLife Daily - Content Generator with Local Videos
"""

import csv
import random
import os
import glob
from datetime import datetime

# ============================================
# GET VIDEOS FROM LOCAL FOLDER
# ============================================

def get_created_videos():
    """Get list of videos created by create_reels.py"""
    videos_dir = "videos"
    video_files = []
    
    if os.path.exists(videos_dir):
        video_files = glob.glob(f"{videos_dir}/*.mp4")
        
        # Also try from CSV
        csv_file = f"{videos_dir}/reel_list.csv"
        if os.path.exists(csv_file):
            try:
                with open(csv_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if os.path.exists(row['file']):
                            video_files.append(row['file'])
            except:
                pass
    
    # Remove duplicates
    return list(set(video_files))

# ============================================
# VIDEO POST CONTENT
# ============================================

VIDEO_POSTS = [
    {
        "content": "🎬 **Intense Workout Session!** Watch this to get inspired.\n\nRemember: 'The only bad workout is the one that didn't happen.'\n\nTurn on sound for maximum motivation! 🎵\n\n#WorkoutMotivation #IntenseWorkout #FitLifeDaily",
    },
    {
        "content": "🏋️ **Master Your Squat Form!**\n\nKey points:\n✅ Feet shoulder-width apart\n✅ Chest up, back straight\n✅ Push through your heels\n✅ Don't let knees cave in\n\nPerfect your form for better results and safety!\n\n#SquatForm #FitnessTips #Gym #FitLifeDaily",
    },
    {
        "content": "⚡ **4-Minute HIIT for Busy People!**\n\n20 seconds work / 10 seconds rest\n8 rounds - only 4 minutes!\n\nChoose any exercise:\n🔹 Jump Squats\n🔹 Burpees\n🔹 Mountain Climbers\n🔹 High Knees\n\nNo excuses - do this now!\n\n#HIIT #QuickWorkout #FatBurn #FitLifeDaily",
    },
    {
        "content": "🌅 **5-Minute Morning Stretch**\n\nWake up your body:\n1️⃣ Neck rolls\n2️⃣ Arm circles\n3️⃣ Torso twists\n4️⃣ Leg swings\n5️⃣ Cat-cow\n6️⃣ Child's pose\n\nStart your day with flexibility!\n\n#MorningStretch #Flexibility #Wellness #FitLifeDaily",
    },
    {
        "content": "🧘 **10-Minute Yoga Flow**\n\nFollow along for:\n🔹 Flexibility\n🔹 Stress relief\n🔹 Better sleep\n🔹 Mind-body connection\n\nPoses: Downward dog, Warrior I, Warrior II, Pigeon, Savasana\n\n#Yoga #Mindfulness #Flexibility #FitLifeDaily",
    },
    {
        "content": "🏃 **20-Minute Cardio Burn!**\n\nWarm up (3 min) → Workout (15 min) → Cool down (2 min)\n\nExercises:\n🔹 Jumping jacks\n🔹 High knees\n🔹 Butt kicks\n🔹 Mountain climbers\n🔹 Burpees\n\nBurn 200+ calories!\n\n#CardioWorkout #FatLoss #Fitness #FitLifeDaily",
    },
    {
        "content": "💪 **Full Body Home Workout**\n\nNo equipment needed:\n1️⃣ Squats - 15 reps\n2️⃣ Push-ups - 10 reps\n3️⃣ Lunges - 12 each\n4️⃣ Plank - 30 sec\n5️⃣ Glute bridges - 15 reps\n6️⃣ Mountain climbers - 30 sec\n\nRepeat 3x. Do this daily!\n\n#HomeWorkout #FullBodyWorkout #NoEquipment #FitLifeDaily",
    },
    {
        "content": "🧍 **Fix Your Posture in 5 Minutes!**\n\nExercises:\n1️⃣ Wall angels - 15 reps\n2️⃣ Chin tucks - 15 reps\n3️⃣ Scapular retractions - 15 reps\n4️⃣ Bird-dog - 10 each side\n5️⃣ Cat-cow - 10 reps\n\nDo daily for better posture and less back pain!\n\n#Posture #BackPainRelief #Exercise #FitLifeDaily",
    },
    {
        "content": "🔥 **The Secret to Success!**\n\n'Success isn't given, it's earned. Behind every achievement are thousands of hours of work. Put in the time and you'll get the reward.'\n\nYour future self is counting on you. Keep going! 💪\n\n#Motivation #Success #Fitness #FitLifeDaily",
    },
    {
        "content": "🧘 **Evening Yoga Relaxation**\n\nWind down with these calming poses:\n🔹 Child's Pose\n🔹 Cat-Cow\n🔹 Pigeon Pose\n🔹 Savasana\n\nImprove sleep quality and reduce stress!\n\n#Yoga #Relaxation #BetterSleep #FitLifeDaily",
    },
    {
        "content": "🔥 **Burn Fat with This HIIT Routine!**\n\n30 seconds work / 15 seconds rest\n8 exercises = 6 minutes\n\nFull body fat burn in minimal time!\n\n#HIIT #FatBurn #QuickWorkout #FitLifeDaily",
    },
    {
        "content": "🏃 **Run Technique Tips**\n\nImprove your running form:\n✅ Lean slightly forward\n✅ Land mid-foot\n✅ Keep cadence high\n✅ Swing arms forward\n✅ Breathe rhythmically\n\nRun faster, longer, injury-free!\n\n#Running #Technique #Fitness #FitLifeDaily",
    },
    {
        "content": "💪 **Upper Body Strength Workout**\n\nExercises:\n1️⃣ Push-ups - 12 reps\n2️⃣ Pull-ups (or rows) - 8 reps\n3️⃣ Overhead Press - 10 reps\n4️⃣ Bicep Curls - 12 reps\n5️⃣ Tricep Dips - 12 reps\n\nBuild a stronger upper body today!\n\n#UpperBody #StrengthTraining #FitLifeDaily",
    },
    {
        "content": "🦵 **Leg Day Workout**\n\nBuild powerful legs:\n1️⃣ Squats - 15 reps\n2️⃣ Lunges - 12 each\n3️⃣ Deadlifts - 10 reps\n4️⃣ Calf Raises - 20 reps\n5️⃣ Glute Bridges - 15 reps\n\nStrong legs = strong foundation!\n\n#LegDay #LowerBody #Strength #FitLifeDaily",
    },
    {
        "content": "🧘 **Morning Meditation Guide**\n\nStart your day with mindfulness:\n1️⃣ Find a quiet space\n2️⃣ Sit comfortably\n3️⃣ Focus on breath\n4️⃣ 5-10 minutes\n5️⃣ Set intentions\n\nReduce anxiety and stay focused!\n\n#Meditation #Mindfulness #Wellness #FitLifeDaily",
    },
    {
        "content": "🥗 **Healthy Meal Prep Ideas**\n\nTips for success:\n✅ Plan your meals\n✅ Shop with a list\n✅ Batch cook proteins\n✅ Use containers\n✅ Include 5 colors\n\nSave time and eat healthy all week!\n\n#MealPrep #HealthyEating #Nutrition #FitLifeDaily",
    },
    {
        "content": "🎬 **Quick Cardio Blast!** Get your heart rate up with this intense cardio session.\n\nPerfect for busy days - just 10 minutes to burn calories and boost your mood!\n\n#Cardio #QuickWorkout #FatBurn #FitLifeDaily",
    },
    {
        "content": "🏋️ **Perfect Deadlift Form**\n\nKey points:\n✅ Bar over mid-foot\n✅ Hinge at hips\n✅ Keep back straight\n✅ Drive through heels\n✅ Lock out at top\n\nMaster this compound lift for strength gains!\n\n#Deadlift #Form #StrengthTraining #FitLifeDaily",
    }
]

# ============================================
# IMAGE POSTS
# ============================================

IMAGE_POSTS = [
    {
        "content": "💪 Start your day with 5 minutes of dynamic stretching! This increases blood flow by 30%, warms up your muscles, and reduces injury risk.\n\n#FitnessTips #WarmUp #FitLifeDaily",
        "image": "https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg"
    },
    {
        "content": "🥗 Add a handful of spinach to your morning smoothie! You'll get 50% of your daily Vitamin K and 20% of your iron needs. You won't even taste it!\n\n#HealthyEating #Smoothie #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2681319/pexels-photo-2681319.jpeg"
    },
    {
        "content": "💧 Drink 8 glasses of water daily to boost your metabolism by up to 30% for one hour! Your skin, energy, and focus will improve.\n\n#Hydration #Metabolism #FitLifeDaily",
        "image": "https://images.pexels.com/photos/414029/pexels-photo-414029.jpeg"
    },
    {
        "content": "😴 Your body repairs muscle during sleep. Getting 7-8 hours increases recovery by 40% and balances hormones.\n\n#SleepWell #Recovery #FitLifeDaily",
        "image": "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg"
    },
    {
        "content": "🏃 The ideal weekly routine: 3 days strength + 2 days cardio + 2 rest days. This balance prevents injury and builds muscle.\n\n#WorkoutPlan #FitnessJourney #FitLifeDaily",
        "image": "https://images.pexels.com/photos/260447/pexels-photo-260447.jpeg"
    },
    {
        "content": "🧘 Take 5 deep breaths using the 4-4-4 method: Inhale 4s, hold 4s, exhale 4s. Stress relief in 60 seconds!\n\n#MentalHealth #StressRelief #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3823039/pexels-photo-3823039.jpeg"
    },
    {
        "content": "🎯 Set SMART goals: Specific, Measurable, Achievable, Relevant, Time-bound. Write your goal down today!\n\n#GoalSetting #Motivation #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2581121/pexels-photo-2581121.jpeg"
    },
    {
        "content": "📱 Download a 7-minute workout app! 7 minutes of high-intensity exercise equals 30 minutes of moderate activity.\n\n#QuickWorkout #FitnessApp #FitLifeDaily",
        "image": "https://images.pexels.com/photos/1954524/pexels-photo-1954524.jpeg"
    },
    {
        "content": "🥑 Slice an avocado with sea salt and chili flakes. Healthy fats, fiber, and potassium in 5 minutes!\n\n#HealthySnacks #CleanEating #FitLifeDaily",
        "image": "https://images.pexels.com/photos/317157/pexels-photo-317157.jpeg"
    },
    {
        "content": "🔥 Quick HIIT: 20 seconds work / 10 seconds rest x 8 rounds. Burns fat for 24 hours post-workout!\n\n#HIIT #FatBurn #QuickWorkout #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2294361/pexels-photo-2294361.jpeg"
    }
]

# ============================================
# GENERATE POSTS
# ============================================

def generate_posts():
    """Generate posts with images and local videos"""
    all_posts = []
    
    # Add Image Posts
    for idx, post in enumerate(IMAGE_POSTS, 1):
        all_posts.append({
            'id': f'post{idx:03d}',
            'content': post['content'],
            'image_url': post['image'],
            'video_url': ''
        })
    
    # Get local videos
    video_files = get_created_videos()
    video_count = len(video_files)
    
    if video_count > 0:
        print(f"✅ Found {video_count} videos in videos/ folder")
        # Add Video Posts with local videos
        for idx, video_post in enumerate(VIDEO_POSTS[:video_count], len(all_posts) + 1):
            all_posts.append({
                'id': f'post{idx:03d}',
                'content': video_post['content'],
                'image_url': '',
                'video_url': video_files[idx - 1] if (idx - 1) < len(video_files) else ''
            })
    else:
        print("⚠️ No videos found! Run 'python create_reels.py' first.")
        # Add fallback text-only video posts
        for idx, video_post in enumerate(VIDEO_POSTS[:10], len(all_posts) + 1):
            all_posts.append({
                'id': f'post{idx:03d}',
                'content': video_post['content'] + "\n\n⚠️ Video not available - run create_reels.py to generate!",
                'image_url': '',
                'video_url': ''
            })
    
    # Shuffle
    random.shuffle(all_posts)
    
    # Reassign IDs
    for i, post in enumerate(all_posts, 1):
        post['id'] = f'post{i:03d}'
    
    return all_posts

# ============================================
# SAVE TO CSV
# ============================================

def save_posts_to_csv(posts, filename='posts.csv'):
    """Save generated posts to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'content', 'image_url', 'video_url'])
        writer.writeheader()
        
        for post in posts:
            writer.writerow({
                'id': post['id'],
                'content': post['content'],
                'image_url': post['image_url'],
                'video_url': post['video_url']
            })
    
    print(f"✅ Generated {len(posts)} posts saved to {filename}")

def print_stats(posts):
    """Print detailed statistics"""
    total = len(posts)
    with_images = sum(1 for p in posts if p['image_url'])
    with_videos = sum(1 for p in posts if p['video_url'])
    text_only = sum(1 for p in posts if not p['image_url'] and not p['video_url'])
    
    print(f"\n📊 Content Statistics:")
    print(f"   {'=' * 50}")
    print(f"   Total Posts:      {total}")
    print(f"   With Images:      {with_images} ({with_images/total*100:.0f}%)")
    print(f"   With Videos:      {with_videos} ({with_videos/total*100:.0f}%)")
    print(f"   Text-Only:        {text_only} ({text_only/total*100:.0f}%)")

def print_samples(posts, count=6):
    """Show sample posts"""
    print(f"\n📌 Sample Posts:")
    print(f"   {'=' * 55}")
    
    samples = random.sample(posts, min(count, len(posts)))
    for idx, post in enumerate(samples, 1):
        print(f"\n   [{idx}] {post['id']}")
        content_preview = post['content'][:60] + "..." if len(post['content']) > 60 else post['content']
        print(f"   Content: {content_preview}")
        print(f"   Image:   {'✅' if post['image_url'] else '❌'}")
        print(f"   Video:   {'✅' if post['video_url'] else '❌'}")
        print(f"   {'-' * 50}")

# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("🏋️ FitLife Daily - Content Generator")
    print("=" * 65)
    print(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Generate posts
    posts = generate_posts()
    
    # Save to CSV
    save_posts_to_csv(posts)
    
    # Show statistics
    print_stats(posts)
    
    # Show sample posts
    print_samples(posts, 5)
    
    print("\n✨ CONTENT GENERATION COMPLETE!")
    print("🚀 Run 'python fb_poster.py' to start posting.")
