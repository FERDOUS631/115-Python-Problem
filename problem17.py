#  Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle.
def triangle_type(a, b, c):
    # Check if the sides can form a triangle
    if a + b > c and a + c > b and b + c > a:
        # Check for equilateral triangle
        if a == b == c:
            return "Equilateral triangle"
        # Check for isosceles triangle
        elif a == b or a == c or b == c:
            return "Isosceles triangle"
        # If not equilateral or isosceles, it must be scalene
        else:
            return "Scalene triangle"
    else:
        return "The sides do not form a triangle"
# Example usage
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))
print(f'The triangle is: {triangle_type(side1, side2, side3)}')