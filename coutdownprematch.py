import pygame

def countdown(screen, font, countdown_duration, WIDTH, HEIGHT):
    for i in range(countdown_duration, 0, -1):
        screen.fill((0, 0, 0))

        # Disegna il countdown
        countdown_text = font.render(str(i), True, (255, 255, 255))
        countdown_rect = countdown_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(countdown_text, countdown_rect)

        pygame.display.flip()
        pygame.time.delay(1000) 

