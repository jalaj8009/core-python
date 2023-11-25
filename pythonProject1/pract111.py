

# To take input from the user
# num = int(input("Enter a number: "))
#
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             #print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")

# # if input number is less than
# # or equal to 1, it is not prime
# else:
#     print(num, "is not a prime number")

# #print all vowel with the value in dictionary with values
# d={}
# for ascii in range(ord('A'),ord('z') +1) :
#     char=chr(ascii)
#     d[char]=ascii
# for x in d:
#     var = d[x]
#     if x in 'aeiouAEIOU':
#             print(x,var)
#
# d={}
# for ascii in range(ord('A'),ord('z') +1) :
#     char=chr(ascii)
#     d[char]=ascii
# for values in d:
#     var=str(d[values])
#     if var[-1] == '0'  or var[-1]=='2' or var[-1]=='4' or var[-1]=='6' or var[-1]=='8':
#         print(values,var)
#
# for x in range(100,-1,-1):
#     print(x)


# import math
# x=64
# print(math.sin(x))
#
# x=0
# print(math.cos(x))
#
# y=60
# print(math.cos(y))

# import random
# a=int(input("enter any number between 1 to 9="))
# b=random.randint(1,9)
# print(b)
# if a>b:
#     print("enter number is bigger than guess")
# elif b>a:
#     print("enter number is less than guess")
# else:
#     print("both are equal")


# a=40
# b=20
# a=(a+b)
#
#
# b=(a-b)
# a=(a-b)
# print(a)
# print(b)


# class Democlass:
#
#
#     def __init__(self):
#         print("hi  hrays")
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

#
# number=int(input("enter any number="))
# if number>1:
#    for i in  range(2,int(number**0.5)+1):
#       if number%i ==0:
#         print("not prime number")
#         break
#
#    else:
#         print("number is a prime number")
#
# else:
#     print("is not prime number")

# prime number
# number=int(input("enter any number="))
# if number>1:
#    for i in  range(2,number):
#       if number%i ==0:
#         print("not prime number")
#         break
#
#    else:
#         print("number is a prime number")
#
# else:
#     print("is not prime number")

#25/11/2023
# x=int(input("enter any number= "))
# y=int(input("enter number should be greater than x= "))
# for number in range(x,y):
#  if number>1:
#    for i in  range(2,number):
#       if number%i ==0:
#
#
#         break
#
#    else:
#         print(number,"number is a prime number")
#
# else:
#     print("upto=",y)

class A:
    car=4
    bike=6
    truck=10

    def showdetailA(self):
        print("this is class A")

class B:
    BMW=1
    AUDI=2

    def showdetailB(self):
        print("this is class B")

objA=A()
print(objA.car)
print(objA.bike)
print(objA.truck)
objA.showdetailA()
