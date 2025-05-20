# Positive, Negative, or Zero: Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
# Example usage
number = float(input("Enter a number: "))
print(f"The number is: {check_number(number)}")
