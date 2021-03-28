import pygame


class Button:
    def __init__(self, rect, surface, text):
        self.rect = pygame.Rect(rect)
        self.surface = surface
        self.text = text

    def draw(self, color):
        pygame.draw.rect(self.surface, color, self.rect)

    def draw_text(self, font=80):
        f1 = pygame.font.Font(None, font)
        text = f1.render(self.text, 1, (0, 0, 0))
        text_r = text.get_rect(center=self.rect.center)
        self.surface.blit(text, text_r)

    def set_new_state(self, text, color):
        self.draw(color)
        self.text = text
        self.draw_text()
