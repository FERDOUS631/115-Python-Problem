# Table of a Number: Write a Python program using a for loop to print the multiplication table of a given number N.
def multiplication_table(n):
    print(f"Multiplication table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
# Example usage
number = int(input("Enter a number to print its multiplication table: "))
multiplication_table(number)