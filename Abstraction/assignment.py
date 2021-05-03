import math

from abc import ABC, abstractmethod


class shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass


class circle(shape):
    def __init__(self, color):
        super(). __init__(color)

    def area(self, radius):
        print(math.pi*radius**2)


class rectangle(shape):
    def __init__(self, color):
        super().__init__(color)

    def area(self, lenght, width):
        print(lenght*width)


shape1 = circle("green")
shape1.area(6)
print(shape1.color)
shape2 = rectangle("red")
shape2.area(7, 5)
print(shape2.color)
