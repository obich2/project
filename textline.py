import pygame


class TextLine:
    def __init__(self, screen, font_size, text, position, color):
        self.screen = screen
        self.font = font_size
        self.text = text
        self.value = 0
        self.position = position
        self.color = color
        self.rect = ''
        self.flag = True

    def draw(self):
        if self.flag:
            self.text = get_font(self.font).render(self.text, True, self.color)
            print(self.text)
            self.rect = self.text.get_rect(center=self.position)
            self.screen.blit(self.text, self.rect)
            self.flag = False
        else:
            self.rect = self.text.get_rect(center=self.position)
            self.screen.blit(self.text, self.rect)

    def change_text(self, text, color='same'):
        if color != 'same':
            self.color = color
        self.text = text
        self.flag = 'True'


def get_font(size):
    return pygame.font.Font("font.ttf", size)
