import os
import sys
import json
import time
import math
import datetime
import random
import subprocess
import requests
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Local SFX generator
from generate_pop_sfx import build_synchronized_soundtrack

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
POSTS_DIR = os.path.join(BASE_DIR, "daily_posts")
HISTORY_FILE = os.path.join(BASE_DIR, "published_history.json")
USER_PHOTO_PATH = os.path.join(ASSETS_DIR, "user_photo.jpg")

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

# 11:00 AM IST Topic Bank (Rotating Technical Scenarios)
DAILY_REEL_TOPICS = [
    {
        "id": "spec_40ka_trap",
        "title": "THE $400K EPC SPEC TRAP",
        "hook": "1 Sentence In Division 26 That Destroys Contractor Margin",
        "keyword": "SPEC",
        "badge": "CSI SPEC CONFLICT",
        "clause": "Clause 26 13 00: 40 kA (3s) Withstand Required",
        "sld_gap": "Tender SLD specifies only standard 31.5 kA",
        "impact": "$400,000 Unbudgeted Switchgear Change Order",
        "solution": "Agentic AI Spec-vs-Drawing Audit in 20 Seconds",
        "caption": (
            "Most $400K+ switchgear change orders hide inside contradictions between Division 26 Specs, the SLD, and the BOQ (31.5 kA vs 40 kA fault levels & IEC 61850 gateways). ⚡\n\n"
            "Here are the 4 pre-bid traps every Project Director, EPC Lead, and Electrical Engineer must audit before signing off:\n"
            "1️⃣ Order-of-precedence conflicts between BOQ line items and spec clauses\n"
            "2️⃣ 33 kV / 11 kV switchgear fault-level mismatches (31.5 kA vs. 40 kA for 3s)\n"
            "3️⃣ Proprietary IEC 61850 / SCADA gateway traps on numerical relays\n"
            "4️⃣ Two-way cable takeoff gaps between feeder schedules and trench routing\n\n"
            "👇 Comment SPEC below and I'll DM you my printable 33 kV Substation & EPC Pre-Bid Diagnostic Checklist (or grab the tools directly at proengineering.in).\n\n"
            "#ElectricalEngineering #PowerSystems #Substation #EPC #ProjectManagement #PrimaveraP6 #ProtectionRelays #IndustrialAI #ProEngineering"
        )
    },
    {
        "id": "day1_substation_trip",
        "title": "33kV DAY-1 ENERGIZATION TRIP",
        "hook": "Why 33kV Breakers Trip on Day-1 Soak After Passing FAT",
        "keyword": "RELAY",
        "badge": "87T DIFFERENTIAL TRIP",
        "clause": "MiCOM P643 / ABB RET670 Relay Tripped in 40ms",
        "sld_gap": "Dyn11 30° Vector Compensation Ignored in Relay",
        "impact": "Unplanned Outage & Commissioning Delay Penalties",
        "solution": "Enable 15% 2nd-Harmonic Inrush Restraint & Cross-Block",
        "caption": (
            "When the 87T differential relay trips your 33 kV incomer on no-load soak, check your site CT burden loop, Dyn11 vector compensation, and 15% 2nd-harmonic inrush restraint on your MiCOM relay. ⚡\n\n"
            "Factory Acceptance Tests (FAT) never replace site secondary injection:\n"
            "1️⃣ Verify CT Class PS knee-point Vk calculation across secondary cable runs\n"
            "2️⃣ Confirm single-point CT star ground inside the relay panel only\n"
            "3️⃣ Verify 15% 2nd-harmonic cross-blocking on transformer core magnetization\n"
            "4️⃣ Perform 3-phase secondary ramp tests with OMICRON CMC 356\n\n"
            "👇 Comment RELAY below for the full Zero-Trip 33kV Energization Protocol!\n\n"
            "#SubstationCommissioning #Switchgear #PowerEngineering #ElectricalEngineering #OMICRON #ProtectionRelays #ProEngineering"
        )
    },
    {
        "id": "primavera_p6_float_trap",
        "title": "PRIMAVERA P6 FLOAT TRAP AUDIT",
        "hook": "Why 80% of EPC Schedules Hide 6-Week Critical Delays",
        "keyword": "P6",
        "badge": "HIDDEN SCHEDULE DELAY",
        "clause": "Artificial SS+15d Lag on Secondary Relay Testing",
        "sld_gap": "Dangling FAT/SAT Precedents Not Linked to Path",
        "impact": "-42 Days Negative Float on Energization Milestone",
        "solution": "Agentic AI P6 Schedule Logic Diagnostic",
        "caption": (
            "Why do 80% of EPC schedules show 'On Track' until substation energization slips by 6 weeks? Dangling FAT/SAT submittals and artificial lag traps. 🤖\n\n"
            "3 critical schedule health checks every Project Controls Manager must run:\n"
            "1️⃣ Remove artificial Start-to-Start lags on commissioning precursors\n"
            "2️⃣ Audit negative float on statutory CEA inspectorate clearances\n"
            "3️⃣ Connect P6 milestones to real-time SCADA commissioning test sheets\n\n"
            "👇 Comment P6 below for my Schedule Health Playbook or visit proengineering.in.\n\n"
            "#PrimaveraP6 #ProjectControls #ProjectManagement #PMP #EPC #IndustrialAI #ProEngineering"
        )
    }
]

def get_font(size, bold=False):
    font_names = ["arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf", "consola.ttf"]
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()

def render_broadcast_video(out_mp4, topic):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30
    duration_sec = 8
    total_frames = duration_sec * fps
    out = cv2.VideoWriter(out_mp4, fourcc, fps, (1080, 1920))
    
    user_img = None
    if os.path.exists(USER_PHOTO_PATH):
        user_img = Image.open(USER_PHOTO_PATH).convert("RGBA")
    else:
        user_img = Image.new("RGBA", (400, 500), (30, 45, 65))
        
    f_hook = get_font(50, bold=True)
    f_badge = get_font(28, bold=True)
    f_body = get_font(24, bold=False)
    f_stat = get_font(42, bold=True)
    
    print(f"[RENDER] Generating 1080x1920 video for topic: {topic['title']}...")
    
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        t_frac = frame_idx / total_frames
        
        img = Image.new("RGB", (1080, 1920), (11, 15, 22))
        draw = ImageDraw.Draw(img)
        
        # Background Grid
        for gx in range(0, 1080, 60):
            draw.line([(gx, 0), (gx, 1920)], fill=(18, 24, 34), width=1)
        for gy in range(0, 1920, 60):
            draw.line([(0, gy), (1080, gy)], fill=(18, 24, 34), width=1)
            
        # Top Progress Retention Bar
        draw.rectangle([0, 0, int(t_frac * 1080), 12], fill=(0, 242, 254))
        
        # Header
        draw.rectangle([0, 12, 1080, 130], fill=(16, 22, 32))
        draw.line([(0, 130), (1080, 130)], fill=(0, 242, 254), width=2)
        draw.text((50, 42), "⚡ PROENGINEERING CLOUD FACTORY", font=get_font(30, bold=True), fill=(0, 242, 254))
        draw.text((50, 82), "23+ YRS SUBSTATIONS & INDUSTRIAL AI", font=get_font(20, bold=False), fill=(200, 220, 240))
        
        # Presenter Framing (with punch-in zoom cut between 2.4s and 4.8s)
        zoom = 1.12 if (2.4 <= t < 4.8) else 1.0
        uw, uh = int(380 * zoom), int(480 * zoom)
        u_resized = user_img.resize((uw, uh), Image.Resampling.LANCZOS)
        ux, uy = 540 - uw // 2, 420 - uh // 2
        
        pulse = (math.sin(t * 8) + 1) / 2
        glow_c = (int(0 + 40 * pulse), int(220 + 35 * pulse), 254)
        draw.rounded_rectangle([ux - 8, uy - 8, ux + uw + 8, uy + uh + 8], radius=22, outline=glow_c, width=4)
        img.paste(u_resized, (ux, uy))
        
        # Presenter Badge
        draw.rounded_rectangle([300, uy + uh - 35, 780, uy + uh + 20], radius=10, fill=(13, 17, 23), outline=(0, 242, 254), width=2)
        draw.text((320, uy + uh - 27), "SENIOR INDUSTRIAL AI ARCHITECT", font=get_font(20, bold=True), fill=(0, 242, 254))
        
        # Hook Card
        draw.rounded_rectangle([50, 720, 1030, 870], radius=16, fill=(24, 18, 22), outline=(255, 75, 75), width=3)
        draw.text((80, 745), topic["title"], font=f_hook, fill=(255, 75, 75))
        draw.text((80, 815), topic["hook"][:65], font=get_font(24, bold=False), fill=(255, 255, 255))
        
        # Pop-Up Element 1 (0.8s)
        if t >= 0.8:
            draw.rounded_rectangle([50, 900, 1030, 1010], radius=12, fill=(45, 15, 20), outline=(255, 60, 60), width=3)
            draw.text((80, 920), f"⚠ {topic['badge']}", font=f_badge, fill=(255, 80, 80))
            draw.text((80, 965), topic["clause"], font=f_body, fill=(240, 210, 210))
            
        # Pop-Up Element 2 (2.0s)
        if t >= 2.0:
            draw.rounded_rectangle([50, 1040, 1030, 1150], radius=12, fill=(35, 28, 15), outline=(255, 184, 0), width=2)
            draw.text((80, 1060), "⚡ SITE & DRAWING REALITY", font=f_badge, fill=(255, 184, 0))
            draw.text((80, 1105), topic["sld_gap"], font=f_body, fill=(255, 240, 200))

        # Pop-Up Element 3 (3.6s)
        if t >= 3.6:
            draw.rounded_rectangle([50, 1180, 1030, 1320], radius=15, fill=(40, 10, 15), outline=(255, 50, 50), width=4)
            draw.text((80, 1205), f"💥 {topic['impact']}", font=f_stat, fill=(255, 70, 70))
            draw.text((80, 1265), "Unbudgeted loss before site mobilization.", font=f_body, fill=(255, 220, 220))

        # Pop-Up Element 4 (4.8s)
        if t >= 4.8:
            draw.rounded_rectangle([50, 1350, 1030, 1470], radius=12, fill=(15, 35, 25), outline=(0, 255, 140), width=3)
            draw.text((80, 1370), "🛡 FIELD RESOLUTION & AI WORKFLOW", font=f_badge, fill=(0, 255, 140))
            draw.text((80, 1415), topic["solution"], font=f_body, fill=(220, 255, 235))

        # Call to Action (6.0s+)
        if t >= 6.0:
            draw.rectangle([0, 1640, 1080, 1920], fill=(13, 17, 23))
            draw.line([(0, 1640), (1080, 1640)], fill=(0, 242, 254), width=3)
            draw.rounded_rectangle([60, 1670, 1020, 1820], radius=18, fill=(20, 26, 38), outline=(0, 255, 140), width=4)
            draw.text((110, 1705), f"👉 COMMENT \"{topic['keyword']}\" BELOW", font=get_font(40, bold=True), fill=(255, 255, 255))
            draw.text((110, 1765), "I'll DM you the technical calculation & sign-off protocol!", font=get_font(24, bold=False), fill=(0, 242, 254))
            draw.text((280, 1855), "⚡ proengineering.in | Senior Power Systems Lead", font=get_font(20, bold=False), fill=(180, 200, 220))
            
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print(f"[SUCCESS] Video rendered at: {out_mp4}")

def mux_audio_and_video(video_path, audio_path, final_output):
    """Muxes video and audio with FFmpeg if available, or renames video as final output."""
    try:
        cmd = [
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-shortest",
            final_output
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode == 0 and os.path.exists(final_output):
            print(f"[FFMPEG] Successfully muxed H.264/AAC video: {final_output}")
            return final_output
    except Exception as e:
        print(f"[WARN] FFmpeg mux skipped ({e}). Using base video.")
        
    if os.path.exists(video_path):
        import shutil
        shutil.copy(video_path, final_output)
        return final_output
    return video_path

class MetaInstagramReelPublisher:
    """Official Meta Instagram Graph API Reel Publishing Flow"""
    def __init__(self, access_token=None, ig_user_id=None):
        self.access_token = access_token or os.environ.get("INSTAGRAM_ACCESS_TOKEN")
        self.ig_user_id = ig_user_id or os.environ.get("INSTAGRAM_USER_ID")
        self.graph_base_url = "https://graph.facebook.com/v19.0"

    def publish_reel(self, public_video_url, caption):
        if not self.access_token or not self.ig_user_id:
            print("[INFO] Meta credentials not provided. Video staged locally ready for publishing.")
            return {"status": "STAGED", "url": public_video_url}

        # Step 1: Initialize Media Container
        init_url = f"{self.graph_base_url}/{self.ig_user_id}/media"
        payload = {
            "media_type": "REELS",
            "video_url": public_video_url,
            "caption": caption,
            "access_token": self.access_token
        }
        res = requests.post(init_url, data=payload).json()
        container_id = res.get("id")
        if not container_id:
            print(f"[ERROR] Container creation failed: {res}")
            return {"status": "ERROR", "error": res}

        print(f"[META] Media Container Created: {container_id}. Polling status...")

        # Step 2: Poll Container Status until FINISHED
        poll_url = f"{self.graph_base_url}/{container_id}"
        for _ in range(30):
            time.sleep(5)
            status_res = requests.get(poll_url, params={"fields": "status_code,status", "access_token": self.access_token}).json()
            code = status_res.get("status_code")
            print(f"[META] Container Status: {code}")
            if code == "FINISHED":
                break
            elif code in ["ERROR", "EXPIRED"]:
                print(f"[ERROR] Container processing failed: {status_res}")
                return {"status": "ERROR", "error": status_res}

        # Step 3: Publish Media Container
        pub_url = f"{self.graph_base_url}/{self.ig_user_id}/media_publish"
        pub_res = requests.post(pub_url, data={"creation_id": container_id, "access_token": self.access_token}).json()
        post_id = pub_res.get("id")
        print(f"[SUCCESS] Reel Published to Instagram! Post ID: {post_id}")
        return {"status": "PUBLISHED", "post_id": post_id}

def run_cloud_factory():
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    timestamp = now.strftime("%Y-%m-%d_%H%M")
    
    print(f"=======================================================")
    print(f"  PROENGINEERING CLOUD REEL FACTORY - 11:00 AM IST")
    print(f"  Execution Time: {timestamp}")
    print(f"=======================================================")
    
    # 1. Select Topic
    topic_override = os.environ.get("TOPIC_OVERRIDE")
    selected_topic = None
    if topic_override:
        for t in DAILY_REEL_TOPICS:
            if t["id"] == topic_override:
                selected_topic = t
                break
    if not selected_topic:
        day_index = int(now.strftime("%j")) # Day of year for deterministic rotation
        selected_topic = DAILY_REEL_TOPICS[day_index % len(DAILY_REEL_TOPICS)]
        
    print(f"[AI DIRECTOR] Selected Topic: {selected_topic['title']}")
    
    day_folder = os.path.join(POSTS_DIR, f"{date_str}_11am")
    os.makedirs(day_folder, exist_ok=True)
    
    # 2. Render Audio & Video
    raw_video = os.path.join(day_folder, "raw_video.mp4")
    render_broadcast_video(raw_video, selected_topic)
    
    sfx_audio = build_synchronized_soundtrack(total_duration=8.0)
    
    final_reel = os.path.join(day_folder, f"ProEngineering_Reel_{date_str}.mp4")
    mux_audio_and_video(raw_video, sfx_audio, final_reel)
    
    # Save Caption
    caption_file = os.path.join(day_folder, "caption.txt")
    with open(caption_file, "w", encoding="utf-8") as f:
        f.write(selected_topic["caption"])
        
    # 3. Publish via Meta API
    publisher = MetaInstagramReelPublisher()
    # In cloud GitHub Actions, video URL will point to the public release or hosted asset
    public_url = os.environ.get("PUBLIC_MEDIA_URL", f"file:///{final_reel.replace(os.sep, '/')}")
    result = publisher.publish_reel(public_video_url=public_url, caption=selected_topic["caption"])
    
    # 4. Log History
    history_entry = {
        "timestamp": timestamp,
        "date": date_str,
        "topic_id": selected_topic["id"],
        "title": selected_topic["title"],
        "video_file": final_reel,
        "result": result
    }
    
    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except Exception:
            history = []
    history.append(history_entry)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
        
    print(f"[SUMMARY] Cloud Reel Factory execution finished successfully.")
    return history_entry

if __name__ == "__main__":
    run_cloud_factory()
