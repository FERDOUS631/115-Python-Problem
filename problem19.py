# Number Ranges: Write a Python program that takes an integer as input and prints whether the number falls within the ranges: 0-50, 51-100, 101-150, or above 150.
def number_range(num):
    if 0 <= num <= 50:
        return "The number is in the range of 0-50"
    elif 51 <= num <= 100:
        return "The number is in the range of 51-100"
    elif 101 <= num <= 150:
        return "The number is in the range of 101-150"
    else:
        return "The number is above 150"
# Example usage

number = int(input("Enter an integer: "))
print(number_range(number))