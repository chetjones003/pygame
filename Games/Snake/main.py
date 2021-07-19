import pygame, sys, random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(
                int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size
            )
            pygame.draw.rect(screen, (0, 0, 0), block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class FOOD:
    def __init__(self):
        self.randomize()

    def draw_food(self):
        food_rect = pygame.Rect(
            int(self.pos.x * cell_size),
            int(self.pos.y * cell_size),
            cell_size,
            cell_size,
        )

        pygame.draw.rect(screen, (126, 166, 114), food_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()


pygame.init()
cell_size = 40
cell_number = 15
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

main = MAIN()

SREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SREEN_UPDATE, 250)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SREEN_UPDATE:
            main.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                main.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                main.snake.direction = Vector2(-1, 0)

    screen.fill((175, 215, 70))
    main.draw_elements()
    pygame.display.update()
    clock.tick(60)
