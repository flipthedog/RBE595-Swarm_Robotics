import random

class Cell:

    def __init__(self, width, height, cell_type):
        self.w = width
        self.h = height
        self.type = cell_type
        self.happiness = 0
        self.neighbors = []
        self.isCell = True

        # print("Created new cell with: w: " + str(self.w) + " h: " + str(self.h) + " type: " + str(self.type))

    def update(self):

        self.updateHappiness()
        return self.happiness

    def updateHappiness(self):

        self.happiness = 0

        for cell in self.neighbors:

            if cell.isCell:

                if cell.type == self.type:
                    self.happiness += 1

    def printNeighbors(self):

        print("CELL COORDS: (x,y): (" + str(self.w) + ", " + str(self.h) + ")")

        for neighbor in self.neighbors:
            if neighbor.isCell:
                print("\tCELL COORDS: (neighx,neighy): (" + str(neighbor.w) + ", " + str(neighbor.h) + ")")
            else:
                print("\tEMPTY CELL")

        for cell in self.neighbors:

            if cell.isCell:

                self.happiness += 1