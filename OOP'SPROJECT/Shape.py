#29/11/2023

class Shape:
    PI=3.14


    def __init__(self,color,bw):
        self.__color = color
        self.__borderWidth=bw


    def setColor(self,c=""):
        self.__color =c
    def getColor(self):
        return self.__color

    def setBorderWidth(self,bw):
        self.__borderWidth = bw
    def getBorderWidth(self):
        return  self.__borderWidth


    @staticmethod        #decorator
    def getPi():
        return Shape.PI