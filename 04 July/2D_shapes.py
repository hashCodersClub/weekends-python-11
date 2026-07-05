print("Please select your shape from the given options")
print("1: Circle")
print("2: Rectangle")
input_shape = int(input("Enter the shape number : "))

if input_shape == 1:
    r = int(input("Enter the radius of the circle"))
    print(f"Area of cirlce : {3.14*r*r}")
    print(f"Perimeter of circle : {2*3.14*r}")
elif input_shape==2:
    l = int(input("Enter the length of the rectangle"))
    b = int(input("Enter the breadth of the rectangle"))
    print(f"Area of rectangle : {l*b}")
    print(f"Perimeter of rectangle : {2*(l+b)}")