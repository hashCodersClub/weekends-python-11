# range -> 1 - 8 | even -> square , odd -> cube

list = [x ** 2 if x % 2 == 0 else x**3 for x in range(1,9)]

list2 = ["even" if x % 2 == 0 else "odd" for x in list]

print(list)
print(list2)