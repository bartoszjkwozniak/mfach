import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_rounded_mask(size, radius):
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    return mask

def make_rounded_image(img, target_size, radius):
    img_ratio = img.width / img.height
    target_ratio = target_size[0] / target_size[1]
    
    if img_ratio > target_ratio:
        new_height = target_size[1]
        new_width = int(new_height * img_ratio)
    else:
        new_width = target_size[0]
        new_height = int(new_width / img_ratio)
        
    resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    left = (new_width - target_size[0]) // 2
    top = (new_height - target_size[1]) // 2
    cropped = resized.crop((left, top, left + target_size[0], top + target_size[1]))
    
    mask = create_rounded_mask(target_size, radius)
    rounded = Image.new('RGBA', target_size, (0, 0, 0, 0))
    rounded.paste(cropped.convert('RGBA'), (0, 0), mask)
    return rounded

def draw_map_pin(draw, x, y, h=22, color=(34, 211, 238)):
    # Crisp vector map pin (avoids missing emoji tofu boxes)
    r = h * 0.36
    cx = x + r
    cy = y + r
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)
    tip = (cx, y + h)
    p_left = (cx - r * 0.82, cy + r * 0.38)
    p_right = (cx + r * 0.82, cy + r * 0.38)
    draw.polygon([p_left, tip, p_right], fill=color)
    dot_r = r * 0.38
    draw.ellipse((cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r), fill=(11, 15, 25))

def generate_banner():
    width, height = 1920, 1080
    bg = Image.new('RGB', (width, height), (11, 15, 25))
    draw = ImageDraw.Draw(bg)
    
    # Ambient background glow spots
    glow1 = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    gdraw1 = ImageDraw.Draw(glow1)
    gdraw1.ellipse((50, 50, 550, 550), fill=(22, 163, 74, 40))
    glow1 = glow1.filter(ImageFilter.GaussianBlur(80))
    bg.paste(glow1, (100, -100), glow1)
    
    glow2 = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    gdraw2 = ImageDraw.Draw(glow2)
    gdraw2.ellipse((50, 50, 550, 550), fill=(8, 145, 178, 45))
    glow2 = glow2.filter(ImageFilter.GaussianBlur(80))
    bg.paste(glow2, (1200, 500), glow2)
    
    # Fonts
    font_logo = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 72)
    font_sub = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 24)
    font_phone = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 34)
    font_card_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 27)
    font_card_tag = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 16)
    font_card_body = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 19)
    font_badge = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 20)
    
    # 1. Header Section
    # Logo box: Blue square with "M", followed by text "FACH"
    draw.rounded_rectangle((80, 50, 155, 125), radius=14, fill=(37, 99, 235))
    draw.text((95, 45), "M", font=font_logo, fill=(255, 255, 255))
    draw.text((175, 48), "FACH", font=font_logo, fill=(248, 250, 252))
    draw.text((178, 124), "USŁUGI FACHOWE • MARCIN", font=font_sub, fill=(148, 163, 184))
    
    # Map & Coverage Pill in Header
    area_pill = (1160, 58, 1840, 120)
    draw.rounded_rectangle(area_pill, radius=31, fill=(26, 34, 52), outline=(8, 145, 178), width=2)
    
    if os.path.exists("assets/map.png"):
        map_img = Image.open("assets/map.png")
        map_thumb = map_img.resize((52, 52), Image.Resampling.LANCZOS)
        m_mask = Image.new('L', (52, 52), 0)
        ImageDraw.Draw(m_mask).ellipse((0, 0, 52, 52), fill=255)
        bg.paste(map_thumb, (1168, 63), m_mask)
        draw.ellipse((1168, 63, 1220, 115), outline=(34, 211, 238), width=2)
        draw.text((1230, 74), "OBSZAR DZIAŁANIA: KĘTRZYN I OKOLICE (DO 50 KM)", font=font_badge, fill=(34, 211, 238))
    else:
        draw_map_pin(draw, 1180, 75, h=24, color=(34, 211, 238))
        draw.text((1215, 74), "OBSZAR DZIAŁANIA: KĘTRZYN I OKOLICE (DO 50 KM)", font=font_badge, fill=(34, 211, 238))
    
    # 2. Main 4 Cards Section
    cards = [
        {
            "img_path": "assets/hero_agro.png",
            "tag": "ROLNICTWO",
            "title": "Ciągniki Rolnicze",
            "points": ["• Remonty silników i skrzyń", "• Hydraulika siłowa", "• Pneumatyka & hamulce", "• Mobilny dojazd w pole"],
            "color": (22, 163, 74),
            "accent": (74, 222, 128)
        },
        {
            "img_path": "assets/hero_auto.png",
            "tag": "MOTORYZACJA",
            "title": "Mechanika Aut",
            "points": ["• Wymiana oleju i filtrów", "• Układy hamulcowe", "• Zawieszenie & rozrządy", "• Diagnostyka komputerowa"],
            "color": (37, 99, 235),
            "accent": (56, 189, 248)
        },
        {
            "img_path": "assets/hero_remont.png",
            "tag": "REMONT DOMU",
            "title": "Wykończenia Wnętrz",
            "points": ["• Gładzie bezpyłowe", "• Precyzyjne malowanie", "• Układanie paneli & płytek", "• Zabudowy G-K & sufity"],
            "color": (234, 88, 12),
            "accent": (251, 146, 60)
        },
        {
            "img_path": "assets/hero_hydro.png",
            "tag": "INSTALACJE",
            "title": "Hydraulika & Kotłownie",
            "points": ["• Nowoczesne kotłownie", "• Pompy ciepła & obiegowe", "• Instalacje wod-kan", "• Biały montaż & Geberit"],
            "color": (8, 145, 178),
            "accent": (34, 211, 238)
        }
    ]
    
    card_w = 415
    card_h = 710
    start_x = 80
    gap = 26
    start_y = 190
    
    for i, card in enumerate(cards):
        cx = start_x + i * (card_w + gap)
        cy = start_y
        
        # Card Background
        card_bg = (22, 30, 46)
        draw.rounded_rectangle((cx, cy, cx + card_w, cy + card_h), radius=22, fill=card_bg, outline=card["color"], width=3)
        
        # Image
        if os.path.exists(card["img_path"]):
            cimg = Image.open(card["img_path"])
            thumb_w = card_w - 24
            thumb_h = 320
            rounded_thumb = make_rounded_image(cimg, (thumb_w, thumb_h), radius=16)
            bg.paste(rounded_thumb, (cx + 12, cy + 12), rounded_thumb)
        
        # Colored Top accent tag with dynamic width
        tag_w = draw.textlength(card["tag"], font=font_card_tag)
        pad_x = 16
        draw.rounded_rectangle((cx + 14, cy + 348, cx + 14 + int(tag_w) + pad_x * 2, cy + 378), radius=14, fill=card["color"])
        draw.text((cx + 14 + pad_x, cy + 353), card["tag"], font=font_card_tag, fill=(255, 255, 255))
        
        # Card Title
        draw.text((cx + 18, cy + 392), card["title"], font=font_card_title, fill=(248, 250, 252))
        
        # Separator line
        draw.line((cx + 18, cy + 440, cx + card_w - 18, cy + 440), fill=(255, 255, 255, 30), width=1)
        
        # Points (well spaced, no unnecessary repeated guarantee badges)
        py = cy + 468
        for pt in card["points"]:
            draw.text((cx + 20, py), pt, font=font_card_body, fill=(226, 232, 240))
            py += 48
            
    # 3. Bottom Big Contact Bar
    footer_bbox = (80, 930, 1840, 1025)
    draw.rounded_rectangle(footer_bbox, radius=24, fill=(17, 24, 39), outline=(56, 189, 248), width=2)
    
    # Phone button inside footer - perfectly sized & centered with generous margins
    call_btn_box = (1260, 945, 1820, 1015)
    draw.rounded_rectangle(call_btn_box, radius=35, fill=(22, 163, 74), outline=(74, 222, 128), width=2)
    
    call_txt = "ZADZWOŃ: 695 525 389"
    tw = draw.textlength(call_txt, font=font_phone)
    call_tx = 1260 + (560 - tw) / 2
    draw.text((call_tx, 958), call_txt, font=font_phone, fill=(255, 255, 255))
    
    # Footer Left text
    font_footer_main = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 30)
    font_footer_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 19)
    draw.text((120, 946), "Potrzebujesz solidnej naprawy, remontu lub instalacji?", font=font_footer_main, fill=(248, 250, 252))
    draw.text((120, 986), "Dojazd mobilny: Kętrzyn, Mrągowo, Giżycko, Węgorzewo, Reszel, Bartoszyce i okolice", font=font_footer_sub, fill=(148, 163, 184))
    
    bg.save("assets/infographic_banner.png", quality=95)
    print("Banner generated successfully!")

def generate_circle_quad():
    width, height = 1200, 1200
    bg = Image.new('RGB', (width, height), (11, 15, 25))
    draw = ImageDraw.Draw(bg)
    
    # Fonts
    font_med_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 28)
    font_center_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 44)
    font_center_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 20)
    font_center_phone = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 36)
    font_quad_tag = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 15)
    font_quad_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 17)
    font_point = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 16)
    font_badge_bold = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 19)
    
    # Symmetrically aligned quadrants (all text and images pushed to outer edges away from center hub)
    quads = [
        # Top-Left: Agro
        {
            "img_path": "assets/hero_agro.png",
            "box": (45, 45, 575, 575),
            "thumb_box": (65, 205, 385, 555),
            "tag": "1. ROLNICTWO & AGRO",
            "title": "Ciągniki Rolnicze",
            "sub": "Silniki • Skrzynie • Hydraulika",
            "points": ["• Remonty silników", "• Hydraulika siłowa", "• Dojazd w pole"],
            "points_pos": (405, 220),
            "color": (22, 163, 74),
            "text_x": 65,
            "text_y": 65
        },
        # Top-Right: Auto
        {
            "img_path": "assets/hero_auto.png",
            "box": (625, 45, 1155, 575),
            "thumb_box": (815, 205, 1135, 555),
            "tag": "2. MECHANIKA AUT",
            "title": "Mechanika Samochodowa",
            "sub": "Olej & filtry • Hamulce • Rozrządy",
            "points": ["• Układy hamulcowe", "• Diagnostyka komputerowa", "• Zawieszenie"],
            "points_pos": (645, 220),
            "color": (37, 99, 235),
            "text_x": 645,
            "text_y": 65
        },
        # Bottom-Left: Remonty
        {
            "img_path": "assets/hero_remont.png",
            "box": (45, 625, 575, 1155),
            "thumb_box": (65, 645, 385, 995),
            "tag": "3. REMONTY DOMÓW",
            "title": "Wykończenia Wnętrz",
            "sub": "Gładzie • Malowanie • Panele • G-K",
            "points": ["• Gładzie bezpyłowe", "• Malowanie ścian", "• Układanie paneli"],
            "points_pos": (405, 830),
            "color": (234, 88, 12),
            "text_x": 65,
            "text_y": 1015
        },
        # Bottom-Right: Hydraulika
        {
            "img_path": "assets/hero_hydro.png",
            "box": (625, 625, 1155, 1155),
            "thumb_box": (815, 645, 1135, 995),
            "tag": "4. HYDRAULIKA & KOTŁOWNIE",
            "title": "Hydraulika & Kotłownie",
            "sub": "Pompy ciepła • Wod-kan • Biały montaż",
            "points": ["• Nowoczesne kotłownie", "• Pompy ciepła & obieg", "• Instalacje wod-kan"],
            "points_pos": (645, 830),
            "color": (8, 145, 178),
            "text_x": 645,
            "text_y": 1015
        }
    ]
    
    # Draw Quadrant Cards
    for q in quads:
        bx1, by1, bx2, by2 = q["box"]
        draw.rounded_rectangle((bx1, by1, bx2, by2), radius=28, fill=(20, 27, 43), outline=q["color"], width=3)
        
        # Image Thumbnail (completely outside center circle zone)
        if os.path.exists(q["img_path"]):
            cimg = Image.open(q["img_path"])
            tx1, ty1, tx2, ty2 = q["thumb_box"]
            tw, th = tx2 - tx1, ty2 - ty1
            rounded_thumb = make_rounded_image(cimg, (tw, th), radius=20)
            bg.paste(rounded_thumb, (tx1, ty1), rounded_thumb)
            draw.rounded_rectangle((tx1, ty1, tx2, ty2), radius=20, outline=q["color"], width=2)
            
        # Header text (Tag, Title, Subtitle) - positioned safely in outer margins
        tx = q["text_x"]
        ty = q["text_y"]
        tag_w = draw.textlength(q["tag"], font=font_quad_tag)
        draw.rounded_rectangle((tx, ty, tx + int(tag_w) + 24, ty + 28), radius=12, fill=q["color"])
        draw.text((tx + 12, ty + 4), q["tag"], font=font_quad_tag, fill=(255, 255, 255))
        draw.text((tx, ty + 38), q["title"], font=font_med_title, fill=(248, 250, 252))
        draw.text((tx, ty + 78), q["sub"], font=font_quad_sub, fill=(148, 163, 184))
        
        # Bullet Points in safe corner zones
        px, py = q["points_pos"]
        for pt in q["points"]:
            draw.text((px, py), pt, font=font_point, fill=(203, 213, 225))
            py += 32

    # Center Emblem (Circle Hub - properly sized so it never covers any card elements)
    center_x = width // 2
    center_y = height // 2
    r = 185
    
    # Outer Glow Ring
    for ring_i in range(8):
        draw.ellipse((center_x - r - ring_i*2, center_y - r - ring_i*2, center_x + r + ring_i*2, center_y + r + ring_i*2), outline=(15, 23, 42))
        
    # Main Center Disk Background
    draw.ellipse((center_x - r, center_y - r, center_x + r, center_y + r), fill=(11, 15, 25), outline=(255, 255, 255), width=3)
    
    # Blended Map Texture inside Center Disk
    if os.path.exists("assets/map.png"):
        map_img = Image.open("assets/map.png").convert("RGBA")
        map_crop_size = (r * 2 - 8, r * 2 - 8)
        map_resized = map_img.resize(map_crop_size, Image.Resampling.LANCZOS)
        
        # Darken overlay so text is 100% legible
        dark_overlay = Image.new('RGBA', map_crop_size, (11, 15, 25, 175))
        map_blended = Image.alpha_composite(map_resized, dark_overlay)
        
        cmask = Image.new('L', map_crop_size, 0)
        ImageDraw.Draw(cmask).ellipse((0, 0, map_crop_size[0], map_crop_size[1]), fill=255)
        bg.paste(map_blended, (center_x - r + 4, center_y - r + 4), cmask)
    
    # 4-color segmented arc border
    draw.arc((center_x - r + 4, center_y - r + 4, center_x + r - 4, center_y + r - 4), start=180, end=270, fill=(22, 163, 74), width=8) # Agro
    draw.arc((center_x - r + 4, center_y - r + 4, center_x + r - 4, center_y + r - 4), start=270, end=360, fill=(37, 99, 235), width=8) # Auto
    draw.arc((center_x - r + 4, center_y - r + 4, center_x + r - 4, center_y + r - 4), start=90, end=180, fill=(234, 88, 12), width=8)  # Remont
    draw.arc((center_x - r + 4, center_y - r + 4, center_x + r - 4, center_y + r - 4), start=0, end=90, fill=(8, 145, 178), width=8)    # Hydro
    
    # Text in Center Disk (dynamically centered)
    txt_logo = "MFACH"
    w_logo = draw.textlength(txt_logo, font=font_center_title)
    draw.text((center_x - w_logo / 2, center_y - 118), txt_logo, font=font_center_title, fill=(255, 255, 255))
    
    txt_sub = "MARCIN • USŁUGI MOBILNE"
    w_sub = draw.textlength(txt_sub, font=font_center_sub)
    draw.text((center_x - w_sub / 2, center_y - 65), txt_sub, font=font_center_sub, fill=(226, 232, 240))
    
    # Phone Button Pill in Center
    pill_w = 320
    pill_h = 58
    pill_box = (center_x - pill_w // 2, center_y - 15, center_x + pill_w // 2, center_y - 15 + pill_h)
    draw.rounded_rectangle(pill_box, radius=29, fill=(22, 163, 74), outline=(74, 222, 128), width=2)
    
    txt_phone = "TEL. 695 525 389"
    w_phone = draw.textlength(txt_phone, font=font_center_phone)
    draw.text((center_x - w_phone / 2, center_y - 11), txt_phone, font=font_center_phone, fill=(255, 255, 255))
    
    # Area Badge in Center with crisp vector map pin
    txt_area = "KĘTRZYN I OKOLICE (DO 50 KM)"
    w_area = draw.textlength(txt_area, font=font_badge_bold)
    pin_w = 16
    pin_h = 22
    total_w = pin_w + 10 + w_area
    start_x = center_x - total_w / 2
    draw_map_pin(draw, start_x, center_y + 68, h=pin_h, color=(34, 211, 238))
    draw.text((start_x + pin_w + 10, center_y + 68), txt_area, font=font_badge_bold, fill=(34, 211, 238))
    
    bg.save("assets/infographic_circle.png", quality=95)
    print("Circle infographic generated successfully!")

if __name__ == '__main__':
    generate_banner()
    generate_circle_quad()
