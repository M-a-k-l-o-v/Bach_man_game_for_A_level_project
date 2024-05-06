import heapq
from collections import defaultdict
from collections import deque
import pygame
from Game.board import *
from Game.game import blinky


game_running  = True
powerup = False
screen = pygame.display.set_mode([WIDTH, HEIGHT])
eaten_ghost = False
spooked_img = pygame.transform.scale(pygame.image.load(f'/Users/marvellous/Desktop/code/Bachman tests/assets/ghost_images/powerup.png'), (45, 45))
dead_img = pygame.transform.scale(pygame.image.load(f'/Users/marvellous/Desktop/code/Bachman tests/assets/ghost_images/dead.png'), (45, 45))



class Ghost:
    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id):
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 22
        self.center_y = self.y_pos + 22
        self.target = target
        self.speed = speed
        self.img = img
        self.direction = direct
        self.dead = dead
        self.in_box = box
        self.id = id
        self.turns, self.in_box = self.check_collisions()
        self.rect = self.draw()

    def draw(self):
        if (not powerup and not self.dead) or (eaten_ghost[self.id] and powerup and not self.dead):
            screen.blit(self.img, (self.x_pos, self.y_pos))
        elif powerup and not self.dead and not eaten_ghost[self.id]:
            screen.blit(spooked_img, (self.x_pos, self.y_pos))
        else:
            screen.blit(dead_img, (self.x_pos, self.y_pos))
        ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
        return ghost_rect

    def check_collisions(self):
        # Your existing implementation for checking collisions
        # R, L, U, D
        num1 = ((HEIGHT - 50) // 32)
        num2 = (WIDTH // 30)
        num3 = 15
        self.turns = [False, False, False, False]
        if 0 < self.center_x // 30 < 29:
            if level_1[(self.center_y - num3) // num1][self.center_x // num2] == 9:
                self.turns[2] = True
            if level_1[self.center_y // num1][(self.center_x - num3) // num2] < 3 \
                    or (level_1[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[1] = True
            if level_1[self.center_y // num1][(self.center_x + num3) // num2] < 3 \
                    or (level_1[self.center_y // num1][(self.center_x + num3) // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[0] = True
            if level_1[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
                    or (level_1[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[3] = True
            if level_1[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
                    or (level_1[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[2] = True

            if self.direction == 2 or self.direction == 3:
                if 12 <= self.center_x % num2 <= 18:
                    if level_1[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
                            or (level_1[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[3] = True
                    if level_1[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
                            or (level_1[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[2] = True
                if 12 <= self.center_y % num1 <= 18:
                    if level_1[self.center_y // num1][(self.center_x - num2) // num2] < 3 \
                            or (level_1[self.center_y // num1][(self.center_x - num2) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[1] = True
                    if level_1[self.center_y // num1][(self.center_x + num2) // num2] < 3 \
                            or (level_1[self.center_y // num1][(self.center_x + num2) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[0] = True

            if self.direction == 0 or self.direction == 1:
                if 12 <= self.center_x % num2 <= 18:
                    if level_1[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
                            or (level_1[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[3] = True
                    if level_1[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
                            or (level_1[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[2] = True
                if 12 <= self.center_y % num1 <= 18:
                    if level_1[self.center_y // num1][(self.center_x - num3) // num2] < 3 \
                            or (level_1[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[1] = True
                    if level_1[self.center_y // num1][(self.center_x + num3) // num2] < 3 \
                            or (level_1[self.center_y // num1][(self.center_x + num3) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[0] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 350 < self.x_pos < 550 and 370 < self.y_pos < 480:
            self.in_box = True
        else:
            self.in_box = False
        return self.turns, self.in_box

    def move(self):
        # This will be implemented by subclasses
        pass

class Pinky(Ghost):
    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id):
        super().__init__(x_coord, y_coord, target, speed, img, direct, dead, box, id)

    def move(self):
        # r, l, u, d
        # pinky is going to move using the manhattan taxi tracking method
        dist_x = abs(self.target[0] - self.x_pos)
        dist_y = abs(self.target[1] - self.y_pos)

        if dist_x >= dist_y:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.direction = 0
                self.x_pos += self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
            elif self.turns[1]:
                self.direction = 1
                self.x_pos -= self.speed
        else:
            if self.target[1] > self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[3]:
                self.direction = 3
                self.y_pos -= self.speed

        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos -= 30

        return self.x_pos, self.y_pos, self.direction

class Blinky(Ghost):
    # r, l, u, d
    # blinky is going to move using the Dijkstra's shortest path tracking method
    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id, grid):
        super().__init__(x_coord, y_coord, target, speed, img, direct, dead, box, id)
        self.grid = grid

    def dijkstra_shortest_path(self, start, target):
        graph = self.grid_to_graph(self.grid)
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        queue = [(0, start)]
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_node == target:
                break
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        return distances[target]

    def grid_to_graph(self, grid):
        graph = defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] not in [3, 4, 5, 6, 7, 8]:  # Considering only positions where Pacman can move (i.e., not walls)
                    if i > 0 and grid[i - 1][j] not in [3, 4, 5, 6, 7, 8]:
                        graph[(i, j)].append(((i - 1, j), 1))
                    if i < len(grid) - 1 and grid[i + 1][j] not in [3, 4, 5, 6, 7, 8]:
                        graph[(i, j)].append(((i + 1, j), 1))
                    if j > 0 and grid[i][j - 1] not in [3, 4, 5, 6, 7, 8]:
                        graph[(i, j)].append(((i, j - 1), 1))
                    if j < len(grid[i]) - 1 and grid[i][j + 1] not in [3, 4, 5, 6, 7, 8]:
                        graph[(i, j)].append(((i, j + 1), 1))
        return graph

    def move(self):
        shortest_distance = self.dijkstra_shortest_path((self.x_pos, self.y_pos), self.target)
        if shortest_distance <= self.speed:
            self.x_pos, self.y_pos = self.target
            return self.x_pos, self.y_pos, self.direction

        # Determine direction to move based on the next node in the shortest path
        next_node = self.grid[0][0]  # Initialize with arbitrary node
        min_distance = float('inf')
        for neighbor, weight in self.grid_to_graph(self.grid)[(self.x_pos, self.y_pos)]:
            if shortest_distance[neighbor] < min_distance:
                min_distance = shortest_distance[neighbor]
                next_node = neighbor

        if next_node[0] > self.x_pos and self.turns[0]:
            self.direction = 0
            self.x_pos += self.speed
        elif next_node[0] < self.x_pos and self.turns[1]:
            self.direction = 1
            self.x_pos -= self.speed
        elif next_node[1] > self.y_pos and self.turns[2]:
            self.direction = 2
            self.y_pos += self.speed
        elif next_node[1] < self.y_pos and self.turns[3]:
            self.direction = 3
            self.y_pos -= self.speed

        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos -= 30

        return self.x_pos, self.y_pos, self.direction
    
class Inky(Ghost):
    # r, l, u, d
    # blinky is going to move using a breadth first path tracking method based on a path queue 
    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id, grid):
        super().__init__(x_coord, y_coord, target, speed, img, direct, dead, box, id)
        self.grid = grid

    def bfs_shortest_path(self, start, target):
        visited = set()
        queue = deque([(start, [])])

        while queue:
            current, path = queue.popleft()
            if current == target:
                return path
            if current in visited:
                continue
            visited.add(current)

            # Generate neighboring cells
            neighbors = []
            x, y = current
            if x > 0 and self.grid[x - 1][y] != '#':
                neighbors.append((x - 1, y))
            if x < len(self.grid) - 1 and self.grid[x + 1][y] != '#':
                neighbors.append((x + 1, y))
            if y > 0 and self.grid[x][y - 1] != '#':
                neighbors.append((x, y - 1))
            if y < len(self.grid[x]) - 1 and self.grid[x][y + 1] != '#':
                neighbors.append((x, y + 1))

            for neighbor in neighbors:
                queue.append((neighbor, path + [neighbor]))

        # If no path is found, return an empty path
        return []

    def move(self):
        # Add the while loop here
        while game_running:
            shortest_path = self.bfs_shortest_path((self.x_pos, self.y_pos), self.target)
            if shortest_path:
                next_cell = shortest_path[0]
                next_x, next_y = next_cell

                if next_x > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif next_x < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif next_y > self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos += self.speed
                elif next_y < self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos -= self.speed

            if self.x_pos < -30:
                self.x_pos = 900
            elif self.x_pos > 900:
                self.x_pos -= 30

            return self.x_pos, self.y_pos, self.direction

class Clyde(Ghost):
    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id):
        super().__init__(x_coord, y_coord, target, speed, img, direct, dead, box, id)

    def move(self):
        target_x, target_y = self.target

        # Calculate horizontal and vertical differences
        dx = target_x - self.x_pos
        dy = target_y - self.y_pos

        # Determine the direction based on differences
        if abs(dx) > abs(dy):
            if dx > 0:
                if self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif dy > 0 and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif dy < 0 and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
            elif dx < 0:
                if self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif dy > 0 and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif dy < 0 and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
        else:
            if dy > 0:
                if self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif dx > 0 and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif dx < 0 and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif dy < 0:
                if self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif dx > 0 and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif dx < 0 and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed

        # Handle teleportation
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos -= 30

        return self.x_pos, self.y_pos, self.direction

def convert_to_board_coordinates(x, y, width, height, board):
    num1 = ((height - 30) // 32)
    num2 = (width // 30)
    j = x // num2
    i = y // num1

    if i < 0:
        i = 0
    elif i >= len(board):
        i = len(board) - 1

    if j < 0:
        j = 0
    elif j >= len(board[0]):
        j = len(board[0]) - 1

    return i, j



print(blinky.target) 

# Example usage
x = 450  # Example pixel x-coordinate
y = 663  # Example pixel y-coordinate
 

# Convert pixel coordinates to grid coordinates
i, j = convert_to_board_coordinates(x, y, WIDTH, HEIGHT, Maze_1)

print("Grid coordinates:", i, j)
