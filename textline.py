import pygame


class TextLine:
    def __init__(self, screen, font_size, text, position, color):
        self.screen = screen
        self.font = font_size
        self.text = text
        self.value = 0
        self.position = position
        self.color = color
        self.rect = ''

    def draw(self):
        self.text = get_font(self.font).render(self.text, True, self.color)
        self.rect = self.text.get_rect(center=self.position)
        self.screen.blit(self.text, self.rect)


def get_font(size):
    return pygame.font.Font("font.ttf", size)
