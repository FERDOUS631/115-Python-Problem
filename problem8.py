# String Reversal with Slicing: Write a Python function to reverse a given string using slicing.

def reverse_string(s):
    # Use slicing to reverse the string
    return s[::-1]
# Example usage
original = "hello world"
reversed_str = reverse_string(original)
print("Reversed String:", reversed_str)
