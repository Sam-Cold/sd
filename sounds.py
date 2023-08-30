import pygame


class SoundManager:

    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound("click.ogg"),
            "tir": pygame.mixer.Sound("tir.ogg"),
        }

    def play(self, name):
        self.sounds[name].play()
