import pygame, sys, os, random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        # loading sprites
        self.head_up = pygame.image.load(
            os.path.join("Snake", "Graphics", "head_up.png")
        ).convert_alpha()
        self.head_down = pygame.image.load(
            os.path.join("Snake", "Graphics", "head_down.png")
        ).convert_alpha()
        self.head_right = pygame.image.load(
            os.path.join("Snake", "Graphics", "head_right.png")
        ).convert_alpha()
        self.head_left = pygame.image.load(
            os.path.join("Snake", "Graphics", "head_left.png")
        ).convert_alpha()

        self.tail_up = pygame.image.load(
            os.path.join("Snake", "Graphics", "tail_up.png")
        ).convert_alpha()
        self.tail_down = pygame.image.load(
            os.path.join("Snake", "Graphics", "tail_down.png")
        ).convert_alpha()
        self.tail_right = pygame.image.load(
            os.path.join("Snake", "Graphics", "tail_right.png")
        ).convert_alpha()
        self.tail_left = pygame.image.load(
            os.path.join("Snake", "Graphics", "tail_left.png")
        ).convert_alpha()

        self.body_vertical = pygame.image.load(
            os.path.join("Snake", "Graphics", "body_vertical.png")
        ).convert_alpha()
        self.body_horizontal = pygame.image.load(
            os.path.join("Snake", "Graphics", "body_horizontal.png")
        ).convert_alpha()

        self.body_tr = pygame.image.load(
            os.path.join("Snake", "Graphics", "body_tr.png")
        ).convert_alpha()
        self.body_tl = pygame.image.load(
            os.path.join("Snake", "Graphics", "body_tl.png")
        ).convert_alpha()
        self.body_br = pygame.image.load(
            os.path.join("Snake", "Graphics", "body_br.png")
        ).convert_alpha()
        self.body_bl = pygame.image.load(
            os.path.join("Snake", "Graphics", "body_bl.png")
        ).convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            # create rect for snake
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            # checking if head
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                # checking if sprite should be vertical
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                # checking if sprite should be horizontal
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                # checking if sprite should be corner
                else:
                    # top left
                    if (
                        previous_block.x == -1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == -1
                    ):
                        screen.blit(self.body_tl, block_rect)
                    # bottom left
                    elif (
                        previous_block.x == -1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == -1
                    ):
                        screen.blit(self.body_bl, block_rect)
                    # top right
                    elif (
                        previous_block.x == 1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == 1
                    ):
                        screen.blit(self.body_tr, block_rect)
                    # bottom right
                    elif (
                        previous_block.x == 1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == 1
                    ):
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        # display proper head sprite based on direction
        head_direction = self.body[1] - self.body[0]
        if head_direction == Vector2(1, 0):
            self.head = self.head_left
        if head_direction == Vector2(-1, 0):
            self.head = self.head_right
        if head_direction == Vector2(0, 1):
            self.head = self.head_up
        if head_direction == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        # display proper tail sprite based on direction
        tail_direction = self.body[-2] - self.body[-1]
        if tail_direction == Vector2(1, 0):
            self.tail = self.tail_left
        if tail_direction == Vector2(-1, 0):
            self.tail = self.tail_right
        if tail_direction == Vector2(0, 1):
            self.tail = self.tail_up
        if tail_direction == Vector2(0, -1):
            self.tail = self.tail_down

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

        # pygame.draw.rect(screen, (126, 166, 114), food_rect)
        screen.blit(apple, food_rect)

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
        self.check_fail()

    def draw_elements(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()

    def check_fail(self):
        # check if snake head is not between 0 and cell_number
        if (
            not 0 <= self.snake.body[0].x < cell_number
            or not 0 <= self.snake.body[0].y < cell_number
        ):
            self.game_over()

        # checking for body collisions
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()
cell_size = 40
cell_number = 15
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load(
    os.path.join("Snake", "Graphics", "apple.png")
).convert_alpha()

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
                if main.snake.direction.y != 1:
                    main.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main.snake.direction.y != -1:
                    main.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main.snake.direction.x != -1:
                    main.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main.snake.direction.x != 1:
                    main.snake.direction = Vector2(-1, 0)

    screen.fill((175, 215, 70))
    main.draw_elements()
    pygame.display.update()
    clock.tick(60)
