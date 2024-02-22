class Button:
    def __init__(self, pos, text, font, base_color, hovering_color):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text = text
        self.text = self.font.render(self.text, True, self.base_color)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.text, self.text_rect)

    def change_color(self, position):
        if self.rect.left <= position[0] <= self.rect.right and self.rect.bottom <= position[1] <= self.rect.top:
            self.text = self.font.render(self.text, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text, True, self.base_color)

    def check_click(self, position):
        if self.rect.left <= position[0] <= self.rect.right and self.rect.bottom <= position[1] <= self.rect.top:
            return True
        return False
