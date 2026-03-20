class point():
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
    def input(self):
        self.symbol = input("Enter the symbol for the point: ")
        self.x = float(input("Enter the x coordinate: "))
        self.y = float(input("Enter the y coordinate: "))