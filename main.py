import pygame as pg
from settings import *
import pygame.display
import time
import sys


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


def main_menu():
    while True:

        sc.fill('black')
        first = TextLine(sc, 100, 'MOVE', (800, 450), 'WHITE')
        fourth = TextLine(sc, 20, 'press any button to START', (800, 800), 'GREY')
        fourth.draw()
        first.draw()
        pg.display.update()

        time.sleep(2)

        sc.fill('black')
        second = TextLine(sc, 100, 'OR', (800, 450), 'WHITE')
        second.draw()
        fifth = TextLine(sc, 20, 'press any button to START', (800, 800), 'GREY')
        fifth.draw()
        pg.display.update()

        time.sleep(2)

        sc.fill('black')
        third = TextLine(sc, 100, 'DIEEE!!!!!', (800, 450), 'RED')
        third.draw()
        six = TextLine(sc, 20, 'press any button to START', (800, 800), 'GREY')
        six.draw()
        pg.display.update()

        time.sleep(2)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()


pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
main_menu()