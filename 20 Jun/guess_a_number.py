import random
computer_generated = random.randint(1,100)

# score -> 100 - (i * 5)
for i in range(10):
    number = int(input("Guess a number :"))

    if computer_generated == number:
        print("Congratulations You have won the game your score is ",(100 - i * 5))
        break
    elif computer_generated > number:
        print("You guessed a number smaller than computer selected ! Please try again")
    elif computer_generated < number:
        print("you guessed a number greater than computer selected")
else:
    print("You lost the game")