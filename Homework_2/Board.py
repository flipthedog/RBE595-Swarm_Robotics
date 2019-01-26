# Imports
import random
import pygame

# Personal imports
import Cell
import EmptyCell

class Board:

    def __init__(self, width, height, t, population):
        self.w = width
        self.h = height
        self.t = t
        self.cells = [0] * self.h
        for i in range(0, self.h):
            self.cells[i] = [0] * self.w

        self.population = population

        self.reshuffle_cells = [] # Cells that need to be moved

        self.createBoard()
        self.populateNeighbors()

    def createBoard(self):

        for i in range(0, self.h):

            for j in range(0, self.w):

                make_cell = random.uniform(0, 1)

                # print(make_cell)

                if make_cell > self.population:
                    type_num = 0
                else:
                    type_num = random.randint(1, 2)

                cell = Cell.Cell(j, i, type_num)

                # Neighbors:
                #     -j
                #    0 1 2
                # -i 3 h 4 +i
                #    5 6 7
                #     +j

                self.cells[i][j] = cell

    def populateNeighbors(self):

        for i in range(0, self.h):

            for j in range(0, self.w):

                cell = self.cells[i][j]

                # Top-left
                if (i - 1) > 0 and (j - 1) > 0:
                    cell.neighbors.append(self.cells[i - 1][j - 1])
                else:
                    cell.neighbors.append(EmptyCell.EmptyCell())

                # Top
                if (j - 1) > 0:
                    cell.neighbors.append(self.cells[i][j - 1])
                else:
                    cell.neighbors.append(EmptyCell.EmptyCell())

                # Top Right
                if (j - 1) > 0 and (i + 1) < self.w:
                    cell.neighbors.append(self.cells[i + 1][j - 1])
                else:
                    cell.neighbors.append(EmptyCell.EmptyCell())

                # Left
                if (i - 1) > 0:
                    cell.neighbors.append(self.cells[i - 1][j])
                else:
                    cell.neighbors.append(EmptyCell.EmptyCell())

                # Right
                if (i + 1) < self.w:
                    cell.neighbors.append(self.cells[i + 1][j])
                else:
                    cell.neighbors.append(EmptyCell.EmptyCell())

                # Left Bottom
                if (i - 1) > 0 and (j + 1) < self.h:
                    cell.neighbors.append(self.cells[i - 1][j + 1])
                else:
                    cell.neighbors.append(EmptyCell.EmptyCell())

                # Bottom
                if (j + 1) < self.h:
                    cell.neighbors.append(self.cells[i][j + 1])
                else:
                    cell.neighbors.append(EmptyCell.EmptyCell())

                # Right Bottom
                if (i + 1) < self.w and (j + 1) < self.h:
                    cell.neighbors.append(self.cells[i + 1][j + 1])
                else:
                    cell.neighbors.append(EmptyCell.EmptyCell())

    def draw(self, screen):
        rect2 = screen.get_rect()

        min_x = rect2[0]
        min_y = rect2[1]

        max_x = rect2[2]
        max_y = rect2[3]

        dist_x = max_x - min_x
        dist_y = max_y - min_y

        cell_width = dist_x / self.w
        cell_height = dist_y / self.h

        # print("Cell Width: " + str(cell_width))
        # print("Cell Height: " + str(cell_height))

        for i in range(0, self.h):

            for j in range(0, self.w):

                cell = self.cells[i][j]

                top_x = cell_width * i
                top_y = cell_height * j
                bottom_x = cell_width * (i + 1)
                bottom_y = cell_height * (j + 1)

                rectangle = pygame.Rect(
                    top_x,
                    top_y,
                    bottom_x,
                    bottom_y)

                if cell.type == 1:
                    color = [255, 0, 0]
                elif cell.type == 2:
                    color = [0, 0, 255]
                else:
                    color = [0, 0, 0]

                pygame.draw.rect(screen, color, rectangle)

        # cell = self.cells[random.randint(0,self.h - 1)][random.randint(0,self.w - 1)]
        #
        # #print("Neighbors: " + str(len(cell.neighbors)))
        #
        # for neighbor in cell.neighbors:
        #
        #     if neighbor.isCell:
        #         #print("Popped: w: " + str(neighbor.w) + " h: " + str(neighbor.h))
        #
        #         top_x = cell_width * neighbor.w
        #         top_y = cell_height * neighbor.h
        #         bottom_x = cell_width
        #         bottom_y = cell_height
        #
        #         rectangle = pygame.Rect(
        #             top_x,
        #             top_y,
        #             bottom_x,
        #             bottom_y)
        #
        #         color = [random.randint(0,255), random.randint(0,255), 0]
        #
        #         pygame.draw.rect(screen, color, rectangle)

    def update(self):

        self.reshuffle_cells = []

        for i in range(0, self.h):

            for j in range(0, self.w):

                cell = self.cells[i][j]

                # cell.printNeighbors()

                happiness = cell.update()

                if happiness <= self.t:
                    self.reshuffle_cells.append(cell)

        self.updateCells()

    def updateCells(self):

        for cell in self.reshuffle_cells:

            closest = self.findNearestEmpty(cell)

            closest.type = cell.type
            cell.type = 0

    # Performs BFS search to find the nearest empty cell
    def findNearestEmpty(self, root):

        visited = []

        queue = [root]

        while queue:

            vertex = queue.pop(0)

            if vertex.type == 0:
                return vertex

            for neighbor in vertex.neighbors:

                if neighbor not in visited and neighbor.isCell:
                    visited.append(neighbor)
                    queue.append(neighbor)




