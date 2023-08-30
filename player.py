import pygame


# Classe du joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.velocity = 10
        self.score = 0
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def add_score(self):
        self.score += 1
        