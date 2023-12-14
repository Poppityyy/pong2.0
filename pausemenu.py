import pygame
import sys
from mainmenu import draw_menu

# Inizializzazione di Pygame
pygame.init()
pygame.mixer.init()  # Inizializzazione del mixer audio

def play_sound(sound_file):
    pygame.mixer.Sound(sound_file).play()

def pause_menu(screen, WIDTH, HEIGHT):
    font = pygame.font.Font(None, 36)

    resume_text = font.render("Riprendi", True, (255, 255, 255))
    main_menu_text = font.render("Torna al Menù", True, (255, 255, 255))
    exit_text = font.render("Esci", True, (255, 255, 255))

    resume_rect = resume_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    main_menu_rect = main_menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    exit_rect = exit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    while True:
        screen.fill((0, 0, 0))

        pause_text = font.render("Pause", True, (255, 255, 255))
        pause_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))

        screen.blit(pause_text, pause_rect)
        screen.blit(resume_text, resume_rect)
        screen.blit(exit_text, exit_rect)
        screen.blit(main_menu_text, main_menu_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Riprendi il gioco

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Verifica se è stato premuto il pulsante sinistro del mouse
                    if exit_rect.collidepoint(event.pos):
                        play_sound("sounds\menuonmouse.wav")
                        pygame.quit()
                        sys.exit()
                    elif resume_rect.collidepoint(event.pos):
                        play_sound("sounds\menuonmouse.wav")
                        return  # Riprendi il gioco
                    elif main_menu_rect.collidepoint(event.pos):
                        play_sound("sounds\menuonmouse.wav")
                        draw_menu(screen, WIDTH, HEIGHT)
                        pygame.display.flip()
                        pygame.time.wait(500)  # Attendi 500 millisecondi
                        return  # Torna al Menù Principale
