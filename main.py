import pygame as pg
from settings import *
from character import *
from blocks import *
import pygame.display
import time
import sys
from button import Button
from slider import Slider
from textline import TextLine, get_font
from music import Game_Music

sc = pg.display.set_mode((1600, 900))
display = pg.Surface((1600, 900))


class Game:
    def __init__(self, sc, display):
        self.sc = sc
        self.display = display
        display = self.display
        pg.display.set_caption('Move or Die')
        pg.display.set_icon(app_icon)
        self.flag = True
        self.menu_flag = True
        self.game_flag = True
        self.game_music = Game_Music()
        self.splash_screen()

    def splash_screen(self):
        sc = self.sc
        while self.flag:
            self.game_music.play('voicer', 1)
            sc.fill('black')
            splash_text = TextLine(sc, 100, 'MOVE', (800, 450), 'WHITE')
            any_button_text = TextLine(sc, 20, 'press any button to START', (800, 800), 'GREY')
            any_button_text.draw()
            splash_text.draw()
            pg.display.update()
            time.sleep(0.75)

            sc.fill('black')
            splash_text.change_text('OR')
            splash_text.draw()
            any_button_text.draw()
            pg.display.update()

            time.sleep(0.5)

            sc.fill('black')
            splash_text.change_text('DIEEEEEE', 'RED')
            splash_text.draw()
            any_button_text.draw()
            pg.display.update()
            time.sleep(0.5)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    self.game_music.stop('voicer')
                    self.flag = False
            self.game_music.stop('voicer')

    def main_menu(self):
        if self.menu_flag:
            self.game_music.change_sound('music', 'menu')
            self.game_music.play('music', -1)
            self.menu_flag = False
            self.game_flag = True

        while True:
            sc = self.sc
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
                        self.game_music.stop('music')
                        self.play()
                    if buttons[1].check_click(mouse_pos):
                        self.leaderboards()
                    if buttons[2].check_click(mouse_pos):
                        self.settings()
                    if buttons[3].check_click(mouse_pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()

    def play(self):
        self.game_music.change_sound('voicer', 'countdown')
        self.game_music.play('voicer', 1)
        sc = self.sc
        before_game_text = ['5', '4', '3', '2', '1', 'READY', 'GO']
        for text in before_game_text:
            if text == 'READY':
                self.game_music.stop('voicer')
                self.game_music.change_sound('voicer', 'ready_go')
                self.game_music.play('voicer', 1)
            sc.fill('black')
            timer_text = TextLine(sc, 100, text, (800, 450), 'WHITE')
            timer_text.draw()
            pg.display.update()
            time.sleep(1)
        self.game_music.stop('voicer')

        if self.game_flag:
            self.game_music.change_sound('music', 'game')
            self.game_music.play('music', -1)
            self.game_flag = False
            self.menu_flag = True

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
            timer_text = f.render(str(counter), True,
                                  (255, 255, 255))
            display.blit(timer_text, (800, 800))
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
                            display.blit(sky_image, (x * 80, y * 45))
                        if tile == 2:
                            pf = Platform(x * 80, y * 45)
                            entities.add(pf)
                            platforms.append(pf)
                            display.blit(round_out, (x * 80, y * 45))
                        if tile == 3:
                            pf = Platform(x * 80, y * 45)
                            entities.add(pf)
                            platforms.append(pf)
                            display.blit(rotated_round_out, (x * 80, y * 45))
                        x += 1
                    y += 1
                for i in hero_1_other:
                    print('РИСУЕМ')
                    display.blit(image_trace_red, (i[0], i[1]))
                for i in hero_2_other:
                    display.blit(image_trace_blue, (i[0], i[1]))
                if event.type == pygame.USEREVENT:
                    counter -= 1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.K_ESCAPE:
                    self.game_music.stop('music')
                    self.main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game_music.stop('music')
                    self.main_menu()
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
                    timer_text = TextLine(sc, 100, 'RED WIN', (800, 450), 'RED')
                    timer_text.draw()
                    pg.display.update()
                elif len(hero_2_other) > len(hero_1_other):
                    sc.fill('black')
                    timer_text = TextLine(sc, 100, 'BLUE WIN', (800, 450), 'BLUE')
                    timer_text.draw()
                    pg.display.update()
                elif len(hero_2_other) == len(hero_1_other):
                    sc.fill('black')
                    timer_text = TextLine(sc, 100, 'draw', (800, 450), 'WHITE')
                    timer_text.draw()
                    pg.display.update()

    def settings(self):
        sc = self.sc
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
                current_textline.change_text(str(int(slider.get_value() // 1)))
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
                        self.main_menu()
                    if apply_button.check_click(mouse_pos):
                        pygame.mixer.music.set_volume(textlines[0].value)

    def leaderboards(self):
        sc = self.sc
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
                        self.main_menu()


pg.init()

# images
block_image = pg.image.load('tiles/block.png')
app_icon = pg.image.load('tiles/icon.png')
round_out = pg.image.load('tiles/RoundOut.png').convert_alpha()
# sounds

rotated_round_out = pygame.transform.flip(round_out, True, False)
sky_image = pg.image.load('tiles/sky.png')
image_trace_red = pygame.image.load('tiles/red.png')
image_trace_blue = pygame.image.load('tiles/blue.png')

TILE_SIZE = block_image.get_width()

game = Game(sc, display)
game.main_menu()
