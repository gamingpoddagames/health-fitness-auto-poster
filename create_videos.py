#!/usr/bin/env python3
"""
FitLife Daily - Video Creator
Creates fitness videos with text overlays using Python
No external APIs needed - runs locally
"""

import os
import random
import csv
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Try to import moviepy - if not installed, user will be prompted
try:
    from moviepy.editor import (
        VideoClip, ImageClip, TextClip, CompositeVideoClip, 
        concatenate_videoclips, AudioFileClip, ColorClip
    )
    from moviepy.video.fx.all import fadein, fadeout
except ImportError:
    print("❌ moviepy not installed! Run: pip install moviepy")
    exit(1)

# ============================================
# VIDEO TEMPLATES & CONTENT
# ============================================

VIDEO_TEMPLATES = [
    {
        "title": "💪 Morning Stretch",
        "text": "5 Minutes to Start Your Day!\nNeck rolls • Arm circles • Torso twists",
        "duration": 10,
        "style": "motivational"
    },
    {
        "title": "🔥 HIIT Workout",
        "text": "20 sec ON • 10 sec OFF\n4 Minutes • 8 Rounds",
        "duration": 8,
        "style": "energetic"
    },
    {
        "title": "🥗 Healthy Tip",
        "text": "Add spinach to your smoothie!\nIron + Fiber • Zero taste change",
        "duration": 10,
        "style": "clean"
    },
    {
        "title": "🧘 Yoga Flow",
        "text": "Find your balance\nDownward Dog → Warrior → Child's Pose",
        "duration": 12,
        "style": "calm"
    },
    {
        "title": "💪 Motivation",
        "text": "The only bad workout\nis the one that didn't happen",
        "duration": 8,
        "style": "motivational"
    },
    {
        "title": "🏃 Cardio Burn",
        "text": "Run. Jump. Repeat.\n200 Calories in 20 Minutes!",
        "duration": 10,
        "style": "energetic"
    },
    {
        "title": "😴 Sleep Recovery",
        "text": "7-8 hours = 40% faster recovery\nYour body repairs during sleep",
        "duration": 10,
        "style": "calm"
    },
    {
        "title": "💧 Hydration",
        "text": "8 glasses water daily\nBoosts metabolism by 30%",
        "duration": 8,
        "style": "clean"
    },
    {
        "title": "🎯 Daily Goal",
        "text": "Walk 10,000 steps today\nEach step = progress!",
        "duration": 8,
        "style": "motivational"
    },
    {
        "title": "🔥 Quick Workout",
        "text": "Squats • Push-ups • Lunges\n15 reps each • 3 rounds",
        "duration": 10,
        "style": "energetic"
    },
    {
        "title": "💪 Strong Mind",
        "text": "Your body can do it\nYour mind is the one that needs convincing",
        "duration": 9,
        "style": "motivational"
    },
    {
        "title": "🥑 Healthy Snack",
        "text": "Avocado with sea salt\nHealthy fats • Fiber • Potassium",
        "duration": 8,
        "style": "clean"
    },
    {
        "title": "🏋️ Compound Exercises",
        "text": "Squats • Deadlifts • Bench Press\nBuild strength • Burn calories",
        "duration": 10,
        "style": "energetic"
    },
    {
        "title": "🧘 Stress Relief",
        "text": "5 deep breaths\nInhale 4s • Hold 4s • Exhale 4s",
        "duration": 9,
        "style": "calm"
    },
    {
        "title": "💪 Progress",
        "text": "Small daily improvements\n= Massive results over time",
        "duration": 8,
        "style": "motivational"
    },
    {
        "title": "🏃 Running Tips",
        "text": "Land mid-foot • Lean forward\nKeep cadence high • Breathe rhythmically",
        "duration": 10,
        "style": "energetic"
    },
    {
        "title": "😴 Better Sleep",
        "text": "Dim lights 1 hour before bed\nScreen off • Read instead",
        "duration": 9,
        "style": "calm"
    },
    {
        "title": "💪 Core Strength",
        "text": "Plank • Bicycle Crunches\nLeg Raises • Russian Twists",
        "duration": 10,
        "style": "energetic"
    },
    {
        "title": "🥗 Meal Prep",
        "text": "Plan • Shop • Batch Cook\nSave time • Eat healthy",
        "duration": 9,
        "style": "clean"
    },
    {
        "title": "🔥 Tabata",
        "text": "20 sec MAX effort\n10 sec rest • 8 rounds",
        "duration": 8,
        "style": "energetic"
    }
]

# Background color schemes
COLOR_SCHEMES = [
    {"bg": "#1a237e", "text": "#ffffff", "accent": "#4fc3f7"},
    {"bg": "#2c3e50", "text": "#ffffff", "accent": "#e74c3c"},
    {"bg": "#1b1b2f", "text": "#ffffff", "accent": "#f39c12"},
    {"bg": "#0a0a0a", "text": "#ffffff", "accent": "#2ecc71"},
    {"bg": "#2c3e50", "text": "#ffffff", "accent": "#3498db"},
    {"bg": "#4a1942", "text": "#ffffff", "accent": "#e91e63"},
    {"bg": "#1a237e", "text": "#ffffff", "accent": "#00bcd4"},
    {"bg": "#2d2d2d", "text": "#ffffff", "accent": "#ff6b35"},
    {"bg": "#1e2a3a", "text": "#ffffff", "accent": "#ffd93d"},
    {"bg": "#1a1a2e", "text": "#ffffff", "accent": "#6bcb77"},
]

# ============================================
# VIDEO CREATION FUNCTIONS
# ============================================

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_text_image(text, width=1080, height=1920, bg_color="#1a237e", text_color="#ffffff", accent_color="#4fc3f7"):
    """
    Create a text image using PIL for better text rendering
    """
    # Create background
    image = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(image)
    
    # Try to load fonts
    try:
        # Try different font paths (Mac)
        font_paths = [
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/Arial.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "C:/Windows/Fonts/Arial.ttf",  # Windows
        ]
        main_font = None
        sub_font = None
        
        for path in font_paths:
            if os.path.exists(path):
                if main_font is None:
                    main_font = ImageFont.truetype(path, 120)
                if sub_font is None:
                    sub_font = ImageFont.truetype(path, 60)
        
        if main_font is None:
            main_font = ImageFont.load_default()
            sub_font = ImageFont.load_default()
    except:
        main_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
    
    # Draw accent line at top
    accent_color_rgb = hex_to_rgb(accent_color)
    draw.rectangle([0, 0, width, 20], fill=accent_color_rgb)
    
    # Split text into lines
    lines = text.split('\n')
    title = lines[0] if lines else ""
    content = '\n'.join(lines[1:]) if len(lines) > 1 else ""
    
    # Draw title
    bbox = draw.textbbox((0, 0), title, font=main_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = height // 2 - 300
    draw.text((x, y), title, fill=text_color, font=main_font)
    
    # Draw content lines
    if content:
        content_lines = content.split('\n')
        y_offset = height // 2 + 50
        for line in content_lines:
            bbox = draw.textbbox((0, 0), line, font=sub_font)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            draw.text((x, y_offset), line, fill=text_color, font=sub_font)
            y_offset += 80
    
    # Draw FitLife Daily branding at bottom
    brand_font = sub_font
    brand_text = "🏋️ FitLife Daily"
    bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    draw.text((x, height - 150), brand_text, fill=accent_color_rgb, font=brand_font)
    
    # Draw bottom accent line
    draw.rectangle([0, height - 20, width, height], fill=accent_color_rgb)
    
    return image

def create_video_from_text(text, duration=10, output_file="video.mp4", fps=24):
    """
    Create a video from text with smooth animations
    """
    # Create text image
    scheme = random.choice(COLOR_SCHEMES)
    img = create_text_image(
        text,
        bg_color=scheme["bg"],
        text_color=scheme["text"],
        accent_color=scheme["accent"]
    )
    
    # Convert PIL image to numpy array
    img_np = np.array(img)
    
    # Create ImageClip
    clip = ImageClip(img_np, duration=duration)
    
    # Add fade in/out
    clip = clip.fx(fadein, 0.5).fx(fadeout, 0.5)
    
    # Write video
    clip.write_videofile(
        output_file,
        fps=fps,
        codec='libx264',
        audio_codec='aac',
        threads=4,
        verbose=False,
        logger=None
    )
    
    return output_file

def generate_fitness_video(template_index=None, output_dir="videos"):
    """
    Generate a fitness video from a template
    """
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Select template
    if template_index is None:
        template = random.choice(VIDEO_TEMPLATES)
    else:
        template = VIDEO_TEMPLATES[template_index % len(VIDEO_TEMPLATES)]
    
    # Create video file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/reel_{timestamp}_{template_index}.mp4"
    
    # Create video
    print(f"🎬 [{template_index+1}] Creating: {template['title']}")
    
    create_video_from_text(
        f"{template['title']}\n{template['text']}",
        duration=template['duration'],
        output_file=filename
    )
    
    print(f"   ✅ {filename}")
    return filename, template

def generate_multiple_videos(count=20):
    """
    Generate multiple fitness videos
    """
    print("🏋️ FitLife Daily - Video Generator")
    print("=" * 60)
    print(f"📅 Generating {count} videos...")
    print()
    
    generated_videos = []
    
    for i in range(count):
        print(f"\n📹 [{i+1}/{count}]")
        video_file, template = generate_fitness_video(i)
        generated_videos.append({
            "file": video_file,
            "title": template['title'],
            "text": template['text']
        })
    
    print("\n" + "=" * 60)
    print("✅ VIDEO GENERATION COMPLETE!")
    print(f"   Generated {len(generated_videos)} videos")
    print(f"   Location: videos/ folder")
    
    # Create a CSV with video info
    os.makedirs("videos", exist_ok=True)
    with open("videos/video_list.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['file', 'title', 'text'])
        for v in generated_videos:
            writer.writerow([v['file'], v['title'], v['text']])
    
    print("   📄 video_list.csv created")
    return generated_videos

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    import sys
    
    # Check if moviepy is installed
    try:
        from moviepy.editor import VideoClip
    except ImportError:
        print("❌ Required packages not installed!")
        print("Run: pip install moviepy pillow numpy")
        sys.exit(1)
    
    # Generate videos
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    else:
        count = 20
    
    generate_multiple_videos(count)
