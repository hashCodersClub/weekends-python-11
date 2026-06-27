text = "I love my india" #string

# string -> group of character
# for i in range(5):
#     print(fruit[i])
# how many times charact i is in the text

vowels_count=0
consonant_count = 0
check_string = "aeiouAEIOU"

for char in text:
    if char in check_string:
        vowels_count += 1
    else:
        consonant_count += 1

print(f"Count of vowels = {vowels_count}")
print(f"Count of Consonant = {consonant_count}")
      

