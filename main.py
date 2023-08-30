import pygame

import player
from game import Game

# Intialliaon de pygame
pygame.init()
game = Game()

# Initialisation de la fenetre
screen = pygame.display.set_mode((1200, 950))
pygame.display.set_caption("SD-PONG")

# Chargement des images
# Image du stade
stade = pygame.image.load("stade.png")
stade = pygame.transform.scale(stade, (950, 950))
# Image acceuil
bg = pygame.image.load("bg.png")
# Boucle du jeu
running = True
while running:
    # Couleur d'arriere plan
    screen.fill("Black")

    # Joueur 2
    if game.pressed.get(pygame.K_UP) and game.player_2.rect.y > 5:
        game.player_2.move_up()
    if game.pressed.get(pygame.K_DOWN) and game.player_2.rect.y < 760:
        game.player_2.move_down()

    # joueur 1
    if game.pressed.get(pygame.K_w) and game.player_1.rect.y > 5:
        game.player_1.move_up()
    if game.pressed.get(pygame.K_s) and game.player_1.rect.y < 760:
        game.player_1.move_down()

    # Affichage du stade
    screen.blit(stade, (0, 0))

    if game.start:
        game.update(screen, stade)
    elif not game.start:
        screen.blit(bg, (0, 0))
        game.game_over()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Gestion des touches
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.sound_manager.play('click')
                game.start = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    # Actualisation de l'ecran
    pygame.display.flip()
