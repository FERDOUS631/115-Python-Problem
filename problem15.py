# Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

def check_vowel_or_consonant(char):
   # Check if the input is a single character
    vowels = "aeiouAEIOU"
    if len(char) != 1:
        return "Please enter a single character."   
    # Check if the character is a vowel
    if char in vowels:
        return f"{char} is a vowel."    
    # Check if the character is a consonant
    elif char.isalpha():
        return f"{char} is a consonant."
    else:
        return "Please enter a valid alphabetic character."
# Example usage
char = input("Enter a single character: ")
print(check_vowel_or_consonant(char))