#29/11/2023

from Shape import Shape


class Circle(Shape):
    def __init__(self, bw=0,r=0):

        self.__radius=r

    def getRadius(self):
        return self.__radius

    def setRadius(self,r):
        self.__radius=r

    def area(self):
        return Shape.getPi()*self.getRadius()**2