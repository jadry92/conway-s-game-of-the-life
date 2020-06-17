'''
Game life of comwale
base on: https://www.youtube.com/watch?v=qPtKv9fSHZY

creted by : johan suarez largo

'''
import pygame
import numpy as np
import sys
import time

pygame.init()

# size of the window
width, height = 600, 600

# Screen creator
screen = pygame.display.set_mode((width, height))

# color
bg = (25, 25, 25)


nxC, nyC = 50, 50

dimCW = width / nxC
dimCH = height / nyC

# logic matrix
gameState = np.zeros((nxC,nyC))

# automat palo
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

# automat move
gameState[21, 21] = 1
gameState[21, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

gameState[20, 5] = 1
gameState[21, 4] = 1
gameState[20, 4] = 1
gameState[21, 5] = 1

# pause control
pauseGame = False
newGameState = np.copy(gameState)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pauseGame = not pauseGame

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]

    screen.fill(bg)
    
    for y in range(0, nxC):
        for x in range(0, nxC):
            if not pauseGame:
                n_neigh = 0
                # calculate state
                for i in range(0, 9):
                    x_i = (i % 3) - 1
                    y_i = ((i - x_i) // 3) - 1
                    if i != 4 :
                        n_neigh += gameState[(x + x_i) % nxC, (y + y_i) % nyC]
                #if ( x == 5 and y >= 3 and y <= 5 ) or ( y == 4 and x >= 4 and x <= 6 ):
                #    print(x,y,'=',n_neigh , gameState[x, y])
                    
                # Rule #1: if the cell is dead and there are 3 cells alife close, will be revivie
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1 
                # Rule #2: if the cell is alive and there are less than two or more tha three cells alive, will be died 
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0
                # draw grid
            poly = [
                (x * dimCW, y * dimCH),
                ((x+1) * dimCW, (y) * dimCH),
                ((x+1) * dimCW, (y+1) * dimCH),
                ((x) * dimCW, (y+1) * dimCH),
            ]
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # copy the matrix
    gameState = np.copy(newGameState)
    pygame.display.flip()
    time.sleep(0.1)