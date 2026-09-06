#!/usr/bin/env python3
"""
FitLife Daily - AI Image Generator
Creates images from scratch using Stable Diffusion
No downloads - generates unique images locally
"""

import os
import random
import csv
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import torch
from diffusers import StableDiffusionPipeline

# ============================================
# IMAGE PROMPTS
# ============================================

IMAGE_PROMPTS = [
    {
        "title": "💪 Morning Stretch",
        "prompt": "A person doing morning stretching exercises in a bright modern gym, warm lighting, professional fitness photography, high quality, 4k, photorealistic",
        "negative": "blurry, low quality, distorted, ugly, cartoon, anime"
    },
    {
        "title": "🥗 Healthy Smoothie",
        "content": "Add spinach to your morning smoothie! 50% Vitamin K • 20% Iron",
        "prompt": "A beautiful healthy green smoothie with spinach and fresh fruits on a modern kitchen counter, bright natural lighting, professional food photography, 4k, photorealistic",
        "negative": "blurry, low quality, cartoon, artificial"
    },
    {
        "title": "💧 Stay Hydrated",
        "content": "Drink 8 glasses of water daily! Boosts metabolism by 30%",
        "prompt": "A crystal clear glass of water with ice cubes, water splashing, modern minimalist setting, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality, cartoon"
    },
    {
        "title": "😴 Better Sleep",
        "content": "7-8 hours of quality sleep! 40% faster muscle recovery",
        "prompt": "A peaceful bedroom with natural light, comfortable bed, calm atmosphere, wellness concept, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality, dark, scary"
    },
    {
        "title": "🏃 Cardio Benefits",
        "content": "30 minutes of cardio, 5x weekly! Reduces heart disease risk by 30%",
        "prompt": "A person jogging on a beautiful nature trail, sunset lighting, professional fitness photography, 4k, photorealistic",
        "negative": "blurry, low quality, cartoon"
    },
    {
        "title": "🧘 Stress Relief",
        "content": "5 deep breaths using the 4-4-4 method! Inhale 4s • Hold 4s • Exhale 4s",
        "prompt": "A person meditating peacefully in a zen garden, soft natural lighting, calm atmosphere, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality, chaotic"
    },
    {
        "title": "🎯 SMART Goals",
        "content": "Specific • Measurable • Achievable • Relevant • Time-bound",
        "prompt": "A person writing goals in a modern notebook, professional workspace, motivational lighting, 4k, photorealistic",
        "negative": "blurry, low quality"
    },
    {
        "title": "📱 Quick Workout",
        "content": "7 minutes of high-intensity exercise! No excuses!",
        "prompt": "A person doing a quick workout at home, modern living space, energetic atmosphere, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality, cartoon"
    },
    {
        "title": "🥑 Healthy Snack",
        "content": "Avocado with sea salt and chili flakes! 5 minutes • Healthy fats",
        "prompt": "A beautifully sliced avocado on a wooden board, modern kitchen, professional food photography, 4k, photorealistic",
        "negative": "blurry, low quality, artificial"
    },
    {
        "title": "🔥 HIIT Workout",
        "content": "20 sec work • 10 sec rest x 8 rounds • Burns fat for 24 hours",
        "prompt": "A person doing intense HIIT workout in a modern gym, dynamic action shot, professional fitness photography, 4k, photorealistic",
        "negative": "blurry, low quality, still, boring"
    },
    {
        "title": "🚶 Daily Steps",
        "content": "Walk 10,000 steps today! Burns 400-500 calories",
        "prompt": "A person walking in a beautiful park, morning sunlight, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality, cartoon"
    },
    {
        "title": "🍽️ Post-Workout Nutrition",
        "content": "Eat protein within 30 minutes! 20-30g protein",
        "prompt": "A nutritious post-workout meal with grilled chicken, vegetables, and protein shake, professional food photography, 4k, photorealistic",
        "negative": "blurry, low quality, artificial"
    },
    {
        "title": "📊 Track Progress",
        "content": "Measurements • Photos • Workout logs • Celebrate wins!",
        "prompt": "A person tracking fitness progress on a modern tablet, organized workspace, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality"
    },
    {
        "title": "🎵 Workout Music",
        "content": "120-140 BPM playlist! Increases performance by 15%",
        "prompt": "A person listening to music while working out, modern gym, energetic atmosphere, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality, boring"
    },
    {
        "title": "👟 Replace Shoes",
        "content": "Every 300-500 miles! Prevents injury • Better support",
        "prompt": "A pair of modern running shoes on a track field, professional sports photography, 4k, photorealistic",
        "negative": "blurry, low quality"
    },
    {
        "title": "🧖 Recovery",
        "content": "Stretch 5-10 minutes post-workout! Reduces soreness by 30%",
        "prompt": "A person stretching after workout in a modern gym, calm atmosphere, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality"
    },
    {
        "title": "🌙 Evening Routine",
        "content": "Dim lights 1 hour before bed! Screen off • Read instead",
        "prompt": "A cozy bedroom with dim warm lighting, book on nightstand, peaceful atmosphere, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality, bright"
    },
    {
        "title": "💪 Progressive Overload",
        "content": "Increase weight or reps by 5% weekly! Key to getting stronger",
        "prompt": "A person lifting weights in a modern gym, showing strength, professional fitness photography, 4k, photorealistic",
        "negative": "blurry, low quality"
    },
    {
        "title": "🥦 Eat the Rainbow",
        "content": "5 different colors daily! Red • Orange • Green • Purple • Yellow",
        "prompt": "A colorful array of fresh vegetables arranged beautifully, professional food photography, 4k, photorealistic",
        "negative": "blurry, low quality, artificial"
    },
    {
        "title": "🏋️ Compound Exercises",
        "content": "Squats • Deadlifts • Bench Press • More muscle",
        "prompt": "A person doing compound exercises in a modern gym, professional fitness photography, 4k, photorealistic",
        "negative": "blurry, low quality"
    },
    {
        "title": "❤️ Heart Health",
        "content": "150 minutes of moderate cardio weekly! Walking • Jogging • Swimming",
        "prompt": "A person swimming in a beautiful pool, professional sports photography, 4k, photorealistic",
        "negative": "blurry, low quality"
    },
    {
        "title": "🧠 Brain Health",
        "content": "Exercise improves memory! 30% less cognitive decline",
        "prompt": "A person exercising outdoors with nature, brain health concept, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality"
    },
    {
        "title": "⏰ Day One",
        "content": "'One day, or Day One. You decide.' Start today!",
        "prompt": "A sunrise over a mountain, motivational scene, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality, dark"
    },
    {
        "title": "💪 Success",
        "content": "Success isn't given, it's earned. Keep going!",
        "prompt": "A person reaching the top of a mountain, victory pose, sunset lighting, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality"
    },
    {
        "title": "🏅 Stay Proud",
        "content": "Make yourself proud. This journey is about you!",
        "prompt": "A person feeling proud after workout, modern gym, motivational atmosphere, professional photography, 4k, photorealistic",
        "negative": "blurry, low quality"
    }
]

# ============================================
# FALLBACK - If Stable Diffusion is not available
# ============================================

def create_text_only_image(title, content, output_dir="images"):
    """Fallback: Create text-only image if Stable Diffusion fails"""
    width = 1080
    height = 1080
    
    # Create gradient background
    image = Image.new('RGB', (width, height), color="#1a237e")
    draw = ImageDraw.Draw(image)
    
    # Draw gradient
    for i in range(height):
        ratio = i / height
        r = int(26 * (1 - ratio) + 13 * ratio)
        g = int(35 * (1 - ratio) + 30 * ratio)
        b = int(126 * (1 - ratio) + 80 * ratio)
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    try:
        font_paths = [
            "/System/Library/Fonts/Helvetica.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "C:/Windows/Fonts/Arial.ttf",
        ]
        main_font = None
        sub_font = None
        
        for path in font_paths:
            if os.path.exists(path):
                if main_font is None:
                    main_font = ImageFont.truetype(path, 80)
                if sub_font is None:
                    sub_font = ImageFont.truetype(path, 45)
        
        if main_font is None:
            main_font = ImageFont.load_default()
            sub_font = ImageFont.load_default()
    except:
        main_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
    
    # Accent bars
    draw.rectangle([0, 0, width, 15], fill="#4fc3f7")
    draw.rectangle([0, height - 15, width, height], fill="#4fc3f7")
    
    # Title
    bbox = draw.textbbox((0, 0), title, font=main_font)
    x = (width - (bbox[2] - bbox[0])) // 2
    y = 300
    draw.text((x, y), title, fill="#ffffff", font=main_font)
    
    # Content
    if content:
        lines = content.split('\n')
        y_offset = 500
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=sub_font)
            x = (width - (bbox[2] - bbox[0])) // 2
            draw.text((x, y_offset), line, fill="#4fc3f7", font=sub_font)
            y_offset += 70
    
    # Branding
    try:
        brand_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 35)
    except:
        brand_font = ImageFont.load_default()
    brand_text = "🏋️ FitLife Daily"
    bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    x = (width - (bbox[2] - bbox[0])) // 2
    draw.text((x, height - 80), brand_text, fill="#4fc3f7", font=brand_font)
    
    return image

# ============================================
# MAIN IMAGE GENERATOR
# ============================================

def generate_ai_image(prompt_data, output_dir="images"):
    """
    Generate image using Stable Diffusion or fallback
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/image_{timestamp}.png"
    
    # Check if Stable Diffusion is available
    try:
        print("🔄 Generating image with AI...")
        
        # Load the pipeline
        device = "cuda" if torch.cuda.is_available() else "cpu"
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )
        pipe = pipe.to(device)
        
        # Generate image
        prompt = prompt_data['prompt']
        negative = prompt_data.get('negative', 'blurry, low quality')
        
        image = pipe(
            prompt=prompt,
            negative_prompt=negative,
            num_inference_steps=30,
            guidance_scale=7.5,
            width=1080,
            height=1080
        ).images[0]
        
        print(f"✅ AI generated image created!")
        
    except Exception as e:
        print(f"⚠️ AI generation failed: {e}")
        print("📝 Creating text-only fallback image...")
        image = create_text_only_image(
            prompt_data['title'],
            prompt_data.get('content', ''),
            output_dir
        )
    
    # Save image
    image.save(filename, "PNG")
    print(f"✅ Saved: {filename}")
    
    return filename

def create_all_images(count=25):
    """
    Generate multiple images
    """
    print("🎨 Creating AI Images for FitLife Daily")
    print("=" * 55)
    print("This may take a few minutes if using AI...")
    print()
    
    os.makedirs("images", exist_ok=True)
    
    # Create placeholder file
    with open("images/.gitkeep", "w") as f:
        f.write("Generated images folder")
    
    images = []
    for i in range(count):
        print(f"\n📷 Image {i+1}/{count}")
        
        # Select prompt
        prompt_data = IMAGE_PROMPTS[i % len(IMAGE_PROMPTS)]
        print(f"   Title: {prompt_data['title']}")
        
        # Generate image
        filename = generate_ai_image(prompt_data)
        
        images.append({
            "file": filename,
            "title": prompt_data['title'],
            "content": prompt_data.get('content', ''),
            "prompt": prompt_data['prompt']
        })
    
    # Save list
    with open("images/image_list.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['file', 'title', 'content', 'prompt'])
        for img in images:
            writer.writerow([img['file'], img['title'], img['content'], img['prompt']])
    
    print(f"\n✅ Created {len(images)} images in images/ folder")
    return images

# ============================================
# QUICK START - WITH OR WITHOUT AI
# ============================================

if __name__ == "__main__":
    # Check if torch and diffusers are installed
    try:
        import torch
        from diffusers import StableDiffusionPipeline
        has_ai = True
    except ImportError:
        has_ai = False
    
    if has_ai:
        print("🚀 AI Mode: Using Stable Diffusion")
        print("   (First run will download the model ~5GB)")
    else:
        print("📝 Text-Only Mode: Creating text-based images")
        print("   To enable AI, install: pip install torch diffusers")
    
    print()
    create_all_images(25)
