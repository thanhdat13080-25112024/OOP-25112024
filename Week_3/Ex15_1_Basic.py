import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        

class Rectangle:
    def __init__(self, point_1, point_2, point_3, point_4):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.point_4 = point_4
        

def Point_in_circle(circle, point):
    x = int(input("x: "))
    y = int(input("y: "))
    p = Point(x, y)
    if math.sqrt(math.pow(point.x - circle.center.x) + math.pow(point.y - circle.center.y)) == circle.radius:
        return True
    return False


def Rect_in_circle(circle, rectangle):
    index = 0
    if math.sqrt(math.pow(rectangle.point_1.x - circle.center.x, 2) + math.pow(rectangle.point_1.y - circle.center.y, 2)) == circle.radius:
        index += 1
    if math.sqrt(math.pow(rectangle.point_2.x - circle.center.x, 2) + math.pow(rectangle.point_2.y - circle.center.y, 2)) == circle.radius:
        index += 1
    if math.sqrt(math.pow(rectangle.point_3.x - circle.center.x, 2) + math.pow(rectangle.point_3.y - circle.center.y, 2)) == circle.radius:
        index += 1
    if math.sqrt(math.pow(rectangle.point_4.x - circle.center.x, 2) + math.pow(rectangle.point_4.y - circle.center.y, 2)) == circle.radius:
        index += 1
    if index == 4:
        return True
    return False


def Rect_circle_overlap(circle, rectangle):
    if math.sqrt(math.pow(rectangle.point_1.x - circle.center.x, 2) + math.pow(rectangle.point_1.y - circle.center.y, 2)) <= circle.radius:
        index += 1
    if math.sqrt(math.pow(rectangle.point_2.x - circle.center.x, 2) + math.pow(rectangle.point_2.y - circle.center.y, 2)) <= circle.radius:
        index += 1
    if math.sqrt(math.pow(rectangle.point_3.x - circle.center.x, 2) + math.pow(rectangle.point_3.y - circle.center.y, 2)) <= circle.radius:
        index += 1
    if math.sqrt(math.pow(rectangle.point_4.x - circle.center.x, 2) + math.pow(rectangle.point_4.y - circle.center.y, 2)) <= circle.radius:
        index += 1
    if index >= 1:
        return True
    return False


center_point = Point(150, 100)
circle_1 = Circle(center_point, 75)
p1 = Point(100, 50)
p2 = Point(200, 50)
p3 = Point(200, 105)
p4 = Point(100, 150)
rect = Rectangle(p1, p2, p3, p4)