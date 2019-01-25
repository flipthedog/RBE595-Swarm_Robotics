# Imports
import random
import pygame

# Personal imports
import Cell

class Board:

    def __init__(self, width, height, t, population):
        self.w = width
        self.h = height
        self.t = t
        self.cells = []
        self.population = population
        self.createBoard()

    def createBoard(self):

        for i in range(0, self.w):

            for j in range(0, self.h):
                make_cell = random.uniform(0, 1)

                if make_cell > self.population:
                    type = 0
                else:
                    type = random.randint(1,2)

                cell = Cell(i, j, type)
                self.cells.append(cell)

    def draw(self, screen):
        rect = screen.get_rect()

        min_x = rect[0]
        min_y = rect[1]

        max_x = rect[2]
        max_y = rect[3]

        dist_x = max_x - min_x
        dist_y = max_y - min_y

        cell_width = dist_x / self.w
        cell_height = dist_y / self.h

        for cell in self.cells:
            rectangle = pygame.rect((-cell_width / 2) + cell_width * cell.w, (- cell_height / 2) + cell_height * cell_height, (cell_width / 2) + cell_width * cell.w, (- cell_height / 2) + cell_height * cell_height)
            color = [255,0,0, 255]
            pygame.draw.rect(screen, color, rectangle, width=0)

    def update(self):
        None