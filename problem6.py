# Data Type Checker: Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).


def data_type_checker(variable,a):
    # Check the type of the variable and return the corresponding string
    if isinstance(variable, int):
        return "int"
    elif isinstance(variable,a, float):
        return "float"
    elif isinstance(variable, str):
        return "str"
    elif isinstance(variable, list):
        return "list"
    elif isinstance(variable, dict):
        return "dict"
    elif isinstance(variable, tuple):
        return "tuple"
    elif isinstance(variable, set):
        return "set"
    else:
        return "unknown type"
# Example usage
variable1 = 42
variable2 = 3.14
variable3 = "Hello, World!"
variable4 = [1, 2, 3]   
variable5 = {"key": "value"}
variable6 = (1, 2, 3)
variable7 = {1, 2, 3}
print(f"Variable 1 is of type: {variable2} = {data_type_checker(variable1,variable2)}")

