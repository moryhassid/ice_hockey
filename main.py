# Old file from New computer!
import pygame
import time
import os

BACKGROUND_COLOR = (0, 151, 171)


def is_disc_hit_the_wall(ball_pos, ball_direction_now):
    # have we reached left wall or right wall?
    if ball_pos.x <= 0 or ball_pos.x >= 1070:
        ball_direction_now['x'] = -ball_direction_now['x']
        print('You have reached the left or right wall')

    if ball_pos.y <= 0 or ball_pos.y >= 550:
        ball_direction_now['y'] = -ball_direction_now['y']
        print('You have reached the upper or lower wall')

    return ball_direction_now


def is_disc_reached_gate(ball_pos, racket1_pos, racket2_pos):
    if 175 <= ball_pos.y <= 375 and (ball_pos.x < 20 or ball_pos.x > 1060):
        print('You should look out for the disc, it might enter the gate')
        # TODO: how to handle a scenario when disc is in the gate region and racket is not?
        # The disc should enter the gate

        # TODO: how to handle a scenario when disc is in the gate region and racket is in the gate too?
        # The disc should be blocked by the racket, therefore the disc will jump to the center of the court.
        # The gate (175-375)
        return True


def is_racket_protecting_gate(ball_pos, racket1_pos, racket2_pos):
    # Rect(left, top, width, height)
    if racket2_pos.top <= ball_pos.y <= racket2_pos.top + racket2_pos.height or \
            racket1_pos.top <= ball_pos.y <= racket1_pos.top + racket1_pos.height:
        print('Racket has protected gate')
        return True

    return False


if __name__ == '__main__':

    print('Welcome to ice hockey!!!')
    player1_name = input("Enter player1 name: ")
    player2_name = input("Enter player2 name: ")

    player1_score = 0
    player2_score = 0
    end_game = 10

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1080, 550))
    screen.fill(BACKGROUND_COLOR)
    clock = pygame.time.Clock()
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    running = True
    color_racket = (25, 0, 0)
    color_gate = (255, 255, 255)
    # Rect(left, top, width, height)
    racket_height = 100
    gate_height = 200
    my_racket1 = pygame.Rect(1060, 220, 10, racket_height)
    my_racket2 = pygame.Rect(10, 220, 10, racket_height)

    # (left, top, width, height)
    gate1 = pygame.Rect(1070, 175, 10, gate_height)
    gate2 = pygame.Rect(0, 175, 10, gate_height)
    gate1_draw = pygame.draw.rect(screen, color_gate, gate1)
    gate2_draw = pygame.draw.rect(screen, color_gate, gate2)

    player_1 = pygame.draw.rect(screen, color_racket, my_racket1)
    player_2 = pygame.draw.rect(screen, color_racket, my_racket2)
    dt = 0

    ball_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    disc = pygame.draw.circle(screen, (255, 0, 0), ball_position, 15)

    ball_direction = {'x': -10, 'y': -10}

    while running:
        screen.fill(BACKGROUND_COLOR)
        ball_position.x += ball_direction['x']
        ball_position.y += ball_direction['y']

        player_1 = pygame.draw.rect(screen, color_racket, my_racket1)
        for event in pygame.event.get():
            # here we are checking if the user wants to exit the game
            if event.type == pygame.QUIT:
                print('Mory is closing the game')
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print('Up was pressed')
            my_racket1.move_ip(0, -5)
        elif keys[pygame.K_DOWN]:
            print('Down was pressed')
            my_racket1.move_ip(0, 5)
            keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            print('Up was pressed')
            my_racket2.move_ip(0, -5)
        elif keys[pygame.K_s]:
            print('Down was pressed')
            my_racket2.move_ip(0, 5)

        pygame.draw.rect(screen, color_racket, my_racket1)
        pygame.draw.rect(screen, color_racket, my_racket2)

        gate1_draw = pygame.draw.rect(screen, color_gate, gate1)
        gate2_draw = pygame.draw.rect(screen, color_gate, gate2)

        disc = pygame.draw.circle(screen, (255, 0, 0), ball_position, 15)

        pygame.display.set_caption(
            f'{player1_name}: {player1_score}, {player2_name}: {player2_score}')

        if is_disc_reached_gate(ball_position, my_racket1, my_racket2):
            if not is_racket_protecting_gate(ball_position, my_racket1, my_racket2):
                print("Swallow ball")
                break
        else:
            ball_direction = is_disc_hit_the_wall(ball_position, ball_direction)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(20) / 1000

    pygame.quit()
