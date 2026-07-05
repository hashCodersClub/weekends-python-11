class Car:
    def __init__(self,model_name,make_year):
        self.wheels = 4
        self.model_name = model_name
        self.make_year = make_year
    
    def __str__(self):
        return f"wheel: {self.wheels}\tModel Name:{self.model_name}\tMake Year:{self.make_year}"



swift_desire = Car("Suzuki",2026)
print(swift_desire)