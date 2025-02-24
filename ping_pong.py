import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_SPEED = 10

# Ball dimensions
BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Initial positions
player1_pos = [50, height // 2 - PADDLE_HEIGHT // 2]  # Left paddle
player2_pos = [width - 50 - PADDLE_WIDTH, height // 2 - PADDLE_HEIGHT // 2]  # Right paddle
ball_pos = [width // 2 - BALL_SIZE // 2, height // 2 - BALL_SIZE // 2]  # Ball at center
ball_velocity = [BALL_SPEED_X, BALL_SPEED_Y]  # Initial ball velocity

def handle_input():
    keys = pygame.key.get_pressed()
    
    # Player 1 (left paddle) movement
    if keys[pygame.K_w] and player1_pos[1] > 0:
        player1_pos[1] -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_pos[1] < height - PADDLE_HEIGHT:
        player1_pos[1] += PADDLE_SPEED
    
    # Player 2 (right paddle) movement
    if keys[pygame.K_UP] and player2_pos[1] > 0:
        player2_pos[1] -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_pos[1] < height - PADDLE_HEIGHT:
        player2_pos[1] += PADDLE_SPEED

def update_ball():
    global ball_velocity

    # Update ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Collision with top and bottom
    if ball_pos[1] <= 0 or ball_pos[1] >= height - BALL_SIZE:
        ball_velocity[1] = -ball_velocity[1]

    # Collision with paddles
    if (ball_pos[0] <= player1_pos[0] + PADDLE_WIDTH and
        player1_pos[1] <= ball_pos[1] <= player1_pos[1] + PADDLE_HEIGHT):
        ball_velocity[0] = -ball_velocity[0]
    elif (ball_pos[0] >= player2_pos[0] - BALL_SIZE and
          player2_pos[1] <= ball_pos[1] <= player2_pos[1] + PADDLE_HEIGHT):
        ball_velocity[0] = -ball_velocity[0]

    # Ball out of bounds (reset)
    if ball_pos[0] < 0 or ball_pos[0] > width:
        ball_pos[0] = width // 2 - BALL_SIZE // 2
        ball_pos[1] = height // 2 - BALL_SIZE // 2
        ball_velocity[0] = -ball_velocity[0]  # Change direction

def draw():
    screen.fill(BLACK)
    
    # Draw paddles
    pygame.draw.rect(screen, WHITE, (player1_pos[0], player1_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_pos[0], player2_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    
    # Draw ball
    pygame.draw.rect(screen, WHITE, (ball_pos[0], ball_pos[1], BALL_SIZE, BALL_SIZE))
    
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update game state
        handle_input()
        update_ball()
        
        # Draw elements
        draw()
        
        # Limit frame rate to 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main()