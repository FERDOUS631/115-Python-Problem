#  Leap Year Checker: Write a Python program that takes a year as input and determines if it is a leap year or not  
def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
        return f'{year} is a leap year'
    else:
        return f'{year} is not a leap year'
# Example usage
year = int(input("Enter a year: "))
print(is_leap_year(year))
