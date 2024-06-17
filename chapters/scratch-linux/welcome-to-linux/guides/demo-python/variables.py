# SPDX-License-Identifier: BSD-3-Clause

# This is a comment in Python, just like bash commands

# Unlike C, there are no explicit types in Python
# The type of each variable is inferred (deduced) when running the code

# We can create variables simply by declaring them
my_integer = 5
my_float = 5.02
my_boolean = True  # or False

my_string = "This is a string"
my_other_string = "This is also a string"
my_third_string = """
This is a
multi-line
string
"""
# Notice there are many ways in which you can declare a string.
# Use whichever fits your style and purpose

# In order to display messages to the console, use the print function:
print("Hello World!")

print("my_integer is:")
print(my_integer)
print()  # This prints an empty line

print("my_boolean is:")
print(my_boolean)
print()

print("my_string is:")
print(my_string)
print()

print("my_float and my_other_string printed together are:")
print(my_float, my_other_string)  # You can give however many parameters to print
print()

print("my_third_string is:")
print(my_third_string)  # The newline characters before and after """ are also printed

# We can also use formatted strings in Python
# And it's simpler than using %s, %d and so on in C.
# Just prefix the string with f and use {} for variables
my_formatted_string = f"integer = {my_integer}; float = {my_float}"
print(my_formatted_string)

# Basic arithmetic is *almost* the same as in C... almost
print("\nArithmetic time:")
print(f"2 + 2 = {2 + 2}")
print(f"4 - 1 = {4 - 1}, quick maths")
print(f"2 * 4 = {2 * 4}")
print(f"10 % 3 = {10 % 3}")
print(f"Python even supports exponentiation using **: 10 ** 4 = {10 ** 4}")

# / performs floating point division
print(f"Be careful: 10 / 3 = {10 / 3}")

# If you only want the quotient use //:
print(f"Be very careful: 10 // 3 = {10 // 3}")

# Also, there are no ++ or -- in Python. You have to do it the ugly way:
print(f"\nmy_integer = {my_integer}")
my_integer += 1
print(f"my_integer += 1 => my_integer = {my_integer}")
my_integer -= 1
print(f"my_integer -= 1 => my_integer = {my_integer}")

# Notice that in the code below we used " for the inner strings as ' would close the starting '.
print(f'\nString concatenation: abc + def = {"abc" + "def"}')
# Yes, it's THIS simple to concatenate strings in Python!

# You can also easily convert between types.
# Most of the time, you'll do this to and from strings.

# Conversion from string
integer_var = int("39")
print(
    f'\nConverting the string "39" to int yields: {integer_var} of type {type(integer_var)}'
)
bool_var = bool("False")
print(
    f'Converting the string "False" to bool yields: {bool_var} of type {type(bool_var)}'
)

# Conversion to string
string_int_var = str(3994)
print(
    f'\nConverting the integer 3994 to string yields: "{string_int_var}" of type {type(string_int_var)}'
)
string_bool_var = str(True)
print(
    f'Converting the boolean True to string yields: "{string_bool_var}" of type {type(string_bool_var)}'
)
