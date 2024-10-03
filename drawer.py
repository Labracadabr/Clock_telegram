from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import pytz


# текст вставки в нужном часовом поясе
def time_now_text() -> str:
    tz = pytz.timezone("Etc/GMT-8")  # gmt+8
    now = datetime.now(tz)
    # text = now.strftime("%A\n%B %d, %Y\n%H:%M")  # раз в минуту, прошлая версия (это слишком часто, будет error 420)
    text = now.strftime("%A\n%B %d, %Y\n%I %p")
    return text


# вставить текст на фото
def draw_text(x, y, text='Hello', show=False):
    template_path, save_path = 'avatar.jpg', 'avatar_time.jpg'
    # открыть фото
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)

    # вставить текст
    font = ImageFont.load_default(size=36)
    position = (int(x), int(y))
    text_color = (50, 50, 50)
    draw.text(position, text, fill=text_color, font=font)

    # save
    template.save(save_path)
    print('💾', save_path)
    if show:
        template.show()


def generate_avatar():
    text = time_now_text()
    draw_text(text=text, x=220, y=40)
    print(f'generated avatar {text = }')


if __name__ == '__main__':
    # можно поэкспериментировать с координатами
    while True:
        x, y = input('x, y:').split()
        if not x:
            exit('no coordinates given')
        draw_text(x, y, text=time_now_text(), show=True)
