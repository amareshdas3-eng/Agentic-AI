import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = "d:/instagram/assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def get_font(size, bold=False):
    # Try standard Windows fonts
    font_names = ["arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf", "consola.ttf"]
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()

def draw_glow_rect(draw, bbox, color, glow_color, radius=15, width=3):
    x0, y0, x1, y1 = bbox
    # Outer glow
    for offset in range(4, 0, -1):
        alpha_color = (*glow_color[:3], int(30 * (5 - offset)))
        draw.rounded_rectangle([x0-offset, y0-offset, x1+offset, y1+offset], radius=radius+offset, outline=glow_color, width=1)
    draw.rounded_rectangle(bbox, radius=radius, outline=color, width=width)

def generate_avatar():
    size = (1080, 1080)
    img = Image.new("RGBA", size, (13, 17, 23, 255)) # GitHub dark
    draw = ImageDraw.Draw(img)
    
    # Grid pattern background
    for x in range(0, 1080, 40):
        draw.line([(x, 0), (x, 1080)], fill=(22, 27, 34, 255), width=1)
    for y in range(0, 1080, 40):
        draw.line([(0, y), (1080, y)], fill=(22, 27, 34, 255), width=1)
        
    cx, cy = 540, 540
    # Outer neon ring
    for r in range(420, 440):
        alpha = int(120 * (r - 420) / 20)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(0, 242, 254, alpha), width=1)
    draw.ellipse([cx - 400, cy - 400, cx + 400, cy + 400], outline=(0, 242, 254, 255), width=6)
    draw.ellipse([cx - 360, cy - 360, cx + 360, cy + 360], outline=(255, 184, 0, 220), width=3)
    
    # Substation Transformer / Relay vector glyph in center
    # Primary coil
    draw.arc([cx - 160, cy - 140, cx - 20, cy + 20], start=0, end=360, fill=(0, 242, 254, 255), width=8)
    # Secondary coil overlapping
    draw.arc([cx - 60, cy - 140, cx + 80, cy + 20], start=0, end=360, fill=(255, 184, 0, 255), width=8)
    # High voltage lightning bolt
    bolt = [
        (cx + 80, cy - 160),
        (cx + 10, cy - 30),
        (cx + 60, cy - 20),
        (cx - 20, cy + 120),
        (cx + 10, cy + 30),
        (cx - 30, cy + 20),
    ]
    draw.polygon(bolt, fill=(255, 230, 0, 255))
    
    # Text
    f_title = get_font(72, bold=True)
    f_sub = get_font(38, bold=True)
    f_tag = get_font(28, bold=True)
    
    title = "PROENGINEERING"
    sub = "INDUSTRIAL AI & 33kV"
    tag = "23+ YRS MEGACAPEX"
    
    bbox_t = draw.textbbox((0, 0), title, font=f_title)
    bbox_s = draw.textbbox((0, 0), sub, font=f_sub)
    bbox_g = draw.textbbox((0, 0), tag, font=f_tag)
    
    draw.text((cx - (bbox_t[2] - bbox_t[0])//2, cy + 170), title, font=f_title, fill=(255, 255, 255, 255))
    draw.text((cx - (bbox_s[2] - bbox_s[0])//2, cy + 260), sub, font=f_sub, fill=(0, 242, 254, 255))
    draw.text((cx - (bbox_g[2] - bbox_g[0])//2, cy + 320), tag, font=f_tag, fill=(255, 184, 0, 255))
    
    path = os.path.join(ASSETS_DIR, "proengineering_avatar.png")
    img.save(path)
    print("Saved:", path)

def generate_character_site_manager():
    # 540 x 720 character card: Stressed EPC Site Manager
    size = (720, 720)
    img = Image.new("RGBA", size, (20, 10, 15, 255))
    draw = ImageDraw.Draw(img)
    
    # Dark industrial emergency background with red glow
    for r in range(350, 0, -5):
        alpha = int(40 * (1 - r/350))
        draw.ellipse([360-r, 360-r, 360+r, 360+r], fill=(255, 40, 40, alpha))
    
    # Hardhat (Yellow)
    draw.chord([260, 150, 460, 320], start=180, end=360, fill=(255, 190, 0, 255), outline=(200, 140, 0, 255), width=3)
    draw.rounded_rectangle([230, 250, 490, 280], radius=8, fill=(255, 205, 30, 255), outline=(220, 150, 0, 255), width=3)
    
    # Face & Stressed expression
    draw.ellipse([290, 270, 430, 420], fill=(240, 190, 160, 255)) # skin
    # Eyes (worried / stressed)
    draw.line([(315, 325), (345, 335)], fill=(120, 40, 30, 255), width=4) # slanted brow
    draw.line([(405, 335), (375, 325)], fill=(120, 40, 30, 255), width=4) # slanted brow
    draw.ellipse([325, 340, 340, 355], fill=(40, 20, 10, 255)) # left eye
    draw.ellipse([380, 340, 395, 355], fill=(40, 20, 10, 255)) # right eye
    # Sweat drop
    draw.polygon([(425, 320), (432, 335), (420, 335)], fill=(100, 200, 255, 255))
    draw.ellipse([418, 332, 434, 345], fill=(100, 200, 255, 255))
    # Mouth (open exclamation / stress)
    draw.ellipse([345, 375, 375, 400], fill=(90, 20, 20, 255))
    
    # High-vis jacket & Radio
    draw.polygon([(250, 420), (470, 420), (520, 600), (200, 600)], fill=(255, 100, 20, 255)) # orange jacket
    # Reflective silver stripes
    draw.line([(280, 430), (260, 600)], fill=(220, 230, 240, 255), width=16)
    draw.line([(440, 430), (460, 600)], fill=(220, 230, 240, 255), width=16)
    
    # Walkie-Talkie in hand
    draw.rectangle([180, 360, 230, 460], fill=(30, 30, 35, 255))
    draw.line([(205, 360), (205, 300)], fill=(20, 20, 20, 255), width=6) # antenna
    draw.ellipse([195, 375, 215, 395], fill=(255, 30, 30, 255)) # red blinking LED
    
    # Badge
    f_badge = get_font(28, bold=True)
    f_desc = get_font(20, bold=False)
    draw.rounded_rectangle([50, 610, 670, 690], radius=12, fill=(40, 10, 15, 230), outline=(255, 60, 60, 255), width=3)
    draw.text((80, 620), "EPC SITE MANAGER", font=f_badge, fill=(255, 80, 80, 255))
    draw.text((80, 655), "\"The 33kV breaker tripped on Day-1 soak! What failed?!\"", font=f_desc, fill=(240, 220, 220, 255))
    
    path = os.path.join(ASSETS_DIR, "character_site_manager.png")
    img.save(path)
    print("Saved:", path)

def generate_character_senior_architect():
    # 720 x 720 character card: Senior Industrial AI & Power Systems Architect
    size = (720, 720)
    img = Image.new("RGBA", size, (10, 20, 30, 255))
    draw = ImageDraw.Draw(img)
    
    # Dark cyber cyan background with tech rings
    for r in range(350, 0, -5):
        alpha = int(45 * (1 - r/350))
        draw.ellipse([360-r, 360-r, 360+r, 360+r], fill=(0, 220, 255, alpha))
        
    for r in [200, 260, 320]:
        draw.arc([360-r, 360-r, 360+r, 360+r], start=30, end=150, fill=(0, 242, 254, 140), width=2)
        draw.arc([360-r, 360-r, 360+r, 360+r], start=210, end=330, fill=(255, 184, 0, 140), width=2)
        
    # Head & Smart Composure
    draw.ellipse([290, 250, 430, 410], fill=(235, 195, 170, 255)) # skin
    # Hair (distinguished grey-black)
    draw.chord([280, 210, 440, 310], start=180, end=360, fill=(60, 65, 75, 255))
    
    # Smart HUD Glasses / AR Eyewear (Cyan glowing frame)
    draw.rounded_rectangle([305, 310, 355, 345], radius=6, fill=(0, 40, 60, 200), outline=(0, 242, 254, 255), width=3)
    draw.rounded_rectangle([365, 310, 415, 345], radius=6, fill=(0, 40, 60, 200), outline=(0, 242, 254, 255), width=3)
    draw.line([(355, 325), (365, 325)], fill=(0, 242, 254, 255), width=3)
    # HUD data projection lines on lens
    draw.line([(310, 320), (330, 320)], fill=(0, 255, 200, 255), width=2)
    draw.line([(310, 330), (345, 330)], fill=(0, 255, 200, 255), width=1)
    
    # Confident Smile
    draw.arc([345, 365, 375, 385], start=0, end=180, fill=(140, 70, 50, 255), width=3)
    
    # Modern Technical Navy/Graphite Jacket with AI lapel badge
    draw.polygon([(250, 410), (470, 410), (530, 600), (190, 600)], fill=(25, 35, 50, 255))
    draw.polygon([(340, 410), (380, 410), (370, 520), (350, 520)], fill=(15, 22, 33, 255))
    # Electric Cyan circuit trace on shoulder
    draw.line([(250, 440), (280, 440), (300, 470)], fill=(0, 242, 254, 255), width=3)
    draw.ellipse([297, 467, 303, 473], fill=(0, 242, 254, 255))
    
    # Badge
    f_badge = get_font(28, bold=True)
    f_desc = get_font(20, bold=False)
    draw.rounded_rectangle([50, 610, 670, 690], radius=12, fill=(10, 25, 45, 230), outline=(0, 242, 254, 255), width=3)
    draw.text((80, 620), "INDUSTRIAL AI & POWER ARCHITECT", font=f_badge, fill=(0, 242, 254, 255))
    draw.text((80, 655), "\"Check Dyn11 vector compensation & 15% 2nd-harmonic inrush.\"", font=f_desc, fill=(220, 240, 255, 255))
    
    path = os.path.join(ASSETS_DIR, "character_senior_architect.png")
    img.save(path)
    print("Saved:", path)

def generate_schematic_33kv_sld():
    # 1080 x 1080 technical dark-mode SLD schematic
    size = (1080, 1080)
    img = Image.new("RGBA", size, (13, 17, 23, 255))
    draw = ImageDraw.Draw(img)
    
    f_lg = get_font(36, bold=True)
    f_md = get_font(26, bold=True)
    f_sm = get_font(20, bold=False)
    
    # Title Block
    draw.rounded_rectangle([40, 30, 1040, 110], radius=8, fill=(22, 27, 34, 255), outline=(0, 242, 254, 255), width=2)
    draw.text((60, 45), "33 kV / 11 kV PRIMARY SUBSTATION SLD", font=f_lg, fill=(0, 242, 254, 255))
    draw.text((60, 80), "DIFF PROTECTION 87T | 31.5kA FOR 3s | OMICRON TESTED", font=f_sm, fill=(255, 184, 0, 255))
    
    # Main 33kV Busbar (Red neon line)
    draw.line([(100, 180), (980, 180)], fill=(255, 60, 60, 255), width=8)
    draw.text((120, 140), "33 kV MAIN BUSBAR - FAULT LEVEL: 31.5 kA", font=f_md, fill=(255, 80, 80, 255))
    
    # Feeder drop
    draw.line([(540, 180), (540, 270)], fill=(255, 255, 255, 255), width=4)
    
    # Isolator (Disconnector)
    draw.line([(520, 270), (560, 270)], fill=(0, 242, 254, 255), width=4)
    draw.line([(540, 270), (570, 310)], fill=(0, 242, 254, 255), width=4)
    draw.line([(520, 310), (560, 310)], fill=(0, 242, 254, 255), width=4)
    draw.text((580, 280), "89A ISOLATOR", font=f_sm, fill=(180, 200, 220, 255))
    
    # Circuit Breaker 52 (Vacuum Circuit Breaker)
    draw.line([(540, 310), (540, 360)], fill=(255, 255, 255, 255), width=4)
    draw.rectangle([510, 360, 570, 420], fill=(22, 27, 34, 255), outline=(0, 255, 140, 255), width=4)
    draw.line([(515, 365), (565, 415)], fill=(0, 255, 140, 255), width=3)
    draw.line([(515, 415), (565, 365)], fill=(0, 255, 140, 255), width=3)
    draw.text((590, 380), "52-1 33kV VCB (1250A)", font=f_md, fill=(0, 255, 140, 255))
    
    # Current Transformer CT (600/1A Class 0.2S + PS)
    draw.line([(540, 420), (540, 480)], fill=(255, 255, 255, 255), width=4)
    draw.ellipse([515, 480, 565, 530], outline=(255, 184, 0, 255), width=4)
    draw.ellipse([515, 500, 565, 550], outline=(255, 184, 0, 255), width=4)
    draw.text((580, 505), "CT: 600/1A Class PS (Vk >= 400V, Rct <= 2.5Ω)", font=f_sm, fill=(255, 184, 0, 255))
    
    # Power Transformer (33/11 kV, 20 MVA ONAN/ONAF Dyn11)
    draw.line([(540, 550), (540, 620)], fill=(255, 255, 255, 255), width=4)
    draw.ellipse([490, 620, 590, 720], outline=(0, 242, 254, 255), width=6)
    draw.ellipse([490, 680, 590, 780], outline=(255, 184, 0, 255), width=6)
    draw.text((610, 660), "20 MVA POWER XFRMR", font=f_lg, fill=(255, 255, 255, 255))
    draw.text((610, 705), "33/11 kV Dyn11 | OLTC ±10%", font=f_md, fill=(0, 242, 254, 255))
    draw.text((610, 740), "%Z = 10.0% | 87T + 50/51 Protection", font=f_sm, fill=(200, 220, 240, 255))
    
    # 11 kV Incomer Breaker & Busbar
    draw.line([(540, 780), (540, 870)], fill=(255, 255, 255, 255), width=4)
    draw.rectangle([510, 870, 570, 930], fill=(22, 27, 34, 255), outline=(0, 255, 140, 255), width=4)
    draw.line([(515, 875), (565, 925)], fill=(0, 255, 140, 255), width=3)
    draw.line([(515, 925), (565, 875)], fill=(0, 255, 140, 255), width=3)
    draw.text((590, 890), "52-2 11kV INCOMER (2000A)", font=f_md, fill=(0, 255, 140, 255))
    
    draw.line([(540, 930), (540, 990)], fill=(255, 255, 255, 255), width=4)
    draw.line([(100, 990), (980, 990)], fill=(255, 184, 0, 255), width=8)
    draw.text((120, 1010), "11 kV DISTRIBUTION BUSBAR - FAULT LEVEL: 25 kA", font=f_md, fill=(255, 184, 0, 255))
    
    path = os.path.join(ASSETS_DIR, "schematic_33kv_sld.png")
    img.save(path)
    print("Saved:", path)

def generate_primavera_p6_ui():
    # 1080 x 1080 Primavera P6 Gantt & Schedule AI Audit UI
    size = (1080, 1080)
    img = Image.new("RGBA", size, (13, 17, 23, 255))
    draw = ImageDraw.Draw(img)
    
    f_hdr = get_font(32, bold=True)
    f_tbl = get_font(22, bold=True)
    f_row = get_font(18, bold=False)
    
    # Top P6 Ribbon Bar
    draw.rectangle([0, 0, 1080, 60], fill=(27, 38, 59, 255))
    draw.text((30, 15), "PRIMAVERA P6 ENTERPRISE PROJECT PORTFOLIO - [33kV SUBSTATION CAPEX]", font=f_tbl, fill=(255, 255, 255, 255))
    
    # AI Audit Warning Banner
    draw.rounded_rectangle([30, 80, 1050, 160], radius=8, fill=(45, 15, 20, 255), outline=(255, 60, 60, 255), width=3)
    draw.text((50, 95), "AI SCHEDULE AUDIT: 3 CRITICAL FLOAT TRAPS DETECTED!", font=f_hdr, fill=(255, 75, 75, 255))
    draw.text((50, 130), "Hidden negative float on Substation Energization Milestone (-42 Days)", font=f_row, fill=(240, 200, 200, 255))
    
    # Table Header
    headers = ["Activity ID", "Activity Description", "OD", "Total Float", "Early Start", "Critical Path Gantt"]
    draw.rectangle([30, 180, 1050, 220], fill=(33, 42, 58, 255))
    draw.text((40, 190), "ID", font=f_tbl, fill=(0, 242, 254, 255))
    draw.text((120, 190), "Activity Name", font=f_tbl, fill=(0, 242, 254, 255))
    draw.text((380, 190), "TF (d)", font=f_tbl, fill=(0, 242, 254, 255))
    draw.text((460, 190), "Status", font=f_tbl, fill=(0, 242, 254, 255))
    draw.text((600, 190), "Schedule Gantt Timeline", font=f_tbl, fill=(0, 242, 254, 255))
    
    rows = [
        ("SUB-1010", "33kV Switchgear FAT at Factory", "0", "CRITICAL", 600, 720, (255, 60, 60)),
        ("SUB-1020", "Delivery & Site Foundation Handover", "0", "CRITICAL", 720, 800, (255, 60, 60)),
        ("SUB-1030", "Secondary Injection Relay Testing", "-14", "FLOAT TRAP", 800, 940, (255, 184, 0)),
        ("SUB-1040", "Statutory CEA Inspection & Clearance", "-28", "DELAYED", 940, 1000, (255, 60, 60)),
        ("SUB-1050", "33kV Zero-Trip Energization & Soak", "-42", "CRITICAL", 1000, 1040, (255, 60, 60)),
    ]
    
    y = 230
    for act_id, name, tf, status, gx1, gx2, color in rows:
        draw.rectangle([30, y, 1050, y+55], fill=(18, 23, 32, 255) if (y//55)%2==0 else (13, 17, 23, 255))
        draw.text((40, y+15), act_id, font=f_row, fill=(200, 220, 240, 255))
        draw.text((120, y+15), name, font=f_row, fill=(255, 255, 255, 255))
        draw.text((380, y+15), tf, font=f_row, fill=color)
        draw.text((460, y+15), status, font=f_row, fill=color)
        
        # Gantt bar
        draw.rounded_rectangle([gx1, y+15, gx2, y+40], radius=6, fill=color)
        y += 65
        
    # AI Diagnostic Card at bottom
    draw.rounded_rectangle([30, 600, 1050, 1040], radius=12, fill=(20, 30, 45, 255), outline=(0, 242, 254, 255), width=3)
    draw.text((60, 630), "AI P6 SCHEDULE ROOT CAUSE ANALYSIS", font=f_hdr, fill=(0, 242, 254, 255))
    diagnostics = [
        "1. Artificial SS+15d Lag on Relay Testing hides 3 weeks of path slippage.",
        "2. Transformer Pre-Commissioning lacks mandatory CEA Inspectorate lead time.",
        "3. CT Saturation curve FAT reports have not been linked to SAT preconditions.",
        "4. Automated Remediation: De-link artificial constraints & re-sequence secondary injection.",
    ]
    dy = 690
    for d in diagnostics:
        draw.text((70, dy), d, font=f_tbl, fill=(220, 240, 255, 255))
        dy += 60
        
    path = os.path.join(ASSETS_DIR, "primavera_p6_ui.png")
    img.save(path)
    print("Saved:", path)

if __name__ == "__main__":
    generate_avatar()
    generate_character_site_manager()
    generate_character_senior_architect()
    generate_schematic_33kv_sld()
    generate_primavera_p6_ui()
    print("All brand assets generated successfully!")

