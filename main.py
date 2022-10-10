#Import pygame
import pygame
pygame.init()
#Colors
white = (255, 255, 255) 
color_player = (41,	134,204)
color_ball = (241,194,50)
color_line = (0, 0, 0)
#window size
screen_width = 800
screen_height = 600
#size players
players_width = 20
players_height = 90
#Coordinates player 1 
player_1_x = 50 
player_1_y = 300 - (players_height/2)
#coordinates player 2
player_2_x = 750 - players_width
player_2_y = player_1_y
#coordinates ball
ball_x = 400
ball_y = 300
ball_radius = 20
#size variable
size =(screen_width, screen_height)
#Display window
screen = pygame.display.set_mode(size)
#TITLE
pygame.display.set_caption('Pong game')
#icon
icon = pygame.image.load('PIN PONG.png')
pygame.display.set_icon(icon)
#game loop
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #fill the screen with color
    screen.fill(white)
    #Drawing area 
    #Define player 1 left : a rectangle
    player_1 = pygame.draw.rect(screen, color_player, (player_1_x, player_1_y, players_width, players_height))
    player_2 = pygame.draw.rect(screen, color_player, (player_2_x, player_2_y, players_width, players_height))
    #Draw the ball
    pygame.draw.circle(screen, color_ball,(ball_x,ball_y),ball_radius)
    #Draw the center line
    pygame.draw.aaline(screen, color_line, (screen_width/2, 0), (screen_width/2, screen_height))
    # Refresh the windows
    pygame.display.flip()
    