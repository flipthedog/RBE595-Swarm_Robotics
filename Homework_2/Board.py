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
        self.cells = [[-1] * width] * height
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

                cell = Cell.Cell(i, j, type)

                # Neighbors:
                # 0 1 2
                # 3 h 4
                # 5 6 7

                self.cells[i][j]

                if (i - 1) > 0 and (j - 1) > 0:
                cell.neighbors[]

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
        # print("Cell Width: " + str(cell_width))
        # print("Cell Height: " + str(cell_height))

        for cell in self.cells:
            rectangle = pygame.Rect(
                cell_width * cell.w,
                cell_height * cell.h,
                cell_width * (cell.w + 1),
                 cell_height * (cell.h + 1))

            if cell.type == 1:
                color = [255, 0, 0]
            elif cell.type == 2:
                color = [0, 0, 255]
            else:
                color = [0, 0, 0]

            pygame.draw.rect(screen, color, rectangle)

    def update(self):
        None