import pygame
import sys
import risorse
import gestione_player

pygame.init()
pygame.font.init()


larghezza = 1366
altezza = 768
button_state = 1
button_state2 = 1
btnframe = [risorse.btn1,risorse.btn2,risorse.btn3,risorse.btn4,risorse.btn5]
mode = "menu"
menu_aperto = False 

schermo = pygame.display.set_mode((larghezza, altezza), pygame.FULLSCREEN)


rect = risorse.btn1.get_rect()
rect.topleft = (800, 200)
rect2 = risorse.btn1.get_rect()
rect2.topleft = (800, 500)

def draw():
    if mode == "menu":
        schermo.blit(risorse.menu, (0,0)) 
        schermo.blit(btnframe[button_state], (800,200))
        schermo.blit(btnframe[button_state2], (800,500))
        play = risorse.font.render("PLAY", True, (255, 255, 255))
        quit = risorse.font.render("QUIT", True, (255, 255, 255))
        schermo.blit(play, (1000, 220))
        schermo.blit(quit, (1000, 520))
        pygame.display.flip()
    if mode == "level":
        schermo.blit(risorse.levelBackground, (0,0))
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            schermo.blit(risorse.playerS, (gestione_player.player["x"],gestione_player.player["y"]))
        elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            schermo.blit(risorse.player, (gestione_player.player["x"],gestione_player.player["y"])) 
        else:
            schermo.blit(risorse.player, (gestione_player.player["x"],gestione_player.player["y"]))
    if mode == "LevelMenu":
        schermo.blit(risorse.levelBackground, (0,0))
        schermo.blit(risorse.player, (gestione_player.player["x"],gestione_player.player["y"])) 
        schermo.blit(risorse.levelMenu, (400,192))

        



while True:
    draw()
    keys = pygame.key.get_pressed()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if rect.collidepoint(pygame.mouse.get_pos()):
            if button_state != 4:
                button_state += 1
        else:
            if button_state != 0:
                button_state -= 1
        if rect2.collidepoint(pygame.mouse.get_pos()):
            if button_state2 != 4:
                button_state2 += 1
        else:
            if button_state2 != 0:
                button_state2 -= 1
        if mode == "menu":
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and rect2.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and rect.collidepoint(pygame.mouse.get_pos()):
                mode = "level"
    if keys[pygame.K_ESCAPE]:
        if not esc_premuto:
            esc_premuto = True  
            menu_aperto = not menu_aperto
    else:
        esc_premuto = False  
    if menu_aperto:
        mode = "LevelMenu"
        pass
    else: 
        mode = "level"    
    if mode == "level":
        gestione_player.movimento()       

    pygame.display.update()
