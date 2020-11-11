from time import sleep
import pygame
import sys
from paddle import Paddle
from ball import Ball

if __name__ == '__main__':
    pygame.init()

    # Screen constants
    size = SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")

    # Player values
    player_A_score = 0
    player_B_score = 0
    VELOCITY_MULTIPLIER = 1.2

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Roboto Mono", SCREEN_HEIGHT // 10)

    # Paddles
    PADDLE_WIDTH, PADDLE_HEIGHT = 10, 150
    paddle_A = Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT, SCREEN_HEIGHT)
    paddle_B = Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT, SCREEN_HEIGHT)

    paddle_A.rect.x, paddle_A.rect.y = 20, (SCREEN_HEIGHT - PADDLE_HEIGHT) / 2
    paddle_B.rect.x, paddle_B.rect.y = SCREEN_WIDTH - 30, (SCREEN_HEIGHT - PADDLE_HEIGHT) / 2

    ball = Ball(WHITE, 20)
    ball.rect.x, ball.rect.y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    all_sprites_list = pygame.sprite.Group()

    all_sprites_list.add(paddle_A)
    all_sprites_list.add(paddle_B)
    all_sprites_list.add(ball)

    sleep(1)

    scored = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B)
        keys = pygame.key.get_pressed()
        paddle_speed = SCREEN_HEIGHT / 50
        if keys[pygame.K_w]:
            paddle_A.move_up(paddle_speed)
        if keys[pygame.K_s]:
            paddle_A.move_down(paddle_speed)
        if keys[pygame.K_UP]:
            paddle_B.move_up(paddle_speed)
        if keys[pygame.K_DOWN]:
            paddle_B.move_down(paddle_speed)

        scored = False
        # Ball boundary conditions
        if ball.rect.x >= SCREEN_WIDTH + 50:
            player_A_score += 1
            scored = True
        if ball.rect.x <= -ball.rect.width - 50:
            player_B_score += 1
            scored = True
        if ball.rect.y > SCREEN_HEIGHT - ball.rect.height:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = abs(ball.velocity[1])

        # Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddle_A) or pygame.sprite.collide_mask(ball, paddle_B):
            ball.bounce(VELOCITY_MULTIPLIER)

        all_sprites_list.update()

        # Drawing
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [SCREEN_WIDTH / 2, 0], [SCREEN_WIDTH / 2, SCREEN_HEIGHT], 5)  # Net
        all_sprites_list.draw(screen)

        score_A = font.render(str(player_A_score), True, WHITE)
        score_B = font.render(str(player_B_score), True, WHITE)

        screen.blit(score_A, (SCREEN_WIDTH // 4, 50))
        screen.blit(score_B, (3 * SCREEN_WIDTH // 4, 50))

        pygame.display.flip()
        clock.tick(90)
        if scored:
            sleep(1)
            ball.rect.x = SCREEN_WIDTH // 2
            ball.rect.y = SCREEN_HEIGHT // 2
            ball.new_velocity()
