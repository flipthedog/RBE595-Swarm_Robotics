# Cell.py
# Cell object for the Board class
# Tracks the individual cell type and neighbors

class Cell:

    def __init__(self, width, height, cell_type):
        # Location
        self.w = width
        self.h = height

        self.type = cell_type
        self.happiness = 0 # satisfaction

        # Neighbors
        self.neighbors = []
        self.isCell = True

    # Cell update function
    def update(self):
        self.updateHappiness()
        return self.happiness

    # Update the happiness of the cell, search through neighbors
    def updateHappiness(self):

        self.happiness = 0

        for cell in self.neighbors:

            if cell.isCell:

                if cell.type == self.type:
                    self.happiness += 1

    # Debugging function to check neighbors
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