import os
from PIL import Image, ImageDraw, ImageFont

CAROUSEL_DIR = "d:/instagram/carousels"
os.makedirs(f"{CAROUSEL_DIR}/carousel_01_sld_mistakes", exist_ok=True)
os.makedirs(f"{CAROUSEL_DIR}/carousel_02_generator_protection", exist_ok=True)

def get_font(size, bold=False):
    font_names = ["arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf", "consola.ttf"]
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()

def draw_carousel_slide(out_path, slide_num, total_slides, tag, headline, bullets, callout_text=None, accent_color=(0, 242, 254)):
    # Standard 1080 x 1350 Instagram Portrait (4:5)
    width, height = 1080, 1350
    img = Image.new("RGB", (width, height), (13, 17, 23))
    draw = ImageDraw.Draw(img)
    
    # Grid pattern background
    for x in range(0, width, 50):
        draw.line([(x, 0), (x, height)], fill=(20, 26, 35), width=1)
    for y in range(0, height, 50):
        draw.line([(0, y), (width, y)], fill=(20, 26, 35), width=1)
        
    # Top Bar: Brand & Slide Indicator
    draw.rectangle([0, 0, width, 130], fill=(16, 22, 30))
    draw.line([(0, 130), (width, 130)], fill=accent_color, width=3)
    draw.text((60, 45), "⚡ PROENGINEERING | 23+ YRS INDUSTRIAL AI", font=get_font(28, bold=True), fill=accent_color)
    
    # Slide Indicator Pill
    pill_text = f"SLIDE {slide_num}/{total_slides}"
    draw.rounded_rectangle([840, 40, 1020, 90], radius=10, fill=(28, 38, 52), outline=accent_color, width=2)
    draw.text((865, 52), pill_text, font=get_font(20, bold=True), fill=(255, 255, 255))
    
    # Topic Tag Pill
    draw.rounded_rectangle([60, 170, 380, 225], radius=8, fill=(25, 35, 48), outline=(255, 184, 0), width=2)
    draw.text((80, 185), tag.upper(), font=get_font(22, bold=True), fill=(255, 184, 0))
    
    # Headline
    f_head = get_font(46, bold=True)
    draw.text((60, 260), headline, font=f_head, fill=(255, 255, 255))
    draw.line([(60, 360), (300, 360)], fill=accent_color, width=4)
    
    # Bullet points / Body Cards
    y = 400
    for b_title, b_desc in bullets:
        draw.rounded_rectangle([60, y, 1020, y + 150], radius=14, fill=(18, 25, 36), outline=(40, 52, 70), width=2)
        # Accent left border strip
        draw.rounded_rectangle([60, y, 75, y + 150], radius=4, fill=accent_color)
        draw.text((100, y + 25), b_title, font=get_font(30, bold=True), fill=accent_color)
        draw.text((100, y + 75), b_desc[:70], font=get_font(22, bold=False), fill=(225, 235, 245))
        if len(b_desc) > 70:
            draw.text((100, y + 105), b_desc[70:], font=get_font(22, bold=False), fill=(225, 235, 245))
        y += 180
        
    # Callout Box at Bottom
    if callout_text:
        draw.rounded_rectangle([60, 1080, 1020, 1220], radius=14, fill=(24, 18, 26), outline=(255, 75, 75), width=2)
        draw.text((90, 1105), "⚠ FIELD REALITY / WARNING:", font=get_font(24, bold=True), fill=(255, 75, 75))
        draw.text((90, 1145), callout_text[:75], font=get_font(20, bold=False), fill=(245, 220, 220))
        if len(callout_text) > 75:
            draw.text((90, 1175), callout_text[75:], font=get_font(20, bold=False), fill=(245, 220, 220))
            
    # Bottom Swipe Reminder
    draw.rectangle([0, 1260, width, 1350], fill=(16, 22, 30))
    swipe_text = "SWIPE FOR NEXT MISTAKE ➡" if slide_num < total_slides else "SAVE FOR YOUR NEXT SITE WALK 🔖"
    draw.text((360, 1290), swipe_text, font=get_font(22, bold=True), fill=(180, 200, 225))
    
    img.save(out_path)
    print("Saved Carousel Slide:", out_path)

def generate_carousel_01():
    # Carousel 1: 5 SLD vs Site Mistakes (7 Slides)
    slides_data = [
        (
            1, 7, "Substation Commissioning",
            "5 SLD vs. SITE MISTAKES\nTHAT DELAY 33kV ENERGIZATION",
            [
                ("Why Substations Fail Soak", "80% of Day-1 trips aren't equipment faults—they are drawing discrepancies."),
                ("23+ Years of Megaproject Scars", "These 5 traps delay commissioning, inflate liquidated damages, and void warranties."),
                ("Who Needs This Guide", "Project Directors, Lead Electrical Engineers, and Site Commissioning Managers.")
            ],
            "Save this post before your next switchyard site walk. Swipe to see Mistake #1.",
            (0, 242, 254)
        ),
        (
            2, 7, "Mistake #1",
            "CT SECONDARY STAR-POINT\nGROUNDED AT BOTH ENDS",
            [
                ("The Drawing Oversight", "SLD shows CT neutral grounded, but site team also grounds CT terminal box at breaker."),
                ("The Physical Result", "Circulating ground currents create false zero-sequence current in 87T loop."),
                ("The Diagnostic Fix", "Keep ONE single point ground inside the relay panel; isolate switchyard star point.")
            ],
            "Dual grounding trips the differential relay the second load or soak current is applied.",
            (255, 75, 75)
        ),
        (
            3, 7, "Mistake #2",
            "DYN11 30° VECTOR DISPLACEMENT\nIGNORED IN NUMERICAL RELAY",
            [
                ("The Drawing Oversight", "Transformer nameplate specifies Dyn11, but relay software configured for Dyn1 or Yy0."),
                ("The Physical Result", "A 30-degree phase shift produces 50% spill current between primary & secondary CTs."),
                ("The Diagnostic Fix", "Verify internal software vector compensation or secondary delta CT wiring connection.")
            ],
            "Even at 10% load, uncompensated Dyn11 trips MiCOM / ABB transformer relays instantly.",
            (255, 184, 0)
        ),
        (
            4, 7, "Mistake #3",
            "MISSING 2ND-HARMONIC\nINRUSH RESTRAINT (<12%)",
            [
                ("The Drawing Oversight", "Protection study leaves harmonic restraint at default without soak curve calculation."),
                ("The Physical Result", "Core magnetization inrush current contains up to 60% second harmonic on cold soak."),
                ("The Diagnostic Fix", "Enable 15% 2nd-harmonic restraint threshold with cross-blocking active on all 3 phases.")
            ],
            "Without 2nd-harmonic blocking, the transformer trips within 40ms of breaker closing.",
            (255, 75, 75)
        ),
        (
            5, 7, "Mistake #4",
            "CABLE TRAY THERMAL DERATING\n& CORROSION SOIL ASSUMPTION",
            [
                ("The Drawing Oversight", "Engineers size 33kV XLPE cables assuming 1.2 K.m/W soil resistivity without site soil test."),
                ("The Physical Result", "Dry summer backfill hits 2.5 K.m/W, reducing cable ampacity by up to 32%."),
                ("The Diagnostic Fix", "Mandate thermal resistivity backfill testing and apply spacing factor corrections.")
            ],
            "Cable overheating under full load causes sheath degradation and long-term dielectric breakdown.",
            (255, 184, 0)
        ),
        (
            6, 7, "Mistake #5",
            "VCB AUXILIARY CHATTERING\nMASKED AS 50BF BREAKER FAIL",
            [
                ("The Drawing Oversight", "52a/52b auxiliary contacts not adjusted for bounce margin in the breaker operating mechanism."),
                ("The Physical Result", "Relay senses current with open aux contact, initiating catastrophic 50BF bus trip."),
                ("The Diagnostic Fix", "Measure contact wipe, bounce time (<3ms), and verify VCB timing analyzer results.")
            ],
            "Mechanical auxiliary misalignment trips the entire upstream 33kV substation busbar.",
            (255, 75, 75)
        ),
        (
            7, 7, "Summary & Lead Magnet",
            "WANT THE FULL 24-POINT\nCOMMISSIONING CHECKLIST?",
            [
                ("Download The Print-Ready PDF", "Includes complete CT knee-point formulas, OMICRON injection test sheet & VCB timing limits."),
                ("How To Get It Instantly", "Comment 'SLD' below and I'll send you the direct download link right away."),
                ("Consulting & Pre-Bid Audits", "Book a confidential Megaproject spec audit or substation RCA at proengineering.in.")
            ],
            "Comment 'SLD' below to receive the complete 2-page ProEngineering Diagnostic Checklist!",
            (0, 255, 140)
        )
    ]
    
    for s in slides_data:
        out_path = f"{CAROUSEL_DIR}/carousel_01_sld_mistakes/slide_0{s[0]}.png"
        draw_carousel_slide(out_path, s[0], s[1], s[2], s[3], s[4], s[5], s[6])

def generate_carousel_02():
    # Carousel 2: Generator Protection Relays (MiCOM P343) Explained (6 Slides)
    slides_data = [
        (
            1, 6, "Protection Engineering",
            "GENERATOR PROTECTION MATRIX\n(MICOM P343 EXPLAINED)",
            [
                ("High-Stakes Machine Protection", "Large synchronous generators require coordination of 12+ protection functions."),
                ("Why Engineers Bookmark This", "One visual guide mapping ANSI relay codes to real rotor and stator failure modes."),
                ("Applicability", "Power Plants, Captive Co-Gen Units, Hydro & Turbo Generators.")
            ],
            "Save this cheat sheet for your next protection setting calculation.",
            (0, 242, 254)
        ),
        (
            2, 6, "ANSI 87G & 64S",
            "STATOR DIFFERENTIAL &\n100% STATOR EARTH FAULT",
            [
                ("ANSI 87G: Phase Differential", "Dual-slope biased characteristic. Clears phase-to-phase internal stator faults in <25ms."),
                ("ANSI 64S: 100% Stator Ground", "Uses 20Hz sub-harmonic voltage injection to protect 100% of the winding down to the neutral."),
                ("Setting Tip", "Ensure CT knee-point voltage Vk matches 2*If*(Rct+2*RL) to avoid CT saturation during through-faults.")
            ],
            "Standard 95% 59N relays leave neutral zone unprotected; 20Hz injection covers 100%.",
            (255, 75, 75)
        ),
        (
            3, 6, "ANSI 40",
            "LOSS OF EXCITATION\n(FIELD FAILURE PROTECTION)",
            [
                ("The Failure Mechanism", "Loss of DC field excitation converts synchronous generator into an induction generator."),
                ("The Offset Mho Characteristic", "Impedance trajectory moves into negative X quadrant on the R-X diagram."),
                ("Zone 1 vs Zone 2 Settings", "Diameter = Xd; Offset = -Xd'/2. Zone 1 trips in 0.2s; Zone 2 coordinated with AVR at 0.75s.")
            ],
            "Failure to trip causes severe stator end-iron overheating and machine instability.",
            (255, 184, 0)
        ),
        (
            4, 6, "ANSI 46",
            "NEGATIVE PHASE SEQUENCE\n(UNBALANCED LOAD HEATING)",
            [
                ("The Failure Mechanism", "Unbalanced phase currents induce double-frequency (100Hz/120Hz) eddy currents in the rotor."),
                ("The Thermal Equation", "Operating time t = K / (I2/In)^2, where K is the machine rotor heating constant (e.g. K=10)."),
                ("Alarm vs Trip Levels", "Continuous I2 alarm set at 8-10%; trip curve protects cylindrical/salient pole rotors.")
            ],
            "Unbalanced line faults or single-phasing burn rotor slot wedges without proper ANSI 46 tripping.",
            (255, 75, 75)
        ),
        (
            5, 6, "ANSI 32R & 64R",
            "REVERSE POWER &\nROTOR EARTH FAULT",
            [
                ("ANSI 32R: Motoring Prevention", "Detects low forward/reverse active power when prime mover trips (steam/gas turbine soak)."),
                ("ANSI 64R: Field Ground Fault", "Monitors field circuit insulation. 1st ground fault alarms; 2nd ground fault trips to prevent rotor magnetic unbalance."),
                ("Setting Guideline", "Set 32R to 0.5-2.0% rated active power with 2 to 10 seconds deliberate time delay.")
            ],
            "Turbine blade overheating occurs within seconds if motoring continues without steam flow.",
            (255, 184, 0)
        ),
        (
            6, 6, "Summary & Lead Magnet",
            "WANT THE 1-PAGE\nPROTECTION WIRING SCHEMATIC?",
            [
                ("Full Vector Wiring & Equations", "Get the high-resolution printable PDF diagram with CT/VT connection schematics."),
                ("Free Download Link", "Comment 'GEN' below and I'll send the vector schematic straight to your DMs."),
                ("Industrial AI Consultation", "Book an automated protection setting & coordination review at proengineering.in.")
            ],
            "Comment 'GEN' below to get the complete MiCOM P343 Engineering Cheat Sheet!",
            (0, 255, 140)
        )
    ]
    
    for s in slides_data:
        out_path = f"{CAROUSEL_DIR}/carousel_02_generator_protection/slide_0{s[0]}.png"
        draw_carousel_slide(out_path, s[0], s[1], s[2], s[3], s[4], s[5], s[6])

if __name__ == "__main__":
    generate_carousel_01()
    generate_carousel_02()
    print("All carousels generated successfully!")
