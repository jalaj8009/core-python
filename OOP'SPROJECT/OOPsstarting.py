# object oriented programming

# class DemoClass:
#     a = 1000
#
#     def sum(self):
#         print(100+900)
#
#
#     def sub(self):
#         print(1000-500)
#
#     def mult(self):
#         print(29*34)
#
#
# obj = DemoClass()
# print(obj.a)
# obj.sum()
# obj.sub()
# obj.mult()


# 23/11/2023
# class Democlass:
#
#
#     def __init__(self):
#         print("hi  rays")
#
#     def showdetail(self):
#         print("welcome to rays")
#
#     def sum(self,a,b):
#         print("sum is = ",a+b)
#
#
#
#
#
# obj=Democlass()
# obj.showdetail()
# obj.sum(100,200)


# Inheritance:


# class A:
#     car=4
#     bike=6
#     truck=10
#
#     def showdetailA(self):
#         print("this is class A")
#
# class B:
#     BMW=1
#     AUDI=2
#
#     def showdetailB(self):
#         print("this is class B")
#
# objA=A()
# print(objA.car)
# print(objA.bike)
# print(objA.truck)
# objA.showdetailA()
#
# objB=B()
# print(objB.BMW)
# print(objB.AUDI)
# objB.showdetailB()


# single level inheritance
# class A:
#     car=4
#     bike=6
#     truck=10
#
#     def showdetailA(self):
#         print("this is class A")
#
# class B(A):
#     BMW=1
#     AUDI=2
#
#     def showdetailB(self):
#         print("this is class B")
#
# objB=B()
# print(objB.car)
# print(objB.bike)
# print(objB.truck)
# print(objB.BMW)
# print(objB.AUDI)
# objB.showdetailB()
# objB.showdetailA()


# more than two class:

# class A:
#     car=4
#     bike=6
#     truck=10
#
#     def showdetailA(self):
#         print("this is class A")
#
# class B(A):
#     BMW=1
#     AUDI=2
#
#     def showdetailB(self):
#         print("this is class B")
#
#
# class C(B):
#     electric=4
#     petrol=8
#     diesel=11
#
#     def showdetailC(self):
#         print("this is class C")
#
# objC=C()
# print(objC.car)
# print(objC.bike)
# print(objC.diesel)
# print(objC.petrol)
# print(objC.electric)
# objC.showdetailC()
# objC.showdetailB()
# objC.showdetailA()


# 24/11/2023


# Multilevel inheritence


# class A:
#     car=4
#     bike=6
#     truck=10
#
#     def showdetailA(self):
#         print("this is class A")
#
# class B(A):
#     BMW=1
#     AUDI=2
#
#     def showdetailB(self):
#         print("this is class B")
#
#
# class C(B):
#     electric=4
#     petrol=8
#     diesel=11
#
#     def showdetailC(self):
#         print("this is class C")
#
# objC=C()
# print(objC.car)
# print(objC.bike)
# print(objC.diesel)
# print(objC.petrol)
# print(objC.electric)
# objC.showdetailC()
# objC.showdetailB()
# objC.showdetailA()



# multiple inheritence
# class A:
#     car=4
#     bike=6
#     truck=10
#
#     def showdetailA(self):
#         print("this is class A")
#
# class B:
#     BMW=1
#     AUDI=2
#
#     def showdetailB(self):
#         print("this is class B")
#
#
# class C(B,A):
#     electric=4
#     petrol=8
#     diesel=11
#
#     def showdetailC(self):
#         print("this is class C")
#
# objC=C()
# print(objC.car)
# print(objC.bike)
# print(objC.diesel)
# print(objC.petrol)
# print(objC.electric)
# objC.showdetailC()
# objC.showdetailB()
# objC.showdetailA()

# self keyword

# class Student:
#     a=100
#
#     def showvalue(self):
#         print(self.a)
#
#
#     def multi(self):
#         self.c=self.a*self.a
#         print(self.c)
#
#     def add(self,a,b,c):
#         print(a+b+c)
#
# obj=Student()
# obj.showvalue()
# obj.multi()
# obj.add(100,200,500)


# 25/11/2023


# ENCAPSULATION
# class Student:
#     __name="ajay"    #FOR sequring data
#
#     def __init__(self):
#         print(self.__name)
#         self.__showdetail()
#
#     def __showdetail(self):
#         print("this is student detail...")
#
# obj=Student()


'''class Person:
    __name =""
    __age=""
    __salary=""
    __bonus=""

    def setpersoninfo(self,name,age,salary,bonus):
        self.__name=name
        self.__age=age
        self.__salary=salary
        self.__bonus=bonus

    def getpersoninfo(self):
        return self.__name,self.__age,self.__salary,self.__bonus

obj=Person()
obj.setpersoninfo()  '''
