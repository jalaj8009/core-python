# 30/11/2023

# Exception Handling
# a=5
# b=0
# try:
#     c=a/b
#     print(c)
# except:
#     print("plz enter a right digit")
#
#
#
# try:
#     age=int(input("enter any number age :"))
#     print(age)
# except:
#     print("enter a numeric value")
#
#
# a=10
# b=0
# try:
#     c=a/b
#     print(c)
# except Exception as E:
#     print("plz enter right num",E)
#
# a=4
# b=8
# try:
#     c=a/b
#     print('C:',c)
# except ZeroDivisionError:
#     print("check your division is zero")
# else:                #it will be executed when no exception
#     print("your division is greater than zero")


# 1/12/2023

# try:
#     number=int(input("enter number"))
#     if number>10:
#         raise Exception("invalid number")
# except Exception as e:
#     print(e)

#
# a=10
# b=5
# try:
#     c=a/b
#     print('C:',c)
# except ZeroDivisionError as e:
#     print("check your division is zero", e)
# finally:
#     print("always executed")


#
# try:
#     num1 = int(input("enter a numerator: "))
#     num2 = int(input("enter a denominator"))
#
#     result=num1/num2
#
#     if result % 1 !=0:
#         raise ValueError("result is not an integer")
#
#     if result < 0:
#         raise ValueError("result is negative")
#
#     print(f"the result of the division is:{result}")
#
# except ValueError as ve:
#     print(f"error: {ve}")
#
# except ZeroDivisionError:
#     print("Error: cannot divide by zero")
#
# except Exception as e:
#     print(e)


#
# try:
#     num1 = int(input("enter a numerator: "))
#     num2 = int(input("enter a denominator"))
#
#     result=num1/num2
#
#     if result % 1 !=0:
#         raise ValueError("result is not an integer")
#
#     if result < 0:
#         raise ValueError("result is negative")
#
#     print(f"the result of the division is:{result}")
#
# except ValueError as ve:
#     print(f"error: {ve}")
#
# except ZeroDivisionError:
#     print("Error: cannot divide by zero")
#
# except Exception as e:
#     print(e)

#
# num1=(input("enter number"))
# num2=(input("enter number"))
#
# try:
#     result=num1/num2
#     if result % 1 !=0:
#         raise ValueError("result is not an integer")

#     if result < 0:
#         raise ValueError("result is negative")
#
#     print(f"the result of the division is:{result}")
#
# except ValueError as ve:
#     print(f"error: {ve}")
#
# except ZeroDivisionError:
#     print("Error: cannot divide by zero")
#
#
# except EOFError:
#     print("please enter input")
#
# except Exception as e:
#     print(e)
#
# import pickle
# l=[1,2,3,4,5,6]
# file=open("asd1.txt","wb")
# pickle.dump(l,file)
# file.close()

# 6/12/2023
# class A:
#     "i am python developer"
#     name="rays"
#     age=23
#     print(name)
#
#     def show(self):
#         "i am a trader"
#         self.salary=1000
#         print(self.salary)
#
# object =A()
# print(A.age)
# print(object.__doc__)
# object.show()
# print(object.show.__doc__)