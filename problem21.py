# Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.
number = int(input("Enter a number to calculate its factorial: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"The factorial of {number} is: {factorial}")