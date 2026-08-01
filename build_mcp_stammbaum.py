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
HEIGHT = 1400 * SCALE

# 1. Base Canvas - Transparent with crisp rounded Light Panel (#ffffff / #f8fafc)
# Transparent PNG outer canvas allows native embedding; light card container provides contrast on both Light & Dark themes
base = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(base)

# Rounded white background panel for optimal presentation in GitHub Light & Dark modes
panel_margin = 12 * SCALE
draw.rounded_rectangle(
    [panel_margin, panel_margin, WIDTH - panel_margin, HEIGHT - panel_margin],
    radius=28 * SCALE,
    fill=(255, 255, 255, 255),
    outline=(226, 232, 240, 255),
    width=2 * SCALE
)

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

# Helper for drawing organic ink curves (Tusche-Stil) - Inverted Black Ink
def draw_ink_curve(draw_ctx, points, start_width, end_width, base_color=(15, 23, 42), opacity=220, num_strokes=10):
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
            
            cr = max(0, min(255, int(r + random.randint(-8, 8))))
            cg = max(0, min(255, int(g + random.randint(-8, 8))))
            cb = max(0, min(255, int(b + random.randint(-5, 8))))
            co = max(30, min(255, int(opacity + random.randint(-25, 15))))
            stroke_w = max(1, int(w * random.uniform(0.35, 0.65)))
            
            draw_ctx.line(
                [(int(p1[0] + dx1), int(p1[1] + dy1)), (int(p2[0] + dx2), int(p2[1] + dy2))],
                fill=(cr, cg, cb, co),
                width=stroke_w
            )

random.seed(20260801)

# Color Palette for Inverted Black Ink Tree Lineart
INK_MAIN = (15, 23, 42)       # Deep slate black ink (#0f172a)
INK_SHADOW = (71, 85, 105)    # Medium dark slate (#475569) for depth

# --- 1. HEADER / TITLE ---
title_text = "STAMMBAUM · MCP SERVER EVOLUTION"
subtitle_text = "Bottom-Up Evolution: Älteste Server unten (2026-02) → Jüngste Server oben (2026-07)"

tb = font_title.getbbox(title_text)
tw = tb[2] - tb[0]
draw.text(((WIDTH - tw)//2, 36 * SCALE), title_text, fill=(15, 23, 42, 255), font=font_title)

sb = font_subtitle.getbbox(subtitle_text)
sw = sb[2] - sb[0]
draw.text(((WIDTH - sw)//2, 72 * SCALE), subtitle_text, fill=(2, 132, 199, 255), font=font_subtitle)

# --- 2. TIMELINE HORIZON GUIDES ---
level_guides = [
    (1140, 1180, "UNTEN · ÄLTESTE MCP-SERVER (#1 — #4 · 2026-02 — 2026-03)", (5, 150, 105)),    # Emerald 600
    (750, 500, "MITTE · EXPANSION & CONTROL PLANE (#5 — #7 · 2026-05 — 2026-06)", (2, 132, 199)),   # Sky 600
    (360, 115, "OBEN · JÜNGSTE ZWEIGE (#8 — #9 · 2026-07)", (147, 51, 234))                        # Purple 600
]

for ly, label_y, ltxt, lcolor in level_guides:
    # Dashed horizon line across canvas
    ly_s = ly * SCALE
    for x in range(50 * SCALE, (1400 - 50) * SCALE, 24 * SCALE):
        draw.line([(x, ly_s), (x + 12 * SCALE, ly_s)], fill=(lcolor[0], lcolor[1], lcolor[2], 70), width=1 * SCALE)
    # Clean level title text positioned with zero collision
    draw.text((50 * SCALE, label_y * SCALE), ltxt, fill=(lcolor[0], lcolor[1], lcolor[2], 240), font=font_level)

# --- 3. BARE TREE SILHOUETTE (SCHWARZE TUSCHE STAMM & ÄSTE) ---

# Roots at ground (Y = 1340..1380)
roots = [
    [(700, 1340), (620, 1360), (500, 1375)],
    [(700, 1340), (780, 1360), (900, 1375)],
    [(700, 1340), (660, 1365), (590, 1380)],
    [(700, 1340), (740, 1365), (810, 1380)],
]
for rpt in roots:
    draw_ink_curve(draw, rpt, 24, 5, INK_MAIN, opacity=200, num_strokes=12)

# MAIN TRUNK (Stamm Y=1340 up to Y=1070)
draw_ink_curve(draw, [(700, 1340), (692, 1250), (708, 1160), (700, 1070)], 42, 28, INK_MAIN, opacity=240, num_strokes=22)
draw_ink_curve(draw, [(696, 1340), (688, 1250), (704, 1160), (696, 1070)], 22, 14, INK_SHADOW, opacity=160, num_strokes=12)

# BOTTOM BRANCHES (Y ≈ 1070 -> Nodes #1, #2, #3, #4)
draw_ink_curve(draw, [(700, 1070), (590, 1070), (480, 1070)], 20, 12, INK_MAIN, num_strokes=14)
draw_ink_curve(draw, [(480, 1070), (325, 1105), (170, 1140)], 12, 6, INK_MAIN, num_strokes=10)

draw_ink_curve(draw, [(700, 1070), (810, 1070), (920, 1070)], 20, 12, INK_MAIN, num_strokes=14)
draw_ink_curve(draw, [(920, 1070), (1075, 1105), (1230, 1140)], 12, 6, INK_MAIN, num_strokes=10)

# MID TRUNK CONTINUATION (Y=1070 up to Y=750)
draw_ink_curve(draw, [(700, 1070), (712, 960), (688, 850), (700, 750)], 26, 18, INK_MAIN, opacity=240, num_strokes=18)
draw_ink_curve(draw, [(696, 1070), (708, 960), (684, 850), (696, 750)], 14, 9, INK_SHADOW, opacity=150, num_strokes=10)

# MID BRANCHES (Y ≈ 750 -> Nodes #5, #6, #7)
draw_ink_curve(draw, [(700, 750), (475, 750), (250, 750)], 18, 8, INK_MAIN, num_strokes=14)
draw_ink_curve(draw, [(700, 750), (690, 710), (700, 680)], 16, 8, INK_MAIN, num_strokes=12)
draw_ink_curve(draw, [(700, 750), (925, 750), (1150, 750)], 18, 8, INK_MAIN, num_strokes=14)

# UPPER TRUNK CONTINUATION (Y=750 up to Y=360)
draw_ink_curve(draw, [(700, 750), (708, 620), (694, 480), (700, 360)], 16, 9, INK_MAIN, opacity=230, num_strokes=14)

# TOP CROWN BRANCHES (Y ≈ 360 -> Nodes #8, #9 & Bare Twigs)
draw_ink_curve(draw, [(700, 360), (525, 360), (350, 360)], 12, 6, INK_MAIN, num_strokes=10)
draw_ink_curve(draw, [(700, 360), (875, 360), (1050, 360)], 12, 6, INK_MAIN, num_strokes=10)

# BARE CROWN TWIGS
bare_twigs = [
    # Top Crown bare twigs
    [(700, 360), (680, 270), (660, 200)],
    [(700, 360), (720, 270), (740, 200)],
    [(680, 270), (700, 220), (690, 170)],
    [(720, 270), (700, 220), (710, 170)],
    [(350, 360), (310, 310), (280, 260)],
    [(1050, 360), (1090, 310), (1120, 260)],
    # Mid-height bare sub-twigs
    [(475, 750), (410, 700), (360, 660)],
    [(925, 750), (990, 700), (1040, 660)],
    [(690, 710), (630, 670), (590, 630)],
    [(690, 710), (750, 670), (790, 630)],
    # Lower bare sub-twigs
    [(590, 1070), (520, 1030), (470, 990)],
    [(810, 1070), (880, 1030), (930, 990)],
    [(325, 1105), (265, 1065), (215, 1025)],
    [(1075, 1105), (1135, 1065), (1185, 1025)]
]

for twg in bare_twigs:
    draw_ink_curve(draw, twg, 5, 1.5, INK_MAIN, opacity=180, num_strokes=6)

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
        'x': 170,
        'y': 1140,
        'level': 'bottom'
    },
    {
        'id': 'codecommander',
        'name': 'CodeCommander',
        'badge_name': '#2 codecommander',
        'date': '2026-02',
        'logo': 'logo-ellmos-codecommander.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-codecommander-mcp',
        'x': 480,
        'y': 1070,
        'level': 'bottom'
    },
    {
        'id': 'n8n-manager',
        'name': 'n8n Manager',
        'badge_name': '#3 n8n-manager',
        'date': '2026-02',
        'logo': 'logo-n8n-manager-mcp.jpg',
        'link': 'https://github.com/ellmos-ai/n8n-manager-mcp',
        'x': 920,
        'y': 1070,
        'level': 'bottom'
    },
    {
        'id': 'clatcher',
        'name': 'Clatcher',
        'badge_name': '#4 clatcher',
        'date': '2026-03',
        'logo': 'logo-clatcher.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-clatcher-mcp',
        'x': 1230,
        'y': 1140,
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
        'x': 250,
        'y': 750,
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
        'y': 680,
        'level': 'mid'
    },
    {
        'id': 'servercommander',
        'name': 'ServerCommander',
        'badge_name': '#7 servercommander',
        'date': '2026-06',
        'logo': 'logo-ellmos-servercommander.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-servercommander-mcp',
        'x': 1150,
        'y': 750,
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
        'x': 350,
        'y': 360,
        'level': 'top'
    },
    {
        'id': 'open-compute',
        'name': 'open-compute',
        'badge_name': '#9 open-compute',
        'date': '2026-07',
        'logo': 'wappen-open-compute-mcp.jpg',
        'link': 'https://github.com/ellmos-ai/open-compute-mcp',
        'x': 1050,
        'y': 360,
        'level': 'top'
    }
]

image_map_coords = []

# --- 5. COMPOSITE ENLARGED FRUIT LOGO NODES & BADGES ---
# Fruit box enlarged to 210px at 1x resolution (~1.46x enlargement from 144px, ~2.18x from original 96px)
BOX_SIZE = 210 * SCALE
INNER_SIZE = 175 * SCALE

for s in servers:
    nx, ny = int(s['x'] * SCALE), int(s['y'] * SCALE)
    
    # Connection dot on branch
    dot_r = 8 * SCALE
    draw.ellipse([nx-dot_r, ny-dot_r, nx+dot_r, ny+dot_r], fill=(2, 132, 199, 255), outline=(15, 23, 42, 255), width=2*SCALE)
    
    logo_path = os.path.join('profile', s['logo'])
    if not os.path.exists(logo_path):
        print(f"Warning: logo missing {logo_path}")
        continue
        
    logo_img = Image.open(logo_path).convert('RGBA')
    
    # Color accents based on level
    if s['level'] == 'bottom':
        border_col = (16, 185, 129, 255)   # Emerald 500
        glow_col = (16, 185, 129, 40)
    elif s['level'] == 'mid':
        border_col = (14, 165, 233, 255)   # Sky 500
        glow_col = (14, 165, 233, 40)
    else:
        border_col = (168, 85, 247, 255)   # Purple 500
        glow_col = (168, 85, 247, 40)
        
    # Fruit Node Frame (Enlarged to 210x210 px at 1x)
    box_w, box_h = BOX_SIZE, BOX_SIZE
    fruit_canvas = Image.new('RGBA', (box_w, box_h), (0, 0, 0, 0))
    fruit_draw = ImageDraw.Draw(fruit_canvas)
    
    # Soft drop shadow / glow behind fruit frame
    fruit_draw.rounded_rectangle(
        [3*SCALE, 3*SCALE, box_w-3*SCALE, box_h-3*SCALE],
        radius=32 * SCALE,
        fill=glow_col,
        outline=None
    )
    
    # Fruit Emblem Frame
    fruit_draw.rounded_rectangle(
        [2*SCALE, 2*SCALE, box_w-4*SCALE, box_h-4*SCALE],
        radius=28 * SCALE,
        fill=(255, 255, 255, 255),
        outline=border_col,
        width=5 * SCALE
    )
    
    # Inner logo fitting (175x175 px at 1x scale)
    logo_img.thumbnail((INNER_SIZE, INNER_SIZE), Image.Resampling.LANCZOS)
    
    mask = Image.new('L', logo_img.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, logo_img.size[0], logo_img.size[1]], radius=20 * SCALE, fill=255)
    
    px = (box_w - logo_img.size[0]) // 2
    py = (box_h - logo_img.size[1]) // 2
    fruit_canvas.paste(logo_img, (px, py), mask)
    
    # Stem line attaching fruit to branch node (fruit bottom sits 20px above node)
    stem_gap = 20 * SCALE
    fruit_bottom_y = ny - stem_gap
    fruit_top_y = fruit_bottom_y - box_h
    
    draw.line([(nx, ny), (nx, fruit_bottom_y)], fill=border_col, width=5 * SCALE)
    
    # Paste fruit onto main canvas
    fruit_left = nx - box_w//2
    fruit_top = fruit_top_y
    base.paste(fruit_canvas, (fruit_left, fruit_top), fruit_canvas)
    
    # Label Badge below fruit
    badge_title = s['badge_name']
    badge_sub = f"· {s['date']}"
    
    bt_box = font_badge_title.getbbox(badge_title)
    bt_w = bt_box[2] - bt_box[0]
    
    bs_box = font_badge_sub.getbbox(badge_sub)
    bs_w = bs_box[2] - bs_box[0]
    
    badge_w = max(bt_w + bs_w + 24 * SCALE, 160 * SCALE)
    badge_h = 34 * SCALE
    
    badge_center_x = nx
    badge_center_y = fruit_bottom_y + 24 * SCALE
    
    bx1 = badge_center_x - badge_w // 2
    by1 = badge_center_y - badge_h // 2
    bx2 = bx1 + badge_w
    by2 = by1 + badge_h
    
    # Badge container (light slate card with border)
    draw.rounded_rectangle(
        [bx1, by1, bx2, by2],
        radius=12 * SCALE,
        fill=(248, 250, 252, 255),
        outline=(203, 213, 225, 255),
        width=int(1.5 * SCALE)
    )
    
    # Text positioning in badge
    total_text_w = bt_w + 6 * SCALE + bs_w
    start_tx = badge_center_x - total_text_w // 2
    
    draw.text((start_tx, by1 + 7 * SCALE), badge_title, fill=(15, 23, 42, 255), font=font_badge_title)
    draw.text((start_tx + bt_w + 6 * SCALE, by1 + 8 * SCALE), badge_sub, fill=border_col[:3] + (255,), font=font_badge_sub)

    # Save 1x scaled bounding box for HTML area map (covering fruit node + badge)
    top_y_1x = fruit_top / SCALE
    bot_y_1x = by2 / SCALE
    left_x_1x = min(fruit_left / SCALE, bx1 / SCALE)
    right_x_1x = max((fruit_left + box_w) / SCALE, bx2 / SCALE)
    
    map_x1 = int(left_x_1x - 4)
    map_y1 = int(top_y_1x - 4)
    map_x2 = int(right_x_1x + 4)
    map_y2 = int(bot_y_1x + 4)
    
    image_map_coords.append((s['id'], s['name'], s['badge_name'], s['date'], s['link'], map_x1, map_y1, map_x2, map_y2))

# Resample down 2x with LANCZOS to 1400x1400 for crisp anti-aliased output
final_img = base.resize((1400, 1400), Image.Resampling.LANCZOS)

# Save to profile/assets/mcp-stammbaum.png
out_png = os.path.join(assets_dir, 'mcp-stammbaum.png')
final_img.save(out_png, 'PNG', optimize=True)

print(f"Generated {out_png} successfully!")

print("\nGenerated Image Map HTML:")
for mc in image_map_coords:
    print(f'    <area shape="rect" coords="{mc[5]},{mc[6]},{mc[7]},{mc[8]}" href="{mc[4]}" alt="{mc[1]}" title="{mc[1]} — {mc[2]} · {mc[3]}">')
