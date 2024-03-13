import pygame


class Slider:
    def __init__(self, pos, size, init_value, min, max):
        self.pos = pos
        self.size = size
        self.init_value = size[0] / 100 * init_value
        self.left_pos = pos[0]
        self.top_pos = pos[1]
        self.right_pos = pos[0] + size[0]
        self.min = min
        self.max = max

        self.slider_rect = pygame.Rect(self.left_pos, self.top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.left_pos + self.init_value, self.top_pos, 10, self.size[1])

        self.number = self.init_value + self.left_pos

    def draw(self, screen):
        pygame.draw.rect(screen, 'blue', self.slider_rect)
        pygame.draw.rect(screen, 'red', self.button_rect)

    def move_slider(self, mouse_pos):
        pos = mouse_pos[0]
        self.number = pos
        if pos > self.right_pos - 5:
            pos = self.right_pos - 5
        if pos < self.left_pos + 5:
            pos = self.left_pos + 5
        self.button_rect.centerx = pos

    def get_value(self):
        whole_range = self.right_pos - self.left_pos - 1
        button_value = self.number - self.left_pos
        return (button_value / whole_range) * (self.max - self.min) + self.min
