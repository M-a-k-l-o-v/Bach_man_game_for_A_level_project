import pygame
from Home.popup_pages import login_popup, highscore_popup, highscore_personal_popup
from db_manager import *
from Home.homescreen import *
from Game.game import *


program = True
home_page_running = True
highscore_page_running = False
game_running = False
logged_in = False

while program:
    while home_page_running:

        display_surface.blit(background_img, background_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home_page_running = False
                program = False

        if play_button.draw(display_surface) and not logged_in:
            username, password = login_popup()
            if (username is not None) and (password is not None):
                player = Login(username,password,username_table,scores_table)
                player.login_process()
                if player.login:
                    logged_in = True
                    home_page_running = False
                    game_running = True

        elif play_button.draw(display_surface) and logged_in: 
            home_page_running = False
            game_running = True
        
        if (highscore_button.draw(display_surface)) and not logged_in:
            username, password = login_popup()
            if (username is not None) and (password is not None):
                player = Login(username,password,username_table,scores_table)
                player.login_process()
                if player.login:
                    logged_in = True
                    home_page_running = False
                    highscore_page_running = True
            
        elif highscore_button.draw(display_surface) and logged_in: 
            home_page_running = False
            highscore_page_running = True
        
        
        pygame.display.flip()

    while highscore_page_running:
        
        leaderboard = player.get_top_high_scores_global()
        Ldpopup_closed,popup_scoreboard = highscore_popup(leaderboard)
        if Ldpopup_closed:
            highscore_popup(leaderboard)
        elif popup_scoreboard:
            home_page_running = True
            highscore_page_running  =False

        scoreboard = player.get_top_high_scores_private()
        homescreen_popup, popup_leaderboard= highscore_personal_popup(scoreboard)
        if popup_leaderboard:
            highscore_popup(leaderboard)
        elif homescreen_popup:
            home_page_running = True
            highscore_page_running  =False
        
    while game_running:
        timer.tick(fps)
        draw_player()
        draw_misc()
        turns_allowed = check_position(center_x, center_y)
        player_circle = pygame.draw.circle(screen, 'black', (center_x, center_y), 20, 2)
        score, powerup, power_counter, weakness, weakness_counter, eaten_ghost = check_collisions(score, powerup, power_counter, weakness, weakness_counter,eaten_ghost)
        targets = get_targets(blinky_x, blinky_y, inky_x, inky_y, pinky_x, pinky_y, clyde_x, clyde_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction_command = 0
                if event.key == pygame.K_LEFT:
                    direction_command = 1
                if event.key == pygame.K_UP:
                    direction_command = 2
                if event.key == pygame.K_DOWN:
                    direction_command = 3


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and direction_command == 0:
                    direction_command = direction
                if event.key == pygame.K_LEFT and direction_command == 1:
                    direction_command = direction
                if event.key == pygame.K_UP and direction_command == 2:
                    direction_command = direction
                if event.key == pygame.K_DOWN and direction_command == 3:
                    direction_command = direction
        if direction_command == 0 and turns_allowed[0]:
            direction = 0
        if direction_command == 1 and turns_allowed[1]:
            direction = 1
        if direction_command == 2 and turns_allowed[2]:
            direction = 2
        if direction_command == 3 and turns_allowed[3]:
            direction = 3

        
        if blinky.in_box and blinky_dead:
            blinky_dead = False
        if inky.in_box and inky_dead:
            inky_dead = False
        if pinky.in_box and pinky_dead:
            pinky_dead = False
        if clyde.in_box and clyde_dead:
            clyde_dead = False


        if counter < 19:
            counter += 1
            if counter > 3:
                flicker = False
        else:
            counter = 0
            flicker = True
        if powerup and power_counter < 600:
            power_counter += 1
        elif powerup and power_counter >= 600:
            power_counter = 0
            powerup = False
            eaten_ghost = [False, False, False, False]
        
        if weakness and weakness_counter < 600:
            weakness_counter += 1
        elif weakness and weakness_counter >= 600:
            weakness_counter = 0
            weakness = False
            eaten_ghost = [False, False, False, False]
    
        if startup_counter < 180 and not game_over and not game_won:
            moving = False
            startup_counter += 1
        else:
            moving = True

        if powerup:
            ghost_speeds = [1, 1, 1, 1]
        else:
            ghost_speeds = [2, 2, 2, 2]
        if eaten_ghost[0]:
            ghost_speeds[0] = 2
        if eaten_ghost[1]:
            ghost_speeds[1] = 2
        if eaten_ghost[2]:
            ghost_speeds[2] = 2
        if eaten_ghost[3]:
            ghost_speeds[3] = 2
        if blinky_dead:
            ghost_speeds[0] = 4
        if inky_dead:
            ghost_speeds[1] = 4
        if pinky_dead:
            ghost_speeds[2] = 4
        if clyde_dead:
            ghost_speeds[3] = 4
            
        if moving:
            player_x, player_y = move_player(player_x, player_y)
            clyde_x, clyde_y, clyde_direction = clyde.move()
            
            if not pinky_dead and not pinky.in_box:
                pinky_x, pinky_y, pinky_direction = pinky.move()
            else:
                pinky_x, pinky_y, pinky_direction = pinky.move()
            
            if not inky_dead and not inky.in_box:
                inky_x, inky_y, inky_direction = inky.move()
            else:
                inky_x, inky_y, inky_direction = inky.move()
            
            if not blinky_dead and not blinky.in_box:
                blinky_x, blinky_y, blinky_direction = blinky.move()
            else:
                blinky_x, blinky_y, blinky_direction = blinky.move()
        
        if not powerup:
            if (player_circle.colliderect(blinky.rect) and not blinky.dead) or \
                    (player_circle.colliderect(inky.rect) and not inky.dead) or \
                    (player_circle.colliderect(pinky.rect) and not pinky.dead) or \
                    (player_circle.colliderect(clyde.rect) and not clyde.dead):
                if lives > 0:
                    lives -= 1
                    startup_counter = 0
                    powerup = False
                    power_counter = 0
                    player_x = 450
                    player_y = 663
                    direction = 0
                    direction_command = 0
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
                    eaten_ghost = [False, False, False, False]
                    blinky_dead = False
                    inky_dead = False
                    clyde_dead = False
                    pinky_dead = False
                else:
                    game_over = True
                    moving = False
                    startup_counter = 0
        if powerup and player_circle.colliderect(blinky.rect) and eaten_ghost[0] and not blinky.dead:
            if lives > 0:
                powerup = False
                power_counter = 0
                lives -= 1
                startup_counter = 0
                player_x = 450
                player_y = 663
                direction = 0
                direction_command = 0
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
                eaten_ghost = [False, False, False, False]
                blinky_dead = False
                inky_dead = False
                clyde_dead = False
                pinky_dead = False
            else:
                game_over = True
                moving = False
                startup_counter = 0
        if powerup and player_circle.colliderect(inky.rect) and eaten_ghost[1] and not inky.dead:
            if lives > 0:
                powerup = False
                power_counter = 0
                lives -= 1
                startup_counter = 0
                player_x = 450
                player_y = 663
                direction = 0
                direction_command = 0
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
                eaten_ghost = [False, False, False, False]
                blinky_dead = False
                inky_dead = False
                clyde_dead = False
                pinky_dead = False
            else:
                game_over = True
                moving = False
                startup_counter = 0
        if powerup and player_circle.colliderect(pinky.rect) and eaten_ghost[2] and not pinky.dead:
            if lives > 0:
                powerup = False
                power_counter = 0
                lives -= 1
                startup_counter = 0
                player_x = 450
                player_y = 663
                direction = 0
                direction_command = 0
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
                eaten_ghost = [False, False, False, False]
                blinky_dead = False
                inky_dead = False
                clyde_dead = False
                pinky_dead = False
            else:
                game_over = True
                moving = False
                startup_counter = 0
        if powerup and player_circle.colliderect(clyde.rect) and eaten_ghost[3] and not clyde.dead:
            if lives > 0:
                powerup = False
                power_counter = 0
                lives -= 1
                startup_counter = 0
                player_x = 450
                player_y = 663
                direction = 0
                direction_command = 0
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
                eaten_ghost = [False, False, False, False]
                blinky_dead = False
                inky_dead = False
                clyde_dead = False
                pinky_dead = False
            else:
                game_over = True
                moving = False
                startup_counter = 0
        if powerup and player_circle.colliderect(blinky.rect) and not blinky.dead and not eaten_ghost[0]:
            blinky_dead = True
            eaten_ghost[0] = True
            score += (2 ** eaten_ghost.count(True)) * 100
        if powerup and player_circle.colliderect(inky.rect) and not inky.dead and not eaten_ghost[1]:
            inky_dead = True
            eaten_ghost[1] = True
            score += (2 ** eaten_ghost.count(True)) * 100
        if powerup and player_circle.colliderect(pinky.rect) and not pinky.dead and not eaten_ghost[2]:
            pinky_dead = True
            eaten_ghost[2] = True
            score += (2 ** eaten_ghost.count(True)) * 100
        if powerup and player_circle.colliderect(clyde.rect) and not clyde.dead and not eaten_ghost[3]:
            clyde_dead = True
            eaten_ghost[3] = True
            score += (2 ** eaten_ghost.count(True)) * 100


        if player_x > 900:
            player_x = -47
        elif player_x < -50:
            player_x = 897

        if (game_over or game_won):
            
            quit, restart, home, player_score = game_end(score)
            if quit:
                program =False
            if restart:
                powerup = False
                power_counter = 0
                lives -= 1
                startup_counter = 0
                player_x = 450
                player_y = 663
                direction = 0
                direction_command = 0
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
                eaten_ghost = [False, False, False, False]
                blinky_dead = False
                inky_dead = False
                clyde_dead = False
                pinky_dead = False
                score = 0
                lives = 3
                level = level_1
                game_over = False
                game_won = False
            if home:
                game_running = False
                home_page_running = True
            player.amend_score(player_score)
        
        pygame.display.flip()

pygame.quit()

