### OOPS - [Object Oriented Programming]

class Student:
    # init method initializes object of class
    def __init__(self,name):
        print("executed")
        self.name = name
        

chandan = Student("Chandan")
print(chandan.name)
abhay = Student("Abhay")
print(abhay.name)
gaurav = Student("Gaurav")
print(gaurav.name)
shiv = Student("Shiv")
print(shiv.name)
himanshu = Student("Himanshu")
print(himanshu.name)





