#!/usr/bin/env python3
"""
FitLife Daily - Content Generator
Generates posts with generated images and local videos
"""

import csv
import random
import os
import glob
from datetime import datetime

# ============================================
# GET GENERATED IMAGES
# ============================================

def get_generated_images():
    """Get list of images created by create_images.py"""
    images_dir = "images"
    image_files = []
    
    if os.path.exists(images_dir):
        image_files = glob.glob(f"{images_dir}/*.png")
        
        csv_file = f"{images_dir}/image_list.csv"
        if os.path.exists(csv_file):
            try:
                with open(csv_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if os.path.exists(row['file']):
                            image_files.append(row['file'])
            except:
                pass
    
    return list(set(image_files))

# ============================================
# GET GENERATED VIDEOS
# ============================================

def get_created_videos():
    """Get list of videos created by create_reels.py"""
    videos_dir = "videos"
    video_files = []
    
    if os.path.exists(videos_dir):
        video_files = glob.glob(f"{videos_dir}/*.mp4")
        
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
# GENERATE POSTS
# ============================================

def generate_posts():
    """Generate posts with generated images and local videos"""
    all_posts = []
    
    # Get generated images
    image_files = get_generated_images()
    image_count = len(image_files)
    
    if image_count > 0:
        print(f"✅ Found {image_count} images in images/ folder")
        for idx, image_file in enumerate(image_files, 1):
            # Create simple content for image
            title = os.path.basename(image_file).replace("_", " ").replace(".png", "")
            all_posts.append({
                'id': f'post{idx:03d}',
                'content': f"🏋️ FitLife Daily\n\nCheck out this fitness tip!\n\n#FitLifeDaily #Fitness #Health",
                'image_url': image_file,
                'video_url': ''
            })
    else:
        print("⚠️ No images found! Run 'python create_images.py' first.")
        # Add fallback text-only posts
        for idx in range(1, 11):
            all_posts.append({
                'id': f'post{idx:03d}',
                'content': f"🏋️ FitLife Daily\n\nDay {idx}: Stay consistent!\n\n#FitLifeDaily #Fitness #Health",
                'image_url': '',
                'video_url': ''
            })
    
    # Get videos
    video_files = get_created_videos()
    video_count = len(video_files)
    
    if video_count > 0:
        print(f"✅ Found {video_count} videos in videos/ folder")
        for idx, video_post in enumerate(VIDEO_POSTS[:video_count], len(all_posts) + 1):
            all_posts.append({
                'id': f'post{idx:03d}',
                'content': video_post['content'],
                'image_url': '',
                'video_url': video_files[idx - 1] if (idx - 1) < len(video_files) else ''
            })
    else:
        print("⚠️ No videos found! Run 'python create_reels.py' first.")
    
    # Shuffle
    random.shuffle(all_posts)
    
    # Reassign IDs
    for i, post in enumerate(all_posts, 1):
        post['id'] = f'post{i:03d}'
    
    return all_posts

def save_posts_to_csv(posts, filename='posts.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'content', 'image_url', 'video_url'])
        writer.writeheader()
        for post in posts:
            writer.writerow(post)
    print(f"✅ Generated {len(posts)} posts saved to {filename}")

def print_stats(posts):
    total = len(posts)
    with_images = sum(1 for p in posts if p['image_url'])
    with_videos = sum(1 for p in posts if p['video_url'])
    print(f"\n📊 Total Posts: {total}")
    print(f"   With Images: {with_images}")
    print(f"   With Videos: {with_videos}")

def print_samples(posts, count=5):
    print(f"\n📌 Sample Posts:")
    samples = random.sample(posts, min(count, len(posts)))
    for idx, post in enumerate(samples, 1):
        print(f"\n   [{idx}] {post['id']}")
        print(f"   Content: {post['content'][:50]}...")
        print(f"   Image: {'✅' if post['image_url'] else '❌'}")
        print(f"   Video: {'✅' if post['video_url'] else '❌'}")

if __name__ == "__main__":
    print("🏋️ FitLife Daily - Content Generator")
    print("=" * 65)
    print(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    posts = generate_posts()
    save_posts_to_csv(posts)
    print_stats(posts)
    print_samples(posts, 5)
    
    print("\n✨ CONTENT GENERATION COMPLETE!")
    print("🚀 Run 'python fb_poster.py' to start posting.")
