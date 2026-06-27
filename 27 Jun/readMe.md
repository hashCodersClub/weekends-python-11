### Function :-

Identified block of re-usable code,has tendency to return something.
NOTE: If you don't return anything from function explicitely(manually) and function implicitely(ultimately) returns None from it.

> def <name-of-function>():

    statement1
    statement2
    stetementn

eg :-
def greeting():
a = 10
b = 20
return a+b

value = greeting()

print(f"Value of value is {value}")

- return [to return a value from function explicitly]
- parameter [temporarily defined variables inside the parenthesis of function definition]
- arguments [value passed inside function call for the parameters]

type of arguments :-

1.  positional arguments
    def greeting(a,b):
    return a+b

value = greeting(30,20\*2)

print(f"Value of value is {value}") 2. named arguments
def greeting(a,b):
return a+b

value = greeting(b=30,a=20\*2)

print(f"Value of value is {value}")
