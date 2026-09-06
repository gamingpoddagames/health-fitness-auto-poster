#!/usr/bin/env python3
"""
FitLife Daily - Image Generator
Creates professional fitness images with text overlays
No external APIs - runs locally with PIL
"""

import os
import random
import csv
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import numpy as np

# ============================================
# IMAGE TEMPLATES
# ============================================

IMAGE_TEMPLATES = [
    {
        "title": "💪 Morning Stretch",
        "text": "Start your day with 5 minutes of dynamic stretching!\nIncreases blood flow by 30% • Reduces injury risk",
        "category": "workout"
    },
    {
        "title": "🥗 Healthy Eating",
        "text": "Add spinach to your morning smoothie!\n50% Vitamin K • 20% Iron • Zero taste change",
        "category": "nutrition"
    },
    {
        "title": "💧 Hydration",
        "text": "Drink 8 glasses of water daily!\nBoosts metabolism by 30% • Better skin • More energy",
        "category": "wellness"
    },
    {
        "title": "😴 Sleep Recovery",
        "text": "7-8 hours of quality sleep!\n40% faster muscle recovery • Balanced hormones",
        "category": "wellness"
    },
    {
        "title": "🏃 Cardio Benefits",
        "text": "30 minutes of cardio, 5x weekly!\nReduces heart disease risk by 30% • Stronger heart",
        "category": "workout"
    },
    {
        "title": "🧘 Stress Relief",
        "text": "5 deep breaths using the 4-4-4 method!\nInhale 4s • Hold 4s • Exhale 4s",
        "category": "wellness"
    },
    {
        "title": "🎯 SMART Goals",
        "text": "Set SMART fitness goals:\nSpecific • Measurable • Achievable • Relevant • Time-bound",
        "category": "motivation"
    },
    {
        "title": "📱 Quick Workout",
        "text": "7 minutes of high-intensity exercise!\n= 30 minutes of moderate activity • No excuses!",
        "category": "workout"
    },
    {
        "title": "🥑 Healthy Snack",
        "text": "Avocado with sea salt and chili flakes!\nHealthy fats • Fiber • Potassium • 5 minutes",
        "category": "nutrition"
    },
    {
        "title": "🔥 HIIT Workout",
        "text": "20 sec work • 10 sec rest x 8 rounds\nBurns fat for 24 hours post-workout!",
        "category": "workout"
    },
    {
        "title": "🚶 Daily Steps",
        "text": "Walk 10,000 steps today!\nBurns 400-500 calories • Improves mood",
        "category": "wellness"
    },
    {
        "title": "🍽️ Post-Workout Nutrition",
        "text": "Eat protein within 30 minutes!\n20-30g protein • Eggs • Chicken • Fish • Shake",
        "category": "nutrition"
    },
    {
        "title": "📊 Track Progress",
        "text": "Track your fitness journey!\nMeasurements • Photos • Workout logs • Celebrate wins!",
        "category": "motivation"
    },
    {
        "title": "🎵 Workout Music",
        "text": "Create a playlist with 120-140 BPM!\nIncreases performance by 15% • More motivation",
        "category": "workout"
    },
    {
        "title": "👟 Replace Shoes",
        "text": "Replace running shoes every 300-500 miles!\nPrevents injury • Better support • Less joint pain",
        "category": "wellness"
    },
    {
        "title": "🧖 Recovery",
        "text": "Spend 5-10 minutes stretching post-workout!\nReduces soreness by 30% • Increases flexibility",
        "category": "wellness"
    },
    {
        "title": "🌙 Better Sleep",
        "text": "Dim lights 1 hour before bed!\nAvoid screens • Read instead • Better sleep = better results",
        "category": "wellness"
    },
    {
        "title": "💪 Progressive Overload",
        "text": "Increase weights or reps by 5% weekly!\nKey to getting stronger • Track your progress",
        "category": "workout"
    },
    {
        "title": "🥦 Eat the Rainbow",
        "text": "Aim for 5 different colors daily!\nRed • Orange • Green • Purple • Yellow",
        "category": "nutrition"
    },
    {
        "title": "🏋️ Compound Exercises",
        "text": "Focus on compound exercises!\nSquats • Deadlifts • Bench Press • More muscle",
        "category": "workout"
    },
    {
        "title": "❤️ Heart Health",
        "text": "150 minutes of moderate cardio weekly!\nWalking • Jogging • Swimming • Cycling",
        "category": "workout"
    },
    {
        "title": "🧠 Brain Health",
        "text": "Exercise improves brain function!\nBetter memory • 30% less cognitive decline",
        "category": "wellness"
    },
    {
        "title": "⏰ Day One",
        "text": "'One day, or Day One. You decide.'\nStart today • No more waiting",
        "category": "motivation"
    },
    {
        "title": "💪 Success",
        "text": "Success isn't given, it's earned.\nThousands of hours of work • Keep going!",
        "category": "motivation"
    },
    {
        "title": "🏅 Stay Proud",
        "text": "Make yourself proud.\nThis journey is about you • Never give up",
        "category": "motivation"
    }
]

# ============================================
# COLOR SCHEMES
# ============================================

COLOR_SCHEMES = [
    {"bg": "#1a237e", "text": "#ffffff", "accent": "#4fc3f7", "gradient": ["#0d47a1", "#1a237e"]},
    {"bg": "#2c3e50", "text": "#ffffff", "accent": "#e74c3c", "gradient": ["#1a252f", "#2c3e50"]},
    {"bg": "#1b1b2f", "text": "#ffffff", "accent": "#f39c12", "gradient": ["#0f0f1f", "#1b1b2f"]},
    {"bg": "#0a0a0a", "text": "#ffffff", "accent": "#2ecc71", "gradient": ["#000000", "#0a0a0a"]},
    {"bg": "#2c3e50", "text": "#ffffff", "accent": "#3498db", "gradient": ["#1a252f", "#2c3e50"]},
    {"bg": "#4a1942", "text": "#ffffff", "accent": "#e91e63", "gradient": ["#2d0d28", "#4a1942"]},
    {"bg": "#1a237e", "text": "#ffffff", "accent": "#00bcd4", "gradient": ["#0d47a1", "#1a237e"]},
    {"bg": "#2d2d2d", "text": "#ffffff", "accent": "#ff6b35", "gradient": ["#1a1a1a", "#2d2d2d"]},
    {"bg": "#1e2a3a", "text": "#ffffff", "accent": "#ffd93d", "gradient": ["#0f172a", "#1e2a3a"]},
    {"bg": "#1a1a2e", "text": "#ffffff", "accent": "#6bcb77", "gradient": ["#0d0d1a", "#1a1a2e"]},
]

# ============================================
# GRADIENT BACKGROUNDS
# ============================================

def create_gradient_background(width, height, color1, color2):
    """Create a gradient background"""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    # Create gradient
    for i in range(height):
        ratio = i / height
        r = int(int(color1[1:3], 16) * (1 - ratio) + int(color2[1:3], 16) * ratio)
        g = int(int(color1[3:5], 16) * (1 - ratio) + int(color2[3:5], 16) * ratio)
        b = int(int(color1[5:7], 16) * (1 - ratio) + int(color2[5:7], 16) * ratio)
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    return image

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def add_rounded_rectangle(draw, xy, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle"""
    x1, y1, x2, y2 = xy
    if fill:
        draw.rectangle([x1+radius, y1, x2-radius, y2], fill=fill)
        draw.rectangle([x1, y1+radius, x2, y2-radius], fill=fill)
        draw.pieslice([x1, y1, x1+radius*2, y1+radius*2], 180, 270, fill=fill)
        draw.pieslice([x2-radius*2, y1, x2, y1+radius*2], 270, 360, fill=fill)
        draw.pieslice([x1, y2-radius*2, x1+radius*2, y2], 90, 180, fill=fill)
        draw.pieslice([x2-radius*2, y2-radius*2, x2, y2], 0, 90, fill=fill)
    
    if outline:
        draw.arc([x1, y1, x1+radius*2, y1+radius*2], 180, 270, fill=outline, width=width)
        draw.arc([x2-radius*2, y1, x2, y1+radius*2], 270, 360, fill=outline, width=width)
        draw.arc([x1, y2-radius*2, x1+radius*2, y2], 90, 180, fill=outline, width=width)
        draw.arc([x2-radius*2, y2-radius*2, x2, y2], 0, 90, fill=outline, width=width)
        draw.line([x1+radius, y1, x2-radius, y1], fill=outline, width=width)
        draw.line([x1+radius, y2, x2-radius, y2], fill=outline, width=width)
        draw.line([x1, y1+radius, x1, y2-radius], fill=outline, width=width)
        draw.line([x2, y1+radius, x2, y2-radius], fill=outline, width=width)

def create_fitness_image(template_index=None, output_dir="images"):
    """
    Create a professional fitness image with text overlays
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Image size (Facebook post optimized)
    width = 1080
    height = 1080
    
    # Select template
    if template_index is None:
        template = random.choice(IMAGE_TEMPLATES)
    else:
        template = IMAGE_TEMPLATES[template_index % len(IMAGE_TEMPLATES)]
    
    # Select color scheme
    colors = random.choice(COLOR_SCHEMES)
    
    # Create gradient background
    bg = create_gradient_background(width, height, colors["bg"], colors["gradient"][1])
    
    # Create drawing context
    draw = ImageDraw.Draw(bg)
    
    # Try to load fonts
    try:
        font_paths = [
            "/System/Library/Fonts/Helvetica.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "C:/Windows/Fonts/Arial.ttf",
            "C:/Windows/Fonts/Calibri.ttf",
        ]
        main_font = None
        sub_font = None
        brand_font = None
        
        for path in font_paths:
            if os.path.exists(path):
                if main_font is None:
                    main_font = ImageFont.truetype(path, 90)
                if sub_font is None:
                    sub_font = ImageFont.truetype(path, 45)
                if brand_font is None:
                    brand_font = ImageFont.truetype(path, 35)
        
        if main_font is None:
            main_font = ImageFont.load_default()
            sub_font = ImageFont.load_default()
            brand_font = ImageFont.load_default()
    except:
        main_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
        brand_font = ImageFont.load_default()
    
    accent_rgb = hex_to_rgb(colors["accent"])
    
    # Draw decorative elements
    # Top accent bar
    draw.rectangle([0, 0, width, 20], fill=accent_rgb)
    
    # Bottom accent bar
    draw.rectangle([0, height - 20, width, height], fill=accent_rgb)
    
    # Add decorative circles
    draw.ellipse([width - 150, 50, width - 50, 150], outline=accent_rgb, width=3)
    draw.ellipse([50, height - 150, 150, height - 50], outline=accent_rgb, width=3)
    
    # Add semi-transparent overlay box for text
    overlay = Image.new('RGBA', (width - 100, height - 200), (0, 0, 0, 100))
    bg.paste(overlay, (50, 100), overlay)
    
    # Draw title
    title = template['title']
    bbox = draw.textbbox((0, 0), title, font=main_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = 200
    draw.text((x, y), title, fill=colors["text"], font=main_font)
    
    # Draw content text (with line wrapping)
    content = template['text']
    lines = content.split('\n')
    y_offset = 350
    
    for line in lines:
        # If line is too long, wrap it
        if len(line) > 50:
            words = line.split()
            current_line = ""
            for word in words:
                test_line = current_line + " " + word if current_line else word
                bbox = draw.textbbox((0, 0), test_line, font=sub_font)
                if bbox[2] - bbox[0] > width - 200:
                    draw.text(((width - (bbox[2] - bbox[0])) // 2, y_offset), current_line, fill=colors["text"], font=sub_font)
                    y_offset += 60
                    current_line = word
                else:
                    current_line = test_line
            if current_line:
                bbox = draw.textbbox((0, 0), current_line, font=sub_font)
                draw.text(((width - (bbox[2] - bbox[0])) // 2, y_offset), current_line, fill=colors["text"], font=sub_font)
                y_offset += 60
        else:
            bbox = draw.textbbox((0, 0), line, font=sub_font)
            draw.text(((width - (bbox[2] - bbox[0])) // 2, y_offset), line, fill=colors["text"], font=sub_font)
            y_offset += 60
    
    # Draw FitLife Daily branding
    brand_text = "🏋️ FitLife Daily"
    bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    x = (width - (bbox[2] - bbox[0])) // 2
    draw.text((x, height - 80), brand_text, fill=accent_rgb, font=brand_font)
    
    # Add small decorative elements
    for i in range(5):
        x_pos = 100 + i * 220
        draw.ellipse([x_pos, height - 50, x_pos + 10, height - 40], fill=accent_rgb)
    
    # Apply subtle filter for polish
    # (optional - uncomment for effects)
    # bg = bg.filter(ImageFilter.SMOOTH_MORE)
    
    # Save image
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/image_{timestamp}_{template_index:03d}.png"
    
    bg.save(filename, "PNG", quality=95)
    print(f"✅ Created: {filename}")
    
    return filename, template

def create_all_images(count=25):
    """
    Generate multiple fitness images
    """
    print("🎨 Creating Images for FitLife Daily")
    print("=" * 55)
    
    images = []
    for i in range(count):
        print(f"\n📷 Image {i+1}/{count}")
        filename, template = create_fitness_image(i)
        images.append({
            "file": filename,
            "title": template['title'],
            "text": template['text'],
            "category": template['category']
        })
    
    # Save list
    os.makedirs("images", exist_ok=True)
    with open("images/image_list.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['file', 'title', 'text', 'category'])
        for img in images:
            writer.writerow([img['file'], img['title'], img['text'], img['category']])
    
    print(f"\n✅ Created {len(images)} images in images/ folder")
    return images

if __name__ == "__main__":
    create_all_images(25)
