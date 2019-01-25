class Cell:

    def __init__(self, width, height, cell_type):
        self.w = width
        self.h = height
        self.type = cell_type
        self.happiness = 0
        self.neighbors = []