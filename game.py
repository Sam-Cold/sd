import pygame
from ball import Ball
from player import Player
from sounds import SoundManager

# Classe du jeu
class Game:

    def __init__(self):
        self.sound_manager = SoundManager()
        self.player_1 = Player(4, 375)
        self.player_2 = Player(920, 375)
        self.ball = Ball(self)
        self.start = False
        self.pressed = {}
        self.font = pygame.font.SysFont("Night Machine", 60)

    def check(self, sprite, sprit_2):
        return pygame.sprite.collide_rect(sprite, sprit_2)

    def update(self, screen, stade):
        # Affichage des images
        screen.blit(self.player_1.image, self.player_1.rect)
        screen.blit(self.player_2.image, self.player_2.rect)
        screen.blit(self.ball.image, self.ball.rect)
        self.ball.move()
        text = self.font.render("{} | {}".format(self.player_1.score, self.player_2.score), 1,
                                      (255, 0, 0))
        screen.blit(text, (1000, 0))

    def game_over(self):
        self.player_1.score = 0
        self.player_2.score = 0
        self.player_1.rect.x = 4
        self.player_1.rect.y = 375
        self.player_2.rect.x = 920
        self.player_2.rect.y = 375
        self.ball.rect.x = 453
        self.ball.rect.y = 450
