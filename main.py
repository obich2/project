import pygame as pg
from settings import *


def get_font(size):
    return pg.font.Font("font.ttf", size)


class TextLine:
    def __init__(self, screen, font_size, text, position, color):
        self.screen = screen
        self.font = font_size
        self.text = text
        self.position = position
        self.color = color
        self.rect = ''

    def draw(self):
        self.text = get_font(self.font).render(self.text, True, self.color)
        self.rect = self.text.get_rect(center=self.position)
        sc.blit(self.text, self.rect)

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))