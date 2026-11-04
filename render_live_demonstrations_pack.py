import os
import math
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

REELS_DIR = "d:/instagram/reels"
ASSETS_DIR = "d:/instagram/assets"
USER_PHOTO = os.path.join(ASSETS_DIR, "user_photo.jpg")
os.makedirs(REELS_DIR, exist_ok=True)

def get_font(size, bold=False):
    font_names = ["arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf", "consola.ttf"]
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()

def render_demo_substation(out_mp4, duration_sec=8, fps=30):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_mp4, fourcc, fps, (1080, 1920))
    total_frames = int(duration_sec * fps)
    
    user_img = Image.open(USER_PHOTO).convert("RGBA") if os.path.exists(USER_PHOTO) else Image.new("RGBA", (350, 450), (20, 30, 45))
    f_hook = get_font(46, bold=True)
    f_title = get_font(30, bold=True)
    f_badge = get_font(22, bold=True)
    f_body = get_font(20, bold=False)
    f_meter = get_font(34, bold=True)
    
    print(f"Rendering Live Substation Demo Reel ({total_frames} frames)...")
    
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        t_frac = frame_idx / total_frames
        
        img = Image.new("RGB", (1080, 1920), (10, 14, 22))
        draw = ImageDraw.Draw(img)
        
        # Grid Background
        grid_y = int((t * 30) % 50)
        for gx in range(0, 1080, 50):
            draw.line([(gx, 0), (gx, 1920)], fill=(16, 22, 34), width=1)
        for gy in range(grid_y, 1920, 50):
            draw.line([(0, gy), (1080, gy)], fill=(16, 22, 34), width=1)
            
        # Top Progress Bar
        draw.rectangle([0, 0, int(t_frac * 1080), 12], fill=(0, 242, 254))
        
        # Header
        draw.rectangle([0, 12, 1080, 130], fill=(15, 20, 30))
        draw.line([(0, 130), (1080, 130)], fill=(0, 242, 254), width=2)
        draw.text((50, 42), "⚡ PROENGINEERING LIVE LAB", font=get_font(28, bold=True), fill=(0, 242, 254))
        draw.text((50, 82), "LIVE 33kV SUBSTATION COMMISSIONING & SLD AUDIT", font=get_font(18, bold=False), fill=(200, 220, 240))
        
        # Red Live Blinker
        if int(t * 3) % 2 == 0:
            draw.ellipse([920, 54, 938, 72], fill=(255, 50, 50))
        draw.text((948, 52), "LIVE", font=get_font(20, bold=True), fill=(255, 70, 70))
        
        # =========================================================================
        # USER PHOTO PRESENTER WITH DYNAMIC BREATHING & CAMERA CUT-ZOOMS
        # =========================================================================
        zoom = 1.10 if (2.0 <= t < 4.5) else 1.0
        breath = 1.0 + 0.012 * math.sin(t * 4.0)
        uw = int(330 * zoom * breath)
        uh = int(420 * zoom * breath)
        u_scaled = user_img.resize((uw, uh), Image.Resampling.LANCZOS)
        
        ux, uy = 540 - uw // 2, 380 - uh // 2
        
        # Cyan neon holographic frame
        draw.rounded_rectangle([ux - 6, uy - 6, ux + uw + 6, uy + uh + 6], radius=18, outline=(0, 242, 254), width=3)
        img.paste(u_scaled, (ux, uy))
        
        # Presenter Tag
        draw.rounded_rectangle([ux + 25, uy + uh - 25, ux + uw - 25, uy + uh + 15], radius=8, fill=(11, 15, 22), outline=(0, 242, 254), width=2)
        draw.text((ux + 40, uy + uh - 20), "AMARESH DAS | 23+ YRS LEAD", font=get_font(17, bold=True), fill=(0, 242, 254))
        
        # Hook Banner
        draw.rounded_rectangle([50, 630, 1030, 760], radius=14, fill=(22, 28, 40), outline=(255, 184, 0), width=3)
        draw.text((80, 650), "LIVE DEMO: 33kV ZERO-TRIP ENERGIZATION", font=f_hook, fill=(255, 184, 0))
        draw.text((80, 710), "Demonstrating Secondary Injection & 87T Relay Inrush Restraint", font=get_font(22, bold=False), fill=(240, 240, 240))
        
        # =========================================================================
        # LIVE INSTRUMENTATION SIMULATOR
        # =========================================================================
        # Gauge Box 1: OMICRON Secondary Injection Current (Live ramping)
        draw.rounded_rectangle([50, 790, 520, 1010], radius=14, fill=(16, 22, 32), outline=(0, 242, 254), width=2)
        draw.text((70, 810), "SECONDARY INJECTION (OMICRON)", font=get_font(20, bold=True), fill=(0, 242, 254))
        
        curr = min(t * 0.75, 5.0)
        draw.text((70, 850), f"{curr:.2f} A", font=f_meter, fill=(0, 255, 140))
        draw.text((70, 900), "Ramped from 0.0A to 5.0A rated", font=f_body, fill=(200, 220, 240))
        # Live meter needle
        draw.rectangle([70, 940, 480, 960], fill=(24, 34, 48), outline=(50, 70, 90), width=1)
        draw.rectangle([70, 940, 70 + int((curr / 5.0) * 410), 960], fill=(0, 255, 140))
        draw.text((70, 970), "CT RATIO: 600/1A Class PS", font=get_font(16, bold=False), fill=(160, 180, 200))
        
        # Gauge Box 2: 87T Relay Trip Status
        draw.rounded_rectangle([560, 790, 1030, 1010], radius=14, fill=(16, 22, 32), outline=(255, 184, 0), width=2)
        draw.text((580, 810), "87T DIFFERENTIAL RELAY STATUS", font=get_font(20, bold=True), fill=(255, 184, 0))
        
        if t < 3.2:
            draw.text((580, 850), "TRIP @ 38ms!", font=f_meter, fill=(255, 60, 60))
            draw.text((580, 900), "CAUSE: 2nd Harmonic Inrush Spilled", font=f_body, fill=(255, 200, 200))
            draw.rounded_rectangle([580, 940, 990, 980], radius=6, fill=(45, 15, 20), outline=(255, 70, 70), width=2)
            draw.text((600, 950), "UNRESTRAINED INRUSH CURRENT", font=get_font(16, bold=True), fill=(255, 100, 100))
        else:
            draw.text((580, 850), "ZERO-TRIP PASS!", font=f_meter, fill=(0, 255, 140))
            draw.text((580, 900), "FIX: 15% 2nd Harmonic Cross-Blocked", font=f_body, fill=(200, 255, 220))
            draw.rounded_rectangle([580, 940, 990, 980], radius=6, fill=(15, 40, 25), outline=(0, 255, 140), width=2)
            draw.text((600, 950), "TRANSFORMER ENERGIZED SAFELY", font=get_font(16, bold=True), fill=(0, 255, 140))
            
        # Live Oscilloscope Screen (y=1030 to y=1240)
        draw.rounded_rectangle([50, 1030, 1030, 1250], radius=14, fill=(8, 12, 18), outline=(0, 242, 254), width=2)
        draw.text((80, 1045), "TEKTRONIX DIGITAL OSCILLOSCOPE (TRANSFORMER MAGNETIZING CURRENT)", font=get_font(18, bold=True), fill=(0, 242, 254))
        
        osc_y = 1145
        draw.line([(80, osc_y), (1000, osc_y)], fill=(25, 40, 60), width=1)
        for ox in range(80, 1000, 4):
            phase = (ox / 28.0) + (t * 14.0)
            h2 = 28 if t < 3.2 else 6
            oy = int(35 * math.sin(phase) + h2 * math.sin(2 * phase))
            draw.line([(ox, osc_y + oy), (ox + 4, osc_y + oy)], fill=(0, 242, 254), width=2)
            
        # Live Step Verification Cards (y=1270 to y=1630)
        draw.rounded_rectangle([50, 1270, 1030, 1630], radius=14, fill=(16, 22, 32), outline=(0, 255, 140), width=2)
        draw.text((80, 1290), "LIVE SUBSTATION SIGN-OFF VERIFICATION", font=f_title, fill=(0, 255, 140))
        
        steps = [
            ("1. Dyn11 Vector Group", "30° internal phase angle displacement verified in numerical relay", 1.0),
            ("2. CT Knee-Point Vk", "Vk >= 2 * If * (Rct + 2*RL + Rr) calculation cleared at 480V", 2.2),
            ("3. Single-Point Star Ground", "Confirmed switchyard CT neutral isolated; star ground at relay panel only", 3.8),
            ("4. VCB Timing Test", "Opening time: 38ms | Closing time: 54ms | Contact bounce: 1.8ms (PASSED)", 5.2)
        ]
        
        cy = 1335
        for s_num, s_desc, st in steps:
            if t >= st:
                draw.rounded_rectangle([80, cy, 1000, cy + 62], radius=8, fill=(20, 32, 45), outline=(0, 255, 140), width=2)
                draw.text((100, cy + 10), f"✔ {s_num}:", font=f_badge, fill=(0, 255, 140))
                draw.text((100, cy + 34), s_desc, font=f_body, fill=(230, 240, 250))
            else:
                draw.rounded_rectangle([80, cy, 1000, cy + 62], radius=8, fill=(12, 16, 24), outline=(30, 42, 55), width=1)
                draw.text((100, cy + 18), f"⏳ RUNNING: {s_num}...", font=f_body, fill=(90, 110, 130))
            cy += 70
            
        # CTA Banner (6.0s+)
        if t >= 6.0:
            draw.rectangle([0, 1660, 1080, 1920], fill=(12, 16, 24))
            draw.line([(0, 1660), (1080, 1660)], fill=(0, 242, 254), width=3)
            draw.rounded_rectangle([60, 1690, 1020, 1840], radius=18, fill=(20, 28, 42), outline=(0, 255, 140), width=4)
            draw.text((100, 1720), "👉 COMMENT \"DEMO\" BELOW", font=get_font(42, bold=True), fill=(255, 255, 255))
            draw.text((100, 1780), "I'll DM you my 33kV Relay Setting & Commissioning Protocol!", font=get_font(22, bold=False), fill=(0, 242, 254))
            draw.text((290, 1870), "⚡ proengineering.in | Senior Power Systems Lead", font=get_font(20, bold=False), fill=(180, 200, 220))
            
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print(f"Substation Demo Video saved: {out_mp4}")

def render_demo_p6_ai(out_mp4, duration_sec=8, fps=30):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_mp4, fourcc, fps, (1080, 1920))
    total_frames = int(duration_sec * fps)
    
    user_img = Image.open(USER_PHOTO).convert("RGBA") if os.path.exists(USER_PHOTO) else Image.new("RGBA", (350, 450), (20, 30, 45))
    f_hook = get_font(46, bold=True)
    f_title = get_font(30, bold=True)
    f_badge = get_font(22, bold=True)
    f_body = get_font(20, bold=False)
    f_stat = get_font(36, bold=True)
    
    print(f"Rendering Live Primavera P6 AI Demo Reel ({total_frames} frames)...")
    
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        t_frac = frame_idx / total_frames
        
        img = Image.new("RGB", (1080, 1920), (10, 14, 22))
        draw = ImageDraw.Draw(img)
        
        # Grid
        for gx in range(0, 1080, 60):
            draw.line([(gx, 0), (gx, 1920)], fill=(16, 22, 34), width=1)
        for gy in range(0, 1920, 60):
            draw.line([(0, gy), (1080, gy)], fill=(16, 22, 34), width=1)
            
        # Top Bar
        draw.rectangle([0, 0, int(t_frac * 1080), 12], fill=(255, 184, 0))
        draw.rectangle([0, 12, 1080, 130], fill=(15, 20, 30))
        draw.line([(0, 130), (1080, 130)], fill=(255, 184, 0), width=2)
        draw.text((50, 42), "⚡ PROENGINEERING AI PROJECT CONTROLS", font=get_font(28, bold=True), fill=(255, 184, 0))
        draw.text((50, 82), "LIVE PRIMAVERA P6 SCHEDULE AUDIT & FLOAT DIAGNOSTIC", font=get_font(18, bold=False), fill=(200, 220, 240))
        
        # Red Live Blinker
        if int(t * 3) % 2 == 0:
            draw.ellipse([920, 54, 938, 72], fill=(255, 50, 50))
        draw.text((948, 52), "LIVE", font=get_font(20, bold=True), fill=(255, 70, 70))
        
        # User Photo Presenter with camera cut-zoom
        zoom = 1.10 if (2.0 <= t < 4.5) else 1.0
        breath = 1.0 + 0.012 * math.sin(t * 4.0)
        uw = int(330 * zoom * breath)
        uh = int(420 * zoom * breath)
        u_scaled = user_img.resize((uw, uh), Image.Resampling.LANCZOS)
        
        ux, uy = 540 - uw // 2, 380 - uh // 2
        draw.rounded_rectangle([ux - 6, uy - 6, ux + uw + 6, uy + uh + 6], radius=18, outline=(255, 184, 0), width=3)
        img.paste(u_scaled, (ux, uy))
        
        draw.rounded_rectangle([ux + 25, uy + uh - 25, ux + uw - 25, uy + uh + 15], radius=8, fill=(11, 15, 22), outline=(255, 184, 0), width=2)
        draw.text((ux + 40, uy + uh - 20), "AMARESH DAS | PMP & AI LEAD", font=get_font(17, bold=True), fill=(255, 184, 0))
        
        # Hook Banner
        draw.rounded_rectangle([50, 630, 1030, 760], radius=14, fill=(28, 22, 14), outline=(255, 184, 0), width=3)
        draw.text((80, 650), "DEMONSTRATING: AI PRIMAVERA P6 FLOAT AUDIT", font=f_hook, fill=(255, 184, 0))
        draw.text((80, 710), "Watch Agentic AI Audit Schedule Logic & Expose Hidden Lags in 20s", font=get_font(22, bold=False), fill=(240, 240, 240))
        
        # Live Gantt Activity Simulator (y=790 to y=1250)
        draw.rounded_rectangle([50, 790, 1030, 1240], radius=16, fill=(16, 22, 32), outline=(0, 242, 254), width=2)
        draw.text((80, 815), "PRIMAVERA P6 ENTERPRISE SCHEDULE VIEW", font=f_title, fill=(0, 242, 254))
        
        activities = [
            ("SUB-1010", "33kV Switchgear Factory FAT", "0d Float", (0, 255, 140)),
            ("SUB-1020", "Civil Foundation Handover", "-14d Float", (255, 184, 0)),
            ("SUB-1030", "Secondary Injection Relay SAT", "-35d Float", (255, 60, 60)),
            ("SUB-1040", "Statutory Clearance Inspection", "-42d Float", (255, 60, 60)),
            ("SUB-1050", "33kV Zero-Trip Energization", "CRITICAL PATH", (255, 60, 60)),
        ]
        
        ay = 860
        for act_id, act_name, float_val, color in activities:
            draw.rounded_rectangle([80, ay, 1000, ay + 62], radius=6, fill=(20, 26, 38), outline=(40, 52, 70), width=1)
            draw.text((95, ay + 12), act_id, font=get_font(20, bold=True), fill=(0, 242, 254))
            draw.text((240, ay + 12), act_name, font=get_font(20, bold=False), fill=(230, 240, 250))
            draw.text((780, ay + 12), float_val, font=get_font(20, bold=True), fill=color)
            
            # Gantt bar simulation
            bar_w = int(180 + (t * 15))
            draw.rounded_rectangle([240, ay + 38, 240 + bar_w, ay + 50], radius=4, fill=color)
            ay += 74
            
        # Live AI Diagnostic Resolution Box (y=1270 to y=1630)
        draw.rounded_rectangle([50, 1270, 1030, 1630], radius=14, fill=(16, 22, 32), outline=(0, 255, 140), width=2)
        draw.text((80, 1290), "AGENTIC AI SCHEDULE REMEDIATION", font=f_title, fill=(0, 255, 140))
        
        if t < 3.5:
            draw.text((80, 1340), "STATUS: SCANNING 3,420 ACTIVITIES FOR LOGIC TRAPS...", font=get_font(22, bold=True), fill=(255, 184, 0))
            draw.text((80, 1385), "• Detected Artificial Start-to-Start + 15d lag on SUB-1030", font=f_body, fill=(240, 220, 220))
            draw.text((80, 1425), "• Transformer Pre-Commissioning lacks mandatory Inspectorate lead time", font=f_body, fill=(240, 220, 220))
            draw.text((80, 1465), "• Projected Liquidated Damages Risk: $280,000", font=get_font(24, bold=True), fill=(255, 75, 75))
        else:
            draw.text((80, 1340), "STATUS: AI SCHEDULE REMEDIATION APPLIED!", font=get_font(22, bold=True), fill=(0, 255, 140))
            draw.text((80, 1385), "✔ Removed artificial SS lags -> Restored critical path float to 0 Days", font=f_body, fill=(220, 255, 235))
            draw.text((80, 1425), "✔ Re-sequenced CEA Inspectorate with parallel witness milestones", font=f_body, fill=(220, 255, 235))
            draw.text((80, 1465), "✔ $280,000 CONTRACTOR LIQUIDATED DAMAGES PROTECTED!", font=get_font(24, bold=True), fill=(0, 255, 140))
            
        # CTA Banner (6.0s+)
        if t >= 6.0:
            draw.rectangle([0, 1660, 1080, 1920], fill=(12, 16, 24))
            draw.line([(0, 1660), (1080, 1660)], fill=(255, 184, 0), width=3)
            draw.rounded_rectangle([60, 1690, 1020, 1840], radius=18, fill=(26, 22, 15), outline=(255, 184, 0), width=4)
            draw.text((100, 1720), "👉 COMMENT \"P6\" BELOW", font=get_font(42, bold=True), fill=(255, 255, 255))
            draw.text((100, 1780), "I'll DM you my Primavera P6 AI Schedule Health Playbook!", font=get_font(22, bold=False), fill=(255, 184, 0))
            draw.text((290, 1870), "⚡ proengineering.in | Senior Project Controls Lead", font=get_font(20, bold=False), fill=(180, 200, 220))
            
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print(f"P6 AI Demo Video saved: {out_mp4}")

if __name__ == "__main__":
    v1 = os.path.join(REELS_DIR, "reel_live_demo_01_substation.mp4")
    v2 = os.path.join(REELS_DIR, "reel_live_demo_02_p6_ai.mp4")
    render_demo_substation(v1)
    render_demo_p6_ai(v2)
    print("Both live demonstration videos generated successfully!")
