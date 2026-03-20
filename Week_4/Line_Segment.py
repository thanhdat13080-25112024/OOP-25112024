from multipledispatch import dispatch

class Point():
    def __init__ (self, x, y):
        self.__x = x
        self.__y = y
    @dispatch(object, object)
    def add (self.Point(), other):
        pass