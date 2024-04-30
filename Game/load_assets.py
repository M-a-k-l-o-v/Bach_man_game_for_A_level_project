import pygame

player_images = []
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'/Users/marvellous/Desktop/code/Bachman tests/assets/player_images/{i}.png'), (45, 45)))
blinky_img = pygame.transform.scale(pygame.image.load(f'/Users/marvellous/Desktop/code/Bachman tests/assets/ghost_images/red.png'), (45, 45))
pinky_img = pygame.transform.scale(pygame.image.load(f'/Users/marvellous/Desktop/code/Bachman tests/assets/ghost_images/pink.png'), (45, 45))
inky_img = pygame.transform.scale(pygame.image.load(f'/Users/marvellous/Desktop/code/Bachman tests/assets/ghost_images/blue.png'), (45, 45))
clyde_img = pygame.transform.scale(pygame.image.load(f'/Users/marvellous/Desktop/code/Bachman tests/assets/ghost_images/orange.png'), (45, 45))
spooked_img = pygame.transform.scale(pygame.image.load(f'/Users/marvellous/Desktop/code/Bachman tests/assets/ghost_images/powerup.png'), (45, 45))
dead_img = pygame.transform.scale(pygame.image.load(f'/Users/marvellous/Desktop/code/Bachman tests/assets/ghost_images/dead.png'), (45, 45))
