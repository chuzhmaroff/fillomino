import pygame
from pygame.locals import *
from Button import Button
import copy
import create_image_for_ascii
import create_film_history_move
import copy

counter_move = 0
history_move = []


class Game:
    colors = {9: (85, 107, 47),
              8: (128, 128, 0),
              7: (154, 205, 50),
              6: (60, 159, 113),
              5: (50, 205, 50),
              4: (255, 69, 0),
              3: (255, 255, 0),
              2: (30, 144, 255),
              1: (255, 99, 71),
              "": (119, 136, 153)}

    def __init__(self):
        # 741*741
        current_list = [[8, "", "", 8, 5, "", "", 5, 3],
                        ["", "", "", 8, "", 6, "", "", ""],
                        [5, 5, 5, 6, 6, 6, 4, 4, ""],
                        [5, 5, 6, 6, 9, 9, 9, 9, 9],
                        [4, 2, 2, 7, 7, 7, 9, 9, 9],
                        [4, 4, 4, 7, 7, 7, 7, 9, 8],
                        [3, 6, 3, 3, 3, 8, 8, 8, 8],
                        [3, 6, 6, 6, 6, 8, 8, 8, 8],
                        [3, 7, "", 7, 7, 7, 7, 7, 7]]

        square_list = []
        action_stack = []
        # net = Network()

        pygame.init()
        screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        background = pygame.display.get_surface()
        background.fill((255, 255, 255))
        clock = pygame.time.Clock()
        fps = 60
        pygame.display.set_caption("Fillomino")
        field = pygame.image.load("background.png")
        screen.blit(field, (200, 170))

        quit_button = Button((1900, 0, 20, 20), screen, "X")
        quit_button.draw((255, 0, 0))
        quit_button.draw_text(40)

        undo_button = Button((1200, 500, 400, 100), screen, "UNDO")
        undo_button.draw((0, 0, 255))
        undo_button.draw_text()

        start_button = Button((1200, 300, 400, 100), screen, "START GAME")
        start_button.draw((0, 255, 0))
        start_button.draw_text()
        game_started = False

        end_move_button = Button((1200, 700, 400, 100), screen, "END MOVE")
        end_move_button.draw((255, 0, 0))
        end_move_button.draw_text()

        create_ascii_button = Button((1200, 900, 700, 150),
                                     screen, "CREATE SCREEN ASCII")
        create_ascii_button.draw((255, 0, 0))
        create_ascii_button.draw_text()

        show_history_move_button = Button((1200, 100, 500, 100),
                                          screen, "HISTORY MOVE")
        show_history_move_button.draw((255, 0, 0))
        show_history_move_button.draw_text()

        while 1:
            # events содержит список событий
            try:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == USEREVENT:
                        counter -= 1

                    if event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos

                        if undo_button.rect.collidepoint(mouse_pos) and len(
                                action_stack) > 0:
                            cur_state = action_stack.pop()
                            for i in range(0, 9):
                                for j in range(0, 9):
                                    square_list[i][j].text = str(
                                        cur_state[i][j])
                                    square_list[i][j].draw(
                                        Game.colors[cur_state[i][j]])
                                    square_list[i][j].draw_text()
                            action_stack.append(cur_state)
                            current_list = copy.deepcopy(cur_state)

                        if create_ascii_button.rect.collidepoint(mouse_pos):
                            ascii_art(current_list)

                        if show_history_move_button.rect.collidepoint(
                                mouse_pos):
                            create_film_history_move_and_open()

                        if end_move_button.rect.collidepoint(mouse_pos):
                            for i in range(0, 9):
                                for j in range(0, 9):
                                    square_list[i][j].draw_text()
                            action_stack.clear()
                            new_state = copy.deepcopy(current_list)
                            action_stack.append(copy.deepcopy(current_list))
                            counter = 60

                        if start_button.rect.collidepoint(
                                mouse_pos) and not game_started:
                            for i in range(0, 9):
                                raw = []
                                for j in range(0, 9):
                                    test_b = Button(
                                        (200 + j * 82, 170 + i * 82, 84, 84),
                                        screen, str(current_list[i][j]))
                                    test_b.draw(
                                        Game.colors[current_list[i][j]])
                                    test_b.draw_text(80)
                                    raw.append(test_b)
                                square_list.append(raw)
                            counter = 60
                            pygame.time.set_timer(USEREVENT, 1000)

                            game_started = True

                        if quit_button.rect.collidepoint(mouse_pos):
                            exit()

                        for i in range(0, 9):
                            for j in range(0, 9):
                                if square_list[i][j].rect.collidepoint(
                                        mouse_pos):
                                    square = (i, j)

                    if event.type == pygame.KEYDOWN:
                        number = get_pressed_number(event.key)
                        if number != "":
                            square_list[square[0]][square[1]].set_new_state(
                                str(number), Game.colors[number])
                            current_list[square[0]][square[1]] = number
                            save_move(counter_move, current_list)
                pygame.display.update()
                clock.tick(fps)
            except IndexError:
                pass
            except UnboundLocalError:
                pass


def ascii_art(current_list):
    print("You push button create ascii art")
    create_image_for_ascii.create_ascii(current_list)
    print("asci art -done ")
    # в отдельный поток


def save_move(counter_move, current_list):
    history_move.append(copy.deepcopy(current_list))
    counter_move += 1
    print("im saving this list:")
    print(current_list)
    print("И теперь лист всех ходов выглядит так:")
    print(history_move)


def create_film_history_move_and_open():
    try:
        create_film_history_move.main(history_move)
    except Exception as ax:
        print(ax)
        pass


def get_pressed_number(key):
    if key == K_1:
        return 1
    elif key == K_2:
        return 2
    elif key == K_3:
        return 3
    elif key == K_4:
        return 4
    elif key == K_5:
        return 5
    elif key == K_6:
        return 6
    elif key == K_7:
        return 7
    elif key == K_8:
        return 8
    elif key == K_9:
        return 9
    else:
        return ""


def create_button(rect, surf, text, b_color, font=80):
    button = Button(rect, surf, text)
    button.draw(b_color)
    button.draw_text(font)
    return button


def apply_new_state(button_list, new_state, cur_state):
    for i in range(0, 9):
        for j in range(0, 9):
            if cur_state[i][j] != new_state[i][j]:
                button_list[i][j].text = str(new_state[i][j])
            else:
                button_list[i][j].text = str(cur_state[i][j])
            button_list[i][j].draw(Game.colors[new_state[i][j]])
            button_list[i][j].draw_text()


def parse_data(data):
    return eval(data)


game = Game()
