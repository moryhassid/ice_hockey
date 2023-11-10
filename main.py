import pygame
import time
import os
import random

# Tasks:
# 5. Scoreboard saving scores on hard-disk
# 6. save how long the game was played

# Done:
# 2. Write name of players
# 3. In case of player losses, he keeps playing until the one of the players reach 5 points.
# 1. Scoreboard
# 4. Change the speed of the disk according to the level

BACKGROUND_COLOR = (0, 151, 171)


def is_disc_hit_the_wall(disc_pos, disc_direction_now):
    # have we reached left wall or right wall?
    if disc_pos.x <= 0 or disc_pos.x >= 1070:
        disc_direction_now['x'] = -disc_direction_now['x']
        print('You have reached the left or right wall')

    if disc_pos.y <= 0 or disc_pos.y >= 550:
        disc_direction_now['y'] = -disc_direction_now['y']
        print('You have reached the upper or lower wall')

    return disc_direction_now


def is_disc_reached_gate(disc_pos, racket1_pos, racket2_pos):
    if 175 <= disc_pos.y <= 375 and (disc_pos.x < 20 or disc_pos.x > 1060):
        print('You should look out for the disc, it might enter the gate')
        # The disc should enter the gate

        # The disc should be blocked by the racket, therefore the disc will jump to the center of the court.
        # The gate (175-375)
        return True

    return False


def is_racket_protecting_gate(disc_pos, racket1_pos, racket2_pos, disc_direction_now):
    # Rect(left, top, width, height)
    print(f"{my_racket2.top=}")
    if (racket2_pos.top <= disc_pos.y <= (racket2_pos.top + racket2_pos.height) and disc_pos.x < 20) \
            or \
            (racket1_pos.top <= disc_pos.y <= (racket1_pos.top + racket1_pos.height) and disc_pos.x > 900):
        print('Racket has protected gate')
        disc_direction_now['x'] = -disc_direction_now['x']
        disc_direction_now['y'] = -disc_direction_now['y']
        return True, disc_direction_now

    return False, disc_direction_now


def init_stage(screen, pace):
    disc_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    disc = pygame.draw.circle(screen, (255, 0, 0), disc_position, 15)
    x_direction = (random.random() > 0.5) * 2 - 1
    y_direction = (random.random() > 0.5) * 2 - 1
    pace = pace * 1.2
    disc_direction = {'x': x_direction * pace, 'y': y_direction * pace}

    return disc_position, disc, disc_direction, pace


def show_score_board(player1_name, player2_name, screen, pace):
    font = pygame.font.Font('fonts/ChrustyRock-ORLA.ttf', 32)
    # white = (255, 255, 255)
    # green = (0, 255, 0)
    # blue = (0, 0, 128)
    text_to_present = f'{player1_name}: 3, {player2_name}: 2'
    text_player = font.render(text_to_present, True, (0, 0, 0))

    # create a rectangular object for the
    # text surface object
    WIDTH_SCREEN = 1080
    HEIGHT_SCREEN = 550

    textRect = text_player.get_rect()

    # set the center of the rectangular object.
    textRect.center = (WIDTH_SCREEN // 2, HEIGHT_SCREEN // 2)
    print(f'{text_player=}')
    screen.blit(text_player, textRect)

    pygame.time.wait(5000)
    init_stage(screen, pace)


if __name__ == '__main__':
    pygame.init()

    font = pygame.font.Font('fonts/ChrustyRock-ORLA.ttf', 32)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    print('Welcome to ice hockey!!!')
    player1_name = input("Enter player1 name: ")
    player2_name = input("Enter player2 name: ")

    text_player1 = font.render(player1_name, True, (0, 0, 0))
    text_player2 = font.render(player2_name, True, (0, 0, 0))

    end_game = 10

    WIDTH_SCREEN = 1080
    HEIGHT_SCREEN = 550
    RACKET_HEIGHT = 100
    GATE_HEIGHT = 200
    POS_Y_PLAYER_1_2 = HEIGHT_SCREEN // 2 - GATE_HEIGHT // 2 - 30
    POS_X_PLAYER_1 = 50
    POS_X_PLAYER_2 = WIDTH_SCREEN - 60

    # pygame setup
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    screen.fill(BACKGROUND_COLOR)
    clock = pygame.time.Clock()
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    running = True
    color_racket = (25, 0, 0)
    color_gate = (255, 255, 255)
    # Rect(left, top, width, height)

    my_racket1 = pygame.Rect(1060, 220, 10, RACKET_HEIGHT)
    my_racket2 = pygame.Rect(10, 220, 10, RACKET_HEIGHT)

    # (left, top, width, height)
    gate1 = pygame.Rect(1070, 175, 10, GATE_HEIGHT)
    gate2 = pygame.Rect(0, 175, 10, GATE_HEIGHT)
    gate1_draw = pygame.draw.rect(screen, color_gate, gate1)
    gate2_draw = pygame.draw.rect(screen, color_gate, gate2)

    player_1 = pygame.draw.rect(screen, color_racket, my_racket1)
    player_2 = pygame.draw.rect(screen, color_racket, my_racket2)
    dt = 0
    pace = 10

    disc_position, disc, disc_direction, pace = init_stage(screen, pace)

    points = [0, 0]

    while running and points[0] < 5 and points[1] < 5:
        screen.fill(BACKGROUND_COLOR)
        # create a rectangular object for the
        # text surface object
        textRect1 = text_player1.get_rect()
        textRect2 = text_player1.get_rect()

        # set the center of the rectangular object.
        textRect1.center = (POS_X_PLAYER_1, POS_Y_PLAYER_1_2)
        textRect2.center = (POS_X_PLAYER_2, POS_Y_PLAYER_1_2)
        screen.blit(text_player1, textRect1)
        screen.blit(text_player2, textRect2)

        disc_position.x += disc_direction['x']
        disc_position.y += disc_direction['y']

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

        disc = pygame.draw.circle(screen, (255, 0, 0), disc_position, 15)

        pygame.display.set_caption(
            f'{player1_name}: {points[0]}, {player2_name}: {points[1]}')

        if is_disc_reached_gate(disc_position, my_racket1, my_racket2):
            was_gate_protected, disc_direction = is_racket_protecting_gate(disc_position, my_racket1, my_racket2,
                                                                           disc_direction)
            if not was_gate_protected:
                print("Swallow disc")
                show_score_board(player1_name, player2_name, screen, pace)
                if disc_position.x > WIDTH_SCREEN - 100:
                    points[1] += 1
                    disc_position, disc, disc_direction, pace = init_stage(screen, pace)
                elif disc_position.x < 10:
                    points[0] += 1
                    disc_position, disc, disc_direction, pace = init_stage(screen, pace)
        else:
            disc_direction = is_disc_hit_the_wall(disc_position, disc_direction)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(20) / 1000

    pygame.quit()
