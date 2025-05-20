#  String Palindrome: Write a Python function to check if a given string is a palindrome or not.
def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] == s[-(i+1)]:
            return True
    # If no mismatches were found, the string is a palindrome
        else:
             return False
# Example usage
string1 = "racecar"
string2 = "eye"
print(f"{string1} is a palindrome: {is_palindrome(string1)}")
print(f"{string2} is a palindrome: {is_palindrome(string2)}")