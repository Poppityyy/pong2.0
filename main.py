import pygame
import sys
from mainmenu import draw_menu
from ponggame import game_loop
from coutdownprematch import countdown

# Inizializzazione di Pygame
pygame.init()

# Definizione di costanti
WIDTH, HEIGHT = 800, 600
FPS = 60

# Creazione della finestra di gioco
screen = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load("assets\desktopicon\pong.jfif")
pygame.display.set_caption("Pong II")
pygame.display.set_icon(icon)

# Inizializzazione delle variabili di gioco
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [5, 5]
right_paddle_pos = [WIDTH - 25, HEIGHT // 2 - 50]
left_paddle_pos = [25, HEIGHT // 2 - 50]
paddle_speed = 10

# Chiamata della funzione principale
play_rect, exit_rect = draw_menu(screen, WIDTH, HEIGHT)

# Loop principale
menu_active = True
while menu_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_rect.collidepoint(mouse_pos):
                menu_active = False
            elif exit_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()


screen.fill((0, 0, 0))
pygame.display.flip()

countdown_duration = 3
countdown_font = pygame.font.Font(None, 72)
countdown(screen, countdown_font, countdown_duration, WIDTH, HEIGHT)

# Chiamata della funzione per il loop principale del gioco
game_loop(screen, WIDTH, HEIGHT, ball_pos, ball_speed, left_paddle_pos, right_paddle_pos, paddle_speed, FPS)
