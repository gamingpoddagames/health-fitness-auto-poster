#!/usr/bin/env python3
"""
FitLife Daily - Image Generator
Creates PNG images in the images/ folder
"""

import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# ============================================
# IMAGE DATA
# ============================================

IMAGE_DATA = [
    {"title": "💪 Morning Stretch", "text": "5 Minutes to Start Your Day!\nNeck rolls • Arm circles • Torso twists", "bg": "#1a237e", "accent": "#4fc3f7"},
    {"title": "🔥 HIIT Workout", "text": "20 sec ON • 10 sec OFF\n4 Minutes • 8 Rounds", "bg": "#2c3e50", "accent": "#e74c3c"},
    {"title": "🥗 Healthy Tip", "text": "Add spinach to your smoothie!\nIron + Fiber • Zero taste change", "bg": "#1b1b2f", "accent": "#f39c12"},
    {"title": "🧘 Yoga Flow", "text": "Find your balance\nDownward Dog → Warrior → Child's Pose", "bg": "#0a0a0a", "accent": "#2ecc71"},
    {"title": "💪 Motivation", "text": "The only bad workout\nis the one that didn't happen", "bg": "#2c3e50", "accent": "#3498db"},
    {"title": "🏃 Cardio Burn", "text": "Run. Jump. Repeat.\n200 Calories in 20 Minutes!", "bg": "#4a1942", "accent": "#e91e63"},
    {"title": "💧 Hydration", "text": "8 glasses water daily\nBoosts metabolism by 30%", "bg": "#1a237e", "accent": "#00bcd4"},
    {"title": "🎯 Daily Goal", "text": "Walk 10,000 steps today\nEach step = progress!", "bg": "#2d2d2d", "accent": "#ff6b35"},
    {"title": "🔥 Quick Workout", "text": "Squats • Push-ups • Lunges\n15 reps each • 3 rounds", "bg": "#1e2a3a", "accent": "#ffd93d"},
    {"title": "💪 Strong Mind", "text": "Your body can do it\nYour mind is the one that needs convincing", "bg": "#1a1a2e", "accent": "#6bcb77"},
    {"title": "🥑 Healthy Snack", "text": "Avocado with sea salt\nHealthy fats • Fiber • Potassium", "bg": "#2d1b2e", "accent": "#ff6b6b"},
    {"title": "🏋️ Compound Exercises", "text": "Squats • Deadlifts • Bench Press\nBuild strength • Burn calories", "bg": "#1a2a3a", "accent": "#4fc3f7"},
    {"title": "🧘 Stress Relief", "text": "5 deep breaths\nInhale 4s • Hold 4s • Exhale 4s", "bg": "#2a1a3a", "accent": "#ab47bc"},
    {"title": "💪 Progress", "text": "Small daily improvements\n= Massive results over time", "bg": "#1a3a2a", "accent": "#66bb6a"},
    {"title": "😴 Better Sleep", "text": "Dim lights 1 hour before bed\nScreen off • Read instead", "bg": "#0a1a2a", "accent": "#42a5f5"},
    {"title": "💪 Core Strength", "text": "Plank • Bicycle Crunches\nLeg Raises • Russian Twists", "bg": "#3a1a1a", "accent": "#ef5350"},
    {"title": "🥗 Meal Prep", "text": "Plan • Shop • Batch Cook\nSave time • Eat healthy", "bg": "#1a3a1a", "accent": "#66bb6a"},
    {"title": "🔥 Tabata", "text": "20 sec MAX effort\n10 sec rest • 8 rounds", "bg": "#3a2a1a", "accent": "#ffa726"},
    {"title": "💪 Mindset", "text": "Your only competition\nis the person in the mirror", "bg": "#1a1a3a", "accent": "#7986cb"},
    {"title": "🥗 Eat Clean", "text": "Eat the rainbow!\n5 colors daily for optimal nutrition", "bg": "#2a3a1a", "accent": "#81c784"},
    {"title": "🏃 Run Tips", "text": "Land mid-foot • Lean forward\nKeep cadence high • Breathe rhythmically", "bg": "#1a2a2a", "accent": "#4dd0e1"},
    {"title": "💪 Upper Body", "text": "Push-ups • Pull-ups\nOverhead Press • Bicep Curls", "bg": "#3a1a2a", "accent": "#ec407a"},
    {"title": "🦵 Lower Body", "text": "Squats • Lunges • Deadlifts\nCalf Raises • Glute Bridges", "bg": "#1a3a2a", "accent": "#66bb6a"},
    {"title": "🧘 Meditation", "text": "Find a quiet space\nSit comfortably • Focus on breath", "bg": "#1a1a2a", "accent": "#7986cb"},
    {"title": "🔥 Stay Motivated", "text": "Motivation gets you started\nHabit keeps you going", "bg": "#2a1a1a", "accent": "#ef5350"},
]

def create_image(template_index, output_dir="images"):
    """Create a single image"""
    os.makedirs(output_dir, exist_ok=True)
    
    width = 1080
    height = 1080
    
    data = IMAGE_DATA[template_index % len(IMAGE_DATA)]
    
    # Create background
    img = Image.new('RGB', (width, height), color=data['bg'])
    draw = ImageDraw.Draw(img)
    
    # Gradient effect
    for i in range(height):
        ratio = i / height
        r = int(int(data['bg'][1:3], 16) * (1 - ratio * 0.3))
        g = int(int(data['bg'][3:5], 16) * (1 - ratio * 0.3))
        b = int(int(data['bg'][5:7], 16) * (1 - ratio * 0.3))
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    # Try to load fonts
    try:
        font_paths = [
            "/System/Library/Fonts/Helvetica.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "C:/Windows/Fonts/Arial.ttf",
            "C:/Windows/Fonts/Calibri.ttf",
        ]
        main_font = None
        sub_font = None
        
        for path in font_paths:
            if os.path.exists(path):
                if main_font is None:
                    main_font = ImageFont.truetype(path, 90)
                if sub_font is None:
                    sub_font = ImageFont.truetype(path, 50)
        
        if main_font is None:
            main_font = ImageFont.load_default()
            sub_font = ImageFont.load_default()
    except:
        main_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
    
    # Accent bars
    accent = data['accent']
    draw.rectangle([0, 0, width, 20], fill=accent)
    draw.rectangle([0, height - 20, width, height], fill=accent)
    
    # Title
    title = data['title']
    bbox = draw.textbbox((0, 0), title, font=main_font)
    x = (width - (bbox[2] - bbox[0])) // 2
    y = 300
    draw.text((x, y), title, fill="#ffffff", font=main_font)
    
    # Text
    text = data['text']
    lines = text.split('\n')
    y_offset = 500
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=sub_font)
        x = (width - (bbox[2] - bbox[0])) // 2
        draw.text((x, y_offset), line, fill="#ffffff", font=sub_font)
        y_offset += 70
    
    # Branding
    try:
        brand_font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 35)
    except:
        brand_font = ImageFont.load_default()
    brand_text = "🏋️ FitLife Daily"
    bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    x = (width - (bbox[2] - bbox[0])) // 2
    draw.text((x, height - 80), brand_text, fill=accent, font=brand_font)
    
    # Save
    filename = f"{output_dir}/image_{template_index:03d}.png"
    img.save(filename, "PNG")
    print(f"✅ Created: {filename}")
    return filename

def create_all_images(count=25):
    """Create all images"""
    print("🎨 Creating Images for FitLife Daily")
    print("=" * 55)
    print()
    
    os.makedirs("images", exist_ok=True)
    
    # Create .gitkeep
    with open("images/.gitkeep", "w") as f:
        f.write("Generated images folder")
    
    for i in range(count):
        print(f"📷 Image {i+1}/{count}")
        create_image(i)
    
    # Create CSV list
    with open("images/image_list.csv", "w") as f:
        f.write("file,title,text\n")
        for i, data in enumerate(IMAGE_DATA[:count]):
            f.write(f"images/image_{i:03d}.png,{data['title']},{data['text']}\n")
    
    print(f"\n✅ Created {count} images in images/ folder")
    return True

if __name__ == "__main__":
    create_all_images(25)
