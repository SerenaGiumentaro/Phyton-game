import pygame

player = {"hp":5,"att":1,"level":1,"x":0,"y":383}

def movimento():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player["x"] > -50:
        player["x"] -= 5
    if keys[pygame.K_RIGHT] and player["x"] < 1360:
        player["x"] += 5
    if keys[pygame.K_UP] and player["y"] > -50:
        player["y"] -= 5
    if keys[pygame.K_DOWN] and player["y"] < 760:
        player["y"] += 5