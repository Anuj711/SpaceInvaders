import pygame,os,sys,random,math
from main import mainGame
from pygame import mixer

## Vital that we add this for every game we make
pygame.init()

#Create main menu
screen = pygame.display.set_mode((800, 600))
# Background music
mixer.music.load("Ashura-Indra.mp3")
#This plays the music on loop
mixer.music.play(-1)
bgStart = pygame.image.load("StartScreen.png")
pygame.display.set_caption("Space Gladiators")
icon = pygame.image.load("Game Icon.png")
pygame.display.set_icon(icon)
runningMenu = True
while runningMenu:
    screen.blit(bgStart, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningMenu = False
        # Check if a keystroke is being pressed at all
        if event.type == pygame.KEYDOWN:
            # Checks to see if the keystroke is right or left2
            if event.key == pygame.K_1:
                mainGame(1)
            elif event.key == pygame.K_2:
                mainGame(2)
            elif event.key == pygame.K_3:
                mainGame(3)
    pygame.display.update()

