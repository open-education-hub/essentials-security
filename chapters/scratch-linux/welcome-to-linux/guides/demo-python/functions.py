# SPDX-License-Identifier: BSD-3-Clause


# The code inside the function isn't run when we run the script.
# It's only run when specifically called:
#  SPDX-License-Identifier: BSD-3-Clause
def replicate(s, n=3):
    """
    This is a docstring comment. They are used in order to document the
    behaviour of functions an classes in Python. You may see them often.
    They typically look like this:

    Replicates a given string by a given number of times.

        Parameters:
            s (str): the string to replicate
            n (int): the number of times to replicate it. 3 by default

        Returns:
            String made up of s replicated n times
    """
    acc = ""

    for _ in range(n):
        acc += s

    return acc


# Implementation using list comprehensions and the join function.
# Check the links at the end of the lecture for details
def replicate_fancy(s, n=3):
    return "".join([s for _ in range(n)])


my_string = "SSS Rulz!"
my_replicated_string = replicate(my_string, 4)
print(f"Initial string is unchanged: {my_string}")
print(f"Returned string is: {my_replicated_string}")

# We can also specify any function parameter by name, like so:
my_replicated_string = replicate(s=my_string, n=2)
print(f"New returned string is: {my_replicated_string}")

# The print function can also take some default parameters, such as end:
# end is the string to be placed at the end of what's printed.
# By default it's \n.
print(my_string, end="$$$\n")  # This now prints 'SSS Rulz!'$$$


# Similarly, range also takes 2 default parameters: start=0 and step=1.
# As a result, its signature could look like this:
def range(end, start=0, step=1):
    pass  # we can use this keyword when we want to leave functions unimplemented


# Functions can also have multiple return variables
def multiple_returns(ret_type):
    if ret_type == 1:
        return 1
    else:
        return "there you go"


print("\nMultiple Returns")
print(f"Function returning an int: {multiple_returns(1)}")
print(f'Same function returning a string: "{multiple_returns(0)}"')
