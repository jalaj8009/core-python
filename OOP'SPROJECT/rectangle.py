#29/11/2023

from Shape import Shape


class Rectangle(Shape):
    def __init__(self, color, bw, length,width):
        super().__init__(color,bw)
        self.__length = length
        self.__width=width

    def setLength(self,length):
        self.__length=length

    def getLength(self):
        return self.__length

    def setWidth(self,w):
        self.__width=w

    def getWidth(self):
        return self.__width

    def area(self):
        return (self.__length)*(self.__width)