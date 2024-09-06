import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
GRID_SIZE = 150
CELL_SIZE = 5
SCREEN_SIZE = GRID_SIZE * CELL_SIZE


WHITE = ((255,255,255))
BLUE = ((0,0,255))
GREEN = ((0,255,0))
RED = ((255,0,0))
BLACK = ((0,0,0))
ORANGE = ((255,100,10))
YELLOW = ((255,255,0))
BLUEGREEN = ((0,255,170))
MARROON = ((115,0,0))
LIME = ((180,255,100))
PINK = ((255,100,180))
PURPLE = ((240,0,255))
GRAY = ((127,127,127))
MAGENTA = ((255,0,230))
BROWN = ((100,40,0))
FORESTGREEN = ((0,50,0))
NAVYBLUE = ((0,0,100))
RUST = ((210,150,75))
LIGHTYELLOW = ((255,200,0))
HIGHLIGHTER = ((255,255,100))
SKYBLUE = ((0,255,255))
LIGHTGRAY = ((200,200,200))
DARKGRAY = ((50,50,50))
TAN = ((230,220,170))
COFFEE =((200,190,140))
MOON = ((235,245,255))

FPS = 10000

# Create screen
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Cell Simulation")

# Define Cell class
class Cell:
    def __init__(self, x, y, color, team):
        self.x = x
        self.y = y
        self.color = color
        self.team = team

    def move(self, grid):
        # Randomly move to a neighboring empty space
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[nx][ny] is None:
                grid[self.x][self.y] = None  # Leave current space empty
                self.x, self.y = nx, ny
                grid[self.x][self.y] = self
                break

    def reproduce(self, grid, cells):
        # Check for ally nearby and empty space between them
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                mid_x, mid_y = self.x + dx // 2, self.y + dy // 2
                if grid[nx][ny] and grid[nx][ny].team == self.team and grid[mid_x][mid_y] is None:
                    # Reproduce in the middle space
                    new_cell = Cell(mid_x, mid_y, self.color, self.team)
                    grid[mid_x][mid_y] = new_cell
                    cells.append(new_cell)
                    break

    def attack(self, grid, cells):
        # Check for enemy nearby and attack
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[nx][ny] and grid[nx][ny].team != self.team:
                if random.random() < 0.5:
                    # 50/50 chance to kill enemy cell
                    cells.remove(grid[nx][ny])
                    grid[nx][ny] = None
                break

# Create grid
grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
cells = []

# Function to initialize teams
def initialize_team(color, team, num_cells):
    for _ in range(num_cells):
        while True:
            x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
            if grid[x][y] is None:  # Only place if space is empty
                cell = Cell(x, y, color, team)
                grid[x][y] = cell
                cells.append(cell)
                break

# Initialize Red and Blue teams with variable starting numbers
initialize_team(GREEN, 'green', 50)
initialize_team(YELLOW, 'yellow', 50)
initialize_team(PURPLE, 'black', 50)
initialize_team(BLUE, 'gray', 50)
initialize_team(ORANGE, 'orange', 50)
initialize_team(MAGENTA, 'magenta', 50)
initialize_team(RED, 'red', 50)
# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Randomly choose actions for each cell
    for cell in cells:
        action = random.choice(['move', 'reproduce', 'attack'])
        if action == 'move':
            cell.move(grid)
        elif action == 'reproduce':
            cell.reproduce(grid, cells)
        elif action == 'attack':
            cell.attack(grid, cells)

    # Draw the grid and cells
    screen.fill(WHITE)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x][y]:
                pygame.draw.rect(screen, grid[x][y].color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()