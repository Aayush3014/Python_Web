from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def printarea(self):   # After using @abstractmethod decorator printarea() is necessarily need to be defined  
        return 0           # in all the classes in which Shape class is being inherited.


class Rectangle(Shape):
    def __init__(self) -> None:
        self.length = 6
        self.breadth = 5

    def printarea(self):
        # return super().printarea()    It will return the value which is returned in abstract base class.
        return self.length*self.breadth


class Square():
    def __init__(self) -> None:
        self.side = 6

    # def printarea(self):
    #     return self.side**2


rect1 = Rectangle()
print(rect1.printarea())
square = Square()
# print(square.printarea())