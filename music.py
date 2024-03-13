import pygame
import random

music_dict = {
    'game': ['sound/Music/InGame' + str(i) + 'Loop.ogg' for i in range(1, 10)],
    'menu': 'sound/Music/MainMenuLoop.ogg'
}

voicer_dict = {
    'countdown': 'sound/Voicer/game@countdown.ogg',
    'draw': 'sound/Voicer/game@draw.ogg',
    'go': 'sound/Voicer/agme@go.ogg',
    'time_up': 'sound/Voicer/game@time_up.ogg',
    'blue_win': 'sound/Voicer/menu@blue_final_win.ogg',
    'game_title': 'sound/Voicer/menu@game_title.ogg',
    'pink_win': 'sound/Voicer/menu@pink_win.ogg'
}

effects_dict = {

}


class Game_Music:
    def __init__(self):
        pygame.mixer.init()
        # default sounds
        self.voicer_sound = pygame.mixer.Sound(voicer_dict['game_title'])
        self.music_sound = pygame.mixer.Sound(music_dict['menu'])
        self.effects_sound = ''

    def change_sound(self, sound, sound_name):
        if sound == 'music':
            if sound_name == 'menu':
                self.music_sound = pygame.mixer.Sound(music_dict['menu'])
            else:
                self.music_sound = pygame.mixer.Sound(music_dict['game'][random.randint(0, 8)])
        elif sound == "voicer":
            self.voicer_sound = pygame.mixer.Sound('')
        else:
            self.effects_sound = pygame.mixer.Sound('')

    def change_voicer(self):
        self.music_sound = pygame.mixer.Sound('')

    def play(self, sound, times):
        if sound == 'music':
            self.music_sound.play(times)
        elif sound == 'voicer':
            self.voicer_sound.play(times)
        else:
            self.effects_sound.play(times)

    def stop(self, sound):
        if sound == 'music':
            self.music_sound.stop()
        elif sound == 'voicer':
            self.voicer_sound.stop()
        else:
            self.effects_sound.stop()
