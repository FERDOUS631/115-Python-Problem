#  Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input and calculates and prints the real roots (if they exist) or a message indicating the complex roots
import math
def quadratic_solver(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is positive, zero, or negative
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"The roots are real and different: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"The roots are real and the same: {root}"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"
# Example usage
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
print(quadratic_solver(a, b, c))