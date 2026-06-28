text = "I love my india" #string

vowels_count=0
consonant_count = 0
check_string = "aeiouAEIOU"

for char in text:
    if char in check_string:
        vowels_count += 1
    elif char != ' ':
        consonant_count += 1

print(f"Count of vowels = {vowels_count}")
print(f"Count of Consonant = {consonant_count}")