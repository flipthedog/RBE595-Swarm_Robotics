# Board.py
# Store the cell states

# Imports
import random
import pygame
import time

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

        self.createBoard() # Populate the arrays
        self.populateNeighbors() # Set the neighbors

    # Initialize the board array
    def createBoard(self):

        for i in range(0, self.h):

            for j in range(0, self.w):

                make_cell = random.uniform(0, 1)

                # Decide whether to make the cell
                if make_cell > self.population:
                    type_num = 0 # Create empty cell
                else:
                    type_num = random.randint(1, 2) # Create cell of type

                # Create the cell
                cell = Cell.Cell(j, i, type_num)

                # Neighbors:
                #     -j
                #    0 1 2
                # -i 3 h 4 +i
                #    5 6 7
                #     +j

                # Add cell to array
                self.cells[i][j] = cell

    # populateNeighbors()
    # Find the neighbors for all the cell objects
    def populateNeighbors(self):

        # Iterate through every cell
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

    # Draw the cells individually on the pygame screen
    def draw(self, screen):
        rect2 = screen.get_rect()

        # Math to determine where to draw and cell dimensions
        min_x = rect2[0]
        min_y = rect2[1]

        max_x = rect2[2]
        max_y = rect2[3]

        dist_x = max_x - min_x
        dist_y = max_y - min_y

        # Cell dimensions
        cell_width = dist_x / self.w
        cell_height = dist_y / self.h

        # Draw all the cells
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

                # Determine cell color
                if cell.type == 1:
                    color = [random.randint(225,255), 0, 0]
                elif cell.type == 2:
                    color = [0, 0, random.randint(225,255)]
                else:
                    color = [0, 0, 0]

                pygame.draw.rect(screen, color, rectangle)

    # Board update function
    def update(self):

        # Empty out the previous array
        self.reshuffle_cells = []

        # Iterate through all the cells and decide which to move
        for i in range(0, self.h):

            for j in range(0, self.w):

                cell = self.cells[i][j]

                happiness = cell.update() # Update the cell happiness

                if happiness <= self.t:
                    # Unhappy cell, so it has to be moved
                    self.reshuffle_cells.append(cell)

        self.updateCells()

    # updateCells()
    # Update the status of the cells
    def updateCells(self):

        for cell in self.reshuffle_cells:
            # start = time.time()
            # Perform BFS to find nearest happy cell
            closest = self.findNearestEmpty(cell, cell.type)
            # end = time.time()

            # print("BFS Time: " + str(end - start))

            # Alter the cell to empty and new cell to type
            closest.type = cell.type

            cell.type = 0


    # Calculate the cell's happiness
    def calc_happiness(self, cell, cell_type):
        neighbors = cell.neighbors

        number = 0

        # Search through neighbor types
        for neighbor in neighbors:
            if neighbor.isCell:
                if neighbor.type == cell_type:
                    number += 1

        return number

    # Performs BFS search to find the nearest empty cell
    def findNearestEmpty(self, root, cell_type):

        visited = [] # Array of visited cells

        queue = [root] # BFS queue

        while queue:

            vertex = queue.pop(0)

            # Check if cell is empty
            if vertex.type == 0:
                # Check if cell will satisfy
                if self.calc_happiness(vertex, cell_type):
                    return vertex

            neighbors = vertex.neighbors

            # Randomize neighbors
            random.shuffle(neighbors)

            for neighbor in neighbors:

                # Check if neighbors have been visited
                if neighbor not in visited and neighbor.isCell:

                    # Neighbor has not been visited, so add it
                    visited.append(neighbor)
                    queue.append(neighbor)
