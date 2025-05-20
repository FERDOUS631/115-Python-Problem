#  Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.

def celsius_to_fahrenheit(celsius):
    #formula= (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius =float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f'{celsius} celsius is equal to {fahrenheit}fahrenheit')
# Example usage