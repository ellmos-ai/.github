import os
import math
import random
from PIL import Image, ImageDraw, ImageFont

os.makedirs('profile', exist_ok=True)
assets_dir = os.path.join('profile', 'assets')
os.makedirs(assets_dir, exist_ok=True)

# 2x Supersampled resolution for ultra-sharp organic ink lineart
SCALE = 2
WIDTH = 1400 * SCALE
HEIGHT = 1350 * SCALE

# 1. Base Canvas - GitHub Dark Theme (#0d1117)
base = Image.new('RGBA', (WIDTH, HEIGHT), (13, 17, 23, 255))
draw = ImageDraw.Draw(base)

# Load fonts (scaled 2x)
try:
    font_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 24 * SCALE)
    font_subtitle = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 14 * SCALE)
    font_badge_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 14 * SCALE)
    font_badge_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 12 * SCALE)
    font_level = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 13 * SCALE)
except Exception:
    font_title = ImageFont.load_default()
    font_subtitle = font_title
    font_badge_title = font_title
    font_badge_sub = font_title
    font_level = font_title

# Correct Bezier curve calculation
def get_bezier_curve(points, steps=120):
    curve = []
    for i in range(steps + 1):
        t = i / steps
        if len(points) == 2:
            p0, p1 = points
            x = (1-t) * p0[0] + t * p1[0]
            y = (1-t) * p0[1] + t * p1[1]
        elif len(points) == 3:
            p0, p1, p2 = points
            x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
            y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
        elif len(points) == 4:
            p0, p1, p2, p3 = points
            x = (1-t)**3 * p0[0] + 3*(1-t)**2*t * p1[0] + 3*(1-t)*t**2 * p2[0] + t**3 * p3[0]
            y = (1-t)**3 * p0[1] + 3*(1-t)**2*t * p1[1] + 3*(1-t)*t**2 * p2[1] + t**3 * p3[1]
        else:
            x = (1-t)*points[0][0] + t*points[-1][0]
            y = (1-t)*points[0][1] + t*points[-1][1]
        curve.append((x * SCALE, y * SCALE))
    return curve

# Helper for drawing organic ink curves (Tusche-Stil)
def draw_ink_curve(draw_ctx, points, start_width, end_width, base_color=(230, 238, 248), opacity=220, num_strokes=10):
    curve_pts = get_bezier_curve(points, steps=120)
    r, g, b = base_color
    s_width = start_width * SCALE
    e_width = end_width * SCALE
    
    for i in range(len(curve_pts) - 1):
        t = i / len(curve_pts)
        w = max(1.5, s_width * (1 - t) + e_width * t)
        p1 = curve_pts[i]
        p2 = curve_pts[i+1]
        
        # Layered multi-stroke drawing for organic Tusche lineart
        for s in range(num_strokes):
            jitter_w = w * random.uniform(0.05, 0.22)
            dx1 = random.uniform(-jitter_w, jitter_w)
            dy1 = random.uniform(-jitter_w, jitter_w)
            dx2 = random.uniform(-jitter_w, jitter_w)
            dy2 = random.uniform(-jitter_w, jitter_w)
            
            cr = max(0, min(255, int(r + random.randint(-10, 10))))
            cg = max(0, min(255, int(g + random.randint(-10, 10))))
            cb = max(0, min(255, int(b + random.randint(-5, 10))))
            co = max(30, min(255, int(opacity + random.randint(-25, 15))))
            stroke_w = max(1, int(w * random.uniform(0.35, 0.65)))
            
            draw_ctx.line(
                [(int(p1[0] + dx1), int(p1[1] + dy1)), (int(p2[0] + dx2), int(p2[1] + dy2))],
                fill=(cr, cg, cb, co),
                width=stroke_w
            )

random.seed(20260801)

# Color Palette for Bare Tree Ink Lineart
INK_MAIN = (232, 240, 250)
INK_SHADOW = (130, 148, 170)

# --- 1. HEADER / TITLE ---
title_text = "STAMMBAUM · MCP SERVER EVOLUTION"
subtitle_text = "Bottom-Up Evolution: Älteste Server unten (2026-02) → Jüngste Server oben (2026-07)"

tb = font_title.getbbox(title_text)
tw = tb[2] - tb[0]
draw.text(((WIDTH - tw)//2, 42 * SCALE), title_text, fill=(240, 246, 252, 255), font=font_title)

sb = font_subtitle.getbbox(subtitle_text)
sw = sb[2] - sb[0]
draw.text(((WIDTH - sw)//2, 80 * SCALE), subtitle_text, fill=(56, 189, 248, 230), font=font_subtitle)

# --- 2. TIMELINE HORIZON GUIDES ---
# Non-colliding label Y coordinates
level_guides = [
    (1020, 1070, "UNTEN · ÄLTESTE MCP-SERVER (#1 — #4 · 2026-02 — 2026-03)", (52, 211, 153)),
    (640, 460, "MITTE · EXPANSION & CONTROL PLANE (#5 — #7 · 2026-05 — 2026-06)", (56, 189, 248)),
    (280, 160, "OBEN · JÜNGSTE ZWEIGE (#8 — #9 · 2026-07)", (192, 132, 252))
]

for ly, label_y, ltxt, lcolor in level_guides:
    # Dashed horizon line across canvas
    ly_s = ly * SCALE
    for x in range(60 * SCALE, (1400 - 60) * SCALE, 24 * SCALE):
        draw.line([(x, ly_s), (x + 12 * SCALE, ly_s)], fill=(lcolor[0], lcolor[1], lcolor[2], 40), width=1 * SCALE)
    # Clean level title text
    draw.text((70 * SCALE, label_y * SCALE), ltxt, fill=(lcolor[0], lcolor[1], lcolor[2], 210), font=font_level)

# --- 3. BARE TREE SILHOUETTE (TUSCHE-STAMM & ÄSTE) ---

# Roots at ground (Y = 1310..1350)
roots = [
    [(700, 1310), (620, 1330), (500, 1345)],
    [(700, 1310), (780, 1330), (900, 1345)],
    [(700, 1310), (660, 1335), (590, 1350)],
    [(700, 1310), (740, 1335), (810, 1350)],
]
for rpt in roots:
    draw_ink_curve(draw, rpt, 24, 5, INK_MAIN, opacity=200, num_strokes=12)

# MAIN TRUNK (Stamm Y=1310 up to Y=980)
draw_ink_curve(draw, [(700, 1310), (692, 1200), (708, 1100), (700, 980)], 42, 28, INK_MAIN, opacity=230, num_strokes=22)
draw_ink_curve(draw, [(696, 1310), (688, 1200), (704, 1100), (696, 980)], 22, 14, INK_SHADOW, opacity=160, num_strokes=12)

# BOTTOM BRANCHES (Y ≈ 980 -> Nodes #1, #2, #3, #4)
draw_ink_curve(draw, [(700, 980), (600, 950), (500, 930)], 20, 12, INK_MAIN, num_strokes=14)
draw_ink_curve(draw, [(500, 930), (340, 940), (180, 970)], 12, 6, INK_MAIN, num_strokes=10)

draw_ink_curve(draw, [(700, 980), (800, 950), (900, 930)], 20, 12, INK_MAIN, num_strokes=14)
draw_ink_curve(draw, [(900, 930), (1060, 940), (1220, 970)], 12, 6, INK_MAIN, num_strokes=10)

# MID TRUNK CONTINUATION (Y=980 up to Y=640)
draw_ink_curve(draw, [(700, 980), (712, 860), (688, 740), (700, 640)], 26, 18, INK_MAIN, opacity=230, num_strokes=18)
draw_ink_curve(draw, [(696, 980), (708, 860), (684, 740), (696, 640)], 14, 9, INK_SHADOW, opacity=150, num_strokes=10)

# MID BRANCHES (Y ≈ 640 -> Nodes #5, #6, #7)
draw_ink_curve(draw, [(700, 640), (490, 610), (280, 590)], 18, 8, INK_MAIN, num_strokes=14)
draw_ink_curve(draw, [(700, 640), (690, 570), (700, 510)], 16, 8, INK_MAIN, num_strokes=12)
draw_ink_curve(draw, [(700, 640), (910, 610), (1120, 590)], 18, 8, INK_MAIN, num_strokes=14)

# UPPER TRUNK CONTINUATION (Y=640 up to Y=320)
draw_ink_curve(draw, [(700, 640), (708, 520), (694, 420), (700, 320)], 16, 9, INK_MAIN, opacity=220, num_strokes=14)

# TOP CROWN BRANCHES (Y ≈ 320 -> Nodes #8, #9 & Bare Twigs)
draw_ink_curve(draw, [(700, 320), (560, 280), (420, 250)], 12, 6, INK_MAIN, num_strokes=10)
draw_ink_curve(draw, [(700, 320), (840, 280), (980, 250)], 12, 6, INK_MAIN, num_strokes=10)

# BARE CROWN TWIGS (Kahle Zweige fanning out naturally without leaves)
bare_twigs = [
    # Top Crown bare twigs
    [(700, 320), (680, 240), (660, 170)],
    [(700, 320), (720, 240), (740, 170)],
    [(680, 240), (700, 190), (690, 140)],
    [(720, 240), (700, 190), (710, 140)],
    [(420, 250), (380, 210), (350, 170)],
    [(980, 250), (1020, 210), (1050, 170)],
    # Mid-height bare sub-twigs
    [(490, 610), (430, 570), (380, 540)],
    [(910, 610), (970, 570), (1020, 540)],
    [(690, 570), (630, 540), (590, 510)],
    [(690, 570), (750, 540), (790, 510)],
    # Lower bare sub-twigs
    [(600, 950), (530, 910), (480, 870)],
    [(800, 950), (870, 910), (920, 870)],
    [(340, 940), (280, 900), (230, 870)],
    [(1060, 940), (1120, 900), (1170, 870)],
    [(708, 1100), (630, 1070), (560, 1050)],
    [(708, 1100), (770, 1070), (840, 1050)]
]

for twg in bare_twigs:
    draw_ink_curve(draw, twg, 5, 1.5, INK_MAIN, opacity=170, num_strokes=6)

# --- 4. SERVER DATA (BOTTOM TO TOP ORDER) ---
servers = [
    # UNTEN (Bottom - Älteste)
    {
        'id': 'filecommander',
        'name': 'FileCommander',
        'badge_name': '#1 filecommander',
        'date': '2026-02',
        'logo': 'logo-ellmos-filecommander.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-filecommander-mcp',
        'x': 180,
        'y': 970,
        'level': 'bottom'
    },
    {
        'id': 'codecommander',
        'name': 'CodeCommander',
        'badge_name': '#2 codecommander',
        'date': '2026-02',
        'logo': 'logo-ellmos-codecommander.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-codecommander-mcp',
        'x': 500,
        'y': 930,
        'level': 'bottom'
    },
    {
        'id': 'n8n-manager',
        'name': 'n8n Manager',
        'badge_name': '#3 n8n-manager',
        'date': '2026-02',
        'logo': 'logo-n8n-manager-mcp.jpg',
        'link': 'https://github.com/ellmos-ai/n8n-manager-mcp',
        'x': 900,
        'y': 930,
        'level': 'bottom'
    },
    {
        'id': 'clatcher',
        'name': 'Clatcher',
        'badge_name': '#4 clatcher',
        'date': '2026-03',
        'logo': 'logo-clatcher.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-clatcher-mcp',
        'x': 1220,
        'y': 970,
        'level': 'bottom'
    },
    # MITTE (Middle - 2026-05 .. 2026-06)
    {
        'id': 'controlcenter',
        'name': 'ControlCenter',
        'badge_name': '#5 controlcenter',
        'date': '2026-05',
        'logo': 'logo-ellmos-controlcenter.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-controlcenter-mcp',
        'x': 280,
        'y': 590,
        'level': 'mid'
    },
    {
        'id': 'homebase',
        'name': 'Homebase',
        'badge_name': '#6 homebase',
        'date': '2026-06',
        'logo': 'logo-ellmos-homebase.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-homebase-mcp',
        'x': 700,
        'y': 510,
        'level': 'mid'
    },
    {
        'id': 'servercommander',
        'name': 'ServerCommander',
        'badge_name': '#7 servercommander',
        'date': '2026-06',
        'logo': 'logo-ellmos-servercommander.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-servercommander-mcp',
        'x': 1120,
        'y': 590,
        'level': 'mid'
    },
    # OBEN (Top - Jüngste 2026-07)
    {
        'id': 'blender-use',
        'name': 'Blender Use',
        'badge_name': '#8 blender-use',
        'date': '2026-07',
        'logo': 'logo-ellmos-blender-use.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-blender-use-mcp',
        'x': 420,
        'y': 250,
        'level': 'top'
    },
    {
        'id': 'open-compute',
        'name': 'open-compute',
        'badge_name': '#9 open-compute',
        'date': '2026-07',
        'logo': 'wappen-open-compute-mcp.jpg',
        'link': 'https://github.com/ellmos-ai/open-compute-mcp',
        'x': 980,
        'y': 250,
        'level': 'top'
    }
]

image_map_coords = []

# --- 5. COMPOSITE FRUIT LOGO NODES & BADGES ---
for s in servers:
    nx, ny = int(s['x'] * SCALE), int(s['y'] * SCALE)
    
    # Connection dot on branch
    dot_r = 7 * SCALE
    draw.ellipse([nx-dot_r, ny-dot_r, nx+dot_r, ny+dot_r], fill=(56, 189, 248, 255), outline=(240, 246, 252, 255), width=2*SCALE)
    
    logo_path = os.path.join('profile', s['logo'])
    if not os.path.exists(logo_path):
        print(f"Warning: logo missing {logo_path}")
        continue
        
    logo_img = Image.open(logo_path).convert('RGBA')
    
    # Fruit Node Frame (Square with rounded corners / Fruit emblem)
    box_w, box_h = 96 * SCALE, 96 * SCALE
    fruit_canvas = Image.new('RGBA', (box_w, box_h), (0, 0, 0, 0))
    fruit_draw = ImageDraw.Draw(fruit_canvas)
    
    # Glow & Border based on level
    if s['level'] == 'bottom':
        border_col = (52, 211, 153, 255) # Emerald green
    elif s['level'] == 'mid':
        border_col = (56, 189, 248, 255) # Sky blue
    else:
        border_col = (192, 132, 252, 255) # Purple / Violet
        
    fruit_draw.rounded_rectangle(
        [2*SCALE, 2*SCALE, box_w-2*SCALE, box_h-2*SCALE],
        radius=18 * SCALE,
        fill=(22, 27, 34, 245),
        outline=border_col,
        width=3 * SCALE
    )
    
    # Inner logo fitting
    inner_w, inner_h = 76 * SCALE, 76 * SCALE
    logo_img.thumbnail((inner_w, inner_h), Image.Resampling.LANCZOS)
    
    mask = Image.new('L', logo_img.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, logo_img.size[0], logo_img.size[1]], radius=12 * SCALE, fill=255)
    
    px = (box_w - logo_img.size[0]) // 2
    py = (box_h - logo_img.size[1]) // 2
    fruit_canvas.paste(logo_img, (px, py), mask)
    
    # Stem line attaching fruit to branch node
    fruit_top_y = ny - 42 * SCALE
    draw.line([(nx, ny), (nx, fruit_top_y)], fill=border_col, width=3 * SCALE)
    
    # Paste fruit onto main canvas
    fruit_left = nx - box_w//2
    fruit_top = fruit_top_y - box_h//2
    base.paste(fruit_canvas, (fruit_left, fruit_top), fruit_canvas)
    
    # Label Badge below fruit
    badge_title = s['badge_name']
    badge_sub = f"· {s['date']}"
    
    bt_box = font_badge_title.getbbox(badge_title)
    bt_w = bt_box[2] - bt_box[0]
    
    bs_box = font_badge_sub.getbbox(badge_sub)
    bs_w = bs_box[2] - bs_box[0]
    
    badge_w = max(bt_w + bs_w + 16 * SCALE, 120 * SCALE)
    badge_h = 28 * SCALE
    
    badge_center_x = nx
    badge_center_y = fruit_top + box_h + 18 * SCALE
    
    bx1 = badge_center_x - badge_w // 2
    by1 = badge_center_y - badge_h // 2
    bx2 = bx1 + badge_w
    by2 = by1 + badge_h
    
    draw.rounded_rectangle(
        [bx1, by1, bx2, by2],
        radius=8 * SCALE,
        fill=(13, 17, 23, 245),
        outline=(48, 54, 61, 230),
        width=int(1.5 * SCALE)
    )
    
    # Text positioning in badge
    total_text_w = bt_w + 6 * SCALE + bs_w
    start_tx = badge_center_x - total_text_w // 2
    
    draw.text((start_tx, by1 + 5 * SCALE), badge_title, fill=(240, 246, 252, 255), font=font_badge_title)
    draw.text((start_tx + bt_w + 6 * SCALE, by1 + 6 * SCALE), badge_sub, fill=border_col[:3] + (255,), font=font_badge_sub)

    # Save 1x scaled bounding box for HTML area map (covering fruit node + badge)
    map_x1 = int((bx1 - 4 * SCALE) / SCALE)
    map_y1 = int((fruit_top - 4 * SCALE) / SCALE)
    map_x2 = int((bx2 + 4 * SCALE) / SCALE)
    map_y2 = int((by2 + 4 * SCALE) / SCALE)
    image_map_coords.append((s['id'], s['name'], s['badge_name'], s['date'], s['link'], map_x1, map_y1, map_x2, map_y2))

# Resample down 2x with LANCZOS to 1400x1350 for crisp anti-aliased output
final_img = base.resize((1400, 1350), Image.Resampling.LANCZOS)

# Save to profile/assets/mcp-stammbaum.png
out_png = os.path.join(assets_dir, 'mcp-stammbaum.png')
final_img.save(out_png, 'PNG', optimize=True)

# Also save to profile/mcp-stammbaum.png
out_png_root = os.path.join('profile', 'mcp-stammbaum.png')
final_img.save(out_png_root, 'PNG', optimize=True)

print(f"Generated {out_png} and {out_png_root} successfully!")

print("\nGenerated Image Map HTML:")
for mc in image_map_coords:
    print(f'    <area shape="rect" coords="{mc[5]},{mc[6]},{mc[7]},{mc[8]}" href="{mc[4]}" alt="{mc[1]}" title="{mc[1]} — {mc[2]} · {mc[3]}">')
