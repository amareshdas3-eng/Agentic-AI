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

def ease_out_bounce(x):
    """Spring bounce easing for popping elements onto the screen"""
    n1 = 7.5625
    d1 = 2.75
    if x < 1 / d1:
        return n1 * x * x
    elif x < 2 / d1:
        x -= 1.5 / d1
        return n1 * x * x + 0.75
    elif x < 2.5 / d1:
        x -= 2.25 / d1
        return n1 * x * x + 0.9375
    else:
        x -= 2.625 / d1
        return n1 * x * x + 0.984375

def render_human_touch_reel(duration_sec=8, fps=30):
    out_path = os.path.join(REELS_DIR, "reel_human_touch_spec_trap.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (1080, 1920))
    total_frames = int(duration_sec * fps)
    
    # Load user portrait photo
    if os.path.exists(USER_PHOTO_PATH):
        user_img_raw = Image.open(USER_PHOTO_PATH).convert("RGBA")
    else:
        # Fallback if file missing
        user_img_raw = Image.new("RGBA", (400, 500), (40, 50, 70))
        
    f_hook = get_font(52, bold=True)
    f_badge = get_font(30, bold=True)
    f_body = get_font(26, bold=False)
    f_stat = get_font(44, bold=True)
    
    print(f"Rendering Fast-Paced Human-Touch Reel ({total_frames} frames)...")
    
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        t_frac = frame_idx / total_frames
        
        # Base dark high-tech background
        img = Image.new("RGB", (1080, 1920), (11, 15, 22))
        draw = ImageDraw.Draw(img)
        
        # Grid lines in background
        for gx in range(0, 1080, 60):
            draw.line([(gx, 0), (gx, 1920)], fill=(18, 24, 34), width=1)
        for gy in range(0, 1920, 60):
            draw.line([(0, gy), (1080, gy)], fill=(18, 24, 34), width=1)
            
        # Top 100% Progress Bar (Hormozi/MrBeast style retention indicator)
        prog_w = int(t_frac * 1080)
        draw.rectangle([0, 0, prog_w, 12], fill=(0, 242, 254))
        
        # Top Header Bar
        draw.rectangle([0, 12, 1080, 130], fill=(16, 22, 32))
        draw.line([(0, 130), (1080, 130)], fill=(0, 242, 254), width=2)
        draw.text((50, 42), "⚡ PROENGINEERING", font=get_font(32, bold=True), fill=(0, 242, 254))
        draw.text((50, 82), "23+ YRS SUBSTATIONS & INDUSTRIAL AI", font=get_font(20, bold=False), fill=(200, 220, 240))
        
        # Authority Tag Pill
        draw.rounded_rectangle([720, 40, 1030, 95], radius=10, fill=(24, 34, 48), outline=(255, 184, 0), width=2)
        draw.text((750, 52), "FIELD REALITY", font=get_font(22, bold=True), fill=(255, 184, 0))
        
        # =========================================================================
        # USER PHOTO - AUTHENTIC HUMAN AUTHORITY PRESENCE
        # =========================================================================
        # Camera Punch-In Cuts:
        # 0.0s - 2.4s: Normal framing (1.0x)
        # 2.4s - 4.8s: Punch-in Cut (1.12x zoom for high drama)
        # 4.8s - 8.0s: Wide framing with tech badge
        if 2.4 <= t < 4.8:
            zoom_factor = 1.12
        else:
            zoom_factor = 1.0
            
        base_w, base_h = 420, 520
        target_w = int(base_w * zoom_factor)
        target_h = int(base_h * zoom_factor)
        
        photo_resized = user_img_raw.resize((target_w, target_h), Image.Resampling.LANCZOS)
        
        # Oval or rounded executive portrait card
        cx = 540
        cy = 440
        px0 = cx - target_w // 2
        py0 = cy - target_h // 2
        
        # Glowing frame behind user photo
        pulse = (math.sin(t * 8) + 1) / 2
        glow_c = (int(0 + 40 * pulse), int(220 + 35 * pulse), 254)
        draw.rounded_rectangle([px0 - 8, py0 - 8, px0 + target_w + 8, py0 + target_h + 8], radius=24, outline=glow_c, width=4)
        
        # Paste user portrait
        img.paste(photo_resized, (px0, py0))
        
        # Presenter Name Plate Banner
        draw.rounded_rectangle([cx - 240, py0 + target_h - 40, cx + 240, py0 + target_h + 15], radius=10, fill=(13, 17, 23), outline=(0, 242, 254), width=2)
        draw.text((cx - 210, py0 + target_h - 32), "SENIOR POWER SYSTEMS & AI LEAD", font=get_font(20, bold=True), fill=(0, 242, 254))
        
        # =========================================================================
        # POPUP 1 (0.0s+): HOOK BANNER (Bounces in at start)
        # =========================================================================
        draw.rounded_rectangle([50, 740, 1030, 890], radius=16, fill=(24, 18, 22), outline=(255, 75, 75), width=3)
        draw.text((80, 765), "THE $400K EPC SPEC TRAP", font=f_hook, fill=(255, 75, 75))
        draw.text((80, 835), "1 Sentence That Destroys Contractor Margin", font=get_font(26, bold=False), fill=(255, 255, 255))
        
        # =========================================================================
        # POPUP 2 (0.8s+): RED ALERT STAMP
        # =========================================================================
        if t >= 0.8:
            pop_progress = min((t - 0.8) / 0.25, 1.0)
            scale = ease_out_bounce(pop_progress)
            bw = int(980 * scale)
            bh = int(110 * scale)
            if bw > 20 and bh > 20:
                bx0 = 540 - bw // 2
                by0 = 920
                draw.rounded_rectangle([bx0, by0, bx0 + bw, by0 + bh], radius=12, fill=(45, 15, 20), outline=(255, 60, 60), width=3)
                if scale > 0.8:
                    draw.text((bx0 + 30, by0 + 20), "⚠ CSI SPECIFICATION CONFLICT DETECTED!", font=f_badge, fill=(255, 80, 80))
                    draw.text((bx0 + 30, by0 + 65), "Section 26 13 00 vs Tender Single-Line Diagram", font=f_body, fill=(240, 210, 210))
                    
        # =========================================================================
        # POPUP 3 (1.6s+): CSI SPEC HIGHLIGHT CARD
        # =========================================================================
        if t >= 1.6:
            pop_progress = min((t - 1.6) / 0.25, 1.0)
            scale = ease_out_bounce(pop_progress)
            cw = int(980 * scale)
            ch = int(120 * scale)
            if cw > 20 and ch > 20:
                cx0 = 540 - cw // 2
                cy0 = 1050
                draw.rounded_rectangle([cx0, cy0, cx0 + cw, cy0 + ch], radius=12, fill=(20, 28, 42), outline=(0, 242, 254), width=2)
                if scale > 0.8:
                    draw.text((cx0 + 30, cy0 + 20), "📄 CLAUSE 26 13 00.32: 40 kA FOR 3 SECONDS", font=f_badge, fill=(0, 242, 254))
                    draw.text((cx0 + 30, cy0 + 65), "Mandates heavy busbar bracing & 40kA VCBs (Not priced in BOQ!)", font=f_body, fill=(220, 240, 255))

        # =========================================================================
        # POPUP 4 (2.4s+): SLD COMPARISON TAG
        # =========================================================================
        if t >= 2.4:
            pop_progress = min((t - 2.4) / 0.25, 1.0)
            scale = ease_out_bounce(pop_progress)
            dw = int(980 * scale)
            dh = int(120 * scale)
            if dw > 20 and dh > 20:
                dx0 = 540 - dw // 2
                dy0 = 1190
                draw.rounded_rectangle([dx0, dy0, dx0 + dw, dy0 + dh], radius=12, fill=(35, 28, 15), outline=(255, 184, 0), width=2)
                if scale > 0.8:
                    draw.text((dx0 + 30, dy0 + 20), "⚡ TENDER SLD SPECIFIES ONLY 31.5 kA (1s)", font=f_badge, fill=(255, 184, 0))
                    draw.text((dx0 + 30, dy0 + 65), "Dynamic short-circuit force increases by 61% (I_peak squared)!", font=f_body, fill=(255, 240, 200))

        # =========================================================================
        # POPUP 5 (3.6s+): $400,000 FINANCIAL DAMAGE STAMP (Slams onto screen)
        # =========================================================================
        if t >= 3.6:
            pop_progress = min((t - 3.6) / 0.2, 1.0)
            scale = ease_out_bounce(pop_progress)
            ew = int(980 * scale)
            eh = int(140 * scale)
            if ew > 20 and eh > 20:
                ex0 = 540 - ew // 2
                ey0 = 1330
                draw.rounded_rectangle([ex0, ey0, ex0 + ew, ey0 + eh], radius=15, fill=(40, 10, 15), outline=(255, 50, 50), width=4)
                if scale > 0.8:
                    draw.text((ex0 + 40, ey0 + 25), "💥 $400,000 SWITCHGEAR CHANGE ORDER!", font=f_stat, fill=(255, 70, 70))
                    draw.text((ex0 + 40, ey0 + 85), "Wipes out 100% of contractor gross profit before mobilization.", font=f_body, fill=(255, 220, 220))

        # =========================================================================
        # POPUP 6 (4.8s+): AGENTIC AI & FIELD REMEDIATION SHIELD
        # =========================================================================
        if t >= 4.8:
            pop_progress = min((t - 4.8) / 0.25, 1.0)
            scale = ease_out_bounce(pop_progress)
            fw = int(980 * scale)
            fh = int(120 * scale)
            if fw > 20 and fh > 20:
                fx0 = 540 - fw // 2
                fy0 = 1490
                draw.rounded_rectangle([fx0, fy0, fx0 + fw, fy0 + fh], radius=12, fill=(15, 35, 25), outline=(0, 255, 140), width=3)
                if scale > 0.8:
                    draw.text((fx0 + 30, fy0 + 20), "🛡 AGENTIC AI PRE-BID SPEC AUDIT", font=f_badge, fill=(0, 255, 140))
                    draw.text((fx0 + 30, fy0 + 65), "Automated Spec-vs-Drawing audit detects contradiction in 20s.", font=f_body, fill=(220, 255, 235))

        # =========================================================================
        # POPUP 7 (6.0s+): CALL TO ACTION & KEYWORD TRIGGER
        # =========================================================================
        if t >= 6.0:
            pulse_cta = (math.sin(t * 10) + 1) / 2
            glow_cta = (int(0 + 40 * pulse_cta), int(220 + 35 * pulse_cta), int(250 + 5 * pulse_cta))
            
            draw.rectangle([0, 1640, 1080, 1920], fill=(13, 17, 23))
            draw.line([(0, 1640), (1080, 1640)], fill=(0, 242, 254), width=3)
            
            draw.rounded_rectangle([60, 1670, 1020, 1820], radius=18, fill=(20, 26, 38), outline=glow_cta, width=4)
            draw.text((110, 1705), "👉 COMMENT \"SPEC\" BELOW", font=get_font(42, bold=True), fill=(255, 255, 255))
            draw.text((110, 1765), "I'll DM you my 33kV Pre-Bid Spec Checklist & Audit Matrix!", font=get_font(24, bold=False), fill=(0, 242, 254))
            draw.text((280, 1855), "⚡ Field-Tested by Senior Power Lead | proengineering.in", font=get_font(20, bold=False), fill=(180, 200, 220))
        else:
            # Baseline animated bottom telemetry
            draw.rectangle([0, 1760, 1080, 1920], fill=(13, 17, 23))
            wave_y = 1840
            for wx in range(60, 1020, 12):
                wy = int(15 * math.sin((wx / 35.0) + (t * 9.0)))
                draw.line([(wx, wave_y + wy), (wx + 8, wave_y + wy)], fill=(0, 242, 254), width=2)
                
        # Convert PIL Image to OpenCV BGR frame
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print(f"Rendered Human-Touch Fast-Paced Reel: {out_path}")
    return out_path

if __name__ == "__main__":
    render_human_touch_reel()

