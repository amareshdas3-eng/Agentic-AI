import os
import math
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

REELS_DIR = "d:/instagram/reels"
ASSETS_DIR = "d:/instagram/assets"
os.makedirs(REELS_DIR, exist_ok=True)

def get_font(size, bold=False):
    font_names = ["arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf", "consola.ttf"]
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()

def draw_top_brand_bar(draw, current_pillar):
    # Top brand bar
    draw.rectangle([0, 0, 1080, 140], fill=(13, 17, 23))
    draw.line([(0, 140), (1080, 140)], fill=(0, 242, 254), width=3)
    
    f_brand = get_font(34, bold=True)
    f_sub = get_font(22, bold=False)
    f_pil = get_font(20, bold=True)
    
    draw.text((50, 35), "⚡ PROENGINEERING", font=f_brand, fill=(0, 242, 254))
    draw.text((50, 80), "23+ YRS INDUSTRIAL AI & MEGACAPEX", font=f_sub, fill=(200, 220, 240))
    
    # Pillar tag pill
    draw.rounded_rectangle([720, 45, 1030, 95], radius=10, fill=(25, 35, 50), outline=(255, 184, 0), width=2)
    draw.text((740, 58), current_pillar, font=f_pil, fill=(255, 184, 0))

def draw_bottom_cta_bar(draw, keyword, t_frac):
    # Bottom CTA bar with pulsing animation
    draw.rectangle([0, 1720, 1080, 1920], fill=(13, 17, 23))
    draw.line([(0, 1720), (1080, 1720)], fill=(255, 184, 0), width=3)
    
    pulse = (math.sin(t_frac * 2 * math.pi * 3) + 1) / 2 # 0 to 1
    glow_color = (int(0 + 50 * pulse), int(200 + 42 * pulse), int(220 + 34 * pulse))
    
    f_cta_main = get_font(42, bold=True)
    f_cta_sub = get_font(24, bold=False)
    
    # CTA button box
    draw.rounded_rectangle([80, 1760, 1000, 1860], radius=18, fill=(22, 27, 34), outline=glow_color, width=4)
    cta_text = f"COMMENT \"{keyword}\" FOR CHECKLIST"
    draw.text((130, 1785), cta_text, font=f_cta_main, fill=(255, 255, 255))
    draw.text((250, 1875), "⚡ Field-Tested by Senior Power Systems Lead | proengineering.in", font=f_cta_sub, fill=(180, 200, 220))

def render_reel_01(duration_sec=8, fps=30):
    # Reel 1: AI Spec Trap Workflow
    out_path = os.path.join(REELS_DIR, "reel_01_spec_trap.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (1080, 1920))
    
    total_frames = int(duration_sec * fps)
    f_hook = get_font(52, bold=True)
    f_sub = get_font(30, bold=False)
    f_card_t = get_font(32, bold=True)
    f_card_d = get_font(22, bold=False)
    
    steps = [
        ("STEP 1: CSI DIVISION 26 INGESTION", "AI ingests 300-page EPC electrical tender spec in 4.2 seconds.", (0, 242, 254)),
        ("STEP 2: FAULT-LEVEL CONTRADICTION", "BOQ specifies 31.5 kA (1s), but Section 26 13 00 mandates 40 kA (3s).", (255, 75, 75)),
        ("STEP 3: SLD CONFORMANCE AUDIT", "Tender SLD conflicts with switchgear physical trench layout.", (255, 184, 0)),
        ("STEP 4: AUTOMATED RFI & SAVING", "$400,000 contractor margin protected before bid submission.", (0, 255, 140))
    ]
    
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        t_frac = frame_idx / total_frames
        
        img = Image.new("RGB", (1080, 1920), (13, 17, 23))
        draw = ImageDraw.Draw(img)
        
        draw_top_brand_bar(draw, "FORENSIC TEARDOWN")
        
        # Hook Header (Top area)
        draw.rounded_rectangle([50, 180, 1030, 380], radius=15, fill=(22, 27, 34), outline=(255, 75, 75), width=3)
        draw.text((80, 210), "THE $400K EPC SPEC TRAP", font=f_hook, fill=(255, 75, 75))
        draw.text((80, 280), "How 1 Missed Spec Sentence Wipes Out Contractor Margin", font=f_sub, fill=(240, 240, 240))
        draw.text((80, 325), "Agentic AI Spec-vs-Drawing Audit in 20 Seconds", font=f_sub, fill=(0, 242, 254))
        
        # Workflow Step Cards
        y_start = 420
        active_step = min(int(t / 1.8), 3) # reveal steps as time progresses
        
        for idx, (title, desc, color) in enumerate(steps):
            y = y_start + idx * 260
            if idx <= active_step:
                # Active/revealed card
                glow = color if idx == active_step else (60, 75, 95)
                draw.rounded_rectangle([50, y, 1030, y + 220], radius=15, fill=(20, 25, 35), outline=glow, width=3 if idx==active_step else 1)
                
                # Step badge
                draw.rounded_rectangle([70, y + 25, 200, y + 70], radius=8, fill=color)
                draw.text((85, y + 33), f"STEP 0{idx+1}", font=get_font(22, bold=True), fill=(0, 0, 0))
                
                draw.text((220, y + 32), title.split(":")[1].strip(), font=f_card_t, fill=color)
                draw.text((80, y + 95), desc, font=f_card_d, fill=(230, 235, 245))
                
                # Animated scanning progress bar
                if idx == active_step:
                    prog_w = int((t % 1.8) / 1.8 * 880)
                    draw.rounded_rectangle([80, y + 175, 80 + prog_w, y + 190], radius=4, fill=color)
            else:
                # Locked/pending step
                draw.rounded_rectangle([50, y, 1030, y + 220], radius=15, fill=(16, 20, 28), outline=(35, 45, 55), width=1)
                draw.text((80, y + 90), f"PENDING AUDIT: STEP 0{idx+1}...", font=f_card_t, fill=(80, 95, 115))
                
        # Scanning HUD beam animation
        scan_y = int(400 + (t_frac * 1100)) % 1100 + 400
        draw.line([(50, scan_y), (1030, scan_y)], fill=(0, 242, 254), width=3)
        
        draw_bottom_cta_bar(draw, "SPEC", t_frac)
        
        # Convert PIL to CV2 BGR
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print("Rendered:", out_path)

def render_reel_02(duration_sec=8, fps=30):
    # Reel 2: 33 kV Substation Zero-Trip Protocol
    out_path = os.path.join(REELS_DIR, "reel_02_substation_commissioning.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (1080, 1920))
    
    total_frames = int(duration_sec * fps)
    f_hook = get_font(48, bold=True)
    f_sub = get_font(28, bold=False)
    f_card_t = get_font(26, bold=True)
    
    # Load schematic image
    schematic_img = Image.open(os.path.join(ASSETS_DIR, "schematic_33kv_sld.png")).convert("RGBA")
    schematic_img = schematic_img.resize((960, 960))
    
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        t_frac = frame_idx / total_frames
        
        img = Image.new("RGB", (1080, 1920), (13, 17, 23))
        draw = ImageDraw.Draw(img)
        
        draw_top_brand_bar(draw, "FIELD COMMISSIONING")
        
        # Hook Header
        draw.rounded_rectangle([50, 170, 1030, 350], radius=15, fill=(22, 27, 34), outline=(0, 242, 254), width=3)
        draw.text((80, 195), "33 kV ZERO-TRIP ENERGIZATION", font=f_hook, fill=(0, 242, 254))
        draw.text((80, 260), "4 Sign-Off Checks Before Breaker Close", font=f_sub, fill=(255, 255, 255))
        draw.text((80, 300), "Transformer OLTC | CT Knee Point | OMICRON Relay Test", font=f_sub, fill=(255, 184, 0))
        
        # Center: Schematic Graphic with Live Pulsing Energy Flow
        img.paste(schematic_img, (60, 380))
        
        # Overlay dynamic electrical pulse tracing down the schematic
        pulse_y = int(480 + (t_frac * 750)) % 750 + 480
        draw.ellipse([510, pulse_y - 15, 570, pulse_y + 15], fill=(255, 255, 0), outline=(255, 255, 255), width=2)
        
        # Lower Checkcards
        check_labels = [
            ("1. Dyn11 Vector Group", "Confirmed 30° phase shift"),
            ("2. 15% 2nd Harmonic", "Inrush restraint active"),
            ("3. OMICRON CMC 356", "Secondary injection verified"),
            ("4. VCB Timing Test", "Opening time < 45 ms")
        ]
        
        # 2x2 grid at bottom above CTA
        for i, (title, sub) in enumerate(check_labels):
            gx = 60 + (i % 2) * 490
            gy = 1400 + (i // 2) * 140
            draw.rounded_rectangle([gx, gy, gx + 470, gy + 120], radius=12, fill=(20, 28, 40), outline=(0, 255, 140), width=2)
            draw.text((gx + 20, gy + 20), title, font=f_card_t, fill=(0, 255, 140))
            draw.text((gx + 20, gy + 65), sub, font=get_font(20, bold=False), fill=(220, 230, 245))
            
        draw_bottom_cta_bar(draw, "SLD", t_frac)
        
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print("Rendered:", out_path)

def render_reel_03(duration_sec=8, fps=30):
    # Reel 3: Primavera P6 Float Audit Workflow
    out_path = os.path.join(REELS_DIR, "reel_03_primavera_p6_ai.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (1080, 1920))
    
    total_frames = int(duration_sec * fps)
    f_hook = get_font(50, bold=True)
    f_sub = get_font(28, bold=False)
    
    p6_img = Image.open(os.path.join(ASSETS_DIR, "primavera_p6_ui.png")).convert("RGBA")
    p6_img = p6_img.resize((980, 980))
    
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        t_frac = frame_idx / total_frames
        
        img = Image.new("RGB", (1080, 1920), (13, 17, 23))
        draw = ImageDraw.Draw(img)
        
        draw_top_brand_bar(draw, "PROJECT CONTROLS & AI")
        
        # Hook Header
        draw.rounded_rectangle([50, 170, 1030, 360], radius=15, fill=(22, 27, 34), outline=(255, 184, 0), width=3)
        draw.text((80, 195), "PRIMAVERA P6 FLOAT AUDIT", font=f_hook, fill=(255, 184, 0))
        draw.text((80, 260), "Why 80% of EPC Schedules Hide 6-Week Delays", font=f_sub, fill=(255, 255, 255))
        draw.text((80, 305), "AI Detects Artificial Lags & Critical Path Traps", font=f_sub, fill=(0, 242, 254))
        
        # Center: P6 UI
        img.paste(p6_img, (50, 390))
        
        # Dynamic AI Diagnostic Spotlight
        pulse_alpha = int(120 + 80 * math.sin(t * 6))
        draw.rounded_rectangle([60, 680, 1020, 830], radius=10, outline=(255, 60, 60), width=4)
        
        # Live Stats bar below P6
        draw.rounded_rectangle([60, 1420, 1020, 1680], radius=15, fill=(18, 25, 38), outline=(0, 242, 254), width=2)
        draw.text((90, 1445), "AI SCHEDULE OPTIMIZATION METRICS:", font=get_font(28, bold=True), fill=(0, 242, 254))
        draw.text((90, 1500), "• Negative Float Resolved: -42 Days -> 0 Days on Target", font=get_font(22, bold=False), fill=(240, 240, 240))
        draw.text((90, 1545), "• Relinked Secondary Injection Precedents to FAT Cleared", font=get_font(22, bold=False), fill=(240, 240, 240))
        draw.text((90, 1590), "• Substation Energization Milestone Saved: \$280K Liquidated Damages", font=get_font(22, bold=True), fill=(0, 255, 140))
        
        draw_bottom_cta_bar(draw, "P6", t_frac)
        
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print("Rendered:", out_path)

def render_reel_04(duration_sec=8, fps=30):
    # Reel 4: Pattern-Interrupt + 2-Character Split-Screen Dialogue
    out_path = os.path.join(REELS_DIR, "reel_04_2char_talkinghead_pattern_video.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (1080, 1920))
    
    total_frames = int(duration_sec * fps)
    f_hook = get_font(46, bold=True)
    f_sub = get_font(26, bold=False)
    
    char1 = Image.open(os.path.join(ASSETS_DIR, "character_site_manager.png")).convert("RGBA")
    char1 = char1.resize((560, 560))
    
    char2 = Image.open(os.path.join(ASSETS_DIR, "character_senior_architect.png")).convert("RGBA")
    char2 = char2.resize((560, 560))
    
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        t_frac = frame_idx / total_frames
        
        img = Image.new("RGB", (1080, 1920), (13, 17, 23))
        draw = ImageDraw.Draw(img)
        
        draw_top_brand_bar(draw, "PATTERN INTERRUPT")
        
        # 0–3s Hook Alert
        draw.rounded_rectangle([50, 160, 1030, 310], radius=15, fill=(45, 12, 18), outline=(255, 60, 60), width=3)
        draw.text((80, 180), "⚠ 33kV ENERGIZATION TRIP ALERT!", font=f_hook, fill=(255, 75, 75))
        draw.text((80, 240), "Why Breakers Trip on Day-1 Soak After Passing FAT", font=f_sub, fill=(255, 255, 255))
        
        # TOP CHARACTER: Stressed EPC Site Manager (Left side, y=340 to y=980)
        draw.rounded_rectangle([50, 330, 1030, 950], radius=16, fill=(20, 12, 16), outline=(255, 75, 75), width=2)
        img.paste(char1, (60, 360), char1)
        # Speech Bubble for Site Manager
        draw.rounded_rectangle([630, 420, 1010, 850], radius=15, fill=(35, 15, 20), outline=(255, 80, 80), width=2)
        draw.text((650, 450), "SITE MANAGER:", font=get_font(26, bold=True), fill=(255, 80, 80))
        lines1 = [
            "\"FAT passed with zero faults!",
            "Breaker closed on 33kV soak,",
            "and 87T differential tripped",
            "in 40 milliseconds!",
            "",
            "Is the transformer dead?!\""
        ]
        ly = 500
        for l in lines1:
            draw.text((650, ly), l, font=get_font(20, bold=False), fill=(255, 220, 220))
            ly += 35
            
        # BOTTOM CHARACTER: Senior AI & Power Systems Architect (y=980 to y=1680)
        draw.rounded_rectangle([50, 980, 1030, 1680], radius=16, fill=(12, 22, 35), outline=(0, 242, 254), width=2)
        img.paste(char2, (60, 1040), char2)
        # Speech Bubble for Senior Architect
        draw.rounded_rectangle([630, 1040, 1010, 1600], radius=15, fill=(15, 30, 48), outline=(0, 242, 254), width=2)
        draw.text((650, 1070), "SENIOR AI ARCHITECT:", font=get_font(26, bold=True), fill=(0, 242, 254))
        lines2 = [
            "\"The transformer is fine.",
            "Check 2 site failure modes:",
            "",
            "1. Dyn11 30° vector group",
            "   compensation polarity.",
            "2. 15% 2nd-Harmonic inrush",
            "   restraint setting was",
            "   disabled on MiCOM P643!\"",
        ]
        ly = 1120
        for l in lines2:
            draw.text((650, ly), l, font=get_font(20, bold=False), fill=(220, 245, 255))
            ly += 35
            
        # Animated sine wave telemetry between characters
        wave_y = 965
        for x in range(60, 1020, 10):
            y_offset = int(12 * math.sin((x / 40.0) + (t * 8.0)))
            draw.line([(x, wave_y + y_offset), (x+8, wave_y + y_offset)], fill=(0, 242, 254), width=3)
            
        draw_bottom_cta_bar(draw, "RELAY", t_frac)
        
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print("Rendered:", out_path)

if __name__ == "__main__":
    print("Starting rendering of all 4 viral Reels...")
    render_reel_01()
    render_reel_02()
    render_reel_03()
    render_reel_04()
    print("All 4 reels rendered successfully in 1080x1920 (9:16) format!")

