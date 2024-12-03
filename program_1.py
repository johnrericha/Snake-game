import pygame
import sys
import time
pygame.init()
import pygame as pg
red1 = (254, 0, 0, 0.8)



# pygame.init() will initialize all 
# imported module 
pygame.init() 

clock = pygame.time.Clock() 

# it will display on screen 
screen = pygame.display.set_mode([600, 500]) 
font = pygame.font.SysFont('Arial', 30)
screen.fill((0, 0, 0))
text_surface = font.render('Welcome in my game and do you want to play or not', True, red1)
screen.blit(text_surface, (100, 100))
pygame.display.flip()  # Update the display
time.sleep(3)
# basic font for user typed 
base_font = pygame.font.Font(None, 32) 
user_text = '' 

# create rectangle 
input_rect = pygame.Rect(200, 200, 140, 32) 

# color_active stores color(lightskyblue3) which 
# gets active when input box is clicked by user 
color_active = pygame.Color('lightskyblue3') 

# color_passive store color(chartreuse4) which is 
# color of input box. 
color_passive = pygame.Color('chartreuse4') 
color = color_passive 

active = False

while True:
    for event in pygame.event.get(): 

        # if user types QUIT then the screen will close 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if input_rect.collidepoint(event.pos): 
                    active = True
                else: 
                    active = False

            if event.type == pygame.KEYDOWN: 

                # Check for backspace 
                if event.key == pygame.K_BACKSPACE: 

                    # get text input from 0 to -1 i.e. end. 
                    user_text = user_text[:-1] 

                # Unicode standard is used for string 
                # formation 
                else: 
                    user_text += event.unicode
        
        # it will set background color of screen 
    screen.fill((255, 255, 255)) 

    if active: 
            color = color_active 
    else: 
            color = color_passive 
            
        # draw rectangle and argument passed which should 
        # be on screen 
    pygame.draw.rect(screen, color, input_rect) 

    text_surface = base_font.render(user_text, True, (255, 255, 255)) 
        
        # render at position stated in arguments 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
        
        # set width of textfield so that text cannot get 
        # outside of user's text input 
    input_rect.w = max(100, text_surface.get_width()+10) 
        
        # display.flip() will update only a portion of the 
        # screen to updated, not full area 
    pygame.display.flip() 
        
        # clock.tick(60) means that for every second at most 
        # 60 frames should be passed. 
    clock.tick(60) 

    
    if user_text == 'not':
        sys.exit()  
    elif user_text == 'play':
        text_surface = base_font.render(user_text, True, (255, 255, 255)) 
        
        red = (254, 0, 0, 0.8)
                
                # write text
                # move turtle
                # Constants
        WIDTH, HEIGHT = 800, 600
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
        BALL_SIZE = 10
        PADDLE_SPEED = 7
        BALL_SPEED_X, BALL_SPEED_Y = 5, 5
        max_scores = 10
        # Set up the screen
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong Game")

        # Create paddles and ball
        left_paddle = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        ball = pygame.Rect((WIDTH - BALL_SIZE) // 2, (HEIGHT - BALL_SIZE) // 2, BALL_SIZE, BALL_SIZE)

        # Scores
        left_score = 0
        right_score = 0
        font = pygame.font.Font(None, 74)  # Font for displaying scores
        game_over = False  # Flag to check if the game is over
        # Game loop
        pygame.display.flip()
        while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    # Key controls
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_w] and left_paddle.top > 0:
                        left_paddle.y -= PADDLE_SPEED
                    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
                        left_paddle.y += PADDLE_SPEED
                    if keys[pygame.K_UP] and right_paddle.top > 0:
                        right_paddle.y -= PADDLE_SPEED
                    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
                        right_paddle.y += PADDLE_SPEED

                    # Move the ball
                    ball.x += BALL_SPEED_X
                    ball.y += BALL_SPEED_Y

                    # Ball collision with top and bottom
                    if ball.top <= 0 or ball.bottom >= HEIGHT:
                        BALL_SPEED_Y = -BALL_SPEED_Y

                    # Ball collision with paddles
                    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
                        BALL_SPEED_X = -BALL_SPEED_X

                    # Ball reset if it goes out of bounds
                    if ball.left <= 0:  # Right player scores
                        right_score += 1
                        ball.x = (WIDTH - BALL_SIZE) // 2
                        ball.y = (HEIGHT - BALL_SIZE) // 2
                        BALL_SPEED_X = -BALL_SPEED_X  # Change direction

                    if ball.right >= WIDTH:  # Left player scores
                        left_score += 1
                        ball.x = (WIDTH - BALL_SIZE) // 2
                        ball.y = (HEIGHT - BALL_SIZE) // 2
                        BALL_SPEED_X = -BALL_SPEED_X  # Change direction
                    if left_score >= max_scores:
                            game_over = True
                            winner_text = "Left Player Wins!"
                            
                    elif right_score >= max_scores:
                            game_over = True
                            winner_text = "Right Player Wins!"
                            


                    # Drawing

                    screen.fill(BLACK)
                    pygame.draw.rect(screen, WHITE, left_paddle)
                    pygame.draw.rect(screen, WHITE, right_paddle)
                    pygame.draw.ellipse(screen, WHITE, ball)


                    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))  # Middle line

                        # Display scores
                    left_text = font.render(str(left_score), True, WHITE)
                    right_text = font.render(str(right_score), True, WHITE)
                    screen.blit(left_text, (WIDTH // 4, 20))  # Left score position
                    screen.blit(right_text, (WIDTH * 3 // 4, 20))  # Right score position
                    if left_score == max_scores:
                            font = pygame.font.SysFont('Arial', 30)
                            screen.fill((0, 0, 0))
                            text_surface = font.render('player 1 is winner because acquired 10 points', True, red)
                            screen.blit(text_surface, (100, 100))
                            pygame.display.flip()  # Update the display
                            time.sleep(3)
                            sys.exit()
                    elif right_score == max_scores:
                            font = pygame.font.SysFont('Arial', 30)
                            screen.fill((0, 0, 0))
                            text_surface = font.render('player 2 is winner because acquired 10 points', True, red)
                            screen.blit(text_surface, (100, 100))
                            pygame.display.flip()  # Update the display
                            time.sleep(3)
                            sys.exit()
                    pygame.display.flip()  # Update the display
                    pygame.time.Clock().tick()  # Frame rate


