# SPDX-License-Identifier: BSD-3-Clause

if False:
    print("This code is not executed")
if True:
    print("This code is executed")

a = 0
b = 1

if a == 0:
    print("This is a correct if statement")
b = 2
# The line above is not indented at the same level as the one above.
# Thus, it is not contained in the body of the above if statement.

# Python does not have a switch instruction.
# In order to create something similar to it, you'll have to use elifs:
if b == 1:
    print("b = 1")
elif b == 2:
    print("b = 2")
elif b == 3:
    print("b == 3")
else:
    print("You get the point")

# In order to create more complex if conditions Python does not use && and ||.
# It simply uses the keywords and, or.
if a == 0 and b == 2:
    print("This is a correct if condition: a == 0 and b == 2")
if a == 1 or b == 2:
    print("This is another correct if condition: a == 1 and b == 2")

# Similarly, in order to negate an expression, we use the not keyword.
if not a:  # Equivalent to if (!a) in C
    print("a == 0, thus not a is True")

# To create even more complex boolean expressions you can use parentheses,
# just like you would for arithmetic expressions.
