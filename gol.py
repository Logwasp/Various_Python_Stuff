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



#Function to check if cell is a edge cell
def isEdgeCell(grid, cell):
    cellIndex = grid.grid.index(cell)
    if (cellIndex % grid.gridWidth == 0) or (cellIndex % grid.gridWidth == grid.gridWidth - 1):
        return True
    elif (cellIndex < grid.gridWidth) or (cellIndex > grid.gridWidth * grid.gridHeight - grid.gridWidth):
        return True
    else:
        return False



#Function to count the number of neighbors
def countNeighbors(grid, cell):
    if isEdgeCell(grid, cell):
        return 0
    
    cellIndex = grid.grid.index(cell)
    neighborCount = 0
    
    #Check right neighbor
    if grid.grid[cellIndex + 1].state == 1 :
        neighborCount += 1
    
    #Check left neighbor
    if grid.grid[cellIndex - 1].state == 1:
        neighborCount += 1

    #Check top neighbor
    if grid.grid[cellIndex - grid.gridWidth].state == 1:
        neighborCount += 1
    
    #Check bottom neighbor
    if grid.grid[cellIndex + grid.gridWidth].state == 1:
        neighborCount += 1
    
    #Check top right neighbor
    if grid.grid[cellIndex - grid.gridWidth + 1].state == 1:
        neighborCount += 1

    #Check top left neighbor
    if grid.grid[cellIndex - grid.gridWidth - 1].state == 1:
        neighborCount += 1
    
    #Check bottom right neighbor
    if grid.grid[cellIndex + grid.gridWidth + 1].state == 1:
        neighborCount += 1
    
    #Check bottom left neighbor
    if grid.grid[cellIndex + grid.gridWidth - 1].state == 1:
        neighborCount += 1
    
    return neighborCount



#Function to reproduce
#def reproduce(grid, cells):
    #for cell in cells:
       # if cell.state == 1:
            #if 
    

        
        




def main():
    global running, screen
    
    #Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game of Life")
    screen.fill(BLACK)

    #Create grid
    realgrid = Grid(40, 40)


    realgrid.grid[46].state = 1
    realgrid.grid[6].state = 1
    realgrid.grid[7].state = 1
    #print(realgrid.grid[4].state)

    drawGrid(realgrid)

    print(countNeighbors(realgrid, realgrid.grid[47]))

    pygame.display.update()

    

    
    while running:
        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                print(f'Mouse clicked at {x}, {y}')
                pygame.display.update()

            if event.type == pygame.QUIT:
                running = False



def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)



if __name__ == '__main__':
    main()