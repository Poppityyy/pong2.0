import pygame
import sys
from pausemenu import pause_menu

def game_loop(screen, WIDTH, HEIGHT, ball_pos, ball_speed, left_paddle_pos, right_paddle_pos, paddle_speed, FPS):
    clock = pygame.time.Clock()

    # Punteggi dei giocatori
    player1_score = 0
    player2_score = 0

    player1_score = 0
    player2_score = 0

    # Font per il testo
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu(screen, WIDTH, HEIGHT)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and right_paddle_pos[1] > 0:
            right_paddle_pos[1] -= paddle_speed
        if keys[pygame.K_DOWN] and right_paddle_pos[1] < HEIGHT - 100:
            right_paddle_pos[1] += paddle_speed

        if keys[pygame.K_w] and left_paddle_pos[1] > 0:
            left_paddle_pos[1] -= paddle_speed
        if keys[pygame.K_s] and left_paddle_pos[1] < HEIGHT - 100:
            left_paddle_pos[1] += paddle_speed

        # Aggiornamento della posizione della palla
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        # Creazione di un oggetto Rect per la palla
        ball_rect = pygame.Rect(ball_pos[0] - 15, ball_pos[1] - 15, 30, 30)

        # Rimbalzo della palla sulle pareti
        if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT:
            ball_speed[1] = -ball_speed[1]

        # Rimbalzo della palla sulle racchette
        if (
            ball_pos[0] <= 25
            and right_paddle_pos[1] <= ball_pos[1] <= right_paddle_pos[1] + 100
        ) or (
            ball_pos[0] >= WIDTH - 25
            and left_paddle_pos[1] <= ball_pos[1] <= left_paddle_pos[1] + 100
        ):
            ball_speed[0] = -ball_speed[0]

        # Gestione dei punti
        if ball_pos[0] <= 0:
            player2_score += 1
            ball_pos = [WIDTH // 2, HEIGHT // 2]
        elif ball_pos[0] >= WIDTH:
            player1_score += 1
            ball_pos = [WIDTH // 2, HEIGHT // 2]

        # Disegno degli elementi
        screen.fill((0, 0, 0))

        # Disegno delle racchette
        pygame.draw.rect(screen, (255, 255, 255), (10, right_paddle_pos[1], 15, 100))
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH - 25, left_paddle_pos[1], 15, 100))

        # Disegno della palla
        pygame.draw.circle(screen, (255, 255, 255), (int(ball_pos[0]), int(ball_pos[1])), 15)

        # Disegno dei punteggi
        player1_text = font.render(str(player1_score), True, (255, 255, 255))
        player2_text = font.render(str(player2_score), True, (255, 255, 255))

        screen.blit(player1_text, (WIDTH // 2 - 50, 10))
        screen.blit(player2_text, (WIDTH // 2 + 20, 10))

        # Draw a dashed line down the middle
        line_color = (255, 255, 255)
        dash_length = 10
        gap_length = 5
        center_line_y = 0
        while center_line_y < HEIGHT:
            pygame.draw.line(
                screen,
                line_color,
                (WIDTH // 2, center_line_y),
                (WIDTH // 2, center_line_y + dash_length),
                1
            )
            center_line_y += dash_length + gap_length


        # Aggiornamento della finestra di gioco
        pygame.display.flip()

        # Impostazione del frame rate
        clock.tick(FPS)