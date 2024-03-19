class Button:
    def __init__(self, pos, text, font, base_color, hovering_color):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.t = text
        self.text = self.font.render(self.t, True, self.base_color)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.text, self.text_rect)

    def change_color(self, position):
        if position[0] not in range(self.rect.left, self.rect.right) or position[1] not in range(self.rect.top,
                                                                                                 self.rect.bottom):
            self.text = self.font.render(self.t, True, self.base_color)
        else:
            self.text = self.font.render(self.t, True, self.hovering_color)

    def check_click(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
