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

def generate_3d_depth_map(w, h):
    """
    Generates a realistic 3D facial depth displacement field:
    Nose / central face is closest (z > 0), temples/hair/shoulders curve backward (z < 0).
    """
    cx, cy = w // 2, int(h * 0.42)
    y_indices, x_indices = np.indices((h, w))
    
    # Elliptical distance from facial center
    dx = (x_indices - cx) / (w * 0.45)
    dy = (y_indices - cy) / (h * 0.45)
    dist_sq = dx**2 + dy**2
    
    # 3D dome curvature for face
    z_map = np.clip(1.0 - dist_sq, 0.0, 1.0)
    
    # Nose prominence peak
    nose_dx = (x_indices - cx) / (w * 0.12)
    nose_dy = (y_indices - int(h * 0.45)) / (h * 0.14)
    nose_peak = np.exp(-(nose_dx**2 + nose_dy**2)) * 0.6
    
    depth = z_map + nose_peak
    return depth / np.max(depth)

def warp_3d_perspective(img_np, depth_map, yaw_angle, pitch_angle):
    """
    Performs 3D spatial perspective re-projection based on facial depth map.
    Simulates turning the head left-right (yaw) and up-down (pitch) in 3D space.
    """
    h, w, c = img_np.shape
    
    # Compute horizontal and vertical pixel displacements proportional to depth
    yaw_rad = math.radians(yaw_angle)
    pitch_rad = math.radians(pitch_angle)
    
    # Displace pixels based on depth: closer features move more than background
    dx = (depth_map - 0.5) * math.sin(yaw_rad) * 45.0
    dy = (depth_map - 0.5) * math.sin(pitch_rad) * 35.0
    
    x_indices, y_indices = np.meshgrid(np.arange(w), np.arange(h))
    map_x = (x_indices + dx).astype(np.float32)
    map_y = (y_indices + dy).astype(np.float32)
    
    warped = cv2.remap(img_np, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return warped

def draw_3d_wireframe_cube(draw, cx, cy, size, rot_x, rot_y, rot_z, color=(0, 242, 254), width=2):
    """Draws a 3D rotating transformer wireframe cube in 3D perspective space"""
    vertices = np.array([
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1],  [1, -1, 1],  [1, 1, 1],  [-1, 1, 1]
    ], dtype=np.float32) * (size / 2.0)
    
    # Rotation matrices
    rx = np.array([[1, 0, 0], [0, math.cos(rot_x), -math.sin(rot_x)], [0, math.sin(rot_x), math.cos(rot_x)]])
    ry = np.array([[math.cos(rot_y), 0, math.sin(rot_y)], [0, 1, 0], [-math.sin(rot_y), 0, math.cos(rot_y)]])
    rz = np.array([[math.cos(rot_z), -math.sin(rot_z), 0], [math.sin(rot_z), math.cos(rot_z), 0], [0, 0, 1]])
    
    rot = rz @ ry @ rx
    rotated = vertices @ rot.T
    
    # Perspective projection
    d = 400.0
    projected = []
    for x, y, z in rotated:
        scale = d / (d + z + 100.0)
        px = int(cx + x * scale)
        py = int(cy + y * scale)
        projected.append((px, py))
        
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    
    for p1, p2 in edges:
        draw.line([projected[p1], projected[p2]], fill=color, width=width)
        
    # Draw central core bushing
    top_center = (
        (projected[4][0] + projected[5][0] + projected[6][0] + projected[7][0]) // 4,
        (projected[4][1] + projected[5][1] + projected[6][1] + projected[7][1]) // 4
    )
    draw.ellipse([top_center[0]-8, top_center[1]-8, top_center[0]+8, top_center[1]+8], fill=(255, 184, 0))

def render_3d_live_demo_reel(duration_sec=8, fps=30):
    out_path = os.path.join(REELS_DIR, "reel_3d_live_person_demo.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (1080, 1920))
    total_frames = int(duration_sec * fps)
    
    user_img = Image.open(USER_PHOTO_PATH).convert("RGB") if os.path.exists(USER_PHOTO_PATH) else Image.new("RGB", (413, 531), (20, 30, 45))
    user_np = np.array(user_img)
    depth_map = generate_3d_depth_map(user_np.shape[1], user_np.shape[0])
    
    f_hook = get_font(48, bold=True)
    f_title = get_font(30, bold=True)
    f_badge = get_font(24, bold=True)
    f_body = get_font(22, bold=False)
    
    print(f"[3D DEMO] Rendering 3D Live Person Demo Reel ({total_frames} frames)...")
    
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        t_frac = frame_idx / total_frames
        
        # Base canvas
        img = Image.new("RGB", (1080, 1920), (8, 12, 18))
        draw = ImageDraw.Draw(img)
        
        # 3D Tunnel Grid (Perspective floor and ceiling)
        horizon_y = 650
        tunnel_speed = (t * 80) % 40
        for tx in range(-400, 1480, 80):
            # Perspective rays expanding from vanishing point
            draw.line([(540, horizon_y), (tx * 2 - 540, 1920)], fill=(15, 22, 35), width=1)
        for ty in range(int(horizon_y + tunnel_speed), 1920, 40):
            scale_y = (ty - horizon_y) / (1920 - horizon_y)
            draw.line([(0, ty), (1080, ty)], fill=(int(12 + 10 * scale_y), int(18 + 15 * scale_y), int(28 + 25 * scale_y)), width=1)
            
        # Top Progress Bar
        draw.rectangle([0, 0, int(t_frac * 1080), 12], fill=(0, 242, 254))
        
        # Header
        draw.rectangle([0, 12, 1080, 130], fill=(12, 18, 28))
        draw.line([(0, 130), (1080, 130)], fill=(0, 242, 254), width=2)
        draw.text((50, 42), ">> PROENGINEERING 3D LAB", font=get_font(28, bold=True), fill=(0, 242, 254))
        draw.text((50, 82), "3D LIVE VOLUMETRIC DEMONSTRATION & SUBSTATION TWIN", font=get_font(18, bold=False), fill=(200, 220, 240))
        
        # 3D Live Indicator
        if int(t * 4) % 2 == 0:
            draw.ellipse([910, 52, 928, 70], fill=(0, 255, 140))
        draw.text((936, 50), "3D LIVE", font=get_font(20, bold=True), fill=(0, 255, 140))
        
        # =========================================================================
        # 1. 3D LIVE PERSON RE-PROJECTION (YAW & PITCH HEAD MOVEMENT)
        # =========================================================================
        # Natural 3D head yaw (turning left and right -14 deg to +14 deg)
        yaw = 14.0 * math.sin(t * 2.2)
        pitch = 6.0 * math.cos(t * 1.8)
        
        warped_face = warp_3d_perspective(user_np, depth_map, yaw, pitch)
        warped_pil = Image.fromarray(warped_face)
        
        # Dynamic 3D camera dolly zoom
        zoom = 1.0 + 0.08 * math.sin(t * 2.8)
        uw = int(360 * zoom)
        uh = int(460 * zoom)
        face_scaled = warped_pil.resize((uw, uh), Image.Resampling.LANCZOS)
        
        ux, uy = 540 - uw // 2, 400 - uh // 2
        
        # 3D Rotating Holographic Rings around Presenter
        ring_rx = int(uw * 0.65)
        ring_ry = int(uh * 0.22)
        ring_cy = uy + int(uh * 0.85)
        
        ring_angle = t * 4.0
        draw.arc([540 - ring_rx, ring_cy - ring_ry, 540 + ring_rx, ring_cy + ring_ry], 
                 start=int(math.degrees(ring_angle)) % 360, 
                 end=int(math.degrees(ring_angle) + 240) % 360, 
                 fill=(0, 242, 254), width=3)
                 
        # Paste 3D Warped User Portrait
        draw.rounded_rectangle([ux - 6, uy - 6, ux + uw + 6, uy + uh + 6], radius=20, outline=(0, 242, 254), width=3)
        img.paste(face_scaled, (ux, uy))
        
        # Presenter Tag
        draw.rounded_rectangle([ux + 25, uy + uh - 25, ux + uw - 25, uy + uh + 18], radius=8, fill=(11, 15, 22), outline=(0, 242, 254), width=2)
        draw.text((ux + 40, uy + uh - 20), "AMARESH DAS | 3D LIVE DEMO", font=get_font(18, bold=True), fill=(0, 242, 254))
        
        # =========================================================================
        # 2. ROTATING 3D SUBSTATION DIGITAL TWIN MODEL (RIGHT/LOWER STAGE)
        # =========================================================================
        # Hook Banner
        draw.rounded_rectangle([50, 660, 1030, 790], radius=14, fill=(18, 24, 38), outline=(0, 255, 140), width=3)
        draw.text((80, 680), "3D DIGITAL TWIN: 33kV TRANSFORMER & VCB", font=f_hook, fill=(0, 255, 140))
        draw.text((80, 740), "Real-time 3D vector rotation, flux density & 87T differential field", font=get_font(22, bold=False), fill=(240, 240, 240))
        
        # Left Panel: 3D Rotating Power Transformer Wireframe
        draw.rounded_rectangle([50, 820, 520, 1220], radius=16, fill=(14, 20, 30), outline=(0, 242, 254), width=2)
        draw.text((75, 840), "3D TRANSFORMER MODEL (Dyn11)", font=get_font(20, bold=True), fill=(0, 242, 254))
        
        # Animate 3D wireframe rotation
        rot_x = 0.35 + 0.1 * math.sin(t * 1.5)
        rot_y = t * 1.8
        rot_z = 0.1 * math.cos(t * 1.2)
        draw_3d_wireframe_cube(draw, cx=285, cy=1010, size=150, rot_x=rot_x, rot_y=rot_y, rot_z=rot_z, color=(0, 242, 254), width=2)
        draw.text((100, 1165), "CORE FLUX: 1.72 Tesla (NOMINAL)", font=get_font(18, bold=True), fill=(0, 255, 140))
        
        # Right Panel: 3D Rotating Polar Phasor Diagram
        draw.rounded_rectangle([560, 820, 1030, 1220], radius=16, fill=(14, 20, 30), outline=(255, 184, 0), width=2)
        draw.text((585, 840), "3D PHASOR VECTORS (30° LAG)", font=get_font(20, bold=True), fill=(255, 184, 0))
        
        pcx, pcy = 795, 1010
        draw.ellipse([pcx-100, pcy-100, pcx+100, pcy+100], outline=(35, 50, 75), width=2)
        draw.line([(pcx-110, pcy), (pcx+110, pcy)], fill=(35, 50, 75), width=1)
        draw.line([(pcx, pcy-110), (pcx, pcy+110)], fill=(35, 50, 75), width=1)
        
        # Rotating 3-phase vectors
        base_angle = t * 3.0
        phases = [
            ("R", base_angle, (255, 75, 75)),
            ("Y", base_angle - 2*math.pi/3, (255, 184, 0)),
            ("B", base_angle - 4*math.pi/3, (0, 242, 254))
        ]
        for name, ang, color in phases:
            px = int(pcx + 85 * math.cos(ang))
            py = int(pcy + 85 * math.sin(ang))
            draw.line([(pcx, pcy), (px, py)], fill=color, width=4)
            draw.text((px + 5, py - 10), name, font=get_font(20, bold=True), fill=color)
            
        draw.text((610, 1165), "VECTOR GROUP: Dyn11 (30° COMP)", font=get_font(18, bold=True), fill=(255, 184, 0))
        
        # =========================================================================
        # 3. LIVE 3D DEMONSTRATION CARDS (y=1250 to y=1630)
        # =========================================================================
        draw.rounded_rectangle([50, 1250, 1030, 1630], radius=16, fill=(14, 20, 30), outline=(0, 255, 140), width=2)
        draw.text((80, 1275), "LIVE 3D DEMONSTRATION MILESTONES", font=f_title, fill=(0, 255, 140))
        
        demo_points = [
            ("1. 3D Spatial Head Tracking", "Depth perspective warp tracking active at 30 fps", 1.0),
            ("2. Transformer Core Flux 3D", "Magnetization inrush cross-blocking active on 87T loop", 2.5),
            ("3. Dynamic 3-Phase Polar Vectors", "Dyn11 30° internal relay phase displacement compensated", 4.0),
            ("4. VCB Millisecond Interruption", "Arc quenched in 38ms with zero pole discrepancy", 5.5)
        ]
        
        dy = 1325
        for p_title, p_desc, pt in demo_points:
            if t >= pt:
                draw.rounded_rectangle([80, dy, 1000, dy + 62], radius=8, fill=(18, 30, 42), outline=(0, 255, 140), width=2)
                draw.text((100, dy + 10), f"[OK] {p_title}:", font=f_badge, fill=(0, 255, 140))
                draw.text((100, dy + 35), p_desc, font=f_body, fill=(220, 240, 250))
            else:
                draw.rounded_rectangle([80, dy, 1000, dy + 62], radius=8, fill=(12, 16, 24), outline=(30, 42, 55), width=1)
                draw.text((100, dy + 18), f"[...] SIMULATING: {p_title}...", font=f_body, fill=(90, 110, 130))
            dy += 72

        # =========================================================================
        # 4. CALL TO ACTION (6.5s+)
        # =========================================================================
        if t >= 6.5:
            draw.rectangle([0, 1660, 1080, 1920], fill=(10, 14, 22))
            draw.line([(0, 1660), (1080, 1660)], fill=(0, 242, 254), width=3)
            draw.rounded_rectangle([60, 1690, 1020, 1840], radius=18, fill=(18, 26, 40), outline=(0, 255, 140), width=4)
            draw.text((100, 1720), ">> COMMENT \"3D\" BELOW", font=get_font(42, bold=True), fill=(255, 255, 255))
            draw.text((100, 1780), "I'll DM you the complete 3D Substation Twin & Relay Protocol!", font=get_font(22, bold=False), fill=(0, 242, 254))
            draw.text((290, 1870), "proengineering.in | Senior Power Systems Lead", font=get_font(20, bold=False), fill=(180, 200, 220))
        else:
            draw.rectangle([0, 1780, 1080, 1920], fill=(10, 14, 22))
            draw.text((310, 1840), "3D LIVE LAB DEMONSTRATION | PROENGINEERING", font=get_font(20, bold=True), fill=(100, 130, 160))
            
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print(f"[SUCCESS] 3D Live Person Demo Reel rendered at: {out_path}")
    return out_path

if __name__ == "__main__":
    render_3d_live_demo_reel()
