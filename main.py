import pygame
import random
import time

WIDTH, HEIGHT = 900, 500
BLACK = (0, 0, 0)
RED = (153, 0, 0)
ORIGIN = (0, 102, 0)
DEST = (153, 51, 153)
NEIGH = (153, 102, 255)
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graph Visualization")
BLOCK_SIZE = 20
GRAPH_WIDTH = WIDTH//BLOCK_SIZE
GRAPH_HEIGHT = HEIGHT//BLOCK_SIZE
#adjency list
GRAPH = [[] for x in range( GRAPH_WIDTH * GRAPH_HEIGHT)]
GRAPH_NODES = []

def draw_window():
    WIN.fill(BLACK)
    pygame.display.update()

def make_graph():
    for x, i in enumerate(GRAPH):
        for neighbor in find_neighbours(i):
            if neighbor != -1:
                x.append(neighbor)

# returns up, down, left, right
def find_neighbours(i):
    row = i // GRAPH_WIDTH
    row_begin = GRAPH_WIDTH * row
    row_end = GRAPH_WIDTH * row + GRAPH_WIDTH - 1
    # node in the down direction
    if i+GRAPH_WIDTH < GRAPH_WIDTH*GRAPH_HEIGHT:
        down = i+GRAPH_WIDTH
    else:
        down = -1
    # node in the up direction
    if i - GRAPH_WIDTH >= 0:
        up = i-GRAPH_WIDTH
    else:
        up = -1
    # node in the right direction
    if i + 1 <= row_end:
        right = i+1
    else:
        right = -1
    # note in the left direction
    if i-1 >= row_begin:
        left = i - 1
    else:
        left = -1
    
    return (up, down, left, right)

def bfs(origin, dest):
    visited_nodes = set()

    queue = [x for x in find_neighbours(origin) if x != -1]
    visited_nodes.add(origin)
    while True:
        #fetch a node
        node = queue.pop(0)
        if node in visited_nodes:
            continue
        if node == dest:
            print("Destination Reached")
            break
        visited_nodes.add(node)
        # get the neighboring nodes
        neighbour_of_node = find_neighbours(node)
        # check validity of the nodes and append it to the queue
        for n in neighbour_of_node:
            if n in visited_nodes or n == -1:
                continue
            else:
                queue.append(n)
        WIN.fill(NEIGH, GRAPH_NODES[node])
        pygame.display.update()

Q = False
def dfs(origin, dest, visited):
    global Q
    if origin == dest:
        print("Destination Found")
        Q = True
    neighbors = [x for x in find_neighbours(origin) if x != -1 and x not in visited]
    while len(neighbors) > 0:
        if Q:
            break
        # pick a random neighbor
        n = neighbors.pop(random.randint(0, len(neighbors)-1))
        if n != dest:
            WIN.fill(NEIGH, GRAPH_NODES[n])
            visited.add(n)
        dfs(n, dest, visited)

def draw_grid(origin, dest):
    count = 0
    for y in range(0, HEIGHT, BLOCK_SIZE):
        for x in range(0, WIDTH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            GRAPH_NODES.append(rect)
            if count == origin:
                WIN.fill(ORIGIN, rect)
            elif count == dest:
                WIN.fill(DEST, rect)
            else:
                pygame.draw.rect(WIN, RED, rect, 1)
            count += 1

def rand_start_end():
    origin = random.randint(0, GRAPH_HEIGHT*GRAPH_WIDTH - 1)

    dest = random.randint(0, GRAPH_HEIGHT*GRAPH_WIDTH - 1)

    return origin, dest

def main():
    run = True
    clock = pygame.time.Clock()
    origin, dest = rand_start_end()
    draw_grid(origin, dest)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_r]:
            WIN.fill(BLACK)
            origin, dest  = rand_start_end()
            draw_grid(origin, dest)
        if keys_pressed[pygame.K_b]:
            bfs(origin, dest)
        if keys_pressed[pygame.K_d]:
            global Q
            Q = False
            print("Depth First Search in progress")
            dfs(origin, dest, set([origin]))
        if keys_pressed[pygame.K_q]:
            break
        
        
        #make changes to the window and then update
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()