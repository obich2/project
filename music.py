import pygame
import random

music_dict = {
    'game': ['sound/Music/InGame' + str(i) + 'Loop.ogg' for i in range(1, 10)],
    'menu': 'sound/Music/MainMenuLoop.ogg'
}

voicer_dict = {
    'countdown': 'sound/Voicer/game@countdown.ogg',
    'draw': 'sound/Voicer/game@draw.ogg',
    'ready_go': 'sound/Voicer/game@go.ogg',
    'time_up': 'sound/Voicer/game@time_up.ogg',
    'blue_win': 'sound/Voicer/menu@blue_final_win.ogg',
    'game_title': 'sound/Voicer/menu@game_title.ogg',
    'pink_win': 'sound/Voicer/menu@pink_win.ogg'
}

effects_dict = {
    'jump': 'sound/Effects/jump.mp3'
}


class Game_Music:
    def __init__(self):
        pygame.mixer.init()
        # default sounds
        self.voicer_sound = pygame.mixer.Sound(voicer_dict['game_title'])
        self.music_sound = pygame.mixer.Sound(music_dict['menu'])
        self.effects_sound = pygame.mixer.Sound(effects_dict['jump'])
        self.sounds = [self.voicer_sound, self.music_sound, self.effects_sound]
        self.voicer_volume = 0.5
        self.music_volume = 0.5
        self.effects_volume = 0.5
        for i in self.sounds[:-1]:
            i.set_volume(0.5)

    def change_sound(self, sound, sound_name):
        if sound == 'music':
            if sound_name == 'menu':
                self.music_sound = pygame.mixer.Sound(music_dict['menu'])
            else:
                self.music_sound = pygame.mixer.Sound(music_dict['game'][random.randint(0, 8)])
        elif sound == "voicer":
            self.voicer_sound = pygame.mixer.Sound(voicer_dict[sound_name])
        else:
            self.effects_sound = pygame.mixer.Sound(effects_dict[sound_name])

    def change_voicer(self):
        self.music_sound = pygame.mixer.Sound('')

    def play(self, sound, times):
        if sound == 'music':
            self.music_sound.set_volume(self.music_volume)
            self.music_sound.play(times)
        elif sound == 'voicer':
            self.voicer_sound.set_volume(self.voicer_volume)
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

    def change_volume(self, sound, volume):
        if sound == 'music':
            self.music_volume = volume
            self.music_sound.set_volume(volume)
        elif sound == 'voicer':
            self.voicer_volume = volume
            self.voicer_sound.set_volume(volume)
        else:
            self.effects_volume = volume
            self.effects_sound.set_volume(volume)
