import pygame
import time
import os

BACKGROUND_COLOR = (0, 151, 171)


def is_disc_hit_the_wall(ball_pos):
    if ball_pos.x == 0 or ball_pos.x == 1070:
        print('You have reached the left or right wall')
    elif ball_pos.y == 0 or ball_pos.y == 440:
        print('You have reached the upper or lower wall')


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
    my_racket1 = pygame.Rect(1070, 220, 10, 60)
    my_racket2 = pygame.Rect(0, 220, 10, 60)
    player_1 = pygame.draw.rect(screen, color, my_racket1)
    player_2 = pygame.draw.rect(screen, color, my_racket2)
    dt = 0

    ball_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    disc = pygame.draw.circle(screen, (255, 0, 0), ball_position, 15)

    ball_direction = {'x': -5, 'y': 0}

    while running:
        screen.fill(BACKGROUND_COLOR)
        ball_position.x += ball_direction['x']
        ball_position.y += ball_direction['y']

        player_1 = pygame.draw.rect(screen, color, my_racket1)
        for event in pygame.event.get():
            # here we are checking if the user wants to exit the game
            if event.type == pygame.QUIT:
                print('Mory is closing the game')
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print('Up was pressed')
            # screen.fill(BACKGROUND_COLOR)
            my_racket1.move_ip(0, -5)
        elif keys[pygame.K_DOWN]:
            print('Down was pressed')
            # screen.fill(BACKGROUND_COLOR)
            my_racket1.move_ip(0, 5)
            keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            print('Up was pressed')
            my_racket2.move_ip(0, -5)
        elif keys[pygame.K_s]:
            print('Down was pressed')
            # screen.fill(BACKGROUND_COLOR)
            my_racket2.move_ip(0, 5)

        pygame.draw.rect(screen, color, my_racket1)
        pygame.draw.rect(screen, color, my_racket2)
        disc = pygame.draw.circle(screen, (255, 0, 0), ball_position, 15)

        is_disc_hit_the_wall(ball_position)
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(20) / 1000

    pygame.quit()
