import pygame
import cv2
import game


# Classe de la balle
class Ball(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = 12
        self.image = pygame.image.load("ball.png")
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.x = 453
        self.rect.y = 450
        self.collide = bool
        self.col = bool

    # Fonction de la physique de la balle
    def move(self):
        if self.rect.x >= 905:
            self.remove()
            self.game.start = False
        if self.rect.x <= 4:
            self.remove()
            self.game.start = False

        # Collision avec le joueur 1
        if self.game.check(self, self.game.player_1):
            self.game.sound_manager.play('tir')
            self.game.player_1.add_score()
            self.collide = False

        # Collision avec le joueur 2
        if self.game.check(self, self.game.player_2):
            self.game.sound_manager.play('tir')
            self.game.player_2.add_score()
            self.collide = True

        if self.collide:
            self.rect.x -= self.velocity
        if not self.collide:
            self.rect.x += self.velocity

        if self.rect.y >= 905:
            self.col = True
        if self.rect.y <= 4:
            self.col = False

        if self.col:
            self.rect.y -= self.velocity
        if not self.col:
            self.rect.y += self.velocity - 0.7


