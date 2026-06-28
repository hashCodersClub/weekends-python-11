
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}.\nI am {self.age} years old")



hasib = Human("Hasib",55)
gaurav = Human("Gaurav",1055)

hasib.introduce()
gaurav.introduce()


