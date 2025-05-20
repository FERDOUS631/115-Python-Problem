#  String Reverse: Write a Python function to reverse a given string and return the reversed string.

def reverse_string(s):
    # Initialize an empty string to store the reversed string
    reversed_string = ""
    
    # Iterate through the original string in reverse order
    for char in s[::-1]:
        # Append each character to the reversed string
        reversed_string += char
    
    return reversed_string
print(reverse_string("Hello, World!"))  

# String Reverse: Write a Python function to reverse a given string and return the reversed string.
def reverse_string(s):
    return s[::-1]
# Example usage

original = "hello world"
reversed_str = reverse_string(original)
print("Reversed String:", reversed_str)
