import pygame as pg
from settings import *
from character import *
from blocks import *
import pygame.display
import time
import sqlite3
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
        self.con = sqlite3.connect("database/games_db.sqlite")

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
        counter = 15
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
                game_running = False
                self.game_music.stop('music')
                if blue < red:
                    sc.fill('black')
                    self.game_music.change_sound('voicer', 'pink_win')
                    self.game_music.play('voicer', 1)
                    timer_text = TextLine(sc, 100, 'PINK WINS', (800, 450), 'PINK')
                    timer_text.draw()
                    pg.display.update()
                    time.sleep(1.8)
                    pg.display.update()
                    self.game_music.stop('voicer')
                    self.main_menu()
                elif blue > red:
                    self.game_music.change_sound('voicer', 'blue_win')
                    self.game_music.play('voicer', 1)
                    sc.fill('black')
                    timer_text = TextLine(sc, 100, 'BLUE WINS', (800, 450), 'BLUE')
                    timer_text.draw()
                    pg.display.update()
                    time.sleep(3)
                    self.game_music.stop('voicer')
                    self.main_menu()
                elif blue == red:
                    self.game_music.change_sound('voicer', 'draw')
                    self.game_music.play('voicer', 1)
                    sc.fill('black')
                    timer_text = TextLine(sc, 100, 'draw', (800, 450), 'WHITE')
                    timer_text.draw()
                    pg.display.update()
                    time.sleep(1)
                    self.game_music.stop('voicer')
                    self.main_menu()

    def settings(self):
        sc = self.sc
        sc.fill('BLACK')
        textlines = [TextLine(sc, 46, str(int(self.game_music.voicer_volume * 100)), (1150, 320), '#d7fcd4'),
                     TextLine(sc, 46, str(int(self.game_music.music_volume * 100)), (1150, 420), '#d7fcd4'),
                     TextLine(sc, 46, str(int(self.game_music.effects_volume * 100)), (1150, 520), '#d7fcd4'),
                     TextLine(sc, 75, 'SETTINGS', (800, 200), '#d7fcd4'),
                     TextLine(sc, 46, 'voicer', (350, 320), '#d7fcd4'),
                     TextLine(sc, 46, 'music', (370, 420), '#d7fcd4'),
                     TextLine(sc, 46, 'effects', (350, 520), '#d7fcd4')
                     ]
        for textline in textlines:
            textline.draw()
        sliders = [
            Slider((540, 310), (500, 30), int(self.game_music.voicer_volume * 100), 0, 100),
            Slider((540, 410), (500, 30), int(self.game_music.music_volume * 100), 0, 100),
            Slider((540, 510), (500, 30), int(self.game_music.effects_volume * 100), 0, 100)
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
                    for index, slider in enumerate(sliders):
                        if slider.slider_rect.collidepoint(mouse_pos) and mouse[0]:
                            slider.move_slider(mouse_pos)
                    if back_button.check_click(mouse_pos):
                        self.main_menu()
                    if apply_button.check_click(mouse_pos):
                        self.game_music.change_volume('voicer', textlines[0].value / 100)
                        self.game_music.change_volume('music', textlines[1].value / 100)
                        # self.game_music.change_volume('effects', textlines[2].value / 100)

    def leaderboards(self):
        cur = self.con.cursor()
        result = sorted([i[0] for i in cur.execute("""SELECT score FROM stats""").fetchall()], reverse=True)
        sc = self.sc
        while True:
            sc.fill('BLACK')
            textlines = [TextLine(sc, 46, str(result[0]), (1150, 340), '#d7fcd4'),
                         TextLine(sc, 46, str(result[1]), (1150, 440), '#d7fcd4'),
                         TextLine(sc, 46, str(result[2]), (1150, 540), '#d7fcd4'),
                         TextLine(sc, 75, 'LEADERBOARDS', (800, 200), '#d7fcd4'),
                         TextLine(sc, 46, 'first record', (600, 340), '#d7fcd4'),
                         TextLine(sc, 46, 'second record', (600, 440), '#d7fcd4'),
                         TextLine(sc, 46, 'third record', (600, 540), '#d7fcd4'),
                         ]
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
