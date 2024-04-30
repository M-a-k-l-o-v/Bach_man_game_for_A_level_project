import game
import copy
import board
import pygame
import homescreen
from game import *
from game import pacman
# from file1 import * 
# this imports all methods and all objects
pygame.init()


player_x = pacman.x_pos
player_y = pacman.y_pos

while homescreen.running:
    homescreen.display_surface.blit(homescreen.background_img,homescreen.background_rect,)
    if homescreen.play_button.draw(homescreen.display_surface):
        print('playing')
        homescreen.running = False
        homescreen.game_running = True
        break

    if homescreen.highscore_button.draw(homescreen.display_surface):
        print('LeaderBoard')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            homescreen.running = False
            pygame.quit()
    pygame.display.update()



while homescreen.game_running:
    # print("the game is running")
    #center_x = player_x + 23
    #center_y = player_y + 24

    # starts clock with fps
    game.timer.tick(game.fps)
    
    # power up timer 
    if game.counter < 19:
        game.counter += 1
        if game.counter > 3:
            flicker = False
    else:
        game.counter = 0
        game.flicker = True
    if game.powerup and game.power_counter < 600:
        game.power_counter += 1
    elif game.powerup and game.power_counter >= 600:
        game.power_counter = 0
        game.powerup = False
        game.eaten_ghost = [False, False, False, False]
    if game.startup_counter < 180 and not game.game_over and not game.game_won:
        game.moving = False
        game.startup_counter += 1
    else:
        game.moving = True


    game.screen.fill('black')
    game.draw_board()
    
    # ghost speed after eaten, change here
    if game.powerup:
        ghost_speeds = [1, 1, 1, 1]
    # ghost speed before eaten, change here
    else:
        ghost_speeds = [2, 2, 2, 2]
    if game.eaten_ghost[0]:
        ghost_speeds[0] = ghost_speeds[0] * 2
    if game.eaten_ghost[1]:
        ghost_speeds[1] = ghost_speeds[1] * 2
    if game.eaten_ghost[2]:
        ghost_speeds[2] = ghost_speeds[2] * 2
    if game.eaten_ghost[3]:
        ghost_speeds[3] = ghost_speeds[3] * 2
    if game.blinky_dead:
        ghost_speeds[0] = 4
    if game.inky_dead:
        ghost_speeds[1] = 4
    if game.pinky_dead:
        ghost_speeds[2] = 4
    if game.clyde_dead:
        ghost_speeds[3] = 4

    game.game_won = True
    for i in range(len(game.level)):
        if 1 in game.level[i] or 2 in game.level[i]:
            game.game_won = False

    
    game.pacman.draw_player()
    game.blinky.draw()
    game.pinky.draw()
    game.inky.draw()
    game.clyde.draw()
    game.draw_misc()
    player_circle = pygame.draw.circle(game.screen, 'black', (pacman.center_x, pacman.center_y), 20, 1)

    #targets = game.get_targets(blinky_x, blinky_y, inky_x, inky_y, pinky_x, pinky_y, clyde_x, clyde_y)

    
    if game.moving:
        player_x, player_y = game.pacman.move_player()
        if not game.blinky_dead and not game.blinky.in_box:
            blinky_x, blinky_y, blinky_direction = game.blinky.move_blinky()
        else:
            blinky_x, blinky_y, blinky_direction = game.blinky.move_clyde()
        if not game.pinky_dead and not game.pinky.in_box:
            pinky_x, pinky_y, pinky_direction = game.pinky.move_pinky()
        else:
            pinky_x, pinky_y, pinky_direction = game.pinky.move_clyde()
        if not game.inky_dead and not game.inky.in_box:
            inky_x, inky_y, inky_direction = game.inky.move_inky()
        else:
            inky_x, inky_y, inky_direction = game.inky.move_clyde()
        clyde_x, clyde_y, clyde_direction = game.clyde.move_clyde()
    game.score, game.powerup, game.power_counter, game.eaten_ghost = game.pacman.check_collisions(game.score, game.powerup, game.power_counter, game.eaten_ghost)
    # add to if not game.powerup to check if eaten ghosts
    if not game.powerup:
        if (player_circle.colliderect(game.blinky.rect) and not game.blinky.dead) or \
                (player_circle.colliderect(game.inky.rect) and not game.inky.dead) or \
                (player_circle.colliderect(game.pinky.rect) and not game.pinky.dead) or \
                (player_circle.colliderect(game.clyde.rect) and not game.clyde.dead):
            if game.lives > 0:
                game.lives -= 1
                game.startup_counter = 0
                game.powerup = False
                game.power_counter = 0
                player_x = 450
                player_y = 663
                game.direction = 0
                game.direction_command = 0
                blinky_x = 56
                blinky_y = 58
                blinky_direction = 0
                inky_x = 440
                inky_y = 388
                inky_direction = 2
                pinky_x = 440
                pinky_y = 438
                pinky_direction = 2
                clyde_x = 440
                clyde_y = 438
                clyde_direction = 2
                game.eaten_ghost = [False, False, False, False]
                game.blinky_dead = False
                game.inky_dead = False
                game.clyde_dead = False
                game.pinky_dead = False
            else:
                game.game_over = True
                game.moving = False
                game.startup_counter = 0
    if game.powerup and player_circle.colliderect(game.blinky.rect) and game.eaten_ghost[0] and not game.blinky.dead:
        if game.lives > 0:
            game.powerup = False
            game.power_counter = 0
            game.lives -= 1
            game.startup_counter = 0
            player_x = 450
            player_y = 663
            game.direction = 0
            game.direction_command = 0
            blinky_x = 56
            blinky_y = 58
            blinky_direction = 0
            inky_x = 440
            inky_y = 388
            inky_direction = 2
            pinky_x = 440
            pinky_y = 438
            pinky_direction = 2
            clyde_x = 440
            clyde_y = 438
            clyde_direction = 2
            game.eaten_ghost = [False, False, False, False]
            game.blinky_dead = False
            game.inky_dead = False
            game.clyde_dead = False
            game.pinky_dead = False
        else:
            game.game_over = True
            game.moving = False
            game.startup_counter = 0
    if game.powerup and player_circle.colliderect(game.inky.rect) and game.eaten_ghost[1] and not game.inky.dead:
        if game.lives > 0:
            game.powerup = False
            game.power_counter = 0
            game.lives -= 1
            game.startup_counter = 0
            player_x = 450
            player_y = 663
            game.direction = 0
            game.direction_command = 0
            blinky_x = 56
            blinky_y = 58
            blinky_direction = 0
            inky_x = 440
            inky_y = 388
            inky_direction = 2
            pinky_x = 440
            pinky_y = 438
            pinky_direction = 2
            clyde_x = 440
            clyde_y = 438
            clyde_direction = 2
            game.eaten_ghost = [False, False, False, False]
            game.blinky_dead = False
            game.inky_dead = False
            game.clyde_dead = False
            game.pinky_dead = False
        else:
            game.game_over = True
            game.moving = False
            game.startup_counter = 0
    if game.powerup and player_circle.colliderect(game.pinky.rect) and game.eaten_ghost[2] and not game.pinky.dead:
        if game.lives > 0:
            game.powerup = False
            game.power_counter = 0
            game.lives -= 1
            game.startup_counter = 0
            player_x = 450
            player_y = 663
            game.direction = 0
            game.direction_command = 0
            blinky_x = 56
            blinky_y = 58
            blinky_direction = 0
            inky_x = 440
            inky_y = 388
            inky_direction = 2
            pinky_x = 440
            pinky_y = 438
            pinky_direction = 2
            clyde_x = 440
            clyde_y = 438
            clyde_direction = 2
            game.eaten_ghost = [False, False, False, False]
            game.blinky_dead = False
            game.inky_dead = False
            game.clyde_dead = False
            game.pinky_dead = False
        else:
            game.game_over = True
            game.moving = False
            game.startup_counter = 0
    if game.powerup and player_circle.colliderect(game.clyde.rect) and game.eaten_ghost[3] and not game.clyde.dead:
        if game.lives > 0:
            game.powerup = False
            game.power_counter = 0
            game.lives -= 1
            game.startup_counter = 0
            player_x = 450
            player_y = 663
            game.direction = 0
            game.direction_command = 0
            blinky_x = 56
            blinky_y = 58
            blinky_direction = 0
            inky_x = 440
            inky_y = 388
            inky_direction = 2
            pinky_x = 440
            pinky_y = 438
            pinky_direction = 2
            clyde_x = 440
            clyde_y = 438
            clyde_direction = 2
            game.eaten_ghost = [False, False, False, False]
            game.blinky_dead = False
            game.inky_dead = False
            game.clyde_dead = False
            game.pinky_dead = False
        else:
            game.game_over = True
            game.moving = False
            game.startup_counter = 0
    if game.powerup and player_circle.colliderect(game.blinky.rect) and not game.blinky.dead and not game.eaten_ghost[0]:
        game.blinky_dead = True
        game.eaten_ghost[0] = True
        game.score += (2 ** game.eaten_ghost.count(True)) * 100
    if game.powerup and player_circle.colliderect(game.inky.rect) and not game.inky.dead and not game.eaten_ghost[1]:
        game.inky_dead = True
        game.eaten_ghost[1] = True
        game.score += (2 ** game.eaten_ghost.count(True)) * 100
    if game.powerup and player_circle.colliderect(game.pinky.rect) and not game.pinky.dead and not game.eaten_ghost[2]:
        game.pinky_dead = True
        game.eaten_ghost[2] = True
        game.score += (2 ** game.eaten_ghost.count(True)) * 100
    if game.powerup and player_circle.colliderect(game.clyde.rect) and not game.clyde.dead and not game.eaten_ghost[3]:
        game.clyde_dead = True
        game.eaten_ghost[3] = True
        game.score += (2 ** game.eaten_ghost.count(True)) * 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            homescreen.game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.direction_command = 0
            if event.key == pygame.K_LEFT:
                game.direction_command = 1
            if event.key == pygame.K_UP:
                game.direction_command = 2
            if event.key == pygame.K_DOWN:
                game.direction_command = 3
            if event.key == pygame.K_SPACE and (game.game_over or game.game_won):
                game.powerup = False
                game.power_counter = 0
                game.lives -= 1
                game.startup_counter = 0
                player_x = 450
                player_y = 663
                game.direction = 0
                game.direction_command = 0
                blinky_x = 56
                blinky_y = 58
                blinky_direction = 0
                inky_x = 440
                inky_y = 388
                inky_direction = 2
                pinky_x = 440
                pinky_y = 438
                pinky_direction = 2
                clyde_x = 440
                clyde_y = 438
                clyde_direction = 2
                game.eaten_ghost = [False, False, False, False]
                game.blinky_dead = False
                game.inky_dead = False
                game.clyde_dead = False
                game.pinky_dead = False
                game.score = 0
                game.lives = 3
                game.level = copy.deepcopy(board.boards)
                game.game_over = False
                game.game_won = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and game.direction_command == 0:
                game.direction_command = game.direction
            if event.key == pygame.K_LEFT and game.direction_command == 1:
                game.direction_command = game.direction
            if event.key == pygame.K_UP and game.direction_command == 2:
                game.direction_command = game.direction
            if event.key == pygame.K_DOWN and game.direction_command == 3:
                game.direction_command = game.direction

    if game.direction_command == 0 and pacman.turns[0]:
        pacman.direction = 0
    if game.direction_command == 1 and pacman.turns[1]:
        pacman.direction = 1
    if game.direction_command == 2 and pacman.turns[2]:
        pacman.direction = 2
    if game.direction_command == 3 and pacman.turns[3]:
        pacman.direction = 3

    if player_x > 900:
        player_x = -47
    elif player_x < -50:
        player_x = 897


    if game.blinky.in_box and game.blinky_dead:
        blinky_dead = False
    if game.inky.in_box and game.inky_dead:
        game.inky_dead = False
    if game.pinky.in_box and game.pinky_dead:
        game.pinky_dead = False
    if game.clyde.in_box and game.clyde_dead:
        game.clyde_dead = False

    pygame.display.flip()
pygame.quit()