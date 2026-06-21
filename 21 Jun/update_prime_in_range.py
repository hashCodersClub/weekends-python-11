# Write a function which takes one number as input and then prints all prime factors of the given number

num = int(input("Enter a num : "))
prime_factor = 2

while num != 1:
    if num % prime_factor == 0:
        print(prime_factor,end=", ")
        num = num / prime_factor
    else:
        prime_factor += 1