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
sky_image = pg.image.load('tiles/sky.png')
image_trace_red = pygame.image.load('tiles/red.png')
image_trace_blue = pygame.image.load('tiles/blue.png')

TILE_SIZE = block_image.get_width()
# print(TILE_SIZE)
flag = True


def main_menu():
    global flag
    while flag:
        # print(flag)
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
    # sc.fill('black')
    # first = TextLine(sc, 100, '5', (800, 450), 'WHITE')
    # first.draw()
    # pg.display.update()

    # time.sleep(1)

    # sc.fill('black')
    # first = TextLine(sc, 100, '4', (800, 450), 'WHITE')
    # first.draw()
    # pg.display.update()

    # time.sleep(1)

    # sc.fill('black')
    # first = TextLine(sc, 100, '3', (800, 450), 'RED')
    # first.draw()
    # pg.display.update()
    
    # time.sleep(1)

    # sc.fill('black')
    # first = TextLine(sc, 100, '2', (800, 450), 'RED')
    # first.draw()
    # pg.display.update()
    
    # time.sleep(1)

    # sc.fill('black')
    # first = TextLine(sc, 100, '1', (800, 450), 'RED')
    # first.draw()
    # pg.display.update()
    
    # создание таймера на 1 секунду
    clock = pygame.time.Clock()
    counter = 30
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    display.fill((146, 244, 255))
    # создаем героя по (x,y) координатам
    hero_1 = Character(200, 100, 'red')
    hero_2 = Character(1400, 100, 'blue')
    hero_1_other = []
    hero_2_other = []
    left_1 = right_1 = False  # по умолчанию - стоим
    left_2 = right_2 = False
    up_1 = up_2 = False
    entities = pygame.sprite.Group()  # Поверхности(стенки, пол и тд)
    platforms = []  # поверхность
    other = []

    entities.add(hero_1)
    entities.add(hero_2)
    display.fill((146, 244, 255))
    while True:
        f = pygame.font.Font(None, 40)
        timer = f.render(str(counter), True,
                  (255, 255, 255))
        display.blit(timer, (800, 800))
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():

            tile_rects = []
            y = 0
            for row in game_map:
                # print(row)
                x = 0
                for tile in row:
                    if tile == 1:
                        pf = Platform(x * 80, y * 45)
                        entities.add(pf)
                        platforms.append(pf)
                        display.blit(block_image, (x * 80, y * 45))
                    elif tile == 0:
                        pf = Platform(x * 80, y * 45)
                        entities.add(pf)
                        other.append(pf)
                        display.blit(sky_image, (x * 80, y * 45))
                    x += 1
                y += 1
            for i in hero_1_other:
                display.blit(image_trace_red, (i[0], i[1]))
            for i in hero_2_other:
                display.blit(image_trace_blue, (i[0], i[1]))
            if event.type == pygame.USEREVENT: 
                counter -= 1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()
            if event.type == KEYDOWN and event.key == K_UP:
                up_1 = True
            if event.type == KEYDOWN and event.key == K_LEFT:
                left_1 = True
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right_1 = True
            if event.type == KEYUP and event.key == K_UP:
                up_1 = False
            if event.type == KEYUP and event.key == K_RIGHT:
                right_1 = False
            if event.type == KEYUP and event.key == K_LEFT:
                left_1 = False
            if event.type == KEYDOWN and event.key == K_w:
                up_2 = True
            if event.type == KEYDOWN and event.key == K_a:
                left_2 = True
            if event.type == KEYDOWN and event.key == K_d:
                right_2 = True
            if event.type == KEYUP and event.key == K_w:
                up_2 = False
            if event.type == KEYUP and event.key == K_d:
                right_2 = False
            if event.type == KEYUP and event.key == K_a:
                left_2 = False
        print(len(hero_2_other))
        print(len(hero_1_other))
        if counter > 0:
            r1 = hero_1.draw_other()
            r2 = hero_2.draw_other()
            if r1 not in hero_1_other:
                hero_1_other.append(r1)
            if r2 not in hero_2_other:
                hero_2_other.append(r2)
            sc.blit(display, (0, 0))
            hero_1.update(left_1, right_1, up_1, platforms, other)  # отображение
            hero_2.update(left_2, right_2, up_2, platforms, other)
            hero_1.draw(sc)
            hero_2.draw(sc)
            pygame.display.update()
        else:
            if len(hero_1_other) > len(hero_2_other):
                sc.fill('black')
                first = TextLine(sc, 100, 'RED WIN', (800, 450), 'RED')
                first.draw()
                pg.display.update()
            elif len(hero_2_other) > len(hero_1_other):
                sc.fill('black')
                first = TextLine(sc, 100, 'BLUE WIN', (800, 450), 'BLUE')
                first.draw()
                pg.display.update()
            elif len(hero_2_other) == len(hero_1_other):
                sc.fill('black')
                first = TextLine(sc, 100, 'draw', (800, 450), 'WHITE')
                first.draw()
                pg.display.update()

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
