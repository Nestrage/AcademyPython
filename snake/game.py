import sys
import pygame
import time
import random
# 1 ... 5
DIFFICULTY = 1

START_LENGTH = 5
WAIT = 0.1 / DIFFICULTY
RADIUS = 10
RES = [800, 600]
WALL = []
FOOD = ()
pygame.init()
SCREEN = pygame.display.set_mode(RES)
pygame.display.set_caption("Snake")


class Obj():
    """class for moving objects
    """
    def __init__(self):
        self.head_x = 100
        self.head_y = 100
        self.length = START_LENGTH
        self.elements = [[self.head_x, self.head_y]]

        while len(self.elements) != (self.length - 1):
            self.elements.append([self.head_x, self.head_y])
        self.speed = [RADIUS * 2, 0]
        pygame.draw.circle(SCREEN, (230, 230, 20), (self.head_x, self.head_y), RADIUS)
        pygame.display.flip()

    def move(self):
        """move function
        """
        pygame.draw.circle(SCREEN, (0, 0, 0), (self.elements[-1][0], self.elements[-1][1]), RADIUS)
        self.elements.pop()
        self.head_x += self.speed[0]
        self.head_y += self.speed[1]
        self.elements = [[self.head_x, self.head_y]] + self.elements[0:]
        self.check_dead()
        for element in self.elements[1:]:
            """body"""
            pygame.draw.circle(SCREEN, (230, 230, 20), (element[0], element[1]), RADIUS)
        """head"""
        pygame.draw.circle(SCREEN, (50, 50, 200), (self.head_x, self.head_y), RADIUS)
        pygame.display.flip()
        self.check_food()

    def check_dead(self):
        """check_dead function
        """
        if [self.head_x, self.head_y] in self.elements[1:]:
            exit_dead()
        if [self.head_x, self.head_y] in WALL:
            exit_dead()

    def check_food(self):
        if (self.head_x, self.head_y) == FOOD:
            self.elements.append(self.elements[-1])
            create_food()

def draw_map():
    for n in range(20, RES[0], 20):
        pygame.draw.circle(SCREEN, (250, 0, 0), (n, 20), 10)
        WALL.append([n, 20])
        pygame.draw.circle(SCREEN,(250, 0, 0),(n, RES[1] - 20), 10)
        WALL.append([n, RES[1] - 20])
    for n in range(20, RES[1], 20):
        pygame.draw.circle(SCREEN, (240, 0, 0),(20, n), 10)
        WALL.append([20, n])
        pygame.draw.circle(SCREEN, (240, 0, 0), (RES[0] - 20, n), 10)
        WALL.append([RES[0] - 20 , n])
    pygame.display.flip()

def create_food():
    global FOOD
    FOOD = ()
    while ( list(FOOD) in WALL ) or ( list(FOOD) in SNAKE.elements) or (not FOOD):
        FOOD = (random.randrange(40, RES[0] - 40, 20),
            (random.randrange(40, RES[1] - 40, 20)))

    pygame.draw.circle(SCREEN, (0, 255, 0), FOOD, RADIUS)
    pygame.display.flip()

def event_loop():
    """main event loop
    """
    while True:
        time.sleep(WAIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_DOWN)	and \
                    (SNAKE.speed != [0, -2*RADIUS]):
                    SNAKE.speed = [0, 2*RADIUS]
                elif (event.key == pygame.K_UP) and \
                    (SNAKE.speed != [0, 2*RADIUS]):
                    SNAKE.speed = [0, -2*RADIUS]
                elif (event.key == pygame.K_RIGHT) and \
                    (SNAKE.speed != [-2* RADIUS, 0]):
                    SNAKE.speed = [2*RADIUS, 0]
                elif (event.key == pygame.K_LEFT) and \
                    (SNAKE.speed != [2* RADIUS, 0]):
                    SNAKE.speed = [-2*RADIUS, 0]
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        SNAKE.move()

def exit_dead():
    """exit if dead
    """
    print("Difficulty:\t%d" % DIFFICULTY)
    print("Foods eaten:\t%d" % (len(SNAKE.elements) - START_LENGTH + 1))
    print("Score:\t\t%d" % ((len(SNAKE.elements) - START_LENGTH + 1) * DIFFICULTY))
    time.sleep(1)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    draw_map()
    SNAKE = Obj()
    create_food()
event_loop()