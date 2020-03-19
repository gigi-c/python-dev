# Snake
import pygame
pygame.init()

pygame.display.set_caption("How Much Can Your Snake Eat?")
# classs food


# class snake
class snake(object):
    snake_body = []
    turns = {}
    def __init__(self, colour, position):
        self.colour = colour
        self.head = cube(position)
        self.snake_body.append(self.head)

        self.direction_x = 0
        self.direction_y = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.direction_x = -1
                    self.direction_y = 0
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

                elif keys[pygame.K_RIGHT]:
                    self.direction_x = 1
                    self.direction_y = 0
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]
                elif keys[pygame.K_UP]:
                    self.direction_x = 0
                    self.direction_y = -1
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]
                elif key[pygame.K_DOWN]:
                    self.direction_x = 0
                    self.direction_y = 1
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

# grid
def grid_lines(width, rows, surface):
    distance_between_lines = width // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + distance_between_lines
        y = y + distance_between_lines

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))

# new window
def new_window(surface):
    surface.fill((0, 0, 0))
    grid_lines(surface)
    pygame.display.update()

# main window
def snake_game():
    global width, rows, snake
    width = 500
    rows = 20
    window = pygame.display.set_mode((width, width))
    snake = snake((255, 0, 0), (10, 10))
    clock = pygame.time.Clock()
    running = True
    while running:
        pygame.time.delay(50)
        clock.tick(10)
        new_window(window)

