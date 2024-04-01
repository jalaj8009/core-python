'''class Shape:
    def __init__(self,color):
        self.color=color
    def display_color(self):
        print(f"the shape is {self.color} ")

class Rectangle(Shape):

    def __init__(self,color,length,breath):
        super().__init__(color)
        self.length=length
        self.breath=breath

    def calculate_area(self):
        return self.length*self.breath

    def display_color__area(self):
        super().display_color()
        area=self.calculate_area()
        print(f"the area of thr rectangle is:{area}")


color=input("enter color: ")
length=int(input("enter length: "))
breath=int(input("enter breath"))
rectangle=Rectangle(color,length,breath)
rectangle.display_color__area()  '''

'''import  smtplib
smtp_server="smtp.gmail.com"
port=587
sender_email="singhshivam10071996@gmail.com"
password=input("enter password and press enter:")
receiver_email="ajaysawle95@gmail.com","aman.jitechno@gmail.com"
message=""" From:Jalaj singh
Subject:Hi from Jalaj"""
smtp=smtplib.SMTP(smtp_server,port)
smtp.starttls()
smtp.login(sender_email,password)
smtp.sendmail(sender_email,receiver_email,message)
print("email send successful") '''



'''class A:
    
    def show(self):

        print("this is class A")

class B(A):
    def show(self):
        super().show()

        print("this class B")

object =B()
object.show()  '''


# class A:
#     car=10
#     bike=20
#
#     def show(self):
#         print("this is class A")
#
#
# class B(A):
#     petrol=108
#     diesel=95
#     def show(self):
#         super().show()
#
#         print("this class B")
#
#
# object = B()
# object.show()
# print(object.diesel)
# print(object.car)
# print(object.bike)
# print(object.petrol)


class A:
    car=10
    bike=20

    def show(self):
        print("this is class A")


class B():
    petrol=108
    diesel=95
    def show(self):


        print("this class B")


object = B()
object.show()
print(object.diesel)
print(object.petrol)
object=A()
object.show()
#print(object.diesel)
print(object.car)
print(object.bike)
#print(object.petrol)
