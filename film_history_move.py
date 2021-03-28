import os
from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random
import datetime
from PIL import Image, ImageDraw, ImageFont
import PIL

path_to_script = os.path.dirname(os.path.abspath(__file__))
path_to_font = r"{}/roman.ttf".format(path_to_script)
path_to_background = r'{}/background.png'.format(path_to_script)
font = ImageFont.truetype(path_to_font, size=45)

image_background = Image.open(path_to_background)
draw_text = ImageDraw.Draw(image_background)

test_list = [[8, "", "", 8, 5, "", "", 5, 3],
             ["", "", "", 8, "", 6, "", "", ""],
             [5, 5, 5, 6, 6, 6, 4, 4, ""],
             [5, 5, 6, 6, 9, 9, 9, 9, 9],
             [4, 2, 2, 7, 7, 7, 9, 9, 9],
             [4, 4, 4, 7, 7, 7, 7, 9, 8],
             [3, 6, 3, 3, 3, 8, 8, 8, 8],
             [3, 6, 6, 6, 6, 8, 8, 8, 8],
             [3, 7, "", 7, 7, 7, 7, 7, 7]]

# create test image

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


create_im(test_list, draw_text)
image_background.show()
