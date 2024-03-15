import pygame as pg
from settings import *
from character import *
from blocks import *
import pygame.display
import time
import sys
from button import Button
from slider import Slider


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
        sc.blit(self.text, self.rect)


def get_font(size):
    return pg.font.Font("font.ttf", size)


pg.init()

sc = pg.display.set_mode((1600, 900))
display = pg.Surface((1600, 900))
pg.display.set_caption('Move or Die')

# images
block_image = pg.image.load('tiles/block.png')
app_icon = pg.image.load('tiles/icon.png')
round_out = pg.image.load('tiles/RoundOut.png').convert_alpha()
pg.display.set_icon(app_icon)
# sounds

rotated_round_out = pygame.transform.flip(round_out, True, False)
sky_image = pg.image.load('tiles/sky.png')
image_trace_red = pygame.image.load('tiles/red.png')
image_trace_blue = pygame.image.load('tiles/blue.png')

TILE_SIZE = block_image.get_width()
# print(TILE_SIZE)
flag = True


def main_menu():
    global flag
    pygame.mixer.music.set_volume(MUSIC_VOLUME)
    pygame.mixer.music.load('sound/Voicer/menu@game_title.ogg')

    while flag:
        pygame.mixer.music.play(1)
        print(flag)
        # print(flag)
        sc.fill('black')
        first = TextLine(sc, 100, 'MOVE', (800, 450), 'WHITE')
        fourth = TextLine(sc, 20, 'press any button to START', (800, 800), 'GREY')
        fourth.draw()
        first.draw()
        pg.display.update()

        time.sleep(0.75)

        sc.fill('black')
        second = TextLine(sc, 100, 'OR', (800, 450), 'WHITE')
        second.draw()
        fifth = TextLine(sc, 20, 'press any button to START', (800, 800), 'GREY')
        fifth.draw()
        pg.display.update()

        time.sleep(0.5)

        sc.fill('black')
        third = TextLine(sc, 100, 'DIEEE!!!!!', (800, 450), 'RED')
        third.draw()
        six = TextLine(sc, 20, 'press any button to START', (800, 800), 'GREY')
        six.draw()
        pg.display.update()
        time.sleep(0.5)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                flag = False
    pygame.mixer.music.set_volume(EFFECTS_VOLUME)

    main_menu_sound = pygame.mixer.music.load('sound/Music/MainMenuLoop.ogg')
    pygame.mixer.music.play(-1)
    while True:
        sc.fill('black')
        buttons = [
            Button((800, 230),
                   "PLAY", get_font(75), "#d7fcd4", "White"),
            Button((800, 380),
                   "LEADERBOARDS", get_font(75), "#d7fcd4", "White"),
            Button((795, 530),
                   "SETTINGS", get_font(75), "#d7fcd4", "White"),
            Button((800, 680),
                   "QUIT", get_font(75), "#d7fcd4", "White")
        ]
        mouse_pos = pygame.mouse.get_pos()

        for button in buttons:
            button.change_color(mouse_pos)
            button.update(sc)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if buttons[0].check_click(mouse_pos):
                    play()
                if buttons[1].check_click(mouse_pos):
                    leaderboards()
                if buttons[2].check_click(mouse_pos):
                    settings()
                if buttons[3].check_click(mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def play():
    # sc.fill('black')
    # first = TextLine(sc, 100, '3', (800, 450), 'WHITE')
    # first.draw()
    # pg.display.update()
    
    # time.sleep(1)

    # sc.fill('black')
    # first = TextLine(sc, 100, '2', (800, 450), 'WHITE')
    # first.draw()
    # pg.display.update()
    
    # time.sleep(1)

    # sc.fill('black')
    # first = TextLine(sc, 100, '1', (800, 450), 'RED')
    # first.draw()
    # pg.display.update()

    # time.sleep(1)

    # создание таймера на 1 секунду
    clock = pygame.time.Clock()
    counter = 30
    FPS = 60
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    display.fill((146, 244, 255))
    # создаем героя по (x,y) координатам
    hero_1 = Character(400, 820, 'red')
    hero_2 = Character(1120, 820, 'blue')
    hero_1_other = []
    hero_2_other = []
    left_1 = right_1 = False  # по умолчанию - стоим
    left_2 = right_2 = False
    up_1 = up_2 = False
    entities = pygame.sprite.Group()  # Поверхности(стенки, пол и тд)
    platforms = []  # поверхность
    other = []
    level = game_map

    y = 0
    for row in level:
        # print(row)
        x = 0
        for tile in row:
            if tile == 1:
                pf = Platform(x * 80, y * 45)
                entities.add(pf)
                platforms.append(pf)
            elif tile == 0:
                pf = Platform(x * 80, y * 45)
                entities.add(pf)
                other.append(pf)
            if tile == 2:
                pf = Platform(x * 80, y * 45)
                entities.add(pf)
                platforms.append(pf)
            if tile == 3:
                pf = Platform(x * 80, y * 45)
                entities.add(pf)
                platforms.append(pf)
            x += 1
        y += 1

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
                        display.blit(block_image, (x * 80, y * 45))
                    elif tile == 0:
                        display.blit(sky_image, (x * 80, y * 45))
                    if tile == 2:
                        display.blit(round_out, (x * 80, y * 45))
                    if tile == 3:
                        display.blit(rotated_round_out, (x * 80, y * 45))
                    if tile == 'b':
                        display.blit(image_trace_blue, (x * 80, y * 45))
                    if tile == 'r':
                        display.blit(image_trace_red, (x * 80, y * 45))
                    x += 1
                y += 1
            # print('--------------------------------')
            # for i in game_map:
            #     print(i)
            # print('--------------------------------')
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
        if counter > 0:
            # hero_1.draw_other('r')
            # hero_2.draw_other('b')
            sc.blit(display, (0, 0))
            hero_1.update(left_1, right_1, up_1, platforms, other, 'r')  # отображение
            hero_2.update(left_2, right_2, up_2, platforms, other, 'b')
            hero_1.draw(sc)
            hero_2.draw(sc)
            pygame.display.update()
        else:
            blue, red = 0, 0
            for row in level:
                for tile in row:
                    if tile == 'r':
                        red += 1
                    elif tile == 'b':
                        blue += 1
            if blue < red:
                sc.fill('black')
                first = TextLine(sc, 100, 'RED WIN', (800, 450), 'RED')
                first.draw()
                pg.display.update()
            elif blue > red:
                sc.fill('black')
                first = TextLine(sc, 100, 'BLUE WIN', (800, 450), 'BLUE')
                first.draw()
                pg.display.update()
            elif blue == red:
                sc.fill('black')
                first = TextLine(sc, 100, 'draw', (800, 450), 'WHITE')
                first.draw()
                pg.display.update()
        # clock.tick(FPS)


def settings():
    sc.fill('BLACK')
    textlines = [TextLine(sc, 46, '10', (1150, 460), '#d7fcd4'),
                 TextLine(sc, 46, '10', (1150, 560), '#d7fcd4'),
                 TextLine(sc, 75, 'SETTINGS', (800, 200), '#d7fcd4'),
                 TextLine(sc, 46, 'music', (370, 460), '#d7fcd4'),
                 TextLine(sc, 46, 'effects', (350, 560), '#d7fcd4')]
    for textline in textlines:
        textline.draw()
    sliders = [
        Slider((540, 450), (500, 30), 10, 0, 100),
        Slider((540, 550), (500, 30), 10, 0, 100)
    ]
    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        back_button = Button((1300, 750),
                             "Back", get_font(75), "#d7fcd4", "White")
        back_button.change_color(mouse_pos)
        back_button.update(sc)
        apply_button = Button((400, 750),
                              "Apply", get_font(75), "#d7fcd4", "White")
        apply_button.change_color(mouse_pos)
        apply_button.update(sc)
        for index, slider in enumerate(sliders):
            if slider.slider_rect.collidepoint(mouse_pos) and mouse[0]:
                slider.move_slider(mouse_pos)
            slider.draw(sc)
            current_textline = textlines[index]
            current_textline.text = str(int(slider.get_value() // 1))
            current_textline.value = int(slider.get_value() // 1)
            sc.fill('black', (current_textline.position[0] - 75, current_textline.position[1] - 30, 150, 75))
            current_textline.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_click(mouse_pos):
                    main_menu()
                if apply_button.check_click(mouse_pos):
                    pygame.mixer.music.set_volume(textlines[0].value)


def leaderboards():
    while True:
        sc.fill('BLACK')
        textlines = [TextLine(sc, 46, '10', (1150, 460), '#d7fcd4'),
                     TextLine(sc, 46, '10', (1150, 560), '#d7fcd4'),
                     TextLine(sc, 75, 'LEADERBOARDS', (800, 200), '#d7fcd4'),
                     TextLine(sc, 46, 'first record', (400, 300), '#d7fcd4'),
                     TextLine(sc, 46, 'second record', (400, 400), '#d7fcd4'),
                     TextLine(sc, 46, 'third record', (400, 500), '#d7fcd4'),
                     TextLine(sc, 46, 'fourth record', (400, 600), '#d7fcd4'),
                     TextLine(sc, 46, 'fifth record', (400, 700), '#d7fcd4')]
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        back_button = Button((1300, 750),
                             "Back", get_font(75), "#d7fcd4", "White")
        back_button.change_color(mouse_pos)
        back_button.update(sc)
        for textline in textlines:
            textline.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_click(mouse_pos):
                    main_menu()


main_menu()
