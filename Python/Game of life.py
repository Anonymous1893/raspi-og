import pygame, sys
from pygame.locals import *
pygame.init()
#-------------------------------------------------------------------------------
# Settings
COLS = int(input("How many columns: "))
ROWS = int(input("How many rows: "))
SIZE = int(input("How wide are the cells: "))
SPACE = int(input("How much spacing between each cell: "))
WIDTH = (SIZE+SPACE)*COLS - SPACE
HEIGHT = (SIZE+SPACE)*ROWS - SPACE + 50
FPS = 60
#-------------------------------------------------------------------------------
# Screen Setup
WINDOW = pygame.display.set_mode([WIDTH,HEIGHT])
CAPTION = pygame.display.set_caption('Test')
SCREEN = pygame.display.get_surface()
TRANSPARENT = pygame.Surface([WIDTH,HEIGHT])
TRANSPARENT.set_alpha(255)
TRANSPARENT.fill((255,255,255))
#-------------------------------------------------------------------------------
# Grid Setup
grid = []
cells = {}

for row in range(ROWS):
    grid.append([])
    for col in range(COLS):
        if row < 155 and col < 155:
            grid[row].append(pygame.draw.rect(SCREEN, (255, 255, 255), (col*(SIZE + SPACE), row*(SIZE + SPACE), SIZE, SIZE)))
            cells[(col*(SIZE + SPACE), row*(SIZE + SPACE))] = [0, 0]
            ###                                             (state, live neighbours)
            
pauseButton = pygame.draw.rect(SCREEN, (255,255,255), (10, HEIGHT - 40, WIDTH - 20, 30))  

pygame.display.flip()

...

#-------------------------------------------------------------------------------
# Main Loop
##while True: 
##    pos = pygame.mouse.get_pos()
##    mouse = pygame.draw.circle(TRANSPARENT, (0, 0, 0), pos , 0)
##    # Event Detection---------------
##    for event in pygame.event.get(): 
##        if event.type == QUIT: 
##            sys.exit() 
##        elif event.type == MOUSEBUTTONDOWN:
##            for row in grid:
##                for cell in row:
##                    if cell.contains(mouse):
##                        coord = cell.topleft
##                        cell = pygame.draw.rect(SCREEN, (155, 155, 155), (coord[0], coord[1], SIZE, SIZE))
##                        pygame.display.flip()

### Functions
def neighbours(y, x):
    output = 0
    for row in range(-1, 2):
        for col in range(-1, 2):
            if col + y < ROWS and col + y > -1:
                if row + x < COLS and row + x > -1:
                    if col != 0 or row != 0:
                        coord = grid[col + y][row + x].topleft
                        if cells[coord][0]:
                            output += 1
    return output

import math
MILI = int(math.floor(pygame.time.get_ticks() / 500.0) * 500.0)

pause = False

while True:
    if not pause:

###     Coloring the Squares
        
        for row in grid:
            for cell in row:
                coord = cell.topleft
                if cells[coord][0] == 1:
                    pygame.draw.rect(SCREEN, (155,155,155), (coord[0] , coord[1], SIZE, SIZE))
                else:
                    pygame.draw.rect(SCREEN, (255,255,255), (coord[0] , coord[1], SIZE, SIZE))

###     Logic
                    
        for y in range(0, ROWS):
            for x in range(0, COLS):
                col, row = grid[y][x].topleft
                cells[col, row][1] = neighbours(y, x)

        for y in range(0, ROWS):
            for x in range(0, COLS):
                coord = grid[y][x].topleft
                if cells[coord][0] == 1 and cells[coord][1] == 2:
                    cells[coord][1] = 1
                elif cells[coord][1] == 3:
                    cells[coord][0] = 1
                else:
                    cells[coord][0] = 0

###     Pausing
                
        pos = pygame.mouse.get_pos()
        mouse = pygame.draw.circle(TRANSPARENT, (0, 0, 0), pos , 0)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if pauseButton.contains(mouse):
                    pause = True
                            
        pygame.time.wait(0)
        print("next frame")
    if pause:

###     Interacting with grid
        
        pos = pygame.mouse.get_pos()
        mouse = pygame.draw.circle(TRANSPARENT, (0, 0, 0), pos , 0)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if pauseButton.contains(mouse):
                    pause = False
                else:
                    for y in range(len(grid)):
                        for x in range(len(grid[y])):
                            cell = grid[y][x]
                            if cell.contains(mouse):
                                coord = cell.topleft
                                if not cells[coord][0]:
                                    cells[coord][0] = 1
                                    grid[y][x] = pygame.draw.rect(SCREEN, (155, 155, 155), (coord[0] , coord[1], SIZE, SIZE))
                                else:
                                    cells[coord][0] = 0
                                    grid[y][x] = pygame.draw.rect(SCREEN, (255, 255, 255), (coord[0] , coord[1], SIZE, SIZE))
                                    
    pygame.display.flip()   
