#  Sum of N Numbers: Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.n= int(input("Enter a natural number N: "))
num = int(input("Enter a natural number N: "))
sum_of_n = 0
for i in range(1, num + 1):
    print(i)
    sum_of_n += i
print(f"The sum of the first {num} natural numbers is: {sum_of_n}")

