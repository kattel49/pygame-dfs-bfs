import pygame

WIDTH, HEIGHT = 900, 500
BLACK = (0, 0, 0)
WHITE = (153, 0, 0)
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graph Visualization")



def draw_window():
    WIN.fill(BLACK)
    pygame.display.update()

def draw_grid():
    block_size = 20
    for x in range(0, WIDTH, block_size):
        for y in range(0, HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(WIN, WHITE, rect, 1)

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_grid()
        #make changes to the window and then update
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()