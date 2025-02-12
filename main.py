import pygame
import sys
from random import randint
from pygame import Vector2

class Bloc:
    def __init__(self):
        self.x = randint(0, cell_number - 1)
        self.y = randint(0, cell_number - 1)
        self.pos = Vector2(self.x , self.y)
        self.direction = Vector2(0, 0)
        self.value = 2

    def draw_bloc(self):
        bloc_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 0, 0), bloc_rect)


    def move(self):
        if self.direction == Vector2(1, 0):
            self.pos.x = cell_number - 1
        elif self.direction == Vector2(-1, 0):
            self.pos.x = 0
        elif self.direction == Vector2(0, 1):
            self.pos.y = cell_number - 1
        elif self.direction == Vector2(0, -1):
            self.pos.y = 0

cell_size = 200
cell_number = 4
screen = pygame.display.set_mode(((cell_number * cell_size), (cell_number * cell_size)))
pygame.display.set_caption("2048")


class Game:

    def __init__(self):
        self.bloc_1 = Bloc()
        self.bloc_2 = Bloc()
        print(self.bloc_1.x)
        pygame.init()

    def draw_grid(self):
        for x in range(cell_number):
            for y in range(cell_number):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, (255, 255, 255), rect, 5)

    def draw_bloc(self):
        self.bloc_1.draw_bloc()
        self.bloc_2.draw_bloc()

        while self.bloc_1.pos == self.bloc_2.pos:
            self.bloc_2 = Bloc()
            self.bloc_2.draw_bloc()

    def move_bloc(self):
        if self.bloc_1.direction == Vector2(0, -1) and self.bloc_1.pos.y > 0:
            self.bloc_1.move()
        elif self.bloc_1.direction == Vector2(0, 1) and self.bloc_1.pos.y < cell_number - 1:
            self.bloc_1.move()
        elif self.bloc_1.direction == Vector2(-1, 0) and self.bloc_1.pos.x > 0:
            self.bloc_1.move()
        elif self.bloc_1.direction == Vector2(1, 0) and self.bloc_1.pos.x < cell_number - 1:
            self.bloc_1.move()


    def update(self):
        self.bloc_1.move()

    def run(self):
        clock = pygame.time.Clock()
        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE, 150)
        while True:
            for event in pygame.event.get():
                if event.type == SCREEN_UPDATE:
                    self.move_bloc()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.bloc_1.direction.y != 1:
                            self.bloc_1.direction = Vector2(0, -1)
                    if event.key == pygame.K_DOWN:
                        if self.bloc_1.direction.y != -1:
                            self.bloc_1.direction = Vector2(0, 1)
                    if event.key == pygame.K_LEFT:
                        if self.bloc_1.direction.x != 1:
                            self.bloc_1.direction = Vector2(-1, 0)
                    if event.key == pygame.K_RIGHT:
                        if self.bloc_1.direction.x != -1:
                            self.bloc_1.direction = Vector2(1, 0)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill((0, 0, 0))
            self.draw_bloc()
            self.draw_grid()
            clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
