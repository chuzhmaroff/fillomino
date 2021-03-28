import os
import datetime
from PIL import Image, ImageDraw, ImageFont
import PIL

path_to_script = os.path.dirname(os.path.abspath(__file__))
path_to_font = r"{}/roman.ttf".format(path_to_script)
path_to_background = r'{}/background.png'.format(path_to_script)
font = ImageFont.truetype(path_to_font, size=45)

image_background = Image.open(path_to_background)
draw_text = ImageDraw.Draw(image_background)

coordinates = [
    [(30, 20), (115, 20), (200, 20), (280, 20), (360, 20), (440, 20),
     (525, 20), (610, 20), (685, 20)],
    [(30, 100), (115, 100), (200, 100), (280, 100), (360, 100), (440, 100),
     (525, 100), (610, 100), (685, 100)],
    [(30, 180), (115, 180), (200, 180), (280, 180), (360, 180), (440, 180),
     (525, 180), (610, 180), (685, 180)],
    [(30, 260), (115, 260), (200, 260), (280, 260), (360, 260), (440, 260),
     (525, 260), (610, 260), (685, 260)],
    [(30, 340), (115, 340), (200, 340), (280, 340), (360, 340), (440, 340),
     (525, 340), (610, 340), (685, 340)],
    [(30, 420), (115, 420), (200, 420), (280, 420), (360, 420), (440, 420),
     (525, 420), (610, 420), (685, 420)],
    [(30, 500), (115, 500), (200, 500), (280, 500), (360, 500), (440, 500),
     (525, 500), (610, 500), (685, 500)],
    [(30, 580), (115, 580), (200, 580), (280, 580), (360, 580), (440, 580),
     (525, 580), (610, 580), (685, 580)],
    [(30, 660), (115, 660), (200, 660), (280, 660), (360, 660), (440, 660),
     (525, 660), (610, 660), (685, 660)]
]


def cnl(coordinates, text, draw_text):
    draw_text.text(
        coordinates,
        text,
        font=font,
        fill='#002aff')


def create_im(list_table_fillomino, draw_text):
    for i in range(0, 9):
        for j in range(0, 9):
            x_y = coordinates[i][j]
            text = list_table_fillomino[i][j]
            cnl(x_y, str(text), draw_text)


def color_ascii_art(int_scale_factor, set_fill, im):
    import math

    c = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:," \
        "\"^`'. "[::-1]
    # chars = "#Wo- "[::-1]
    charArray = list(c)
    charLength = len(charArray)
    interval = charLength / 256

    scaleFactor = float(int_scale_factor)

    oneCharWidth = 10
    oneCharHeight = 18

    def getChar(inputInt):
        return charArray[math.floor(inputInt * interval)]

    fnt = PIL.ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

    width, height = im.size
    im = im.resize((int(scaleFactor * width), int(
        scaleFactor * height * (oneCharWidth / oneCharHeight))),
                   PIL.Image.NEAREST)
    width, height = im.size
    pix = im.load()

    outputImage = PIL.Image.new('RGB',
                                (oneCharWidth * width, oneCharHeight * height),
                                color=(0, 0, 0))
    d = PIL.ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r / 3 + g / 3 + b / 3)
            pix[j, i] = (h, h, h)
            if set_fill == 1:
                d.text((j * oneCharWidth, i * oneCharHeight), getChar(h),
                       font=fnt, fill=(r, g, b))
            if set_fill == 0:
                d.text((j * oneCharWidth, i * oneCharHeight), getChar(h),
                       font=fnt, fill=(h, h, h))
            # fill=(r, g, b)

    # outputImage.save('Ascii_art.png')
    return outputImage


def create_ascii(list_table_fillomino):
    create_im(list_table_fillomino, draw_text)
    im = color_ascii_art(float(0.6), 0, image_background)
    nowtime = datetime.datetime.now()
    im.save("screen_fillomino {}-{}-{} {} {} {}.jpg".format(nowtime.day,
                                                            nowtime.month,
                                                            nowtime.year,
                                                            nowtime.hour,
                                                            nowtime.minute,
                                                            nowtime.second))

# im.show()
