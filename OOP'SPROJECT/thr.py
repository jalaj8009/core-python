5/12/2024

# threading
# def hello():
#     for i in range(15):
#         print('hello',i)
#
#
# def hi():
#     for i in range(15):
#         print('Hi',i)
#
# hello()
# hi()



# import threading
# from threading import *
# def hello():
#     for i in range(15):
#         print('hello',i)
#
#
# def hi():
#     for i in range(15):
#         print('Hi',i)
#
# t1=threading.Thread(target=hello)
# t2=threading.Thread(target=hi)
#
# t1.start()
# t2.start()


# import threading
# from threading import *
# def hello():
#     for i in range(15):
#         print('hello',i)
#


# import threading
# from threading import *
# def hello(name):
#     for i in range(15):
#         print(name,i)
#
#
# def hi(name):
#     for i in range(15):
#         print(name,i)
#
# t1=threading.Thread(target=hello, args=('ram',))
# t2=threading.Thread(target=hi, args=('shyam',))
#
# t1.start()
# t2.start()
#

# 6/12/2023
# from time import sleep
#
# class A:
#     def run(self):
#         for i in range(5):
#             print("aman ")
#             sleep(1)
#
# class B:
#     def run(self):
#         for i in range(5):
#             print("ajay")
#             sleep(1)
#
# t1=A()
# t2=B()
# t1.run()
# t2.run()

# multithreading
from time import sleep
from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
            print("aman")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("ajay")
            sleep(1)
t1=A()
t2=B()
t1.start()
t2.start()
t1.join()
t2.join()

print("jalaj")