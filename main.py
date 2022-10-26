#Import
from locale import strcoll
from turtle import speed
import pygame
import random as rd
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
player_1_y_speed = 0
#coordinates player 2
player_2_x = 750 - players_width
player_2_y = player_1_y
player_2_y_speed = 0
#coordinates ball
ball_x = 400
ball_y = 300
ball_radius = 20
ball_speed_x = 1.5
ball_speed_y = 1.5
#size variable
size =(screen_width, screen_height)
#Display window
screen = pygame.display.set_mode(size)
#TITLE
pygame.display.set_caption('Pong game')
#icon
icon = pygame.image.load('PIN PONG.png')
pygame.display.set_icon(icon)
#Score var
player_1_score = 0
player_2_score = 0
#Score font 
score_font = pygame.font.Font('MagicalStory.ttf', 35) 
#Score position in thr screen player 1 
player_1_score_x = 15
player_1_score_y = 10
#Score position in thr screen player 2 
player_2_score_x = 650
player_2_score_y = 10
#player 1 score function
def show_1_score(x, y):
    score1 = score_font.render('Player 1:' + str(player_1_score), True, (0,0,0))
    screen.blit(score1, (x,y))
#player 2 score function
def show_2_score(x, y):
    score2 = score_font.render('Player 2:' + str(player_2_score), True, (0,0,0))
    screen.blit(score2, (x,y))
#game loop
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #player key controls
        #checks for KEYDOWN event
        if event.type == pygame.KEYDOWN :
            #Player 1
            if event.key == pygame.K_w :
                player_1_y_speed = -1
            if event.key == pygame.K_s :
                player_1_y_speed = 1
            #Player 2
            if event.key == pygame.K_UP :
                player_2_y_speed = -1
            if event.key == pygame.K_DOWN :
                player_2_y_speed = 1
        if event.type == pygame.KEYUP : 
             #Player 1
            if event.key == pygame.K_w :
                player_1_y_speed = 0
            if event.key == pygame.K_s :
                player_1_y_speed = 0
            #Player 2
            if event.key == pygame.K_UP :
                player_2_y_speed = 0
            if event.key == pygame.K_DOWN :
                player_2_y_speed = 0
        
    #players movement
    player_1_y += player_1_y_speed
    player_2_y += player_2_y_speed
    #player boundaries
    #player 1
    if player_1_y <= 0:
        player_1_y = 0
    if player_1_y >= screen_height - players_height:
        player_1_y = screen_height - players_height
    #player 2
    if player_2_y <= 0:
        player_2_y = 0
    if player_2_y >= screen_height - players_height:
        player_2_y = screen_height - players_height
    #ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    #ball boundaries
    if ball_y >(screen_height - ball_radius) or ball_y < ball_radius:
        ball_speed_y *= -1
    #rigth or left and score update
    if ball_x > screen_width :
        player_1_score += 1 
        ball_x = screen_width/2
        ball_y = screen_width/2
        ball_speed_x *= rd.choice([-1, 1]) 
    elif ball_x < 0 :
        player_2_score += 1 
        ball_x = screen_width/2
        ball_y = screen_width/2
        ball_speed_x *= rd.choice([-1, 1]) 

    #fill the screen with color
    screen.fill(white)
    #Drawing area 
    #Define player 1 left : a rectangle
    player_1 = pygame.draw.rect(screen, color_player, (player_1_x, player_1_y, players_width, players_height))
    player_2 = pygame.draw.rect(screen, color_player, (player_2_x, player_2_y, players_width, players_height))
    #Draw the center line
    pygame.draw.aaline(screen, color_line, (screen_width/2, 0), (screen_width/2, screen_height))
    #Draw the ball
    ball = pygame.draw.circle(screen, color_ball,(ball_x,ball_y),ball_radius)
    #Colitions 
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1
    #call the score 1 function 
    show_1_score(player_1_score_x, player_1_score_y)
    #call the score 2 function 
    show_2_score(player_2_score_x, player_2_score_y)
    # Refresh the windows
    pygame.display.flip()
    