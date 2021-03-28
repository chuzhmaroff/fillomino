import cv2
import os
import datetime
from PIL import Image, ImageDraw, ImageFont
import PIL

path_to_script = os.path.dirname(os.path.abspath(__file__))

path_to_video = r'{}/data/history_move_last_game.avi'.format(path_to_script)
path_to_save_img_history_move = r'{}\data\history_move'.format(path_to_script)
path_to_font = r"{}/roman.ttf".format(path_to_script)

count = 0
path_to_background = r'{}/background.png'.format(path_to_script)
font = ImageFont.truetype(path_to_font, size=45)

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
list_path_to_image_for_film = []


def create_image_for_film(history_move):
    counter = 0
    for move in history_move:
        image_background = Image.open(path_to_background)
        draw = ImageDraw.Draw(image_background)
        for i in range(0, 9):
            for j in range(0, 9):
                x_y = coordinates[i][j]
                text = move[i][j]
                draw.text(x_y, str(text), font=font, fill='#000000')
        image_background.save("{}/{}.png".format(
            path_to_save_img_history_move, counter))
        list_path_to_image_for_film.append("{}/{}.png".format(
            path_to_save_img_history_move, counter))
        counter += 1
    return list_path_to_image_for_film


def cleaner_data():
    for x in range(0, 100):
        try:
            path = os.path.join((path_to_save_img_history_move),
                                '{}.png'.format(x))
            os.remove(path)
        except Exception as ax:
            print(ax)
            pass


def main(history_move):
    paths_to_save_img_history_move = create_image_for_film(history_move)
    out = cv2.VideoWriter(path_to_video,
                          cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 1.0,
                          (741, 741))
    print(path_to_video)
    for path in paths_to_save_img_history_move:
        print(path)
        out.write(cv2.imread(path))
    #cleaner_data()
    out.release()
    cv2.destroyAllWindows()
    os.startfile("{}".format(path_to_video))
