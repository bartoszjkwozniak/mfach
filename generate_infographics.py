import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_rounded_mask(size, radius):
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    return mask

def make_rounded_image(img, target_size, radius):
    # Resize preserving aspect ratio (crop fill)
    img_ratio = img.width / img.height
    target_ratio = target_size[0] / target_size[1]
    
    if img_ratio > target_ratio:
        new_height = target_size[1]
        new_width = int(new_height * img_ratio)
    else:
        new_width = target_size[0]
        new_height = int(new_width / img_ratio)
        
    resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Center crop
    left = (new_width - target_size[0]) // 2
    top = (new_height - target_size[1]) // 2
    cropped = resized.crop((left, top, left + target_size[0], top + target_size[1]))
    
    # Apply rounded mask
    mask = create_rounded_mask(target_size, radius)
    rounded = Image.new('RGBA', target_size, (0, 0, 0, 0))
    rounded.paste(cropped.convert('RGBA'), (0, 0), mask)
    return rounded

def draw_glow_border(draw, bbox, color, border_width=3, radius=16):
    draw.rounded_rectangle(bbox, radius=radius, outline=color, width=border_width)

def generate_banner():
    width, height = 1920, 1080
    bg = Image.new('RGB', (width, height), (11, 15, 25))
    draw = ImageDraw.Draw(bg)
    
    # Gradient background glow spots
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
    font_phone = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 44)
    font_card_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 27)
    font_card_tag = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 16)
    font_card_body = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 18)
    font_badge = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 20)
    
    # 1. Header Section
    # Logo box
    draw.rounded_rectangle((80, 50, 155, 125), radius=14, fill=(37, 99, 235))
    draw.text((95, 45), "M", font=font_logo, fill=(255, 255, 255))
    
    draw.text((175, 48), "MFACH", font=font_logo, fill=(248, 250, 252))
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
        draw.text((1190, 72), "📍 OBSZAR DZIAŁANIA: KĘTRZYN I OKOLICE (DO 50 KM)", font=font_badge, fill=(34, 211, 238))
    
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
        
        # Colored Top accent bar inside card
        draw.rounded_rectangle((cx + 12, cy + 348, cx + 130, cy + 376), radius=14, fill=card["color"])
        draw.text((cx + 24, cy + 353), card["tag"], font=font_card_tag, fill=(255, 255, 255))
        
        # Card Title
        draw.text((cx + 18, cy + 392), card["title"], font=font_card_title, fill=(248, 250, 252))
        
        # Separator line
        draw.line((cx + 18, cy + 440, cx + card_w - 18, cy + 440), fill=(255, 255, 255, 30), width=1)
        
        # Points
        py = cy + 465
        for pt in card["points"]:
            draw.text((cx + 20, py), pt, font=font_card_body, fill=(226, 232, 240))
            py += 44
            
        # Bottom small badge in card
        badge_y = cy + card_h - 60
        draw.rounded_rectangle((cx + 18, badge_y, cx + card_w - 18, badge_y + 40), radius=10, fill=(15, 23, 42))
        draw.text((cx + 30, badge_y + 10), "Gwarancja solidnego wykonania", font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 15), fill=card["accent"])
        
    # 3. Bottom Big Contact Bar
    footer_bbox = (80, 930, 1840, 1025)
    draw.rounded_rectangle(footer_bbox, radius=24, fill=(17, 24, 39), outline=(56, 189, 248), width=2)
    
    # Phone button inside footer
    call_btn_box = (1350, 945, 1820, 1010)
    draw.rounded_rectangle(call_btn_box, radius=32, fill=(22, 163, 74))
    draw.text((1380, 953), "📞 ZADZWOŃ: 695 525 389", font=font_phone, fill=(255, 255, 255))
    
    # Footer Left text
    font_footer_main = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 32)
    font_footer_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 20)
    draw.text((120, 946), "Potrzebujesz naprawy, remontu lub instalacji?", font=font_footer_main, fill=(248, 250, 252))
    draw.text((120, 986), "Dojazd mobilny: Kętrzyn, Mrągowo, Giżycko, Węgorzewo, Reszel, Bartoszyce i okolice", font=font_footer_sub, fill=(148, 163, 184))
    
    bg.save("assets/infographic_banner.png", quality=95)
    print("Banner generated successfully!")

def generate_circle_quad():
    width, height = 1200, 1200
    bg = Image.new('RGB', (width, height), (11, 15, 25))
    draw = ImageDraw.Draw(bg)
    
    # Fonts
    font_logo = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 60)
    font_med_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 28)
    font_center_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 44)
    font_center_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 22)
    font_center_phone = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 42)
    font_quad_tag = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 17)
    font_quad_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 18)
    
    # Quadrant data
    quads = [
        # Top-Left: Agro
        {
            "img_path": "assets/hero_agro.png",
            "box": (50, 50, 570, 570),
            "thumb_box": (70, 70, 550, 420),
            "title": "Ciągniki Rolnicze",
            "sub": "Silniki • Skrzynie • Hydraulika siłowa",
            "tag": "1. ROLNICTWO & AGRO",
            "color": (22, 163, 74),
            "accent": (74, 222, 128)
        },
        # Top-Right: Auto
        {
            "img_path": "assets/hero_auto.png",
            "box": (630, 50, 1150, 570),
            "thumb_box": (650, 70, 1130, 420),
            "title": "Mechanika Samochodowa",
            "sub": "Olej & filtry • Hamulce • Rozrządy",
            "tag": "2. MECHANIKA AUT",
            "color": (37, 99, 235),
            "accent": (56, 189, 248)
        },
        # Bottom-Left: Remonty
        {
            "img_path": "assets/hero_remont.png",
            "box": (50, 630, 570, 1150),
            "thumb_box": (70, 790, 550, 1130),
            "title": "Wykończenia Wnętrz",
            "sub": "Gładzie • Malowanie • Panele • G-K",
            "tag": "3. REMONTY DOMÓW",
            "color": (234, 88, 12),
            "accent": (251, 146, 60),
            "text_top": True
        },
        # Bottom-Right: Hydraulika
        {
            "img_path": "assets/hero_hydro.png",
            "box": (630, 630, 1150, 1150),
            "thumb_box": (650, 790, 1130, 1130),
            "title": "Hydraulika & Kotłownie",
            "sub": "Pompy ciepła • Wod-kan • Biały montaż",
            "tag": "4. HYDRAULIKA",
            "color": (8, 145, 178),
            "accent": (34, 211, 238),
            "text_top": True
        }
    ]
    
    # Draw Quadrants
    for q in quads:
        bx1, by1, bx2, by2 = q["box"]
        draw.rounded_rectangle((bx1, by1, bx2, by2), radius=32, fill=(22, 30, 46), outline=q["color"], width=4)
        
        # Image
        if os.path.exists(q["img_path"]):
            cimg = Image.open(q["img_path"])
            tx1, ty1, tx2, ty2 = q["thumb_box"]
            tw = tx2 - tx1
            th = ty2 - ty1
            rounded_thumb = make_rounded_image(cimg, (tw, th), radius=22)
            bg.paste(rounded_thumb, (tx1, ty1), rounded_thumb)
            
        # Text placement
        if q.get("text_top"):
            # Text at the top of bottom cards
            draw.rounded_rectangle((bx1 + 25, by1 + 25, bx1 + 220, by1 + 58), radius=12, fill=q["color"])
            draw.text((bx1 + 38, by1 + 31), q["tag"], font=font_quad_tag, fill=(255, 255, 255))
            draw.text((bx1 + 25, by1 + 72), q["title"], font=font_med_title, fill=(248, 250, 252))
            draw.text((bx1 + 25, by1 + 115), q["sub"], font=font_quad_sub, fill=(148, 163, 184))
        else:
            # Text at the bottom of top cards
            draw.rounded_rectangle((bx1 + 25, by2 - 130, bx1 + 220, by2 - 97), radius=12, fill=q["color"])
            draw.text((bx1 + 38, by2 - 124), q["tag"], font=font_quad_tag, fill=(255, 255, 255))
            draw.text((bx1 + 25, by2 - 86), q["title"], font=font_med_title, fill=(248, 250, 252))
            draw.text((bx1 + 25, by2 - 45), q["sub"], font=font_quad_sub, fill=(148, 163, 184))

    # Center Emblem (Circle Hub)
    center_x = width // 2
    center_y = height // 2
    r = 220
    
    # Outer Glow Ring
    for ring_i in range(10):
        draw.ellipse((center_x - r - ring_i*2, center_y - r - ring_i*2, center_x + r + ring_i*2, center_y + r + ring_i*2), outline=(15, 23, 42))
        
    # Main Center Disk Background
    draw.ellipse((center_x - r, center_y - r, center_x + r, center_y + r), fill=(11, 15, 25), outline=(255, 255, 255), width=3)
    
    # Blended Map Texture inside Center Disk
    if os.path.exists("assets/map.png"):
        map_img = Image.open("assets/map.png").convert("RGBA")
        map_crop_size = (r * 2 - 12, r * 2 - 12)
        map_resized = map_img.resize(map_crop_size, Image.Resampling.LANCZOS)
        
        # Darken overlay so text is 100% legible
        dark_overlay = Image.new('RGBA', map_crop_size, (11, 15, 25, 175))
        map_blended = Image.alpha_composite(map_resized, dark_overlay)
        
        cmask = Image.new('L', map_crop_size, 0)
        ImageDraw.Draw(cmask).ellipse((0, 0, map_crop_size[0], map_crop_size[1]), fill=255)
        bg.paste(map_blended, (center_x - r + 6, center_y - r + 6), cmask)
    
    # 4-color segmented arc border
    draw.arc((center_x - r + 4, center_y - r + 4, center_x + r - 4, center_y + r - 4), start=180, end=270, fill=(22, 163, 74), width=10) # Agro
    draw.arc((center_x - r + 4, center_y - r + 4, center_x + r - 4, center_y + r - 4), start=270, end=360, fill=(37, 99, 235), width=10) # Auto
    draw.arc((center_x - r + 4, center_y - r + 4, center_x + r - 4, center_y + r - 4), start=90, end=180, fill=(234, 88, 12), width=10)  # Remont
    draw.arc((center_x - r + 4, center_y - r + 4, center_x + r - 4, center_y + r - 4), start=0, end=90, fill=(8, 145, 178), width=10)    # Hydro
    
    # Text in Center Disk (dynamically centered)
    txt_logo = "MFACH"
    w_logo = draw.textlength(txt_logo, font=font_center_title)
    draw.text((center_x - w_logo / 2, center_y - 135), txt_logo, font=font_center_title, fill=(255, 255, 255))
    
    txt_sub = "MARCIN • USŁUGI MOBILNE"
    w_sub = draw.textlength(txt_sub, font=font_center_sub)
    draw.text((center_x - w_sub / 2, center_y - 75), txt_sub, font=font_center_sub, fill=(226, 232, 240))
    
    # Phone Button Pill in Center
    pill_w = 360
    pill_h = 64
    pill_box = (center_x - pill_w // 2, center_y - 25, center_x + pill_w // 2, center_y - 25 + pill_h)
    draw.rounded_rectangle(pill_box, radius=32, fill=(22, 163, 74), outline=(74, 222, 128), width=2)
    
    txt_phone = "📞 695 525 389"
    w_phone = draw.textlength(txt_phone, font=font_center_phone)
    draw.text((center_x - w_phone / 2, center_y - 20), txt_phone, font=font_center_phone, fill=(255, 255, 255))
    
    # Area Badge in Center
    font_badge_bold = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 20)
    font_badge_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 16)
    
    txt_area = "📍 KĘTRZYN I OKOLICE (DO 50 KM)"
    w_area = draw.textlength(txt_area, font=font_badge_bold)
    draw.text((center_x - w_area / 2, center_y + 55), txt_area, font=font_badge_bold, fill=(34, 211, 238))
    
    txt_field = "Dojazd pod dom i w pole"
    w_field = draw.textlength(txt_field, font=font_badge_sub)
    draw.text((center_x - w_field / 2, center_y + 85), txt_field, font=font_badge_sub, fill=(203, 213, 225))
    
    bg.save("assets/infographic_circle.png", quality=95)
    print("Circle infographic generated successfully!")

if __name__ == '__main__':
    generate_banner()
    generate_circle_quad()
