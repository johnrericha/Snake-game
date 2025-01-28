import pygame
import time
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Window size
window_x = 720
window_y = 480

# Snake speed
snake_speed = 15

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set up the game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Snake initial position
snake_position = [100, 50]

# Snake body (initially 4 blocks)
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# Fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# Default snake direction (right)
direction = 'RIGHT'
change_to = direction

# Initial score
score = 0

# Font for displaying score and messages
font = pygame.font.SysFont('Arial', 32)

# File path for storing leaderboard
leaderboard_file = "leaderboard.txt"

# Default leaderboard (in case the file doesn't exist)
default_leaderboard = [("Player1", 500), ("Player2", 400), ("Player3", 300)]

# Function to load leaderboard from file
def load_leaderboard():
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as file:
            scores = [line.strip().split(",") for line in file.readlines()]
            return [(name, int(score)) for name, score in scores]
    else:
        return default_leaderboard

# Function to save leaderboard to file
def save_leaderboard(leaderboard):
    with open(leaderboard_file, "w") as file:
        for name, score in leaderboard:
            file.write(f"{name},{score}\n")

# Function to display leaderboard
def display_leaderboard(leaderboard):
    game_window.fill(white)
    y_offset = 50
    for idx, (name, score) in enumerate(leaderboard):
        leaderboard_text = font.render(f"{idx + 1}. {name}: {score}", True, black)
        game_window.blit(leaderboard_text, (100, y_offset))
        y_offset += 40
    pygame.display.flip()

# Display score on the screen
def show_score():
    score_surface = font.render(f"Score : {score}", True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (window_x / 2, 10)
    game_window.blit(score_surface, score_rect)

# Function to capture player name
def enter_name():
    name = ""
    input_active = True
    while input_active:
        game_window.fill(black)
        name_text = font.render(f"Enter your name: {name}", True, white)
        game_window.blit(name_text, (window_x // 2 - name_text.get_width() // 2, window_y // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # When 'Enter' is pressed, return the name
                    return name if name != "" else "Player"
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]  # Remove last character
                else:
                    # Only allow alphanumeric characters and spaces
                    if len(name) < 20:  # Limit name length
                        if event.unicode.isalnum() or event.unicode.isspace():
                            name += event.unicode

# Game over function
def game_over():
    game_over_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = game_over_font.render(f'Your Score is : {score}', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)

    # Prompt player for name and save score
    player_name = enter_name()

    # Load leaderboard, add the score and sort
    leaderboard = load_leaderboard()
    leaderboard.append((player_name, score))  # Use the entered name
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    leaderboard = leaderboard[:5]  # Keep top 5 scores
    save_leaderboard(leaderboard)

    # Display leaderboard
    display_leaderboard(leaderboard)

    # Wait for the user to close the window
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Main Game Loop
while True:
    # Handle key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Ensure snake can't move in the opposite direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True

    # Fill background color
    game_window.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw fruit
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10 or snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Snake collision with itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Display score continuously
    show_score()

    # Update the display
    pygame.display.update()

    # Control game speed
    fps.tick(snake_speed)
