import pygame

# Funzione per disegnare il menu iniziale
def draw_menu(screen, WIDTH, HEIGHT):
    screen.fill((0, 0, 0))

    font = pygame.font.Font(None, 36)
    play_text = font.render("Gioca", True, (255, 255, 255))
    exit_text = font.render("Esci", True, (255, 255, 255))
    
    made_by_text = font.render("Made by Poppity", True, (255, 255, 255))

    play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    exit_rect = exit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    
    made_by_rect = made_by_text.get_rect(bottomleft=(10, HEIGHT - 10))

    screen.blit(play_text, play_rect)
    screen.blit(exit_text, exit_rect)
    screen.blit(made_by_text, made_by_rect)

    pygame.display.flip()

    return play_rect, exit_rect

def play_sound(sound_file):
    pygame.mixer.Sound(sound_file).play()