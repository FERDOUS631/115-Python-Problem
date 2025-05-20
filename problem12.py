# Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return f'{a} is the largest number'
    elif b >= a and b >= c:
        return f'{b} is the largest number'
    else:
        return f'{c} is the largest number'
# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print(largest_of_three(num1, num2, num3))