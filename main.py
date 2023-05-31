import pygame
import time
import os

BACKGROUND_COLOR = (0, 151, 171)

if __name__ == '__main__':
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1080, 550))
    screen.fill(BACKGROUND_COLOR)
    clock = pygame.time.Clock()
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    running = True
    color = (25, 0, 0)
    # Rect(left, top, width, height)
    my_racket = pygame.Rect(1070, 220, 10, 60)
    player_1 = pygame.draw.rect(screen, color, my_racket)
    player_2 = pygame.draw.rect(screen, color, pygame.Rect(0, 220, 10, 60))
    dt = 0

    ball_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    disc = pygame.draw.circle(screen, (255, 0, 0), ball_position, 15)

    while running:

        player_1 = pygame.draw.rect(screen, color, my_racket)
        for event in pygame.event.get():
            # here we are checking if the user wants to exit the game
            if event.type == pygame.QUIT:
                print('Mory is closing the game')
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print('Up was pressed')
            screen.fill(BACKGROUND_COLOR)
            my_racket.move_ip(0, -5)
            pygame.draw.rect(screen, color, my_racket)
        if keys[pygame.K_DOWN]:
            print('Down was pressed')
            screen.fill(BACKGROUND_COLOR)
            my_racket.move_ip(0, 5)
            pygame.draw.rect(screen, color, my_racket)

        # TODO: Add keypress listener for the keys: "w" and "s"
        # "w" - for up
        # "s" - for down

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(20) / 1000

    pygame.quit()
