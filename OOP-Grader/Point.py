import math as m

class Point:
    def __init__(self, x ,y):
        self.__x = x
        self.__y = y
        
    @property
    def getX(self):
        return self.x
    @property
    def getY(self):
        return self.y
    
    def setter(self,x_new ,y_new):
        self.x = x_new
        self.y = y_new
        
    def read(self):
        self.x = input("Nhap toa do x moi: ")
        self.y = input("Nhap toa do y moi: ")
        
    def __str__(self):
        return f"({self.x}, {self.y})"
        
    def move(self):
        dx = input("Khoang cach di chuyen cua x: ")
        dy = input("Khoang cach di chuyen cua y: ")
        self.x = self.x + dx
        self.y = self.y + dy
        
    def distance(self):
        value = m.sqrt(m.pow(self.x, 2) + m.pow(self.y, 2))
        return value
    
    def distance_p2p (self, other):
        value = m.sqrt((m.pow(self.x, 2) + m.pow(other.x,2) + (m.pow(self.y, 2) + m.pow(other.y, 2))))
        return value