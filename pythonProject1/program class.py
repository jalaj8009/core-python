# PALINDROME  24/11/2023
#
# input_string=input("enter a string ")
#
# s=input_string.lower().replace(" ","")
# if s == s[::-1]:
#     print("the string is a palindrome")
# else:
#     print("the string is not a palindrome")


# prime number 25/11/2023
# number=int(input("enter any number="))
# if number>1:
#    for i in  range(2,number):
#       if number%i ==0:
#         print("not prime number")
#         print(i,"times",number//i,"and",number)
#         break
#
#    else:
#         print("number is a prime number")
#
# else:
#     print("is not prime number")


# 5/12/2023
# maxima of two
# a=int(input("enter number 1= "))
# b=int(input("enter number 2= "))
# if a>b:
#     print("number1 is maximum")
# elif a==b:
#     print("both are same")
#
# else:
#     print("number2 is maximum")



# smallest of two using conditional operator 5/12/2023
# a=int(input("enter number 1= "))
# b=int(input("enter number 2= "))
# if a>b:
#     print("number2 is smaller")
# elif a==b:
#     print("both are same")
#
# else:
#     print("number1 is smaller")


# print 5 random integer between 1-100 5/12/2023
# import random
# n=random.randint(1,100)
# m=random.randint(1,100)
# o=random.randint(1,100)
# p=random.randint(1,100)
# q=random.randint(1,100)
# print(n,m,o,p,q)


# write a program to find a factorial of given number 5/12/2023
# import math
# a=int(input("enter number"))
# b=math.factorial(a)
# print(b)


# Write a program to reverse digits of a given number 6/12/2023
a=(input("enter number : "))
b=a[::-1]
print(b)