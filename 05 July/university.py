### parent class|base class|super class
class Human:
     def __init__(self,name,age,mobile,dob,gender):
        self.name = name 
        self.age = age
        self.mobile = mobile 
        self.dob = dob
        self.gender = gender


# children class|derived class
class Teacher(Human):
    def __init__(self,schedule):
        self.schedule = schedule 

# children class|derived class
class Student(Human):
    def __init__(self,course):
        self.course = course

# children class|derived class
class Guard(Human):
    def __init__(self,shift,name,age,mobile,dob,gender):
        super().__init__(name,age,mobile,dob,gender)
        self.shift = shift


gaurav = Guard("Evening Shift","Gaurav",56,9874563210,"16-02-2025","Male")

print(gaurav.name,gaurav.shift)