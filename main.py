import pygame as pg
from settings import *
from character import *
from blocks import *
import pygame.display
import time
import sys
from button import Button


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


def get_font(size):
    return pg.font.Font("font.ttf", size)


block_image = pg.image.load('tiles/block.png')


TILE_SIZE = block_image.get_width()
print(TILE_SIZE)
flag = True


def main_menu():
    global flag
    while flag:
        print(flag)
        sc.fill('black')
        first = TextLine(sc, 100, 'MOVE', (800, 450), 'WHITE')
        # fourth = TextLine(sc, 20, 'press any button to START', (800, 800), 'GREY')
        # fourth.draw()
        first.draw()
        pg.display.update()

        time.sleep(2)

        sc.fill('black')
        second = TextLine(sc, 100, 'OR', (800, 450), 'WHITE')
        second.draw()
        # fifth = TextLine(sc, 20, 'press any button to START', (800, 800), 'GREY')
        # fifth.draw()
        pg.display.update()

        time.sleep(0.5)

        sc.fill('black')
        third = TextLine(sc, 100, 'DIEEE!!!!!', (800, 450), 'RED')
        third.draw()
        pg.display.update()
        time.sleep(0.5)

        six = TextLine(sc, 20, 'press any button to START', (800, 800), 'GREY')
        six.draw()
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type != pg.QUIT:
                flag = False

        time.sleep(0.5)

    while True:
        sc.fill('black')

        play_button = Button((640, 250),
                             "PLAY", get_font(75), "#d7fcd4", "White")
        settings_button = Button((640, 400),
                                 "SETTINGS", get_font(75), "#d7fcd4", "White")
        quit_button = Button((640, 550),
                             "QUIT", get_font(75), "#d7fcd4", "White")

        mouse_pos = pygame.mouse.get_pos()

        for button in [play_button, settings_button, quit_button]:
            button.change_color(mouse_pos)
            button.update(sc)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.check_click(mouse_pos):
                    play()
                if settings_button.check_click(mouse_pos):
                    settings()
                if quit_button.check_click(mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def play():
    display.fill((146, 244, 255))
    hero = Character(160, 80)  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию - стоим
    up = False
    entities = pygame.sprite.Group()  # Поверхности(стенки, пол и тд)
    platforms = []  # поверхность

    entities.add(hero)
    display.fill((146, 244, 255))
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():

            tile_rects = []
            y = 0
            for row in game_map:
                print(row)
                x = 0
                for tile in row:
                    if tile == 1:
                        pf = Platform(x * 80, y * 45)
                        entities.add(pf)
                        platforms.append(pf)
                        display.blit(block_image, (x * 80, y * 45))

                    x += 1
                y += 1

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()
            if event.type == KEYDOWN and event.key == K_UP:
                up = True
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
            if event.type == KEYUP and event.key == K_UP:
                up = False
            if event.type == KEYUP and event.key == K_RIGHT:
                right = False
            if event.type == KEYUP and event.key == K_LEFT:
                left = False

        sc.blit(display, (0, 0))
        hero.update(left, right, up, platforms)
        hero.draw(sc)  # отображение
        pygame.display.update()


def settings():
    while True:
        mouse_pos = pygame.mouse.get_pos()

        sc.fill('BLACK')
        back_button = Button((640, 400),
                             "Back", get_font(75), "#d7fcd4", "White")
        back_button.change_color(mouse_pos)
        back_button.update(sc)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_click(mouse_pos):
                    main_menu()


pg.init()
sc = pg.display.set_mode((1600, 900))
display = pg.Surface((1600, 900))

main_menu()
