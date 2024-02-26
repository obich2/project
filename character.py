import pygame
from pygame import *
import os

MOVE_SPEED = 7
WIDTH = 80
HEIGHT = 45
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.1  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


class Character(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.V_x = 0  # скорость горизонтального перемещения
        self.startX = x
        self.startY = y
        self.V_y = 0  # скорость вертикального перемещения
        self.onGround = False  # опирается ли на что-то персоонаж
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image = pygame.image.load('tiles/body.png').convert_alpha()

    def update(self, left, right, up, platforms):

        if up:  # прыжок
            if self.onGround:  # проверка на соприкосновение с поверхностью
                self.V_y = -JUMP_POWER

        if left:
            self.V_x = -MOVE_SPEED  # Лево = x- n

        if right:
            self.V_x = MOVE_SPEED  # Право = x + n

        if not (left or right):  # стоим, когда нет указаний идти
            self.V_x = 0

        if not self.onGround:
            self.V_y += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле
        self.rect.y += self.V_y
        self.collide(0, self.V_y, platforms)

        self.rect.x += self.V_x  # переносим положение на V_x
        self.collide(self.V_x, 0, platforms)

    def collide(self, V_x, V_y, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # столкновение с объектами

                if V_x > 0:  # право
                    self.rect.right = p.rect.left

                if V_x < 0:  # лево
                    self.rect.left = p.rect.right

                if V_y > 0:  # падение
                    self.rect.bottom = p.rect.top
                    self.onGround = True  # есть прикосновение к земле
                    self.V_y = 0

                if V_y < 0:  # прыжок
                    self.rect.top = p.rect.bottom
                    self.V_y = 0

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))
