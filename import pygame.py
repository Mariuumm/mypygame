import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock and FPS
clock = pygame.time.Clock()
FPS = 15

# Snake settings
SNAKE_SIZE = 20


def draw_snake(snake_body):
    """Draw the snake on the screen."""
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (*segment, SNAKE_SIZE, SNAKE_SIZE))


def display_score():
    """Display the current score and high score."""
    score_text = font.render(f"Score: {score}  High Score: {high_score}", True, BLUE)
    screen.blit(score_text, (10, 10))


def show_restart_screen():
    """Display the restart game prompt along with the high score."""
    screen.fill(BLACK)
    restart_text = font.render(
        f"Game Over! Press 'R' to Restart or 'Q' to Quit.", True, WHITE
    )
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)

    # Position the text in the center of the screen
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
    screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))
    pygame.display.flip()


def reset_game():
    """Reset the game state to initial values."""
    global snake_body, snake_direction, food_position, score
    snake_body = [[100, 50], [80, 50], [60, 50]]  # Reset snake position
    snake_direction = "RIGHT"
    food_position = [random.randrange(0, SCREEN_WIDTH // SNAKE_SIZE) * SNAKE_SIZE,
                     random.randrange(0, SCREEN_HEIGHT // SNAKE_SIZE) * SNAKE_SIZE]
    score = 0


# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Game loop variables
running = True
snake_body = [[100, 50], [80, 50], [60, 50]]  # Initial snake position
snake_direction = "RIGHT"
food_position = [random.randrange(0, SCREEN_WIDTH // SNAKE_SIZE) * SNAKE_SIZE,
                 random.randrange(0, SCREEN_HEIGHT // SNAKE_SIZE) * SNAKE_SIZE]
score = 0
high_score = 0  # Track the high score

# Font for displaying score
font = pygame.font.Font(None, 36)

# Main Game Loop
game_over = False

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP and snake_direction != "DOWN":
                    snake_direction = "UP"
                elif event.key == pygame.K_DOWN and snake_direction != "UP":
                    snake_direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    snake_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    snake_direction = "RIGHT"
            else:  # Game over state logic
                if event.key == pygame.K_r:  # Restart the game
                    reset_game()
                    game_over = False
                elif event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    exit()

    if not game_over:
        # Move the snake
        if snake_direction == "UP":
            new_head = [snake_body[0][0], snake_body[0][1] - SNAKE_SIZE]
        elif snake_direction == "DOWN":
            new_head = [snake_body[0][0], snake_body[0][1] + SNAKE_SIZE]
        elif snake_direction == "LEFT":
            new_head = [snake_body[0][0] - SNAKE_SIZE, snake_body[0][1]]
        elif snake_direction == "RIGHT":
            new_head = [snake_body[0][0] + SNAKE_SIZE, snake_body[0][1]]

        # Check collisions
        if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
                new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
                new_head in snake_body):
            # Game over
            game_over = True
        else:
            # Update snake body
            snake_body.insert(0, new_head)

            # Collision detection with food
            snake_head_rect = pygame.Rect(new_head[0], new_head[1], SNAKE_SIZE, SNAKE_SIZE)
            food_rect = pygame.Rect(food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE)

            if snake_head_rect.colliderect(food_rect):
                score += 10
                # Update high score if necessary
                if score > high_score:
                    high_score = score
                while True:
                    food_position = [random.randrange(0, SCREEN_WIDTH // SNAKE_SIZE) * SNAKE_SIZE,
                                     random.randrange(0, SCREEN_HEIGHT // SNAKE_SIZE) * SNAKE_SIZE]
                    if food_position not in snake_body:
                        break
            else:
                snake_body.pop()

    # Draw everything
    screen.fill(BLACK)
    draw_snake(snake_body)
    if not game_over:
        pygame.draw.rect(screen, RED, food_rect)  # Draw food
        display_score()
    else:
        show_restart_screen()

    pygame.display.flip()
    clock.tick(FPS)
