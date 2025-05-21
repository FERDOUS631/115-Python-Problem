# Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.
number = int(input("Enter a number to calculate its factorial: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
    print(i)
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    print(f"The factorial of {number} is: {factorial}")
