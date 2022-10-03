#Import pygame
import pygame
pygame.init()
#window size
screen_width = 800
screen_height = 600
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
