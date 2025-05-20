# Type Conversion: Given a list of integers, write a Python program to convert each element of the list to a string.

def convert_to_strings(int_list):
   return [str(i) for i in int_list]
# Example usage
# [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 4, 5]
string_list =convert_to_strings(numbers)
print(string_list)



