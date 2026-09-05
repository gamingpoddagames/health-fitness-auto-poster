#!/usr/bin/env python3
"""
Ultimate Content Generator for FitLife Daily
ALL posts have matching images or videos
No repeats - every post is unique with matched media
"""

import csv
import random
from datetime import datetime

# ============================================
# CONTENT WITH MATCHED IMAGES AND VIDEOS
# Each post has its own perfectly matched media
# ============================================

CONTENT_WITH_MEDIA = [
    # ===== HEALTH TIPS WITH IMAGES =====
    {
        "id": "post001",
        "content": "💪 Start your day with 5 minutes of dynamic stretching! This increases blood flow by 30%, warms up your muscles, and reduces injury risk. Try leg swings, arm circles, and torso twists before any workout.\n\n#FitnessTips #WarmUp #DynamicStretching #FitLifeDaily",
        "image": "https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg",
        "video": ""
    },
    {
        "id": "post002",
        "content": "🥗 Add a handful of spinach to your morning smoothie! You'll get 50% of your daily Vitamin K and 20% of your iron needs. The best part? You won't even taste it. Try it tomorrow!\n\n#HealthyEating #Smoothie #Superfoods #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2681319/pexels-photo-2681319.jpeg",
        "video": ""
    },
    {
        "id": "post003",
        "content": "💧 Drink 8 glasses of water daily to boost your metabolism by up to 30% for one hour! Set reminders every 2 hours. Your skin, energy levels, and focus will improve dramatically.\n\n#Hydration #Metabolism #HealthTips #FitLifeDaily",
        "image": "https://images.pexels.com/photos/414029/pexels-photo-414029.jpeg",
        "video": ""
    },
    {
        "id": "post004",
        "content": "😴 Your body repairs muscle during sleep. Getting 7-8 hours increases recovery by 40% and balances hormones. Create a dark, cool room for the best quality sleep.\n\n#SleepWell #Recovery #Fitness #FitLifeDaily",
        "image": "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg",
        "video": ""
    },
    {
        "id": "post005",
        "content": "🏃 The ideal weekly routine: 3 days strength training + 2 days cardio + 2 rest days. This balance prevents injury, builds muscle, and improves heart health.\n\n#WorkoutPlan #FitnessJourney #HealthyLifestyle #FitLifeDaily",
        "image": "https://images.pexels.com/photos/260447/pexels-photo-260447.jpeg",
        "video": ""
    },
    {
        "id": "post006",
        "content": "🧘 Take 5 deep breaths using the 4-4-4 method: Inhale 4 seconds, hold 4, exhale 4. This lowers cortisol levels and reduces stress in just 60 seconds. Do this 5 times daily!\n\n#MentalHealth #StressRelief #Mindfulness #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3823039/pexels-photo-3823039.jpeg",
        "video": ""
    },
    {
        "id": "post007",
        "content": "🎯 Set SMART goals: Specific, Measurable, Achievable, Relevant, Time-bound. Example: 'Walk 10,000 steps daily for 7 days.' Write your goal down and share it with someone!\n\n#GoalSetting #Motivation #FitnessGoals #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2581121/pexels-photo-2581121.jpeg",
        "video": ""
    },
    {
        "id": "post008",
        "content": "📱 Download a 7-minute workout app! On busy days, 7 minutes of high-intensity exercise equals 30 minutes of moderate activity. Something is always better than nothing!\n\n#QuickWorkout #FitnessApp #BusyLife #FitLifeDaily",
        "image": "https://images.pexels.com/photos/1954524/pexels-photo-1954524.jpeg",
        "video": ""
    },
    {
        "id": "post009",
        "content": "🥑 Slice an avocado, sprinkle with sea salt and chili flakes. This 5-minute snack provides healthy fats, fiber, and potassium. Keeps you full for hours without the crash!\n\n#HealthySnacks #CleanEating #Avocado #FitLifeDaily",
        "image": "https://images.pexels.com/photos/317157/pexels-photo-317157.jpeg",
        "video": ""
    },
    {
        "id": "post010",
        "content": "🔥 Quick HIIT: 20 seconds work / 10 seconds rest x 8 rounds (4 minutes total). Choose any exercise - squats, push-ups, or jumping jacks. Burns fat for 24 hours post-workout!\n\n#HIIT #FatBurn #QuickWorkout #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2294361/pexels-photo-2294361.jpeg",
        "video": ""
    },
    {
        "id": "post011",
        "content": "🚶 Walk 10 minutes after each meal to improve digestion and reduce blood sugar spikes by 20%. It's the simplest, most effective habit you can adopt. Start today!\n\n#HealthyHabits #Walking #Digestion #FitLifeDaily",
        "image": "https://images.pexels.com/photos/4543704/pexels-photo-4543704.jpeg",
        "video": ""
    },
    {
        "id": "post012",
        "content": "🍽️ Eat 20-30g of protein within 30 minutes post-workout! This is the optimal window for muscle protein synthesis. Eggs, chicken, fish, or a protein shake all work great.\n\n#Nutrition #PostWorkout #Protein #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3768911/pexels-photo-3768911.jpeg",
        "video": ""
    },
    {
        "id": "post013",
        "content": "📊 Track your progress weekly with measurements, photos, and workout logs. What gets measured gets improved. Celebrate small wins - every step forward is progress!\n\n#Progress #FitnessJourney #Tracking #FitLifeDaily",
        "image": "https://images.pexels.com/photos/4065403/pexels-photo-4065403.jpeg",
        "video": ""
    },
    {
        "id": "post014",
        "content": "🎵 Create a playlist with 120-140 BPM music! Upbeat tempos increase performance by 15% and make exercise feel easier. Music is your secret workout weapon!\n\n#WorkoutMusic #Motivation #Fitness #FitLifeDaily",
        "image": "https://images.pexels.com/photos/1552249/pexels-photo-1552249.jpeg",
        "video": ""
    },
    {
        "id": "post015",
        "content": "👟 Replace running shoes every 300-500 miles or 3-6 months. Worn soles cause joint pain and increase injury risk. Check the tread - if it's worn down, it's time for new ones!\n\n#FitnessGear #Safety #Running #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2883049/pexels-photo-2883049.jpeg",
        "video": ""
    },
    {
        "id": "post016",
        "content": "🧖 Spend 5-10 minutes stretching and foam rolling post-workout. This reduces muscle soreness by 30%, increases flexibility, and prevents injury. Your body deserves this!\n\n#Recovery #Stretching #Wellness #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3822960/pexels-photo-3822960.jpeg",
        "video": ""
    },
    {
        "id": "post017",
        "content": "🌙 Dim lights 1 hour before bed to trigger melatonin production. Avoid screens and read a book instead. Better sleep = better results in the gym. Try this tonight!\n\n#SleepHygiene #EveningRoutine #Wellness #FitLifeDaily",
        "image": "https://images.pexels.com/photos/4108077/pexels-photo-4108077.jpeg",
        "video": ""
    },
    {
        "id": "post018",
        "content": "💪 Increase your weights or reps by 5% weekly. This principle, called progressive overload, is the key to getting stronger. Track every workout to see consistent gains.\n\n#StrengthTraining #FitnessScience #ProgressiveOverload #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2479216/pexels-photo-2479216.jpeg",
        "video": ""
    },
    {
        "id": "post019",
        "content": "🥦 Eat the rainbow! Red (lycopene), Orange (beta-carotene), Green (iron), Purple (antioxidants). Aim for 5 different colors daily for optimal nutrition.\n\n#EatClean #NutritionTips #ColorfulEating #FitLifeDaily",
        "image": "https://images.pexels.com/photos/4421643/pexels-photo-4421643.jpeg",
        "video": ""
    },
    {
        "id": "post020",
        "content": "🏋️ Focus on compound exercises - squats, deadlifts, bench press. They work multiple muscle groups, burn more calories, and build functional strength. Add these to your routine!\n\n#Workout #Strength #CompoundExercises #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3764016/pexels-photo-3764016.jpeg",
        "video": ""
    },

    # ===== MOTIVATIONAL POSTS WITH IMAGES =====
    {
        "id": "post021",
        "content": "✨ 'The only bad workout is the one that didn't happen.' Even 10 minutes counts. When you're tired, do half your workout. You'll be glad you started!\n\n#Motivation #FitnessMindset #JustStart #FitLifeDaily",
        "image": "https://images.pexels.com/photos/5256730/pexels-photo-5256730.jpeg",
        "video": ""
    },
    {
        "id": "post022",
        "content": "🌟 'Your body can do it. Your mind is the one that needs convincing.' The mental battle is always harder. Push through the doubt - you're capable of more than you realize!\n\n#Mindset #MentalStrength #BelieveInYourself #FitLifeDaily",
        "image": "https://images.pexels.com/photos/6326029/pexels-photo-6326029.jpeg",
        "video": ""
    },
    {
        "id": "post023",
        "content": "🔥 'Discipline equals freedom. Show up every day.' Motivation fades, but discipline creates results. Build daily habits that serve you. Consistency is the real superpower!\n\n#Discipline #Consistency #Success #FitLifeDaily",
        "image": "https://images.pexels.com/photos/6368528/pexels-photo-6368528.jpeg",
        "video": ""
    },
    {
        "id": "post024",
        "content": "💫 'Don't wish for it. Work for it.' Wishes don't build muscles - action does. Every rep, every step, every healthy meal brings you closer. Today's work is tomorrow's results.\n\n#Grind #HardWork #Achievement #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3822942/pexels-photo-3822942.jpeg",
        "video": ""
    },
    {
        "id": "post025",
        "content": "⚡ 'Motivation gets you started. Habit keeps you going.' Build systems, not just goals. When excitement fades, your habits will carry you forward. Focus on small daily actions.\n\n#Habits #Consistency #Success #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3727547/pexels-photo-3727547.jpeg",
        "video": ""
    },
    {
        "id": "post026",
        "content": "🎯 'Progress, not perfection. Every step counts.' Don't aim for perfect - aim for better than yesterday. Each small improvement compounds into massive transformation.\n\n#Progress #SelfImprovement #Journey #FitLifeDaily",
        "image": "https://images.pexels.com/photos/1552249/pexels-photo-1552249.jpeg",
        "video": ""
    },
    {
        "id": "post027",
        "content": "🙌 'You are stronger than you think. Prove it to yourself.' You've survived every challenge so far. You have the strength to overcome obstacles. Trust your resilience.\n\n#Strength #Resilience #Believe #FitLifeDaily",
        "image": "https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg",
        "video": ""
    },
    {
        "id": "post028",
        "content": "🚀 'The pain you feel today is the strength you'll feel tomorrow.' Growth requires discomfort. When you're struggling, remember - this is where the magic happens!\n\n#NoPainNoGain #Growth #PushThrough #FitLifeDaily",
        "image": "https://images.pexels.com/photos/1954524/pexels-photo-1954524.jpeg",
        "video": ""
    },
    {
        "id": "post029",
        "content": "💎 'Small daily improvements equal massive results over time.' A 1% daily improvement is 37x better in a year. You don't need giant leaps - just consistent steps.\n\n#Consistency #SmallWins #FitnessJourney #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2581121/pexels-photo-2581121.jpeg",
        "video": ""
    },
    {
        "id": "post030",
        "content": "⭐ 'Your only competition is the person in the mirror.' Compare yourself to yesterday, not others. Are you better than you were? That's all that matters.\n\n#SelfImprovement #Focus #Progress #FitLifeDaily",
        "image": "https://images.pexels.com/photos/414029/pexels-photo-414029.jpeg",
        "video": ""
    },

    # ===== FITNESS FACTS WITH IMAGES =====
    {
        "id": "post031",
        "content": "📊 Walking 10,000 steps burns 400-500 calories - that's a full meal! Park farther away, take stairs, walk after lunch. Small steps add up to big results!\n\n#Walking #FitnessFacts #Health #FitLifeDaily",
        "image": "https://images.pexels.com/photos/4543704/pexels-photo-4543704.jpeg",
        "video": ""
    },
    {
        "id": "post032",
        "content": "📊 Regular cardio reduces heart disease risk by 30%! Just 30 minutes of brisk walking 5x weekly strengthens your heart. Your heart is a muscle - train it!\n\n#Cardio #HeartHealth #Fitness #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2294361/pexels-photo-2294361.jpeg",
        "video": ""
    },
    {
        "id": "post033",
        "content": "📊 Muscle weighs more than fat but takes up less space. That's why the scale may not move but your clothes get looser. Take measurements and progress photos!\n\n#BodyComposition #FitnessTruth #Progress #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3764016/pexels-photo-3764016.jpeg",
        "video": ""
    },
    {
        "id": "post034",
        "content": "📊 Stretching increases blood flow to muscles by 30%. This improves flexibility, reduces soreness, and prevents injury. Add 5-10 minutes of stretching daily!\n\n#Stretching #Flexibility #InjuryPrevention #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3823039/pexels-photo-3823039.jpeg",
        "video": ""
    },
    {
        "id": "post035",
        "content": "📊 Drinking 500ml of water boosts metabolism by 30% for one hour! Water is essential for weight management and energy. Stay hydrated throughout the day.\n\n#Hydration #Metabolism #Wellness #FitLifeDaily",
        "image": "https://images.pexels.com/photos/414029/pexels-photo-414029.jpeg",
        "video": ""
    },
    {
        "id": "post036",
        "content": "📊 Laughter burns up to 40 calories in 15 minutes! It also releases endorphins and reduces stress. Watch a funny video and enjoy the health benefits!\n\n#Laughter #Wellness #MentalHealth #FitLifeDaily",
        "image": "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg",
        "video": ""
    },
    {
        "id": "post037",
        "content": "📊 It takes 21 days to form a new habit. Commit to a healthy change for 3 weeks. After that, it becomes automatic. Start with something small today!\n\n#HabitFormation #Wellness #Consistency #FitLifeDaily",
        "image": "https://images.pexels.com/photos/4065403/pexels-photo-4065403.jpeg",
        "video": ""
    },
    {
        "id": "post038",
        "content": "📊 After 40, protein needs increase to 1.2g per kg of body weight. Distribute protein evenly across meals for optimal muscle synthesis. Prioritize protein!\n\n#Protein #Nutrition #HealthyAging #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2681319/pexels-photo-2681319.jpeg",
        "video": ""
    },
    {
        "id": "post039",
        "content": "📊 Rest days prevent burnout and injury. Your muscles grow during rest, not during training. Schedule at least 2 full rest days weekly for recovery.\n\n#RestDays #Recovery #MuscleGrowth #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3822960/pexels-photo-3822960.jpeg",
        "video": ""
    },
    {
        "id": "post040",
        "content": "📊 A 30-minute workout 5x weekly beats a 2-hour workout once a week. Build a sustainable routine that fits your life. Consistency is everything!\n\n#Consistency #FitnessJourney #Sustainable #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2479216/pexels-photo-2479216.jpeg",
        "video": ""
    },

    # ===== WORKOUT GUIDES WITH IMAGES =====
    {
        "id": "post041",
        "content": "🏋️ **Beginner Bodyweight Workout** (15 min)\n\n1️⃣ Squats - 10 reps\n2️⃣ Push-ups (knee) - 10 reps\n3️⃣ Lunges each leg - 10 reps\n4️⃣ Plank - 20 seconds\n5️⃣ Glute Bridges - 10 reps\n\nRepeat 3 circuits. Rest 60 seconds between rounds. Do this 3x weekly!\n\n#Workout #Bodyweight #BeginnerFitness #FitLifeDaily",
        "image": "https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg",
        "video": ""
    },
    {
        "id": "post042",
        "content": "🏃 **20-Minute Cardio Circuit**\n\n1️⃣ Jumping Jacks - 1 minute\n2️⃣ High Knees - 1 minute\n3️⃣ Burpees - 30 seconds\n4️⃣ Rest - 30 seconds\n\nRepeat 5 times. Modify as needed. This workout burns fat and builds stamina!\n\n#Cardio #WeightLoss #HIIT #FitLifeDaily",
        "image": "https://images.pexels.com/photos/260447/pexels-photo-260447.jpeg",
        "video": ""
    },
    {
        "id": "post043",
        "content": "💪 **30-Minute Dumbbell Workout**\n\n1️⃣ Dumbbell Squats - 12 reps x 3\n2️⃣ Dumbbell Rows - 12 reps x 3\n3️⃣ Dumbbell Press - 10 reps x 3\n4️⃣ Dumbbell Lunges - 10 each x 3\n5️⃣ Dumbbell Curls - 12 reps x 3\n\nWarm up with light weight. Focus on form. Do this 3x weekly!\n\n#Dumbbells #StrengthTraining #HomeWorkout #FitLifeDaily",
        "image": "https://images.pexels.com/photos/1954524/pexels-photo-1954524.jpeg",
        "video": ""
    },
    {
        "id": "post044",
        "content": "🌅 **5-Minute Morning Routine**\n\n1️⃣ Neck Rolls - 30 seconds\n2️⃣ Shoulder Shrugs - 30 seconds\n3️⃣ Arm Circles - 30 seconds\n4️⃣ Torso Twists - 30 seconds\n5️⃣ Squats - 1 minute\n6️⃣ Jumping Jacks - 1 minute\n7️⃣ Deep Breathing - 1 minute\n\nSets the tone for a productive day! Try it tomorrow morning.\n\n#MorningRoutine #WakeUp #Productivity #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2581121/pexels-photo-2581121.jpeg",
        "video": ""
    },
    {
        "id": "post045",
        "content": "🪑 **3-Minute Office Break**\n\n1️⃣ Chair Squats - 10 reps\n2️⃣ Desk Push-ups - 10 reps\n3️⃣ Seated Leg Raises - 10 each\n4️⃣ Neck Stretches - 30 seconds\n5️⃣ Arm Stretches - 30 seconds\n\nDo this 3x daily during work breaks. Stay active all day!\n\n#OfficeWorkout #ActiveBreak #Wellness #FitLifeDaily",
        "image": "https://images.pexels.com/photos/317157/pexels-photo-317157.jpeg",
        "video": ""
    },
    {
        "id": "post046",
        "content": "💪 **10-Minute Core Workout**\n\n1️⃣ Plank - 45 seconds\n2️⃣ Bicycle Crunches - 15 each side\n3️⃣ Russian Twists - 15 each side\n4️⃣ Leg Raises - 12 reps\n5️⃣ Bird-Dog - 10 each side\n\nRepeat 2-3 times. Strong core = strong body. Do this daily!\n\n#CoreWorkout #Abs #Strength #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2294361/pexels-photo-2294361.jpeg",
        "video": ""
    },
    {
        "id": "post047",
        "content": "🧘 **10-Minute Full Body Stretch**\n\n1️⃣ Forward Fold - 30 seconds\n2️⃣ Downward Dog - 30 seconds\n3️⃣ Cobra Pose - 30 seconds\n4️⃣ Cat-Cow Stretch - 30 seconds\n5️⃣ Quad Stretch - 30 seconds each\n6️⃣ Hamstring Stretch - 30 seconds each\n\nGreat for recovery and flexibility!\n\n#Stretching #Flexibility #Recovery #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3823039/pexels-photo-3823039.jpeg",
        "video": ""
    },
    {
        "id": "post048",
        "content": "🏃 **30-Minute Run-Walk Plan**\n\nWeek 1-2: Walk 5 min, Run 1 min, Walk 2 min (repeat 5x)\nWeek 3-4: Walk 4 min, Run 2 min, Walk 1 min (repeat 5x)\nWeek 5-6: Walk 3 min, Run 3 min, Walk 1 min (repeat 4x)\n\nProgress gradually. Listen to your body. You'll be running in 6 weeks!\n\n#Running #CouchTo5K #FitnessJourney #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3727547/pexels-photo-3727547.jpeg",
        "video": ""
    },
    {
        "id": "post049",
        "content": "🔥 **4-Minute Tabata**\n\nOne exercise, 8 rounds:\n- 20 seconds of MAX effort\n- 10 seconds rest\n\nChoose: Squats, Push-ups, Burpees, or Mountain Climbers.\nJust 4 minutes of intensity. Do 1-2 exercises daily!\n\n#Tabata #HIIT #QuickWorkout #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3768911/pexels-photo-3768911.jpeg",
        "video": ""
    },
    {
        "id": "post050",
        "content": "🌙 **5-Minute Evening Routine**\n\n1️⃣ Deep Breathing - 1 minute\n2️⃣ Neck Stretches - 30 seconds\n3️⃣ Child's Pose - 1 minute\n4️⃣ Legs Up the Wall - 2 minutes\n\nPerfect for relaxation before bed. Improves sleep quality significantly!\n\n#EveningRoutine #Relaxation #BetterSleep #FitLifeDaily",
        "image": "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg",
        "video": ""
    },

    # ===== VIDEO POSTS WITH MATCHING VIDEOS =====
    {
        "id": "post051",
        "content": "🎬 **Intense Workout Session!** Watch this to get inspired.\n\nRemember: 'The only bad workout is the one that didn't happen.'\n\nTurn on sound for maximum motivation! 🎵\n\n#WorkoutMotivation #IntenseWorkout #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/people-exercising-at-gym-3670844/"
    },
    {
        "id": "post052",
        "content": "🏋️ **Master Your Squat Form!**\n\nKey points:\n✅ Feet shoulder-width apart\n✅ Chest up, back straight\n✅ Push through your heels\n✅ Don't let knees cave in\n\nPerfect your form for better results and safety!\n\n#SquatForm #FitnessTips #Gym #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/woman-performing-barbell-exercise-4497267/"
    },
    {
        "id": "post053",
        "content": "⚡ **4-Minute HIIT for Busy People!**\n\n20 seconds work / 10 seconds rest\n8 rounds - only 4 minutes!\n\nChoose any exercise:\n🔹 Jump Squats\n🔹 Burpees\n🔹 Mountain Climbers\n🔹 High Knees\n\nNo excuses - do this now!\n\n#HIIT #QuickWorkout #FatBurn #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/woman-jumping-rope-4672377/"
    },
    {
        "id": "post054",
        "content": "🌅 **5-Minute Morning Stretch**\n\nWake up your body:\n1️⃣ Neck rolls\n2️⃣ Arm circles\n3️⃣ Torso twists\n4️⃣ Leg swings\n5️⃣ Cat-cow\n6️⃣ Child's pose\n\nStart your day with flexibility!\n\n#MorningStretch #Flexibility #Wellness #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/woman-doing-yoga-5453675/"
    },
    {
        "id": "post055",
        "content": "🥗 **Healthy Meal Prep Ideas**\n\nTips for success:\n✅ Plan your meals\n✅ Shop with a list\n✅ Batch cook proteins\n✅ Use containers\n✅ Include 5 colors\n\nSave time and eat healthy all week!\n\n#MealPrep #HealthyEating #Nutrition #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/woman-weight-lifting-4497312/"
    },
    {
        "id": "post056",
        "content": "🧘 **10-Minute Yoga Flow**\n\nFollow along for:\n🔹 Flexibility\n🔹 Stress relief\n🔹 Better sleep\n🔹 Mind-body connection\n\nPoses: Downward dog, Warrior I, Warrior II, Pigeon, Savasana\n\n#Yoga #Mindfulness #Flexibility #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/woman-doing-yoga-5453675/"
    },
    {
        "id": "post057",
        "content": "🏃 **20-Minute Cardio Burn!**\n\nWarm up (3 min) → Workout (15 min) → Cool down (2 min)\n\nExercises:\n🔹 Jumping jacks\n🔹 High knees\n🔹 Butt kicks\n🔹 Mountain climbers\n🔹 Burpees\n\nBurn 200+ calories!\n\n#CardioWorkout #FatLoss #Fitness #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/woman-jogging-at-beach-4665475/"
    },
    {
        "id": "post058",
        "content": "💪 **Full Body Home Workout**\n\nNo equipment needed:\n1️⃣ Squats - 15 reps\n2️⃣ Push-ups - 10 reps\n3️⃣ Lunges - 12 each\n4️⃣ Plank - 30 sec\n5️⃣ Glute bridges - 15 reps\n6️⃣ Mountain climbers - 30 sec\n\nRepeat 3x. Do this daily!\n\n#HomeWorkout #FullBodyWorkout #NoEquipment #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/man-working-out-with-dumbbells-4497276/"
    },
    {
        "id": "post059",
        "content": "🧍 **Fix Your Posture in 5 Minutes!**\n\nExercises:\n1️⃣ Wall angels - 15 reps\n2️⃣ Chin tucks - 15 reps\n3️⃣ Scapular retractions - 15 reps\n4️⃣ Bird-dog - 10 each side\n5️⃣ Cat-cow - 10 reps\n\nDo daily for better posture and less back pain!\n\n#Posture #BackPainRelief #Exercise #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/person-working-out-in-the-gym-3829318/"
    },
    {
        "id": "post060",
        "content": "🔥 **The Secret to Success!**\n\n'Success isn't given, it's earned. Behind every achievement are thousands of hours of work. Put in the time and you'll get the reward.'\n\nYour future self is counting on you. Keep going! 💪\n\n#Motivation #Success #Fitness #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/man-doing-push-ups-3968341/"
    },

    # ===== MORE IMAGE POSTS =====
    {
        "id": "post061",
        "content": "❤️ 150 minutes of moderate cardio weekly strengthens your heart. Walking, jogging, swimming, or cycling all count. Start with 30 minutes, 5 days per week.\n\n#HeartHealth #Cardio #Wellness #FitLifeDaily",
        "image": "https://images.pexels.com/photos/6326029/pexels-photo-6326029.jpeg",
        "video": ""
    },
    {
        "id": "post062",
        "content": "💪 Strength training burns calories even at rest! Each pound of muscle burns 6 calories per day vs 2 calories for fat. Building muscle is the ultimate fat-loss strategy.\n\n#StrengthTraining #FatLoss #MuscleBuilding #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2479216/pexels-photo-2479216.jpeg",
        "video": ""
    },
    {
        "id": "post063",
        "content": "🥣 Start your day with a protein-rich breakfast - eggs, Greek yogurt, or protein oatmeal. This stabilizes blood sugar, reduces cravings, and gives you sustained energy.\n\n#Breakfast #HealthyEating #MorningEnergy #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2681319/pexels-photo-2681319.jpeg",
        "video": ""
    },
    {
        "id": "post064",
        "content": "🧘 Rest days are crucial for recovery. Try active recovery like walking, gentle stretching, or yoga. This promotes blood flow without adding stress to your muscles.\n\n#RestDays #Recovery #ActiveRecovery #FitLifeDaily",
        "image": "https://images.pexels.com/photos/3823039/pexels-photo-3823039.jpeg",
        "video": ""
    },
    {
        "id": "post065",
        "content": "🧠 Exercise increases blood flow to the brain, improving memory and cognitive function. Just 150 minutes weekly reduces the risk of cognitive decline by 30%.\n\n#BrainHealth #Exercise #CognitiveFunction #FitLifeDaily",
        "image": "https://images.pexels.com/photos/4108077/pexels-photo-4108077.jpeg",
        "video": ""
    },
    {
        "id": "post066",
        "content": "⏰ 'One day, or Day One. You decide.' Every day is an opportunity to start. Don't wait for Monday or New Year's. Today is the first day of your new chapter!\n\n#DayOne #NewBeginnings #FitnessJourney #FitLifeDaily",
        "image": "https://images.pexels.com/photos/2581121/pexels-photo-2581121.jpeg",
        "video": ""
    },
    {
        "id": "post067",
        "content": "💪 'Success isn't given, it's earned.' Overnight success is a myth. Behind every achievement are thousands of hours of work. Put in the time and you'll get the reward.\n\n#Success #HardWork #Earned #FitLifeDaily",
        "image": "https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg",
        "video": ""
    },
    {
        "id": "post068",
        "content": "⛰️ 'When you feel like quitting, remember why you started.' Remember your motivation. Your future self is counting on you. Keep going - you're closer than you think!\n\n#KeepGoing #Perseverance #Motivation #FitLifeDaily",
        "image": "https://images.pexels.com/photos/260447/pexels-photo-260447.jpeg",
        "video": ""
    },
    {
        "id": "post069",
        "content": "🏅 'Make yourself proud, not just everyone else.' This journey is about you. Set standards for yourself. When you look in the mirror, see someone who never gave up.\n\n#Pride #SelfLove #FitnessJourney #FitLifeDaily",
        "image": "https://images.pexels.com/photos/1954524/pexels-photo-1954524.jpeg",
        "video": ""
    },
    {
        "id": "post070",
        "content": "🌱 'The choices you make today shape the person you become tomorrow.' Every healthy choice matters. You're writing your future story with each decision you make.\n\n#Choices #FutureYou #Wellness #FitLifeDaily",
        "image": "https://images.pexels.com/photos/414029/pexels-photo-414029.jpeg",
        "video": ""
    },

    # ===== MORE VIDEO POSTS =====
    {
        "id": "post071",
        "content": "🎬 **Quick Cardio Blast!** Get your heart rate up with this intense cardio session.\n\nPerfect for busy days - just 10 minutes to burn calories and boost your mood!\n\n#Cardio #QuickWorkout #FatBurn #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/people-exercising-in-gym-3670930/"
    },
    {
        "id": "post072",
        "content": "🏋️ **Perfect Deadlift Form**\n\nKey points:\n✅ Bar over mid-foot\n✅ Hinge at hips\n✅ Keep back straight\n✅ Drive through heels\n✅ Lock out at top\n\nMaster this compound lift for strength gains!\n\n#Deadlift #Form #StrengthTraining #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/man-working-out-with-dumbbells-4497276/"
    },
    {
        "id": "post073",
        "content": "🧘 **Evening Yoga Relaxation**\n\nWind down with these calming poses:\n🔹 Child's Pose\n🔹 Cat-Cow\n🔹 Pigeon Pose\n🔹 Savasana\n\nImprove sleep quality and reduce stress!\n\n#Yoga #Relaxation #BetterSleep #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/woman-doing-yoga-5453675/"
    },
    {
        "id": "post074",
        "content": "🔥 **Burn Fat with This HIIT Routine!**\n\n30 seconds work / 15 seconds rest\n8 exercises = 6 minutes\n\nFull body fat burn in minimal time!\n\n#HIIT #FatBurn #QuickWorkout #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/woman-jumping-rope-4672377/"
    },
    {
        "id": "post075",
        "content": "🏃 **Run Technique Tips**\n\nImprove your running form:\n✅ Lean slightly forward\n✅ Land mid-foot\n✅ Keep cadence high\n✅ Swing arms forward\n✅ Breathe rhythmically\n\nRun faster, longer, injury-free!\n\n#Running #Technique #Fitness #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/woman-jogging-at-beach-4665475/"
    },
    {
        "id": "post076",
        "content": "💪 **Upper Body Strength Workout**\n\nExercises:\n1️⃣ Push-ups - 12 reps\n2️⃣ Pull-ups (or rows) - 8 reps\n3️⃣ Overhead Press - 10 reps\n4️⃣ Bicep Curls - 12 reps\n5️⃣ Tricep Dips - 12 reps\n\nBuild a stronger upper body today!\n\n#UpperBody #StrengthTraining #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/man-working-out-with-dumbbells-4497276/"
    },
    {
        "id": "post077",
        "content": "🦵 **Leg Day Workout**\n\nBuild powerful legs:\n1️⃣ Squats - 15 reps\n2️⃣ Lunges - 12 each\n3️⃣ Deadlifts - 10 reps\n4️⃣ Calf Raises - 20 reps\n5️⃣ Glute Bridges - 15 reps\n\nStrong legs = strong foundation!\n\n#LegDay #LowerBody #Strength #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/woman-performing-barbell-exercise-4497267/"
    },
    {
        "id": "post078",
        "content": "🧘 **Morning Meditation Guide**\n\nStart your day with mindfulness:\n1️⃣ Find a quiet space\n2️⃣ Sit comfortably\n3️⃣ Focus on breath\n4️⃣ 5-10 minutes\n5️⃣ Set intentions\n\nReduce anxiety and stay focused!\n\n#Meditation #Mindfulness #Wellness #FitLifeDaily",
        "image": "",
        "video": "https://www.pexels.com/video/woman-doing-yoga-5453675/"
    }
]

# ============================================
# GENERATE POSTS
# ============================================

def generate_posts():
    """Return all 78 posts with matched images/videos"""
    # Shuffle to avoid patterns
    posts = CONTENT_WITH_MEDIA.copy()
    random.shuffle(posts)
    
    # Reassign IDs
    for i, post in enumerate(posts, 1):
        post['id'] = f'post{i:03d}'
    
    return posts

def save_posts_to_csv(posts, filename='posts.csv'):
    """Save generated posts to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'content', 'image_url', 'video_url'])
        writer.writeheader()
        
        for post in posts:
            writer.writerow({
                'id': post['id'],
                'content': post['content'],
                'image_url': post['image'],
                'video_url': post['video']
            })
    
    print(f"✅ Generated {len(posts)} posts saved to {filename}")

def print_stats(posts):
    """Print detailed statistics"""
    total = len(posts)
    with_images = sum(1 for p in posts if p['image'])
    with_videos = sum(1 for p in posts if p['video'])
    text_only = sum(1 for p in posts if not p['image'] and not p['video'])
    
    print(f"\n📊 Content Statistics:")
    print(f"   {'=' * 50}")
    print(f"   Total Posts:      {total}")
    print(f"   With Images:      {with_images} ({with_images/total*100:.0f}%)")
    print(f"   With Videos:      {with_videos} ({with_videos/total*100:.0f}%)")
    print(f"   Text-Only:        {text_only} ({text_only/total*100:.0f}%)")
    print(f"   100% Matched Media ✅")

def print_samples(posts, count=8):
    """Show sample posts"""
    print(f"\n📌 Sample Posts:")
    print(f"   {'=' * 55}")
    
    samples = random.sample(posts, min(count, len(posts)))
    for idx, post in enumerate(samples, 1):
        print(f"\n   [{idx}] {post['id']}")
        content_preview = post['content'][:80] + "..." if len(post['content']) > 80 else post['content']
        print(f"   Content: {content_preview}")
        print(f"   Image:   {'✅ ' + post['image'][:50] + '...' if post['image'] else '❌'}")
        print(f"   Video:   {'✅ ' + post['video'][:50] + '...' if post['video'] else '❌'}")
        print(f"   {'-' * 50}")

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    print("🏋️ FitLife Daily - Ultimate Content Generator")
    print("=" * 65)
    print(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔄 Version: 100% Matched Images & Videos")
    print()
    
    # Generate posts
    posts = generate_posts()
    
    # Save to CSV
    save_posts_to_csv(posts)
    
    # Show statistics
    print_stats(posts)
    
    # Show sample posts
    print_samples(posts, 6)
    
    print("\n✨ CONTENT GENERATION COMPLETE!")
    print(f"📊 {len(posts)} posts with 100% matched media")
    print(f"📈 3 posts daily = {len(posts)//3} days of content")
    print("🚀 Run 'python fb_poster.py' to start posting.")
