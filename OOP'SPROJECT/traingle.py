from Shape import Shape


class traingle(Shape):
    def __init__(self,base,length,thirdside):
        self.__base=base
        self.__length=length
        self.__thirdside=thirdside


    def setlength(self,length):
        self.__length=length


    def getlength(self):
        return self.__length


    def setbase(self,base):
        self.__base=base

    def getbase(self):
        return self.__base

    def setthirdside(self,thirdside):
        self.__thirdside=thirdside

    def getbase(self):
        return self.__thirdside



    def area(self):
        return (0.5*(self.__base)*(self.__length)*(self.__thirdside))/(self.__thirdside)

    def parameter(self):
        return (self.__length + self.__thirdside + self.__base)
