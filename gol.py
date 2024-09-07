import pygame

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
BLACK = (  0,   0,  0)
(width, height) = (800, 800)

running = True

#Class for each cell
class Cell:
    def __init__(self, xpos, ypos, state):
        self.xpos = xpos
        self.ypos = ypos
        self.state = state

    

#Class for the grid
class Grid:
    def __init__(self, gridWidth, gridHeight):
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight

        self.grid = []
        
        for i in range(gridWidth):
            for j in range(gridHeight):
                self.grid.append(Cell(i, j, 0))



#Function to draw the grid
def drawGrid(Grid):
    cellsize = width / Grid.gridWidth
    for i in range(Grid.gridHeight):
        for j in range(Grid.gridWidth):
            if Grid.grid[i*Grid.gridWidth + j].state == 1:
                pygame.draw.rect(screen, WHITE, [j*cellsize, i*cellsize, cellsize, cellsize])



#Function to count the number of neighbors
def countNeighbors(grid, cell):
    count = 0
    if cell.state == 1:
        count += 1
    
    return count



#Function to reproduce
#def reproduce(grid, cells):
    #for cell in cells:
       # if cell.state == 1:
            #if 
    

        
        




def main():
    global running, screen
    
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game of Life")
    screen.fill(BLACK)

    realgrid = Grid(40, 40)


    realgrid.grid[44].state = 1
    #print(realgrid.grid[4].state)

    drawGrid(realgrid)

    print(countNeighbors(realgrid, realgrid.grid[44]))

    pygame.display.update()

    

    
    while running:
        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
                pygame.display.update()

            if event.type == pygame.QUIT:
                running = False



def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)



if __name__ == '__main__':
    main()