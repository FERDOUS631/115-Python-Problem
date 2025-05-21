# Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.   
def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
# Example usage
number = int(input("Enter an integer to count its digits: "))
if number < 0:
    # number = -number  # Make the number positive for counting digits
    print(f"The number is negative, converting to positive: {number}")
    # print("Please enter a positive integer.")
else:
    digit_count = count_digits(number)
    print(f"The number of digits in {number} is: {digit_count}")

    
    # The num