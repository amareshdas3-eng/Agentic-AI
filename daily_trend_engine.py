import os
import json
import datetime
import random
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

POSTS_DIR = "d:/instagram/daily_posts"
os.makedirs(POSTS_DIR, exist_ok=True)

# Trend topic repository across Power Systems, 33kV Substations, EPC Megaprojects & Industrial AI
TREND_TOPICS = [
    {
        "hook": "Why 33kV Vacuum Circuit Breakers fail contact resistance tests after 100 operations",
        "pillar": "Field Commissioning",
        "keyword": "VCB",
        "facts": [
            "Contact resistance must stay under 35 micro-ohms per IEC 62271-100.",
            "Contact erosion and copper-chromium oxidation cause micro-arcing.",
            "Solution: Perform 100A DC digital micro-ohmmeter test and vacuum bottle integrity check."
        ]
    },
    {
        "hook": "The \$500K Cable Sizing error EPC engineers make with thermal resistivity",
        "pillar": "Forensic Teardown",
        "keyword": "CABLE",
        "facts": [
            "Standard soil thermal resistivity (1.2 K.m/W) is often assumed without soil testing.",
            "Dry backfill reaches 2.5 K.m/W, derating cable ampacity by 30%.",
            "Solution: Agentic AI thermal derating calculation and fluidised thermal backfill."
        ]
    },
    {
        "hook": "How Agentic AI audits Primavera P6 EVM and detects fake '85% Complete' progress",
        "pillar": "Project Controls & AI",
        "keyword": "EVM",
        "facts": [
            "Contractors claim physical progress without completing secondary test records.",
            "CPI looks healthy while critical path float drops to -35 days.",
            "Solution: Connect P6 API to SCADA commissioning test records to verify milestone truth."
        ]
    },
    {
        "hook": "Why transformer differential relay 87T trips during energization without an internal fault",
        "pillar": "Protection Relays",
        "keyword": "87T",
        "facts": [
            "Magnetizing inrush current contains high 2nd-harmonic components.",
            "If 2nd-harmonic restraint is set below 12%, relay mistakes inrush for internal fault.",
            "Solution: Verify dual-slope percentage bias and 15% 2nd-harmonic cross-blocking."
        ]
    }
]

def generate_daily_post():
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    topic = random.choice(TREND_TOPICS)
    
    post_folder = os.path.join(POSTS_DIR, date_str)
    os.makedirs(post_folder, exist_ok=True)
    
    # 1. Generate Spoken Script & Caption Package
    script_path = os.path.join(post_folder, "script_and_caption.json")
    package = {
        "date": date_str,
        "pillar": topic["pillar"],
        "hook_title": topic["hook"],
        "keyword_trigger": topic["keyword"],
        "spoken_script_45s": {
            "00_03s_hook": f"{topic['hook']}—and how to fix it before your client issues a delay penalty.",
            "03_20s_field_reality": f"In 23 years across 33kV substations and megaprojects, this single blindspot delays energization more than hardware defects. {topic['facts'][0]} {topic['facts'][1]}",
            "20_38s_solution": f"Instead of arguing on site during pre-commissioning, here is the exact protocol: {topic['facts'][2]}",
            "38_45s_cta": f"Comment '{topic['keyword']}' below and I'll send you my complete technical standard operating procedure and checklist."
        },
        "instagram_caption": (
            f"⚡ {topic['hook']} ⚡\n\n"
            f"Here is what happens on site when this gets overlooked:\n"
            f"1️⃣ {topic['facts'][0]}\n"
            f"2️⃣ {topic['facts'][1]}\n"
            f"3️⃣ {topic['facts'][2]}\n\n"
            f"👇 Comment '{topic['keyword']}' below and I'll DM you the technical calculation sheet and commissioning checklist! (Or grab it at proengineering.in)\n\n"
            f"#ElectricalEngineering #PowerSystems #33kVSubstation #EPC #ProjectControls #PrimaveraP6 #ProtectionRelays #IndustrialAI #ProEngineering"
        )
    }
    
    with open(script_path, "w", encoding="utf-8") as f:
        json.dump(package, f, indent=2)
    print("Generated daily script & caption:", script_path)
    
    # 2. Render Daily Reel Video
    reel_video_path = os.path.join(post_folder, f"daily_reel_{date_str}.mp4")
    render_daily_video(reel_video_path, topic, duration_sec=6, fps=30)
    print("Generated daily video:", reel_video_path)
    
    return package

def render_daily_video(out_path, topic, duration_sec=6, fps=30):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (1080, 1920))
    total_frames = int(duration_sec * fps)
    
    for frame_idx in range(total_frames):
        t_frac = frame_idx / total_frames
        img = Image.new("RGB", (1080, 1920), (13, 17, 23))
        draw = ImageDraw.Draw(img)
        
        # Header
        draw.rectangle([0, 0, 1080, 140], fill=(13, 17, 23))
        draw.line([(0, 140), (1080, 140)], fill=(0, 242, 254), width=3)
        draw.text((50, 45), "⚡ PROENGINEERING DAILY REEL", font=ImageFont.load_default(), fill=(0, 242, 254))
        
        # Hook Card
        draw.rounded_rectangle([50, 200, 1030, 480], radius=16, fill=(22, 27, 34), outline=(255, 184, 0), width=3)
        draw.text((80, 240), topic["pillar"].upper(), font=ImageFont.load_default(), fill=(255, 184, 0))
        draw.text((80, 300), topic["hook"][:60], font=ImageFont.load_default(), fill=(255, 255, 255))
        draw.text((80, 360), topic["hook"][60:], font=ImageFont.load_default(), fill=(255, 255, 255))
        
        # Facts
        y = 540
        for i, fact in enumerate(topic["facts"]):
            draw.rounded_rectangle([50, y, 1030, y+240], radius=12, fill=(18, 24, 34), outline=(0, 242, 254), width=2)
            draw.text((80, y+30), f"INSIGHT 0{i+1}", font=ImageFont.load_default(), fill=(0, 242, 254))
            draw.text((80, y+90), fact[:75], font=ImageFont.load_default(), fill=(240, 240, 240))
            draw.text((80, y+140), fact[75:], font=ImageFont.load_default(), fill=(240, 240, 240))
            y += 280
            
        # Bottom CTA
        draw.rounded_rectangle([80, 1760, 1000, 1860], radius=18, fill=(22, 27, 34), outline=(0, 255, 140), width=3)
        draw.text((150, 1800), f"COMMENT \"{topic['keyword']}\" FOR FULL PDF", font=ImageFont.load_default(), fill=(0, 255, 140))
        
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()

if __name__ == "__main__":
    generate_daily_post()

