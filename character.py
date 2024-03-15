import pygame
from pygame import *
import os
from settings import *

MOVE_SPEED = 7
WIDTH = 80
HEIGHT = 40
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз


class Character(sprite.Sprite):
    def __init__(self, x, y, color):
        sprite.Sprite.__init__(self)
        self.V_x = 0  # скорость горизонтального перемещения
        self.startX = x
        self.startY = y
        self.V_y = 0  # скорость вертикального перемещения
        self.onGround = False  # опирается ли на что-то персоонаж
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image_player = pygame.image.load('tiles/body_' + color + '.png').convert_alpha()
        # self.image_player_b = pygame.image.load('tiles/body_bomb_' + color + '.png').convert_alpha()
        self.image = self.image_player
        self.rect_other = Rect(x, y, WIDTH, HEIGHT)
        self.color = color

    def update(self, left, right, up, platforms, other, color):

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
        self.collide(0, self.V_y, platforms, other, color)

        self.rect.x += self.V_x # переносим положение на V_x
        self.collide(self.V_x, 0, platforms, other, color)

    def collide(self, V_x, V_y, platforms, other, color):
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
        for i in other:
            if sprite.collide_rect(self, i):  # столкновение с объектами
                self.rect_other.left = i.rect.left
                self.rect_other.top = i.rect.top
                level(int(self.rect_other.top) // 45, int(self.rect_other.left) // 80, color)
    
    def collide_bomb(self, bomb):
        if sprite.collide_rect(self, bomb):
            self.image = self.image_player_b
            return True
        else:
            self.image = self.image_player
            return False


    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    # def draw_other(self, color):
    #     print(int(self.rect_other.left) // 80, int(self.rect_other.top) // 45)
    #     level(int(self.rect_other.left) // 80, int(self.rect_other.top) // 45, color)
    