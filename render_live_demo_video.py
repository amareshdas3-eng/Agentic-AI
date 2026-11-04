import os
import math
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Local sound generator
from generate_pop_sfx import build_synchronized_soundtrack

REELS_DIR = "d:/instagram/reels"
ASSETS_DIR = "d:/instagram/assets"
USER_PHOTO_PATH = os.path.join(ASSETS_DIR, "user_photo.jpg")
os.makedirs(REELS_DIR, exist_ok=True)

def get_font(size, bold=False):
    font_names = ["arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf", "consola.ttf"]
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()

def render_live_demonstration_video(duration_sec=8, fps=30):
    out_path = os.path.join(REELS_DIR, "reel_live_substation_demo.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (1080, 1920))
    total_frames = int(duration_sec * fps)
    
    # Load user authentic photo
    if os.path.exists(USER_PHOTO_PATH):
        raw_user_img = Image.open(USER_PHOTO_PATH).convert("RGBA")
    else:
        raw_user_img = Image.new("RGBA", (400, 500), (30, 45, 65))
        
    f_hook = get_font(48, bold=True)
    f_title = get_font(32, bold=True)
    f_badge = get_font(24, bold=True)
    f_body = get_font(22, bold=False)
    f_val = get_font(36, bold=True)
    
    print(f"[LIVE DEMO] Rendering Live Demonstration Video ({total_frames} frames)...")
    
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        t_frac = frame_idx / total_frames
        
        img = Image.new("RGB", (1080, 1920), (10, 14, 20))
        draw = ImageDraw.Draw(img)
        
        # Cyber-industrial animated grid
        grid_offset = int((t * 25) % 50)
        for gx in range(0, 1080, 50):
            draw.line([(gx, 0), (gx, 1920)], fill=(16, 22, 32), width=1)
        for gy in range(grid_offset, 1920, 50):
            draw.line([(0, gy), (1080, gy)], fill=(16, 22, 32), width=1)
            
        # Top Retention Progress Bar
        draw.rectangle([0, 0, int(t_frac * 1080), 12], fill=(0, 242, 254))
        
        # Header Status Bar
        draw.rectangle([0, 12, 1080, 130], fill=(15, 20, 30))
        draw.line([(0, 130), (1080, 130)], fill=(0, 242, 254), width=2)
        draw.text((50, 40), "⚡ PROENGINEERING LIVE LAB", font=get_font(28, bold=True), fill=(0, 242, 254))
        draw.text((50, 80), "LIVE FIELD DEMONSTRATION & AI DIAGNOSTIC", font=get_font(18, bold=False), fill=(200, 220, 240))
        
        # LIVE Broadcast Indicator (Blinking Red Dot)
        blink = (math.sin(t * 6) + 1) / 2
        if blink > 0.3:
            draw.ellipse([920, 52, 940, 72], fill=(255, 40, 40))
        draw.text((950, 50), "LIVE", font=get_font(22, bold=True), fill=(255, 60, 60))
        
        # =====================================================================
        # 1. LIVE ANIMATED PRESENTER FROM USER PHOTOGRAPH
        # =====================================================================
        # Dynamic subtle breathing scale + Camera Cuts:
        # Shot 1 (0.0s - 2.5s): Normal establishing shot (1.0x)
        # Shot 2 (2.5s - 5.0s): Dramatic punch-in zoom (1.12x)
        # Shot 3 (5.0s - 8.0s): Side-by-side demonstration angle
        breath = 1.0 + 0.015 * math.sin(t * 3.5) # subtle natural life breathing
        camera_zoom = 1.12 if (2.5 <= t < 5.0) else 1.0
        final_scale = breath * camera_zoom
        
        uw, uh = int(340 * final_scale), int(430 * final_scale)
        u_scaled = raw_user_img.resize((uw, uh), Image.Resampling.LANCZOS)
        
        # Position user photo
        if t < 5.0:
            ux, uy = 540 - uw // 2, 380 - uh // 2
        else:
            # Shift slightly to left in Shot 3 to give stage to live demonstration
            ux, uy = 280 - uw // 2, 380 - uh // 2
            
        # Glowing holographic portrait border with rotating telemetry ticks
        pulse = (math.sin(t * 8) + 1) / 2
        glow_color = (int(0 + 30 * pulse), int(220 + 35 * pulse), 254)
        draw.rounded_rectangle([ux - 6, uy - 6, ux + uw + 6, uy + uh + 6], radius=20, outline=glow_color, width=3)
        img.paste(u_scaled, (ux, uy))
        
        # Name Plate
        draw.rounded_rectangle([ux + 20, uy + uh - 30, ux + uw - 20, uy + uh + 18], radius=8, fill=(11, 15, 22), outline=(0, 242, 254), width=2)
        draw.text((ux + 35, uy + uh - 24), "AMARESH DAS | 23+ YRS LEAD", font=get_font(18, bold=True), fill=(0, 242, 254))
        
        # =====================================================================
        # 2. DEMONSTRATION STAGE (MIDDLE / LOWER FRAME)
        # =====================================================================
        # Topic Hook Banner (0.0s - 2.5s)
        draw.rounded_rectangle([50, 640, 1030, 780], radius=14, fill=(20, 25, 36), outline=(255, 184, 0), width=3)
        draw.text((80, 660), "DEMONSTRATING: ZERO-TRIP 33kV ENERGIZATION", font=f_hook, fill=(255, 184, 0))
        draw.text((80, 725), "Live 87T Differential Relay Vector & Inrush Compensation", font=get_font(22, bold=False), fill=(240, 240, 240))
        
        # =====================================================================
        # LIVE INTERACTIVE INSTRUMENT GAUGES & SIMULATION (y=810 to y=1620)
        # =====================================================================
        # Card 1: 33kV Substation Current Waveform & Restraint Meter
        draw.rounded_rectangle([50, 800, 1030, 1200], radius=16, fill=(16, 22, 32), outline=(0, 242, 254), width=2)
        draw.text((80, 825), "LIVE OMICRON SECONDARY INJECTION SIMULATOR", font=f_title, fill=(0, 242, 254))
        draw.line([(80, 875), (1000, 875)], fill=(30, 42, 60), width=1)
        
        # Live current ramp simulation (0.0A -> 5.2A)
        sim_current = min(t * 0.75, 5.2)
        draw.text((80, 900), "SECONDARY CURRENT (If):", font=f_badge, fill=(200, 220, 240))
        draw.text((80, 935), f"{sim_current:.2f} A (Ramped)", font=f_val, fill=(0, 255, 140))
        
        # Live 2nd Harmonic Inrush Restraint Status
        draw.text((580, 900), "2nd-HARMONIC RESTRAINT:", font=f_badge, fill=(200, 220, 240))
        if t < 3.5:
            draw.text((580, 935), "DISABLED (0%) -> 87T TRIP!", font=f_val, fill=(255, 60, 60))
        else:
            draw.text((580, 935), "ACTIVE @ 15% -> RESTRAINED!", font=f_val, fill=(0, 255, 140))
            
        # Live Animated Sine Wave Oscilloscope
        wave_y = 1080
        draw.rectangle([80, 1000, 1000, 1160], fill=(8, 12, 18), outline=(30, 45, 65), width=2)
        draw.line([(80, wave_y), (1000, wave_y)], fill=(35, 50, 70), width=1)
        
        for wx in range(80, 1000, 4):
            # Phase A fundamental (50Hz) + simulated 2nd harmonic (100Hz)
            phase = (wx / 25.0) + (t * 12.0)
            h2_amp = 30 if t < 3.5 else 6
            wy1 = int(45 * math.sin(phase) + h2_amp * math.sin(2 * phase))
            draw.line([(wx, wave_y + wy1), (wx + 4, wave_y + wy1)], fill=(0, 242, 254), width=2)
            
        draw.text((100, 1010), "TEKTRONIX DIGITAL OSCILLOSCOPE (PHASE-A INRUSH CURRENT)", font=get_font(16, bold=True), fill=(140, 160, 180))
        
        # Card 2: Live Diagnostic Checklist Popups
        draw.rounded_rectangle([50, 1220, 1030, 1620], radius=16, fill=(16, 22, 32), outline=(255, 184, 0), width=2)
        draw.text((80, 1245), "REAL-TIME COMMISSIONING VERIFICATION STEPS", font=f_title, fill=(255, 184, 0))
        
        demo_steps = [
            ("1. Dyn11 Vector Group", "Confirmed 30° phase displacement compensation", 1.2),
            ("2. CT Knee-Point Vk >= 400V", "Verified Vk >= 2 * If * (Rct + 2*RL + Rr)", 2.8),
            ("3. Single-Point Star Ground", "Substation CT neutral grounded at panel only", 4.4),
            ("4. VCB Millisecond Timing", "Closing <60ms, Opening <45ms, Bounce <3ms", 5.8)
        ]
        
        sy = 1300
        for s_title, s_desc, start_t in demo_steps:
            if t >= start_t:
                draw.rounded_rectangle([80, sy, 1000, sy + 65], radius=8, fill=(22, 32, 45), outline=(0, 255, 140), width=2)
                draw.text((100, sy + 12), f"✔ {s_title}:", font=f_badge, fill=(0, 255, 140))
                draw.text((100, sy + 38), s_desc, font=f_body, fill=(220, 235, 245))
            else:
                draw.rounded_rectangle([80, sy, 1000, sy + 65], radius=8, fill=(14, 18, 26), outline=(30, 40, 55), width=1)
                draw.text((100, sy + 20), f"⏳ PENDING TEST: {s_title}...", font=f_body, fill=(80, 100, 120))
            sy += 75
            
        # =====================================================================
        # 3. CALL TO ACTION (6.2s+)
        # =====================================================================
        if t >= 6.2:
            draw.rectangle([0, 1660, 1080, 1920], fill=(12, 16, 24))
            draw.line([(0, 1660), (1080, 1660)], fill=(0, 242, 254), width=3)
            
            draw.rounded_rectangle([60, 1690, 1020, 1840], radius=18, fill=(20, 28, 42), outline=(0, 255, 140), width=4)
            draw.text((100, 1720), "👉 COMMENT \"DEMO\" BELOW", font=get_font(42, bold=True), fill=(255, 255, 255))
            draw.text((100, 1780), "I'll DM you the complete 33kV Commissioning & Relay Test Protocol!", font=get_font(22, bold=False), fill=(0, 242, 254))
            draw.text((290, 1870), "⚡ proengineering.in | Senior Power Systems Lead", font=get_font(20, bold=False), fill=(180, 200, 220))
        else:
            draw.rectangle([0, 1780, 1080, 1920], fill=(12, 16, 24))
            draw.text((310, 1840), "⚡ LIVE LAB DEMONSTRATION | PROENGINEERING", font=get_font(20, bold=True), fill=(100, 120, 145))
            
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print(f"[SUCCESS] Live Demonstration Video Rendered: {out_path}")
    return out_path

if __name__ == "__main__":
    render_live_demonstration_video()
