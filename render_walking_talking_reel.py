import os
import math
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

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

def create_walking_talking_frame(user_img, t, is_talking=True):
    """
    Transforms the still portrait into an animated walking, talking presenter:
    1. Walking Gait: Vertical sinusoidal bobbing (2 steps/sec) + lateral shoulder tilt.
    2. Talking Lip-Sync: Natural lower-face/jaw articulation based on speech phoneme frequency.
    """
    # Clone image
    frame_user = user_img.copy()
    w, h = frame_user.size
    
    # ------------------ TALKING ANIMATION (LIP-SYNC & JAW) ------------------
    if is_talking:
        # Mouth & Jaw region coordinates in the original 413x531 photo
        # Mouth center approx x=206, y=295
        mx0, my0, mx1, my1 = 175, 275, 245, 335
        mouth_crop = frame_user.crop((mx0, my0, mx1, my1))
        
        # Talking mouth aperture modulation (3 to 6 syllables per second)
        syllable_osc = abs(math.sin(t * 14.0)) * (0.6 + 0.4 * math.sin(t * 22.0))
        jaw_drop = int(syllable_osc * 10) # 0 to 10 pixels vertical stretch
        
        if jaw_drop > 1:
            mw, mh = mouth_crop.size
            stretched_mouth = mouth_crop.resize((mw, mh + jaw_drop), Image.Resampling.LANCZOS)
            # Create dark inner oral cavity gap
            draw_mouth = ImageDraw.Draw(stretched_mouth)
            gap_h = int(jaw_drop * 0.6)
            gy = int(mh * 0.4)
            draw_mouth.ellipse([int(mw * 0.35), gy, int(mw * 0.65), gy + gap_h], fill=(45, 18, 22, 220))
            
            # Composite animated mouth back onto face
            frame_user.paste(stretched_mouth, (mx0, my0))
            
    # ------------------ WALKING ANIMATION (GAIT & TILT) ------------------
    # Step frequency: ~1.8 Hz (walking cadence)
    walk_cycle = t * 1.8 * math.pi * 2
    vertical_bob = int(14 * abs(math.sin(walk_cycle))) # 0 to 14px up and down
    lateral_sway = 2.4 * math.sin(walk_cycle / 2)       # -2.4 to +2.4 deg shoulder roll
    
    # Rotate for shoulder sway
    rotated_user = frame_user.rotate(lateral_sway, resample=Image.Resampling.BICUBIC, expand=False)
    
    return rotated_user, vertical_bob

def render_walking_talking_reel(duration_sec=8, fps=30):
    out_path = os.path.join(REELS_DIR, "reel_walking_talking_engineer.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (1080, 1920))
    total_frames = int(duration_sec * fps)
    
    user_img = Image.open(USER_PHOTO_PATH).convert("RGBA") if os.path.exists(USER_PHOTO_PATH) else Image.new("RGBA", (400, 500), (30, 45, 65))
    
    f_hook = get_font(50, bold=True)
    f_speech = get_font(34, bold=True)
    f_badge = get_font(26, bold=True)
    f_body = get_font(22, bold=False)
    
    print(f"[WALKING & TALKING] Rendering 1080x1920 Reel ({total_frames} frames)...")
    
    # Speech script line bursts for kinetic subtitles
    script_cues = [
        (0.0, 2.0, "I'm walking through a 33kV switchyard right now..."),
        (2.0, 4.0, "And FAT test certificates DO NOT stop site trips!"),
        (4.0, 6.0, "If your 87T differential relay trips on Day-1 soak..."),
        (6.0, 8.0, "Check your Dyn11 vector compensation & 2nd-harmonic restraint!")
    ]
    
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        t_frac = frame_idx / total_frames
        
        img = Image.new("RGB", (1080, 1920), (10, 15, 24))
        draw = ImageDraw.Draw(img)
        
        # =========================================================================
        # 1. MOVING PARALLAX BACKGROUND (WALKING THROUGH SWITCHYARD)
        # =========================================================================
        # Perspective floor grid rushing backwards to simulate walking forward
        speed = t * 160
        for gx in range(0, 1080, 70):
            draw.line([(gx, 0), (gx, 1920)], fill=(16, 24, 38), width=1)
        for gy in range(int(speed % 70), 1920, 70):
            # Ground grid lines moving down
            draw.line([(0, gy), (1080, gy)], fill=(20, 32, 50), width=1)
            
        # Top Retention Progress Bar
        draw.rectangle([0, 0, int(t_frac * 1080), 12], fill=(0, 242, 254))
        
        # Header Status Bar
        draw.rectangle([0, 12, 1080, 130], fill=(14, 20, 32))
        draw.line([(0, 130), (1080, 130)], fill=(0, 242, 254), width=2)
        draw.text((50, 42), "⚡ PROENGINEERING SITE WALK", font=get_font(28, bold=True), fill=(0, 242, 254))
        draw.text((50, 82), "WALKING & TALKING | 33kV SUBSTATION COMMISSIONING", font=get_font(18, bold=False), fill=(200, 220, 240))
        
        # Rec Icon
        draw.ellipse([930, 52, 948, 70], fill=(255, 50, 50))
        draw.text((958, 50), "REC", font=get_font(20, bold=True), fill=(255, 70, 70))
        
        # =========================================================================
        # 2. WALKING & TALKING USER ANIMATION
        # =========================================================================
        animated_user, vert_bob = create_walking_talking_frame(user_img, t, is_talking=True)
        
        # Walking forward dolly zoom (scale grows naturally as you walk towards camera)
        # Cuts back at 4.0s for dramatic multi-angle effect
        if t < 4.0:
            walk_scale = 1.0 + (t * 0.04) # smooth forward movement
        else:
            walk_scale = 1.05 + ((t - 4.0) * 0.035)
            
        uw = int(380 * walk_scale)
        uh = int(490 * walk_scale)
        u_scaled = animated_user.resize((uw, uh), Image.Resampling.LANCZOS)
        
        # Position with walking bobbing
        base_y = 380 - uh // 2
        ux = 540 - uw // 2
        uy = base_y + vert_bob # vertical walking gait bobbing
        
        # Glowing executive frame
        pulse = (math.sin(t * 8) + 1) / 2
        glow_c = (int(0 + 35 * pulse), int(220 + 35 * pulse), 254)
        draw.rounded_rectangle([ux - 8, uy - 8, ux + uw + 8, uy + uh + 8], radius=22, outline=glow_c, width=4)
        img.paste(u_scaled, (ux, uy))
        
        # Presenter Badge
        draw.rounded_rectangle([ux + 30, uy + uh - 25, ux + uw - 30, uy + uh + 18], radius=8, fill=(11, 15, 22), outline=(0, 242, 254), width=2)
        draw.text((ux + 45, uy + uh - 20), "AMARESH DAS | 23+ YRS LEAD", font=get_font(18, bold=True), fill=(0, 242, 254))
        
        # =========================================================================
        # 3. KINETIC TALKING SPEECH BUBBLE & SUBTITLES
        # =========================================================================
        # Determine current spoken subtitle
        active_text = ""
        for st, et, txt in script_cues:
            if st <= t < et:
                active_text = txt
                break
                
        # High-Impact Talking Subtitle Box
        draw.rounded_rectangle([60, 680, 1020, 830], radius=16, fill=(20, 28, 42), outline=(255, 184, 0), width=3)
        draw.text((90, 705), "🗣 SPEAKING LIVE FROM SWITCHYARD:", font=get_font(20, bold=True), fill=(255, 184, 0))
        draw.text((90, 745), f"\"{active_text}\"", font=f_speech, fill=(255, 255, 255))
        
        # =========================================================================
        # 4. DEMONSTRATION POPUPS IN REAL TIME (y=860 to y=1620)
        # =========================================================================
        # Card 1: 33kV Transformer Bay Live Simulation
        draw.rounded_rectangle([50, 860, 1030, 1220], radius=16, fill=(16, 22, 32), outline=(0, 242, 254), width=2)
        draw.text((80, 885), "LIVE DEMONSTRATION: TRANSFORMER 87T DIFFERENTIAL TEST", font=f_badge, fill=(0, 242, 254))
        
        # Live Current Meter
        cur_val = min(t * 0.7, 5.0)
        draw.text((80, 935), f"SECONDARY TEST CURRENT: {cur_val:.2f} A", font=get_font(24, bold=True), fill=(0, 255, 140))
        
        # Oscilloscope Waveform with walking motion
        osc_y = 1080
        draw.rectangle([80, 980, 1000, 1180], fill=(8, 12, 18), outline=(30, 45, 65), width=2)
        draw.line([(80, osc_y), (1000, osc_y)], fill=(30, 45, 65), width=1)
        for ox in range(80, 1000, 4):
            phase = (ox / 24.0) + (t * 15.0)
            oy = int(38 * math.sin(phase) + 12 * math.sin(2 * phase))
            draw.line([(ox, osc_y + oy), (ox + 4, osc_y + oy)], fill=(0, 242, 254), width=2)
        draw.text((100, 995), "LIVE CT SECONDARY INJECTION WAVEFORM", font=get_font(16, bold=True), fill=(140, 170, 200))

        # Card 2: 4-Step Field Commissioning Verification
        draw.rounded_rectangle([50, 1250, 1030, 1630], radius=16, fill=(16, 22, 32), outline=(255, 184, 0), width=2)
        draw.text((80, 1275), "CRITICAL COMMISSIONING CHECKS (DEMONSTRATED ON SITE):", font=f_badge, fill=(255, 184, 0))
        
        checks = [
            ("1. Dyn11 Vector Group", "30° software compensation verified in MiCOM P643", 1.5),
            ("2. CT Knee-Point Vk", "Vk >= 2 * If * (Rct + 2*RL + Rr) calculation verified at 480V", 3.0),
            ("3. Single Star Point", "Isolated switchyard neutral; grounded at relay panel only", 4.5),
            ("4. VCB Timing Test", "Opening time: 38ms | Bounce: 1.8ms (ZERO-TRIP PASS)", 6.0)
        ]
        
        y_pos = 1325
        for c_title, c_desc, ct in checks:
            if t >= ct:
                draw.rounded_rectangle([80, y_pos, 1000, y_pos + 64], radius=8, fill=(20, 32, 45), outline=(0, 255, 140), width=2)
                draw.text((100, y_pos + 10), f"✔ {c_title}:", font=f_badge, fill=(0, 255, 140))
                draw.text((100, y_pos + 36), c_desc, font=f_body, fill=(230, 240, 250))
            else:
                draw.rounded_rectangle([80, y_pos, 1000, y_pos + 64], radius=8, fill=(12, 16, 24), outline=(30, 42, 55), width=1)
                draw.text((100, y_pos + 20), f"⏳ VERIFYING: {c_title}...", font=f_body, fill=(90, 110, 130))
            y_pos += 72
            
        # =========================================================================
        # 5. CALL TO ACTION (6.5s+)
        # =========================================================================
        if t >= 6.5:
            draw.rectangle([0, 1660, 1080, 1920], fill=(12, 16, 24))
            draw.line([(0, 1660), (1080, 1660)], fill=(0, 242, 254), width=3)
            draw.rounded_rectangle([60, 1690, 1020, 1840], radius=18, fill=(20, 28, 42), outline=(0, 255, 140), width=4)
            draw.text((100, 1720), "👉 COMMENT \"WALK\" BELOW", font=get_font(42, bold=True), fill=(255, 255, 255))
            draw.text((100, 1780), "I'll DM you my 33kV Substation Commissioning & Relay Guide!", font=get_font(22, bold=False), fill=(0, 242, 254))
            draw.text((290, 1870), "⚡ proengineering.in | Senior Power Systems Lead", font=get_font(20, bold=False), fill=(180, 200, 220))
        else:
            draw.rectangle([0, 1780, 1080, 1920], fill=(12, 16, 24))
            draw.text((310, 1840), "⚡ LIVE LAB DEMONSTRATION | PROENGINEERING", font=get_font(20, bold=True), fill=(100, 120, 145))
            
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print(f"[SUCCESS] Walking & Talking Reel rendered at: {out_path}")
    return out_path

if __name__ == "__main__":
    render_walking_talking_reel()
