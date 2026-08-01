import os
import math
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

os.makedirs('profile', exist_ok=True)
assets_dir = os.path.join('profile', 'assets')
os.makedirs(assets_dir, exist_ok=True)

WIDTH = 1440
HEIGHT = 820

# 1. Base Image - Dark Theme (#0d1117)
base = Image.new('RGBA', (WIDTH, HEIGHT), (13, 17, 23, 255))
draw = ImageDraw.Draw(base)

# Load fonts
try:
    font_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 16)
    font_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 12)
    font_anno = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 14)
    font_trunk = ImageFont.truetype('C:/Windows/Fonts/georgia.ttf', 15)
except Exception:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_anno = font_title
    font_trunk = font_title

# Helper for colored-pencil stroke drawing
def draw_pencil_line(draw_ctx, p1, p2, width, base_color, num_strokes=8, opacity=130):
    x1, y1 = p1
    x2, y2 = p2
    length = math.hypot(x2 - x1, y2 - y1)
    if length == 0:
        return
    
    r, g, b = base_color
    
    for i in range(num_strokes):
        dx1 = random.uniform(-width * 0.35, width * 0.35)
        dy1 = random.uniform(-width * 0.35, width * 0.35)
        dx2 = random.uniform(-width * 0.35, width * 0.35)
        dy2 = random.uniform(-width * 0.35, width * 0.35)
        
        cr = max(0, min(255, r + random.randint(-30, 30)))
        cg = max(0, min(255, g + random.randint(-25, 25)))
        cb = max(0, min(255, b + random.randint(-20, 20)))
        co = max(20, min(255, opacity + random.randint(-35, 35)))
        
        stroke_w = max(1, int(width * random.uniform(0.2, 0.45)))
        draw_ctx.line(
            [(x1 + dx1, y1 + dy1), (x2 + dx2, y2 + dy2)],
            fill=(cr, cg, cb, co),
            width=stroke_w
        )

# Helper for curved pencil path
def draw_pencil_curve(draw_ctx, points, start_width, end_width, base_color, num_strokes=10):
    steps = 80
    curve_pts = []
    for i in range(steps + 1):
        t = i / steps
        if len(points) == 3:
            p0, p1, p2 = points
            x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
            y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
        elif len(points) == 4:
            p0, p1, p2, p3 = points
            x = (1-t)**3 * p0[0] + 3*(1-t)**2*t * p1[0] + 3*(1-t)*t**2 * p2[0] + t**3 * p3[0]
            y = (1-t)**3 * p0[1] + 3*(1-t)**2*t * p1[1] + 3*(1-t)*t**2 * p2[0] + t**3 * p3[0]
        else:
            x = (1-t)*points[0][0] + t*points[-1][0]
            y = (1-t)*points[0][1] + t*points[-1][1]
        curve_pts.append((x, y))
        
    for i in range(len(curve_pts) - 1):
        t = i / len(curve_pts)
        w = start_width * (1 - t) + end_width * t
        draw_pencil_line(draw_ctx, curve_pts[i], curve_pts[i+1], w, base_color, num_strokes=num_strokes)

random.seed(20260801)

BROWN_DARK = (74, 46, 24)     # Umber
BROWN_MID = (139, 90, 43)     # Terracotta / Sienna
BROWN_LIGHT = (205, 133, 63)  # Ochre pencil highlight
BROWN_BARK = (110, 71, 32)
LEAF_GREEN = (46, 160, 67)
LEAF_LIGHT = (74, 222, 128)

# --- 1. DRAW TRUNK (STAMM) ---
# Roots at bottom left
draw_pencil_curve(draw, [(50, 810), (90, 790), (140, 765)], 24, 38, BROWN_DARK, num_strokes=14)
draw_pencil_curve(draw, [(100, 815), (130, 790), (145, 765)], 20, 32, BROWN_MID, num_strokes=12)
draw_pencil_curve(draw, [(220, 815), (185, 790), (150, 765)], 20, 32, BROWN_DARK, num_strokes=12)

# Trunk rising from root (145, 765) up to bend (175, 520)
draw_pencil_curve(
    draw,
    [(145, 765), (132, 670), (148, 590), (175, 520)],
    start_width=45,
    end_width=28,
    base_color=BROWN_MID,
    num_strokes=22
)
draw_pencil_curve(
    draw,
    [(140, 765), (128, 670), (142, 590), (170, 520)],
    start_width=22,
    end_width=14,
    base_color=BROWN_DARK,
    num_strokes=14
)
draw_pencil_curve(
    draw,
    [(150, 755), (140, 665), (154, 585), (180, 515)],
    start_width=14,
    end_width=8,
    base_color=BROWN_LIGHT,
    num_strokes=12
)

# --- 2. MAIN BRANCH (HAUPTAST) ---
main_branch_pts = [(175, 520), (350, 505), (750, 500), (1150, 510), (1390, 520)]
draw_pencil_curve(
    draw,
    main_branch_pts,
    start_width=28,
    end_width=8,
    base_color=BROWN_MID,
    num_strokes=24
)
draw_pencil_curve(
    draw,
    main_branch_pts,
    start_width=14,
    end_width=4,
    base_color=BROWN_DARK,
    num_strokes=14
)
draw_pencil_curve(
    draw,
    main_branch_pts,
    start_width=10,
    end_width=3,
    base_color=BROWN_LIGHT,
    num_strokes=12
)

# Servers array with organic branch tips & high/low stagger
servers = [
    {
        'id': 'filecommander',
        'name': 'FileCommander',
        'date': '1. Früh (2024)',
        'logo': 'logo-ellmos-filecommander.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-filecommander-mcp',
        'x': 165,
        'y_tip': 250,
        'node_x': 175,
        'node_y': 520
    },
    {
        'id': 'codecommander',
        'name': 'CodeCommander',
        'date': '2. 2024',
        'logo': 'logo-ellmos-codecommander.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-codecommander-mcp',
        'x': 310,
        'y_tip': 335,
        'node_x': 315,
        'node_y': 508
    },
    {
        'id': 'n8n-manager',
        'name': 'n8n Manager',
        'date': '3. 2024',
        'logo': 'logo-n8n-manager-mcp.jpg',
        'link': 'https://github.com/ellmos-ai/n8n-manager-mcp',
        'x': 455,
        'y_tip': 250,
        'node_x': 460,
        'node_y': 502
    },
    {
        'id': 'clatcher',
        'name': 'Clatcher',
        'date': '4. 2025',
        'logo': 'logo-clatcher.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-clatcher-mcp',
        'x': 600,
        'y_tip': 335,
        'node_x': 605,
        'node_y': 500
    },
    {
        'id': 'controlcenter',
        'name': 'ControlCenter',
        'date': '5. 2025 (Trunk Hub)',
        'logo': 'logo-ellmos-controlcenter.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-controlcenter-mcp',
        'x': 745,
        'y_tip': 250,
        'node_x': 750,
        'node_y': 500
    },
    {
        'id': 'homebase',
        'name': 'Homebase',
        'date': '6. 2025',
        'logo': 'logo-ellmos-homebase.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-homebase-mcp',
        'x': 890,
        'y_tip': 335,
        'node_x': 895,
        'node_y': 503
    },
    {
        'id': 'servercommander',
        'name': 'ServerCommander',
        'date': '7. 2025',
        'logo': 'logo-ellmos-servercommander.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-servercommander-mcp',
        'x': 1035,
        'y_tip': 250,
        'node_x': 1040,
        'node_y': 507
    },
    {
        'id': 'blender-use',
        'name': 'Blender Use',
        'date': '8. 2026',
        'logo': 'logo-ellmos-blender-use.jpg',
        'link': 'https://github.com/ellmos-ai/ellmos-blender-use-mcp',
        'x': 1180,
        'y_tip': 335,
        'node_x': 1185,
        'node_y': 512
    },
    {
        'id': 'open-compute',
        'name': 'open-compute',
        'date': '9. Spät (2026)',
        'logo': 'wappen-open-compute-mcp.jpg',
        'link': 'https://github.com/ellmos-ai/open-compute-mcp',
        'x': 1320,
        'y_tip': 250,
        'node_x': 1325,
        'node_y': 517
    }
]

# --- 3. SIDE BRANCHES (NEBENÄSTE) ---
for s in servers:
    nx, ny = s['node_x'], s['node_y']
    tx, ty = s['x'], s['y_tip']
    
    # Node dot ● on main branch
    draw.ellipse([nx-6, ny-6, nx+6, ny+6], fill=(160, 82, 45, 240), outline=(210, 140, 70, 255), width=2)
    
    # Side branch curving upwards to tip with slight organic curve
    mid_x = nx + (tx - nx) * 0.5 + (-15 if (tx < nx) else 10)
    mid_y = ny - (ny - ty) * 0.55
    branch_pts = [(nx, ny), (mid_x, mid_y), (tx, ty)]
    
    draw_pencil_curve(
        draw,
        branch_pts,
        start_width=12,
        end_width=4,
        base_color=BROWN_MID,
        num_strokes=12
    )
    draw_pencil_curve(
        draw,
        branch_pts,
        start_width=6,
        end_width=2,
        base_color=BROWN_DARK,
        num_strokes=8
    )

# --- 4. DRAW ANNOTATIONS & LABELS ---
# Trunk Label ("STAMM")
draw.text((115, 770), "STAMM", fill=(210, 140, 70, 255), font=font_trunk)
draw.text((90, 792), "(braun, kahl, Wurzel)", fill=(140, 140, 140, 200), font=font_sub)

# Clean ASCII Main Branch Arrow & Description
draw.text((320, 532), "--- HAUPTAST ------------------------------------------------------------>", fill=(180, 120, 60, 220), font=font_anno)
draw.text((450, 555), "Entstehungsreihenfolge (früh links --> spät rechts)", fill=(56, 189, 248, 240), font=font_anno)

# --- 5. COMPOSITE LEAF LOGOS & SERVER NAMES ---
for idx, s in enumerate(servers):
    lx = s['x']
    ly = s['y_tip'] - 50 # center of leaf frame
    
    logo_path = os.path.join('profile', s['logo'])
    if not os.path.exists(logo_path):
        continue
        
    logo_img = Image.open(logo_path).convert('RGBA')
    
    box_w, box_h = 104, 104
    leaf_canvas = Image.new('RGBA', (box_w, box_h), (0, 0, 0, 0))
    leaf_draw = ImageDraw.Draw(leaf_canvas)
    
    # Leaf frame: Leaf shape mask with green border
    # Green leaf outline (#2ea043), background (#161b22)
    leaf_draw.rounded_rectangle(
        [2, 2, box_w-2, box_h-2],
        radius=24,
        fill=(22, 27, 34, 240),
        outline=(46, 160, 67, 255),
        width=3
    )
    
    # Draw leaf vein decoration at top
    leaf_draw.line([(box_w//2, 2), (box_w//2, 12)], fill=(74, 222, 128, 255), width=3)
    
    # Fit logo inside leaf frame
    inner_w, inner_h = 84, 84
    logo_img.thumbnail((inner_w, inner_h), Image.Resampling.LANCZOS)
    
    mask = Image.new('L', logo_img.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, logo_img.size[0], logo_img.size[1]], radius=14, fill=255)
    
    pos_x = (box_w - logo_img.size[0]) // 2
    pos_y = (box_h - logo_img.size[1]) // 2
    leaf_canvas.paste(logo_img, (pos_x, pos_y), mask)
    
    # Draw Leaf Stem connecting branch tip to top of leaf
    draw.line([(lx, ly - box_h//2), (s['x'], s['y_tip'])], fill=(46, 160, 67, 255), width=3)
    
    # Paste leaf canvas onto main base image
    base.paste(leaf_canvas, (lx - box_w//2, ly - box_h//2), leaf_canvas)
    
    # Draw Server Title & Subtitle Badge above leaf
    title = s['name']
    subtitle = f"#{idx+1} · {s['date'].split('.')[1].strip()}"
    
    t_box = font_title.getbbox(title)
    t_w = t_box[2] - t_box[0]
    
    sub_box = font_sub.getbbox(subtitle)
    sub_w = sub_box[2] - sub_box[0]
    
    title_x = lx - t_w // 2
    title_y = ly - box_h//2 - 38
    
    sub_x = lx - sub_w // 2
    sub_y = ly - box_h//2 - 20
    
    badge_w = max(t_w, sub_w) + 16
    badge_h = 36
    badge_x1 = lx - badge_w // 2
    badge_y1 = title_y - 3
    
    draw.rounded_rectangle(
        [badge_x1, badge_y1, badge_x1 + badge_w, badge_y1 + badge_h],
        radius=8,
        fill=(13, 17, 23, 235),
        outline=(48, 54, 61, 200),
        width=1
    )
    
    draw.text((title_x, title_y), title, fill=(240, 246, 252, 255), font=font_title)
    draw.text((sub_x, sub_y), subtitle, fill=(56, 189, 248, 255), font=font_sub)

# Save images to profile/mcp-tree.png & profile/assets/mcp-tree.png
output_path = os.path.join('profile', 'mcp-tree.png')
base.save(output_path, 'PNG', optimize=True)

output_path_assets = os.path.join(assets_dir, 'mcp-tree.png')
base.save(output_path_assets, 'PNG', optimize=True)

print(f"Generated {output_path} and {output_path_assets} successfully!")
