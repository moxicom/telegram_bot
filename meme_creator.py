from PIL import Image, ImageDraw, ImageFont
import textwrap

meme_list = ['ronaldo', 'fresko']


def resize_text(size):
    pass


def ronaldo(text):
    img = Image.open('memes/ronaldo.jpg')
    size = 0
    pos = (0, 0)
    if len(text) <= 10:
        size = 30
        pos = (40, 150)
    elif 10 < len(text) <= 60:
        size = 20
        pos = (40, 120)
        text = textwrap.fill(text, 13)
    else:
        ronaldo('попробуйте сделать текст меньше')
        size = 20
        pos = (40, 50)
    font = ImageFont.truetype('times.ttf', size=size)
    draw = ImageDraw.Draw(img)
    draw.text(pos, text, font=font, fill=('#1C0606'))
    return img


def fresko(text):
    text = text
    img = Image.open('memes/fresko.jpg')
    size = 0
    pos = (0, 0)
    if len(text) <= 20:
        size = 27
        pos = (40, 50)
    elif 20 < len(text) <= 100:
        size = 20
        pos = (40, 20)
        text = textwrap.fill(text, 30)
        print('aa')
    else:
        text = 'попробуйте сделать текст меньше'
        size = 20
        pos = (40, 50)
    print(text)
    font = ImageFont.truetype('times.ttf', size=size)
    draw = ImageDraw.Draw(img)
    draw.text(pos, text, font=font, fill=('#1C0606'))
    return img

