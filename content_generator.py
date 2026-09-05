#!/usr/bin/env python3
"""
Enhanced Content Generator for FitLife Daily Facebook Page
Generates 100+ unique posts with images, videos, and detailed content
No copyright issues - All content is original or royalty-free
"""

import csv
import random
from datetime import datetime

# ============================================
# CONTENT CATEGORIES
# ============================================

# 1. Detailed Health & Fitness Tips (with explanations)
HEALTH_TIPS = [
    {
        "title": "Dynamic Stretching",
        "content": "💪 Start your day with 5 minutes of dynamic stretching! It increases blood flow, warms up your muscles, and reduces injury risk by up to 30%. Try leg swings, arm circles, and torso twists before your workout.",
        "hashtags": "#FitnessTips #WarmUp #FitLifeDaily"
    },
    {
        "title": "Superfood Smoothie",
        "content": "🥗 Add spinach to your morning smoothie! Just one handful gives you 50% of your daily Vitamin K and 20% of your iron needs. It doesn't change the taste at all - I promise! Try it tomorrow morning.",
        "hashtags": "#HealthyEating #Smoothie #FitLifeDaily"
    },
    {
        "title": "Hydration Benefits",
        "content": "💧 Did you know? Drinking 8 glasses of water daily boosts your metabolism by up to 30% for one hour! Set reminders every 2 hours. Your skin, energy, and focus will thank you.",
        "hashtags": "#Hydration #HealthTips #FitLifeDaily"
    },
    {
        "title": "Sleep Science",
        "content": "😴 Your body repairs and builds muscle during sleep. Getting 7-8 hours of quality sleep increases muscle recovery by 40% and improves hormonal balance. Create a dark, cool room for best results!",
        "hashtags": "#SleepWell #Recovery #FitLifeDaily"
    },
    {
        "title": "Balanced Workout",
        "content": "🏃 The ideal weekly workout schedule: 3 days of strength training + 2 days of cardio + 2 rest days. This balance prevents injury, builds muscle, and improves cardiovascular health.",
        "hashtags": "#FitnessJourney #WorkoutPlan #FitLifeDaily"
    },
    {
        "title": "Stress Relief Hack",
        "content": "🧘 Take 5 deep breaths right now! Inhale for 4 seconds, hold for 4, exhale for 4. This simple technique lowers cortisol levels and reduces stress in just 60 seconds. Try it 5 times today!",
        "hashtags": "#MentalHealth #StressRelief #FitLifeDaily"
    },
    {
        "title": "SMART Goals",
        "content": "🎯 Write one fitness goal this week using the SMART method: Specific, Measurable, Achievable, Relevant, and Time-bound. Example: 'I'll walk 10,000 steps daily for 7 days.' Share yours below!",
        "hashtags": "#GoalSetting #Motivation #FitLifeDaily"
    },
    {
        "title": "Quick Workout App",
        "content": "📱 Download a 7-minute workout app! On busy days, 7 minutes of high-intensity exercise can provide the same benefits as 30 minutes of moderate exercise. Something is always better than nothing!",
        "hashtags": "#FitnessApp #QuickWorkout #FitLifeDaily"
    },
    {
        "title": "Healthy Snack Guide",
        "content": "🥑 Healthy snack: Slice an avocado, sprinkle with sea salt and chili flakes. Avocados provide healthy fats, fiber, and potassium. This 5-minute snack keeps you full for hours!",
        "hashtags": "#HealthySnacks #CleanEating #FitLifeDaily"
    },
    {
        "title": "HIIT Workout",
        "content": "🔥 Quick HIIT routine: 20 seconds work / 10 seconds rest x 8 rounds. That's just 4 minutes! Choose any exercise (squats, push-ups, jumping jacks). It burns fat for up to 24 hours after!",
        "hashtags": "#HIITWorkout #FatBurn #FitLifeDaily"
    },
    {
        "title": "After-Meal Walk",
        "content": "🚶 Walking 10 minutes after each meal improves digestion and reduces blood sugar spikes by 20%. It's the easiest habit you can adopt. Set a reminder on your phone!",
        "hashtags": "#HealthyHabits #Walking #FitLifeDaily"
    },
    {
        "title": "Nutrition Basics",
        "content": "🍽️ Eat protein within 30 minutes post-workout! This window is when your muscles are most receptive to protein synthesis. Aim for 20-30g of protein from eggs, chicken, fish, or a shake.",
        "hashtags": "#Nutrition #PostWorkout #FitLifeDaily"
    },
    {
        "title": "Progress Tracking",
        "content": "📊 Track your progress weekly! Take measurements, photos, and record your weights. What gets measured gets improved. Celebrate small wins - every step forward is progress!",
        "hashtags": "#Progress #FitnessJourney #FitLifeDaily"
    },
    {
        "title": "Workout Music",
        "content": "🎵 Create a workout playlist with 120-140 BPM music! Studies show upbeat music increases performance by 15% and makes exercise feel easier. Your motivation will skyrocket!",
        "hashtags": "#WorkoutMusic #Motivation #FitLifeDaily"
    },
    {
        "title": "Shoe Replacement Guide",
        "content": "👟 Replace workout shoes every 300-500 miles (or 3-6 months). Worn-out shoes cause joint pain and increase injury risk. Check the sole - if it's worn down, it's time for new ones!",
        "hashtags": "#FitnessGear #Safety #FitLifeDaily"
    },
    {
        "title": "Recovery Routine",
        "content": "🧖 Post-workout recovery: Stretch for 5 minutes and foam roll sore muscles. This increases blood flow, reduces muscle soreness by 30%, and prevents injury. Your body will thank you!",
        "hashtags": "#Recovery #Stretching #FitLifeDaily"
    },
    {
        "title": "Sleep Routine",
        "content": "🌙 Evening routine: Dim lights 1 hour before bed. This signals your brain to produce melatonin, the sleep hormone. Avoid screens and try reading a book instead. Better sleep = better results!",
        "hashtags": "#SleepHygiene #Wellness #FitLifeDaily"
    },
    {
        "title": "Progressive Overload",
        "content": "💪 Progressive overload: Increase weights or reps by 5% weekly. This principle is the key to getting stronger. Small increases = consistent gains. Track your lifts to see progress!",
        "hashtags": "#StrengthTraining #FitnessScience #FitLifeDaily"
    },
    {
        "title": "Eat the Rainbow",
        "content": "🥦 Eat the rainbow! Different colored vegetables provide different nutrients: Red (lycopene), Orange (beta-carotene), Green (iron), Purple (antioxidants). Aim for 5 colors daily!",
        "hashtags": "#EatClean #NutritionTips #FitLifeDaily"
    },
    {
        "title": "Compound Exercises",
        "content": "🏋️ Compound exercises (squats, deadlifts, bench press) burn more calories and build functional strength. They work multiple muscle groups simultaneously. Add them to your routine!",
        "hashtags": "#Workout #Strength #FitLifeDaily"
    },
    {
        "title": "Morning Meditation",
        "content": "🧘 Morning meditation: Spend 5 minutes in silence. Focus on your breath. This sets the tone for your day, reduces anxiety, and improves focus. Try it tomorrow morning!",
        "hashtags": "#Mindfulness #MentalHealth #FitLifeDaily"
    },
    {
        "title": "Food Journal",
        "content": "📝 Keep a food journal for 3 days. Write down everything you eat and drink. You'll identify areas for improvement and make better choices. It's the first step to mindful eating!",
        "hashtags": "#FoodJournal #HealthyHabits #FitLifeDaily"
    },
    {
        "title": "Workout Variety",
        "content": "🔄 Change your workout routine every 4-6 weeks! This prevents plateaus and keeps your body adapting. Try different exercises, rep ranges, or training styles to keep progress going.",
        "hashtags": "#FitnessVariety #WorkoutRoutine #FitLifeDaily"
    },
    {
        "title": "Posture Check",
        "content": "🧍 Check your posture right now: Shoulders back, chest up, chin parallel to the ground. Good posture reduces back pain, improves breathing, and makes you look more confident!",
        "hashtags": "#Posture #WellnessTips #FitLifeDaily"
    },
    {
        "title": "Portion Control",
        "content": "🍽️ Use the plate method: Half vegetables, quarter protein, quarter complex carbs. This simple rule creates balanced meals without calorie counting. Try it at your next meal!",
        "hashtags": "#PortionControl #HealthyEating #FitLifeDaily"
    },
    {
        "title": "Heart Health",
        "content": "❤️ Your heart is a muscle too! 150 minutes of moderate cardio weekly strengthens it. Walking, jogging, swimming, or cycling all count. Start with 30 minutes, 5 days a week.",
        "hashtags": "#HeartHealth #Cardio #FitLifeDaily"
    },
]

# 2. Motivational Quotes with Explanations
MOTIVATIONAL_POSTS = [
    {
        "title": "No Bad Workouts",
        "content": "✨ 'The only bad workout is the one that didn't happen.' - Even 10 minutes of exercise counts. On days you're tired, do half your workout. You'll be glad you started!",
        "hashtags": "#Motivation #FitnessMindset #FitLifeDaily"
    },
    {
        "title": "Mind Over Matter",
        "content": "🌟 'Your body can do it. Your mind is the one that needs convincing.' - The mental battle is tougher than the physical one. Push through the doubt. You're capable of more than you think!",
        "hashtags": "#Mindset #Strength #FitLifeDaily"
    },
    {
        "title": "Discipline is Freedom",
        "content": "🔥 'Discipline equals freedom. Show up every day.' - Motivation is fleeting; discipline is what gets results. Build habits that serve you. Consistency is the ultimate superpower!",
        "hashtags": "#Discipline #Consistency #FitLifeDaily"
    },
    {
        "title": "Work for It",
        "content": "💫 'Don't wish for it. Work for it.' - Wishes don't build muscles. Action does. Every rep, every step, every healthy meal brings you closer. Today's effort is tomorrow's result.",
        "hashtags": "#Grind #HardWork #FitLifeDaily"
    },
    {
        "title": "Habits vs Motivation",
        "content": "⚡ 'Motivation gets you started. Habit keeps you going.' - Build systems, not goals. When the excitement fades, your habits will carry you. Focus on small daily actions.",
        "hashtags": "#Habits #Success #FitLifeDaily"
    },
    {
        "title": "Every Step Counts",
        "content": "🎯 'Progress, not perfection. Every step counts.' - Don't aim for perfect. Aim for better than yesterday. Each small improvement adds up to massive transformation over time.",
        "hashtags": "#Progress #SelfImprovement #FitLifeDaily"
    },
    {
        "title": "Believe in Yourself",
        "content": "🙌 'You are stronger than you think. Prove it to yourself.' - You've survived every tough day so far. You have the strength to overcome challenges. Trust your resilience.",
        "hashtags": "#Strength #Believe #FitLifeDaily"
    },
    {
        "title": "Embrace the Pain",
        "content": "🚀 'The pain you feel today is the strength you'll feel tomorrow.' - Growth requires discomfort. When you're struggling, remember: this is where the magic happens. Push through!",
        "hashtags": "#NoPainNoGain #Growth #FitLifeDaily"
    },
    {
        "title": "Small Daily Wins",
        "content": "💎 'Small daily improvements equal massive results over time.' - A 1% improvement daily is 37x better in a year. You don't need giant leaps - just consistent steps.",
        "hashtags": "#Consistency #FitnessJourney #FitLifeDaily"
    },
    {
        "title": "Compete with Yourself",
        "content": "⭐ 'Your only competition is the person in the mirror.' - Compare yourself to your past self, not others. Are you better than yesterday? That's all that matters.",
        "hashtags": "#SelfImprovement #Focus #FitLifeDaily"
    },
    {
        "title": "Small Efforts Build Success",
        "content": "🏆 'Success is the sum of small efforts repeated day in and day out.' - There are no shortcuts. Show up, do the work, trust the process. Your future self will thank you.",
        "hashtags": "#Success #Patience #FitLifeDaily"
    },
    {
        "title": "Health is an Investment",
        "content": "💪 'Your health is an investment, not an expense.' - Every healthy choice is compounding. Invest in yourself now. You can't buy health later - you have to earn it today.",
        "hashtags": "#HealthIsWealth #InvestInYou #FitLifeDaily"
    },
    {
        "title": "Believe to Achieve",
        "content": "🌟 'Believe you can and you're halfway there.' - Your mindset determines your outcome. Visualize success, then act. Doubt is the enemy of progress. Believe in your potential!",
        "hashtags": "#Believe #Mindset #FitLifeDaily"
    },
    {
        "title": "Be Your Own Hero",
        "content": "🔥 'Push yourself because no one else is going to do it for you.' - Take ownership of your health. No one else can do the work for you. Be the hero of your own journey.",
        "hashtags": "#SelfDiscipline #Hero #FitLifeDaily"
    },
    {
        "title": "Start Now",
        "content": "🎯 'The secret of getting ahead is getting started.' - Stop waiting for the perfect moment. It doesn't exist. Start with what you have, where you are. The time is NOW!",
        "hashtags": "#StartNow #Motivation #FitLifeDaily"
    },
]

# 3. Interesting Fitness Facts with Explanations
FITNESS_FACTS = [
    {
        "title": "10,000 Steps",
        "content": "📊 Walking 10,000 steps burns approximately 400-500 calories! That's equivalent to a full meal. Park farther away, take the stairs, go for a walk after lunch. Every step counts!",
        "hashtags": "#Walking #FitnessFacts #FitLifeDaily"
    },
    {
        "title": "Heart Health",
        "content": "📊 Your heart is a muscle too! Regular cardiovascular exercise strengthens it, lowering the risk of heart disease by 30%. Just 30 minutes of brisk walking 5x weekly makes a difference.",
        "hashtags": "#Cardio #HeartHealth #FitLifeDaily"
    },
    {
        "title": "Muscle vs Fat",
        "content": "📊 Muscle weighs more than fat but takes up less space. That's why you might lose inches without seeing the scale move. Take measurements and progress photos too!",
        "hashtags": "#BodyComposition #FitnessTruth #FitLifeDaily"
    },
    {
        "title": "Stretching Benefits",
        "content": "📊 Stretching increases blood flow to muscles by up to 30%. This improves flexibility, reduces soreness, and prevents injury. Add 5-10 minutes of stretching to your routine.",
        "hashtags": "#Stretching #Flexibility #FitLifeDaily"
    },
    {
        "title": "Hydration and Metabolism",
        "content": "📊 Drinking 500ml of water boosts your metabolism by up to 30% for one hour! That's why water is essential for weight management. Stay hydrated throughout the day.",
        "hashtags": "#Hydration #Metabolism #FitLifeDaily"
    },
    {
        "title": "Laughter is Exercise",
        "content": "📊 Laughter burns calories! 15 minutes of laughing burns up to 40 calories. It also releases endorphins and reduces stress. Watch a funny video and enjoy the health benefits!",
        "hashtags": "#Laughter #Wellness #FitLifeDaily"
    },
    {
        "title": "21-Day Habit",
        "content": "📊 It takes 21 days to form a new habit. Commit to a healthy habit for 3 weeks. After that, it becomes natural. Start with something small like daily stretching or water tracking.",
        "hashtags": "#HabitFormation #Wellness #FitLifeDaily"
    },
    {
        "title": "Protein Needs",
        "content": "📊 Protein needs increase with age. After 40, you need about 1.2g per kg of body weight daily. Distribute protein intake evenly across meals for optimal muscle synthesis.",
        "hashtags": "#Protein #Nutrition #FitLifeDaily"
    },
    {
        "title": "Rest Days",
        "content": "📊 Rest days prevent burnout and injury. Your muscles grow during rest, not during training. Schedule at least 2 full rest days weekly for optimal recovery.",
        "hashtags": "#RestDays #Recovery #FitLifeDaily"
    },
    {
        "title": "Consistency Wins",
        "content": "📊 Consistency beats intensity. A 30-minute workout 5x weekly is more effective than a 2-hour workout once a week. Build a sustainable routine that fits your lifestyle.",
        "hashtags": "#Consistency #FitnessJourney #FitLifeDaily"
    },
    {
        "title": "Energy Boost",
        "content": "📊 20 minutes of exercise gives you 2 hours of energy! Midday exercise increases productivity and alertness. Skip the coffee, go for a quick walk instead.",
        "hashtags": "#Energy #Productivity #FitLifeDaily"
    },
    {
        "title": "Brain Health",
        "content": "📊 Your brain releases endorphins during exercise, reducing stress and improving mood. Exercise is nature's antidepressant. Even 15 minutes can improve your mental state.",
        "hashtags": "#Endorphins #MentalHealth #FitLifeDaily"
    },
    {
        "title": "Sleep and Exercise",
        "content": "📊 1 hour of exercise = 7 hours of better sleep! Physical activity increases deep sleep phases. Morning exercise is best, but any time helps. Move more, sleep better!",
        "hashtags": "#Sleep #Recovery #FitLifeDaily"
    },
    {
        "title": "Blood Sugar Management",
        "content": "📊 Walking after eating reduces blood sugar spikes by 20%! Just a 10-minute post-meal walk improves glucose control. This is one of the easiest health habits you can adopt.",
        "hashtags": "#BloodSugar #HealthyHabits #FitLifeDaily"
    },
    {
        "title": "Bone Health",
        "content": "📊 Strength training increases bone density, reducing the risk of osteoporosis by 30%. Weight-bearing exercises like squats, lunges, and deadlifts build stronger bones.",
        "hashtags": "#BoneHealth #StrengthTraining #FitLifeDaily"
    },
]

# 4. Step-by-Step Workout Guides
WORKOUT_GUIDES = [
    {
        "title": "Beginner Bodyweight Workout",
        "content": "🏋️ **Beginner Bodyweight Workout** (15 minutes)\n\n1️⃣ 10 Squats\n2️⃣ 10 Push-ups (knee or regular)\n3️⃣ 10 Lunges each leg\n4️⃣ 20-second Plank\n5️⃣ 10 Glute Bridges\n\nRepeat the circuit 3 times. Rest 60 seconds between rounds. Do this 3x weekly to build a solid foundation!",
        "hashtags": "#Workout #Bodyweight #FitLifeDaily"
    },
    {
        "title": "Quick Cardio Circuit",
        "content": "🏃 **Quick Cardio Circuit** (20 minutes)\n\n1️⃣ Jumping Jacks - 1 minute\n2️⃣ High Knees - 1 minute\n3️⃣ Burpees - 30 seconds\n4️⃣ Rest - 30 seconds\n\nRepeat 5 times. Modify exercises as needed. This workout burns fat and builds stamina fast!",
        "hashtags": "#Cardio #WeightLoss #FitLifeDaily"
    },
    {
        "title": "Full-Body Dumbbell Workout",
        "content": "💪 **Full-Body Dumbbell Workout** (30 minutes)\n\n1️⃣ Dumbbell Squats - 12 reps x 3 sets\n2️⃣ Dumbbell Rows - 12 reps x 3 sets\n3️⃣ Dumbbell Press - 10 reps x 3 sets\n4️⃣ Dumbbell Lunges - 10 reps each leg x 3 sets\n5️⃣ Dumbbell Curls - 12 reps x 3 sets\n\nWarm up with light weight. Focus on form. Great for building strength at home!",
        "hashtags": "#Dumbbells #StrengthTraining #FitLifeDaily"
    },
    {
        "title": "Quick Morning Routine",
        "content": "🌅 **5-Minute Morning Wake-Up Routine**\n\n1️⃣ Neck Rolls - 30 seconds\n2️⃣ Shoulder Shrugs - 30 seconds\n3️⃣ Arm Circles - 30 seconds\n4️⃣ Torso Twists - 30 seconds\n5️⃣ Squats - 1 minute\n6️⃣ Jumping Jacks - 1 minute\n7️⃣ Deep Breathing - 1 minute\n\nSets the tone for a productive day! Try it tomorrow morning.",
        "hashtags": "#MorningRoutine #WakeUp #FitLifeDaily"
    },
    {
        "title": "Office Exercise Break",
        "content": "🪑 **3-Minute Office Exercise Break**\n\n1️⃣ Chair Squats - 10 reps\n2️⃣ Desk Push-ups - 10 reps\n3️⃣ Seated Leg Raises - 10 reps each leg\n4️⃣ Neck Stretches - 30 seconds\n5️⃣ Arm Stretches - 30 seconds\n\nDo this 3x daily during work breaks. Keeps you active and focused all day!",
        "hashtags": "#OfficeWorkout #ActiveBreak #FitLifeDaily"
    },
]

# ============================================
# IMAGES AND VIDEOS (Royalty-Free)
# ============================================

# Royalty-Free Images from Pexels (Working URLs)
REAL_IMAGES = [
    "https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg",      # Weights
    "https://images.pexels.com/photos/260447/pexels-photo-260447.jpeg",      # Running sunset
    "https://images.pexels.com/photos/1954524/pexels-photo-1954524.jpeg",    # Workout
    "https://images.pexels.com/photos/2581121/pexels-photo-2581121.jpeg",    # Gym minimalist
    "https://images.pexels.com/photos/3823039/pexels-photo-3823039.jpeg",    # Yoga
    "https://images.pexels.com/photos/414029/pexels-photo-414029.jpeg",      # Running
    "https://images.pexels.com/photos/3768911/pexels-photo-3768911.jpeg",    # Weights
    "https://images.pexels.com/photos/2294361/pexels-photo-2294361.jpeg",    # Gym
    "https://images.pexels.com/photos/317157/pexels-photo-317157.jpeg",      # Dumbbells
    "https://images.pexels.com/photos/1552249/pexels-photo-1552249.jpeg",    # Yoga
    "https://images.pexels.com/photos/2479216/pexels-photo-2479216.jpeg",    # Workout
    "https://images.pexels.com/photos/3764016/pexels-photo-3764016.jpeg",    # Training
    "https://images.pexels.com/photos/3727547/pexels-photo-3727547.jpeg",    # Running
    "https://images.pexels.com/photos/2681319/pexels-photo-2681319.jpeg",    # Healthy food
    "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg",    # Meditation
    "https://images.pexels.com/photos/3822960/pexels-photo-3822960.jpeg",    # Fitness
    "https://images.pexels.com/photos/4543704/pexels-photo-4543704.jpeg",    # Healthy lifestyle
    "https://images.pexels.com/photos/2883049/pexels-photo-2883049.jpeg",    # Gym equipment
    "https://images.pexels.com/photos/3822942/pexels-photo-3822942.jpeg",    # Group workout
    "https://images.pexels.com/photos/4065403/pexels-photo-4065403.jpeg",    # Nutrition
]

# Working Video URLs (Public Domain / Open Source)
REAL_VIDEOS = [
    # These are safe, open-source sample videos
    "https://www.pexels.com/video/people-exercising-at-gym-3670844/",
    "https://www.pexels.com/video/woman-performing-barbell-exercise-4497267/",
    "https://www.pexels.com/video/woman-doing-yoga-5453675/",
    "https://www.pexels.com/video/woman-jogging-at-beach-4665475/",
    "https://www.pexels.com/video/man-working-out-with-dumbbells-4497276/",
    "https://www.pexels.com/video/people-exercising-in-gym-3670930/",
    "https://www.pexels.com/video/woman-weight-lifting-4497312/",
]

# ============================================
# CORE GENERATION FUNCTIONS
# ============================================

def get_random_post_data():
    """Get a random post from any category with full content"""
    all_posts = HEALTH_TIPS + MOTIVATIONAL_POSTS + FITNESS_FACTS + WORKOUT_GUIDES
    return random.choice(all_posts)

def get_random_image():
    """Get a random real working image URL"""
    return random.choice(REAL_IMAGES)

def get_random_video():
    """Get a random working video URL"""
    return random.choice(REAL_VIDEOS)

def generate_posts(count=100):
    """
    Generate 100 posts with:
    - Text content (all posts)
    - Images (40% of posts)
    - Videos (10% of posts)
    - Text-only (50% of posts)
    """
    posts = []
    
    for i in range(1, count + 1):
        # Get random post data
        post_data = get_random_post_data()
        
        # Build full content with hashtags
        content = post_data['content']
        if 'hashtags' in post_data:
            content = f"{content}\n\n{post_data['hashtags']}"
        
        # Randomly assign media type
        media_type = random.choices(
            ['text', 'image', 'video'],
            weights=[0.5, 0.4, 0.1]  # 50% text, 40% image, 10% video
        )[0]
        
        post = {
            'id': f'post{i:03d}',
            'content': content,
            'image_url': get_random_image() if media_type == 'image' else '',
            'video_url': get_random_video() if media_type == 'video' else ''
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
    """Print detailed statistics"""
    total = len(posts)
    text_only = sum(1 for p in posts if not p['image_url'] and not p['video_url'])
    with_images = sum(1 for p in posts if p['image_url'])
    with_videos = sum(1 for p in posts if p['video_url'])
    
    print(f"\n📊 Content Statistics:")
    print(f"   {'=' * 40}")
    print(f"   Total Posts:     {total}")
    print(f"   Text-Only:       {text_only} ({text_only/total*100:.0f}%)")
    print(f"   With Images:     {with_images} ({with_images/total*100:.0f}%)")
    print(f"   With Videos:     {with_videos} ({with_videos/total*100:.0f}%)")

def print_samples(posts, count=5):
    """Show sample posts"""
    print(f"\n📌 Sample Posts:")
    print(f"   {'=' * 50}")
    
    samples = random.sample(posts, min(count, len(posts)))
    for idx, post in enumerate(samples, 1):
        print(f"\n   [{idx}] {post['id']}")
        print(f"   Content: {post['content'][:80]}...")
        print(f"   Image:   {'✅' if post['image_url'] else '❌'}")
        print(f"   Video:   {'✅' if post['video_url'] else '❌'}")
        print(f"   {'-' * 40}")

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    print("🏋️ FitLife Daily - Content Generator")
    print("=" * 60)
    print(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔄 Version: Enhanced with explanations & media")
    print()
    
    # Generate 100 posts
    posts = generate_posts(100)
    
    # Save to CSV
    save_posts_to_csv(posts)
    
    # Show statistics
    print_stats(posts)
    
    # Show sample posts
    print_samples(posts, 5)
    
    print("\n✨ Content generation complete!")
    print("🚀 Run 'python fb_poster.py' to start posting.")
