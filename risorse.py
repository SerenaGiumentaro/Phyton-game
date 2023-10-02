import pygame

pygame.font.init()

#immaggini
menu = pygame.image.load("menu.png")
levelMenu = pygame.image.load("levelMenu.png")
levelBackground = pygame.image.load("levelBackground.png")
player = pygame.image.load("player.png")
playerS = pygame.transform.flip(player, True, False)
btn1 = pygame.image.load("bottone\\1.png")
btn2 = pygame.image.load("bottone\\2.png")
btn3 = pygame.image.load("bottone\\3.png")
btn4 = pygame.image.load("bottone\\4.png")
btn5 = pygame.image.load("bottone\\5.png")

#font
font = pygame.font.Font("qualcosa.ttf", 70)
