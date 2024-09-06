import pygame

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
BLACK = (  0,   0,  0)
(width, height) = (1200, 800)

running = True

def main():
    global running, screen
    
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TUFF")
    screen.fill(BLACK)

    
    drawPlayer2()
    pygame.display.update()
    
    while running:
        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
                drawPlayer1()
                pygame.display.update()

            if event.type == pygame.QUIT:
                running = False

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawPlayer1():
    pygame.draw.circle(screen, RED, [200, 400], 25)

def drawPlayer2():
    pygame.draw.circle(screen, BLUE, [1000, 400], 25)


if __name__ == '__main__':
    main()