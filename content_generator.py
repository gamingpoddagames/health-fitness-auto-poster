#!/usr/bin/env python3
"""
FitLife Daily - Content Generator (Text-Only)
Works without any external dependencies!
"""

import csv
import random
from datetime import datetime

# ============================================
# CONTENT DATABASE (50 unique posts)
# ============================================

POSTS_CONTENT = [
    # Health Tips (15)
    "Start your day with 5 minutes of dynamic stretching! Increases blood flow by 30% and reduces injury risk.\n\n#FitnessTips #HealthyLiving #FitLifeDaily",
    "Add spinach to your morning smoothie! 50% Vitamin K, 20% Iron - and you won't even taste it!\n\n#HealthyEating #Nutrition #FitLifeDaily",
    "Drink 8 glasses of water daily! Boosts metabolism by 30% and improves skin health.\n\n#Hydration #Wellness #FitLifeDaily",
    "Get 7-8 hours of quality sleep! 40% faster muscle recovery and balanced hormones.\n\n#SleepWell #Recovery #FitLifeDaily",
    "3 days strength + 2 days cardio + 2 rest days = the ideal weekly routine!\n\n#WorkoutPlan #Fitness #FitLifeDaily",
    "Take 5 deep breaths using the 4-4-4 method: Inhale 4s, Hold 4s, Exhale 4s. Stress relief in 60 seconds!\n\n#MentalHealth #StressRelief #FitLifeDaily",
    "Set SMART goals: Specific, Measurable, Achievable, Relevant, Time-bound. Write your goal down today!\n\n#GoalSetting #Motivation #FitLifeDaily",
    "7 minutes of high-intensity exercise = 30 minutes of moderate activity. No excuses!\n\n#QuickWorkout #Fitness #FitLifeDaily",
    "Avocado with sea salt and chili flakes. Healthy fats, fiber, and potassium in 5 minutes!\n\n#HealthySnacks #CleanEating #FitLifeDaily",
    "HIIT: 20 sec work / 10 sec rest x 8 rounds. Burns fat for 24 hours post-workout!\n\n#HIIT #FatBurn #FitLifeDaily",
    "Walk 10 minutes after each meal! Improves digestion and reduces blood sugar spikes by 20%.\n\n#HealthyHabits #Walking #FitLifeDaily",
    "Eat protein within 30 minutes post-workout! 20-30g protein for optimal muscle recovery.\n\n#Nutrition #PostWorkout #FitLifeDaily",
    "Track your progress weekly! Measurements, photos, workout logs - celebrate every win!\n\n#Progress #FitnessJourney #FitLifeDaily",
    "Create a playlist with 120-140 BPM music! Increases workout performance by 15%.\n\n#WorkoutMusic #Motivation #FitLifeDaily",
    "Replace running shoes every 300-500 miles! Prevents injury and joint pain.\n\n#FitnessGear #Safety #FitLifeDaily",
    
    # Motivational Quotes (15)
    "The only bad workout is the one that didn't happen. Even 10 minutes counts!\n\n#Motivation #FitnessMindset #FitLifeDaily",
    "Your body can do it. Your mind is the one that needs convincing. Push through the doubt!\n\n#Mindset #BelieveInYourself #FitLifeDaily",
    "Discipline equals freedom. Show up every day. Consistency is the real superpower!\n\n#Discipline #Consistency #FitLifeDaily",
    "Don't wish for it. Work for it. Every rep, every step brings you closer.\n\n#Grind #HardWork #FitLifeDaily",
    "Motivation gets you started. Habit keeps you going. Build systems, not just goals.\n\n#Habits #Success #FitLifeDaily",
    "Progress, not perfection. Every step counts. Small improvements = massive results.\n\n#Progress #SelfImprovement #FitLifeDaily",
    "You are stronger than you think. Prove it to yourself. Trust your resilience.\n\n#Strength #Believe #FitLifeDaily",
    "The pain you feel today is the strength you'll feel tomorrow. Growth requires discomfort!\n\n#NoPainNoGain #Growth #FitLifeDaily",
    "Small daily improvements equal massive results over time. 1% daily = 37x in a year!\n\n#Consistency #SmallWins #FitLifeDaily",
    "Your only competition is the person in the mirror. Are you better than yesterday?\n\n#SelfImprovement #Focus #FitLifeDaily",
    "Success isn't given, it's earned. Thousands of hours of work behind every achievement.\n\n#Success #HardWork #FitLifeDaily",
    "When you feel like quitting, remember why you started. Keep going!\n\n#KeepGoing #Perseverance #FitLifeDaily",
    "Make yourself proud. This journey is about you. Never give up!\n\n#Pride #SelfLove #FitLifeDaily",
    "The choices you make today shape the person you become tomorrow.\n\n#Choices #FutureYou #FitLifeDaily",
    "One day, or Day One. You decide. Start today!\n\n#DayOne #NewBeginnings #FitLifeDaily",
    
    # Fitness Facts (10)
    "Walking 10,000 steps burns 400-500 calories! Park farther, take stairs, walk after lunch.\n\n#Walking #FitnessFacts #FitLifeDaily",
    "Regular cardio reduces heart disease risk by 30%! Just 30 minutes, 5x weekly.\n\n#Cardio #HeartHealth #FitLifeDaily",
    "Muscle weighs more than fat but takes up less space. The scale may not move but your clothes get looser!\n\n#BodyComposition #FitnessTruth #FitLifeDaily",
    "Stretching increases blood flow to muscles by 30%. Improves flexibility and prevents injury.\n\n#Stretching #Flexibility #FitLifeDaily",
    "Drinking 500ml of water boosts metabolism by 30% for one hour! Stay hydrated!\n\n#Hydration #Metabolism #FitLifeDaily",
    "Laughter burns up to 40 calories in 15 minutes! Watch a funny video and enjoy!\n\n#Laughter #Wellness #FitLifeDaily",
    "It takes 21 days to form a new habit. Commit for 3 weeks and it becomes automatic!\n\n#HabitFormation #Consistency #FitLifeDaily",
    "After 40, protein needs increase to 1.2g per kg of body weight. Prioritize protein!\n\n#Protein #Nutrition #HealthyAging #FitLifeDaily",
    "Rest days prevent burnout and injury. Your muscles grow during rest, not during training!\n\n#RestDays #Recovery #FitLifeDaily",
    "A 30-minute workout 5x weekly beats a 2-hour workout once a week. Consistency is everything!\n\n#Consistency #FitnessJourney #FitLifeDaily",
    
    # Workout Guides (10)
    "Beginner Bodyweight Workout (15 min): 10 squats, 10 push-ups, 10 lunges, 20s plank, 10 glute bridges. Repeat 3x!\n\n#Workout #Bodyweight #FitLifeDaily",
    "20-Minute Cardio Circuit: 1 min jumping jacks, 1 min high knees, 30s burpees, 30s rest. Repeat 5x!\n\n#Cardio #HIIT #FitLifeDaily",
    "30-Minute Dumbbell Workout: Squats 12x3, Rows 12x3, Press 10x3, Lunges 10x3, Curls 12x3.\n\n#Dumbbells #StrengthTraining #FitLifeDaily",
    "5-Minute Morning Routine: Neck rolls, shoulder shrugs, arm circles, torso twists, squats, jumping jacks!\n\n#MorningRoutine #WakeUp #FitLifeDaily",
    "3-Minute Office Break: Chair squats 10, desk push-ups 10, leg raises 10, neck stretches 30s!\n\n#OfficeWorkout #ActiveBreak #FitLifeDaily",
    "10-Minute Core Workout: Plank 45s, bicycle crunches 15, Russian twists 15, leg raises 12, bird-dog 10!\n\n#CoreWorkout #Abs #FitLifeDaily",
    "10-Minute Full Body Stretch: Forward fold, downward dog, cobra, cat-cow, quad stretch, hamstring stretch!\n\n#Stretching #Flexibility #FitLifeDaily",
    "4-Minute Tabata: One exercise, 8 rounds. 20s MAX effort, 10s rest. Squats, push-ups, burpees, or climbers!\n\n#Tabata #HIIT #FitLifeDaily",
    "5-Minute Evening Routine: Deep breathing 1min, neck stretches 30s, child's pose 1min, legs up wall 2min!\n\n#EveningRoutine #Relaxation #FitLifeDaily",
    "Full Body Home Workout: Squats 15, push-ups 10, lunges 12, plank 30s, glute bridges 15, mountain climbers 30s!\n\n#HomeWorkout #NoEquipment #FitLifeDaily",
]

def generate_posts(count=50):
    """Generate text-only posts"""
    posts = []
    for i, content in enumerate(POSTS_CONTENT[:count], 1):
        posts.append({
            'id': f'post{i:03d}',
            'content': content,
            'image_url': '',
            'video_url': ''
        })
    return posts

def save_posts(posts, filename='posts.csv'):
    """Save posts to CSV"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'content', 'image_url', 'video_url'])
        writer.writeheader()
        writer.writerows(posts)
    print(f"Generated {len(posts)} posts saved to {filename}")

def print_stats(posts):
    total = len(posts)
    print(f"\nTotal Posts: {total}")
    print(f"Type: Text-only (no external dependencies)")

def print_samples(posts, count=3):
    print(f"\nSample Posts:")
    for i, post in enumerate(posts[:count], 1):
        print(f"\n   [{i}] {post['id']}")
        preview = post['content'][:70] + "..." if len(post['content']) > 70 else post['content']
        print(f"   {preview}")

if __name__ == "__main__":
    print("FitLife Daily - Content Generator")
    print("=" * 55)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    posts = generate_posts(50)
    save_posts(posts)
    print_stats(posts)
    print_samples(posts, 3)
    
    print(f"\nGenerated {len(posts)} posts ready to publish!")
    print("Run 'python fb_poster.py' to start posting")
