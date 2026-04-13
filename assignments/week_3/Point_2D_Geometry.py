import math

class Point():
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        
    def Input(self):
        self.symbol = input("Enter the symbol for the point: ")
        self.x = float(input("Enter the x coordinate: "))
        self.y = float(input("Enter the y coordinate: "))
    
    def Distance(self, other):
        distance = math.sqrt(pow(self.x * other.x, 2) + pow(self.y * other.y, 2))
        return distance
    
    