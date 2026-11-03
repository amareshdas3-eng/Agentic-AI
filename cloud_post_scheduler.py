import os
import sys
import json
import argparse
import datetime
import random
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Local imports
from instagram_publisher import InstagramPublisher

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, "daily_posts")
HISTORY_FILE = os.path.join(BASE_DIR, "published_history.json")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

# Rich technical topic bank for ProEngineering 2-3x daily publishing
TOPICS_DATABASE = {
    "morning": [
        {
            "id": "spec_40ka_withstand",
            "title": "The 40kA Fault Level Trap in Division 26",
            "format": "REEL",
            "hook": "How 1 clause in Division 26 triggers a $400,000 switchgear change order",
            "keyword": "SPEC",
            "facts": [
                "BOQs frequently specify standard 31.5 kA (1s), but Section 26 13 00 mandates 40 kA (3s).",
                "Switchgear dynamic withstand forces scale with the square of peak current (I_peak^2).",
                "Solution: Run automated Spec-vs-Drawing audit before submitting EPC bids."
            ]
        },
        {
            "id": "cable_ampacity_derating",
            "title": "The $500K Cable Trench Thermal Trap",
            "format": "REEL",
            "hook": "Why 33kV XLPE cables overheat after site backfilling",
            "keyword": "CABLE",
            "facts": [
                "Contractors assume 1.2 K.m/W soil resistivity without site thermal testing.",
                "Dry summer backfill reaches 2.5 K.m/W, cutting ampacity by 30%.",
                "Solution: Implement fluidised thermal backfill and run Agentic AI ampacity modeling."
            ]
        },
        {
            "id": "order_of_precedence_trap",
            "title": "Order-of-Precedence Contract Blindspots",
            "format": "REEL",
            "hook": "When the BOQ conflicts with the CSI specification, who pays?",
            "keyword": "AUDIT",
            "facts": [
                "Tender General Conditions usually state Specs take precedence over BOQ drawings.",
                "Subcontractors price based on BOQ line items and get hit with unbudgeted spec clauses.",
                "Solution: File pre-bid Clarification Requests (RFIs) within the first 14 days of tender."
            ]
        }
    ],
    "afternoon": [
        {
            "id": "ct_kneepoint_formula",
            "title": "Class PS CT Knee-Point (Vk) Calculation",
            "format": "CAROUSEL",
            "hook": "CT Knee-Point Voltage: What Every Commissioning Lead Must Calculate",
            "keyword": "KNEE",
            "slides": [
                ("1. The High-Voltage Equation", "Vk >= 2 * If_sec * (Rct + 2*RL + Rr)."),
                ("2. The Fault Factor", "If_sec is primary fault current divided by the CT transformation ratio."),
                ("3. Cable Lead Resistance RL", "Always measure loop resistance of the switchyard multicore cable."),
                ("4. CT Secondary Resistance Rct", "Obtained from factory test certificates or measured at ambient."),
                ("5. Numerical Relay Burden Rr", "Modern numerical relays introduce <0.1 ohm, but CT loop dominates.")
            ]
        },
        {
            "id": "ansi_relay_matrix",
            "title": "Transformer Protection Matrix (87T, 50/51, 64R)",
            "format": "CAROUSEL",
            "hook": "33/11kV Transformer Protection on One Page",
            "keyword": "MATRIX",
            "slides": [
                ("ANSI 87T: Differential", "Dual-slope percentage bias clears internal faults in <30ms."),
                ("ANSI 50/51: Overcurrent/Earth", "Definite time & IDMT coordination with upstream busbar."),
                ("ANSI 64R: REF Protection", "High-impedance restricted earth fault covering star winding."),
                ("ANSI 49: Thermal Replica", "Models winding hot-spot temperature under cyclic peak load."),
                ("ANSI 51V: Voltage Restraint", "Prevents tripping on system voltage dips during motor starts.")
            ]
        },
        {
            "id": "vcb_timing_limits",
            "title": "Vacuum Circuit Breaker (VCB) Timing Limits",
            "format": "CAROUSEL",
            "hook": "5 Mechanical VCB Acceptance Tests Before Energization",
            "keyword": "VCB",
            "slides": [
                ("1. Closing Time", "Must not exceed 60ms per IEC 62271-100 standards."),
                ("2. Opening Time", "Must stay under 45ms for fast fault interruption."),
                ("3. Contact Bounce", "Bounce duration must be less than 3ms to avoid contact welding."),
                ("4. Pole Discrepancy", "Inter-pole delta between R, Y, and B phases must be <5ms."),
                ("5. Contact Resistance", "Measured with 100A DC micro-ohmmeter; must be <35 micro-ohms.")
            ]
        }
    ],
    "evening": [
        {
            "id": "day1_breaker_trip",
            "title": "Why Breakers Trip on Day-1 Soak After Passing FAT",
            "format": "REEL",
            "hook": "⚠ 33kV Energization Alert: 87T Differential Trip on No-Load Soak!",
            "keyword": "RELAY",
            "facts": [
                "Site Manager: 'FAT passed with zero faults! Why did 87T trip in 40ms?'",
                "Senior AI Architect: 'Check Dyn11 vector compensation and 15% 2nd-harmonic inrush restraint.'",
                "Solution: Cross-block 2nd-harmonic magnetization inrush during breaker closure."
            ]
        },
        {
            "id": "p6_float_trap_audit",
            "title": "How AI Detects Hidden Float Traps in Primavera P6",
            "format": "REEL",
            "hook": "Why 80% of EPC schedules hide 6-week delays behind artificial lags",
            "keyword": "P6",
            "facts": [
                "Subcontractors insert artificial SS+15d lags to mask path delays.",
                "Critical path shifts without management visibility until FAT slips.",
                "Solution: Connect Agentic AI to P6 API to audit logic integrity."
            ]
        },
        {
            "id": "omicron_secondary_injection",
            "title": "Secondary Injection Traps with OMICRON CMC 356",
            "format": "REEL",
            "hook": "The OMICRON test mistake that leaves differential relays blind",
            "keyword": "OMICRON",
            "facts": [
                "Injecting single-phase current without simulating restraining bias causes false trip.",
                "Ramping slope 1 (20-30%) and slope 2 (70-80%) must be verified independently.",
                "Solution: Follow standardized 3-phase automated test templates."
            ]
        }
    ]
}

def get_font(size, bold=False):
    font_names = ["arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf", "consola.ttf"]
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()

def determine_active_slot():
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    hour_utc = now_utc.hour
    
    # 02:00 - 07:00 UTC = 07:30 - 12:30 IST (Morning)
    # 07:00 - 12:00 UTC = 12:30 - 17:30 IST (Afternoon)
    # 12:00 - 22:00 UTC = 17:30 - 03:30 IST (Evening)
    if 2 <= hour_utc < 7:
        return "morning"
    elif 7 <= hour_utc < 12:
        return "afternoon"
    else:
        return "evening"

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_history(entry):
    history = load_history()
    history.append(entry)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

def select_topic_for_slot(slot):
    candidates = TOPICS_DATABASE.get(slot, TOPICS_DATABASE["morning"])
    history = load_history()
    published_ids = {h.get("topic_id") for h in history}
    
    # Filter candidates not yet published
    unseen = [c for c in candidates if c["id"] not in published_ids]
    if not unseen:
        # If all candidates published, cycle through all
        unseen = candidates
        
    return random.choice(unseen)

def render_slot_reel(out_path, topic, slot_name):
    # 1080 x 1920 vertical MP4 video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30
    duration_sec = 6
    total_frames = duration_sec * fps
    out = cv2.VideoWriter(out_path, fourcc, fps, (1080, 1920))
    
    color_map = {
        "morning": ((255, 75, 75), "FORENSIC SPEC TEARDOWN"),
        "afternoon": ((0, 242, 254), "TECHNICAL COMMISSIONING"),
        "evening": ((255, 184, 0), "INDUSTRIAL AI & DIALOGUE")
    }
    accent_color, slot_tag = color_map.get(slot_name, ((0, 242, 254), "PROENGINEERING"))
    
    for frame_idx in range(total_frames):
        t_frac = frame_idx / total_frames
        img = Image.new("RGB", (1080, 1920), (13, 17, 23))
        draw = ImageDraw.Draw(img)
        
        # Header
        draw.rectangle([0, 0, 1080, 140], fill=(16, 22, 30))
        draw.line([(0, 140), (1080, 140)], fill=accent_color, width=3)
        draw.text((50, 40), "⚡ PROENGINEERING | 23+ YRS INDUSTRIAL AI", font=get_font(28, bold=True), fill=accent_color)
        
        # Tag
        draw.rounded_rectangle([60, 170, 480, 225], radius=8, fill=(25, 35, 48), outline=accent_color, width=2)
        draw.text((80, 185), slot_tag, font=get_font(20, bold=True), fill=accent_color)
        
        # Hook Card
        draw.rounded_rectangle([60, 250, 1020, 520], radius=16, fill=(22, 27, 34), outline=accent_color, width=3)
        draw.text((90, 280), topic["title"].upper(), font=get_font(38, bold=True), fill=accent_color)
        draw.text((90, 360), topic["hook"][:60], font=get_font(28, bold=False), fill=(255, 255, 255))
        if len(topic["hook"]) > 60:
            draw.text((90, 410), topic["hook"][60:], font=get_font(28, bold=False), fill=(255, 255, 255))
            
        # Facts / Insights
        y = 560
        for i, fact in enumerate(topic["facts"]):
            draw.rounded_rectangle([60, y, 1020, y+240], radius=12, fill=(18, 25, 36), outline=(40, 52, 70), width=2)
            draw.text((90, y+25), f"INSIGHT 0{i+1}:", font=get_font(24, bold=True), fill=accent_color)
            draw.text((90, y+80), fact[:70], font=get_font(22, bold=False), fill=(230, 240, 250))
            if len(fact) > 70:
                draw.text((90, y+125), fact[70:140], font=get_font(22, bold=False), fill=(230, 240, 250))
            y += 270
            
        # Bottom CTA
        draw.rectangle([0, 1740, 1080, 1920], fill=(16, 22, 30))
        draw.rounded_rectangle([80, 1770, 1000, 1870], radius=16, fill=(22, 27, 34), outline=(0, 255, 140), width=3)
        draw.text((160, 1805), f"COMMENT \"{topic['keyword']}\" FOR FULL PDF CHECKLIST", font=get_font(30, bold=True), fill=(0, 255, 140))
        
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print(f"Rendered Slot Reel: {out_path}")

def render_slot_carousel(folder_path, topic):
    os.makedirs(folder_path, exist_ok=True)
    slides = topic["slides"]
    total = len(slides)
    
    for idx, (head, desc) in enumerate(slides):
        slide_num = idx + 1
        img = Image.new("RGB", (1080, 1350), (13, 17, 23))
        draw = ImageDraw.Draw(img)
        
        # Grid
        for x in range(0, 1080, 50):
            draw.line([(x, 0), (x, 1350)], fill=(20, 26, 35), width=1)
        for y in range(0, 1350, 50):
            draw.line([(0, y), (1080, y)], fill=(20, 26, 35), width=1)
            
        # Header
        draw.rectangle([0, 0, 1080, 130], fill=(16, 22, 30))
        draw.line([(0, 130), (1080, 130)], fill=(0, 242, 254), width=3)
        draw.text((60, 45), "⚡ PROENGINEERING TECHNICAL CAROUSEL", font=get_font(28, bold=True), fill=(0, 242, 254))
        draw.text((880, 45), f"{slide_num}/{total}", font=get_font(28, bold=True), fill=(255, 255, 255))
        
        # Topic Title
        draw.text((60, 180), topic["title"].upper(), font=get_font(42, bold=True), fill=(255, 184, 0))
        draw.line([(60, 240), (400, 240)], fill=(255, 184, 0), width=3)
        
        # Main Slide Content Box
        draw.rounded_rectangle([60, 300, 1020, 1050], radius=18, fill=(18, 25, 36), outline=(0, 242, 254), width=2)
        draw.text((100, 360), head, font=get_font(38, bold=True), fill=(0, 242, 254))
        draw.text((100, 450), desc[:65], font=get_font(26, bold=False), fill=(240, 245, 255))
        if len(desc) > 65:
            draw.text((100, 500), desc[65:], font=get_font(26, bold=False), fill=(240, 245, 255))
            
        # Bottom CTA
        draw.rectangle([0, 1240, 1080, 1350], fill=(16, 22, 30))
        draw.text((180, 1275), f"COMMENT \"{topic['keyword']}\" FOR COMPLETE STUDY PDF", font=get_font(26, bold=True), fill=(0, 255, 140))
        
        out_slide = os.path.join(folder_path, f"slide_{slide_num:02d}.png")
        img.save(out_slide)
        
    print(f"Rendered Slot Carousel ({total} slides) at: {folder_path}")

def dispatch_post(slot_name="auto"):
    if slot_name == "auto":
        slot_name = determine_active_slot()
        
    now = datetime.datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d_%H%M")
    date_str = now.strftime("%Y-%m-%d")
    
    print(f"--- Running ProEngineering Cloud Publisher for Slot: {slot_name.upper()} ({timestamp_str}) ---")
    
    topic = select_topic_for_slot(slot_name)
    slot_dir = os.path.join(POSTS_DIR, f"{date_str}_{slot_name}")
    os.makedirs(slot_dir, exist_ok=True)
    
    caption = (
        f"⚡ {topic['title']} ⚡\n\n"
        f"{topic['hook']}\n\n"
        f"Key Engineering Realities:\n"
        f"1️⃣ {topic.get('facts', ['Field Verified Protocol'])[0]}\n"
        f"2️⃣ 23+ Years of Commissioning & Megaproject Scars\n"
        f"3️⃣ Agentic AI Spec-vs-Drawing Conformance\n\n"
        f"👇 Comment '{topic['keyword']}' below and I'll send you the complete technical calculation and sign-off checklist! (Or visit proengineering.in)\n\n"
        f"#ElectricalEngineering #PowerSystems #33kVSubstation #EPC #ProjectControls #PrimaveraP6 #IndustrialAI #ProEngineering"
    )
    
    caption_path = os.path.join(slot_dir, "caption.txt")
    with open(caption_path, "w", encoding="utf-8") as f:
        f.write(caption)
        
    media_path = ""
    if topic["format"] == "REEL":
        media_path = os.path.join(slot_dir, f"reel_{slot_name}.mp4")
        render_slot_reel(media_path, topic, slot_name)
    else:
        carousel_dir = os.path.join(slot_dir, "carousel")
        render_slot_carousel(carousel_dir, topic)
        media_path = os.path.join(carousel_dir, "slide_01.png")
        
    # Attempt publication via InstagramPublisher
    publisher = InstagramPublisher()
    published = publisher.publish_reel_via_graph_api(video_url=media_path, caption=caption)
    
    # Save to history
    history_entry = {
        "timestamp": timestamp_str,
        "slot": slot_name,
        "topic_id": topic["id"],
        "title": topic["title"],
        "format": topic["format"],
        "keyword": topic["keyword"],
        "media_path": media_path,
        "published": published
    }
    save_history(history_entry)
    print(f"[SUCCESS] Dispatched post for {slot_name.upper()} slot: {topic['title']}")
    return history_entry

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ProEngineering Cloud Post Scheduler")
    parser.add_argument("--slot", choices=["auto", "morning", "afternoon", "evening", "all"], default="auto")
    args = parser.parse_args()
    
    if args.slot == "all":
        for s in ["morning", "afternoon", "evening"]:
            dispatch_post(s)
    else:
        dispatch_post(args.slot)
