# SPDX-License-Identifier: BSD-3-Clause

# While loops are pretty simple. They're similar to if statements:
print("While loop:")
a = 0
while a < 5:
    print(a)
    a += 1
print()

# For loops, however, are a lot more interesting
# The equivalent of for (int i = 0; i < 5; ++i) is:
print("For loop")
for i in range(5):
    print(i)
print()

# Notice the range(5) construction.
# range(n) returns an object that generates numbers in the *range* [0, n)
# We can also specify a start and a step to a range:
print("For loop with another range")
r = range(2, 11, 3)  # range(start, end, step)
for i in r:
    print(i)
print()

# We can also use reversed ranges by using the reversed function:
print("For loop with a reversed range")
r = reversed(range(0, 5))
for i in r:
    print(i)
