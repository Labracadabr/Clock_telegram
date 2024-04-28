from PIL import Image, ImageDraw, ImageFont
import random
from datetime import datetime

def draw_text(template_path, text, save_path):
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)

    # text
    font = ImageFont.load_default(size=40)
    x, y = 350, 40  # random.randint(100, 600), random.randint(100, 700)
    position = (x, y)
    text_color = (255, 250, 250)
    draw.text(position, text, fill=text_color, font=font)

    # save
    template.save(save_path)
    print('💾', save_path)


def generate_avatar():
    now = datetime.now()
    text = now.strftime("%A\n%B %d, %Y\n%H:%M")
    print(f'generate_avatar {text = }')
    draw_text(template_path='avatar.jpg', text=text, save_path='avatar_time.jpg')


if __name__ == '__main__':
    generate_avatar()
