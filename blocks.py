#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os

PLATFORM_WIDTH = 80
PLATFORM_HEIGHT = 45
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
