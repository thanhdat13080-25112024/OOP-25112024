from multipledispatch import dispatch
import turtle
import _tkinter

class Point():
    def __init__ (self, x, y):
        self.__x = x
        self.__y = y


print(turtle.forward(100))
turtle.done()