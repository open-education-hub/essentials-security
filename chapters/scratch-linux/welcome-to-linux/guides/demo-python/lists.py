# SPDX-License-Identifier: BSD-3-Clause

lst = [1, "some string", True, 2.9]
print(lst, end="\n\n")

# Iterating a list.
# We can use for loops as well.
for el in lst:
    print(el)
print()

# Strings are just lists of characters:
for c in "SSS Rulz!":
    print(c)

# The length of a list is given by the function len.
print(f"\nLength of lst = {len(lst)}")
# Being lists of characters, len also works on strings.
print(f'\nLength of "SSS Rulz!" = {len("SSS Rulz!")}')


# We can concatenate lists just like we concatenate strings.
print(f'\nlst + [1, "a", False] = {lst + [1, "a", False]}\n')

# We can also modify lists in-place.
# append adds an element to the end of the list.
lst.append(0)
print(f"lst.append(0) => lst = {lst}\n")  # This is equivalent to lst += [0].

# remove removes the *first occurrence* of the element it receives as argument.
lst.remove(0)
print(f"lst.remove(0) => lst = {lst}\n")

# reversed also works lists.
# The code below is an object that generates the reversed list, not the reversed
# list itself.
print(f"reversed(lst) = {reversed(lst)}")
# In order to obtain the reversed list, we need to ask for it specifically:
print(f"list(reversed(lst)) = {list(reversed(lst))}\n")

# Modify an element at a given position.
lst[2] = "SSS"
print(f"lst[2] = False => lst = {lst}\n")

# You can check if an element is present in the list.
print(f'Is "SSS" in lst? {"SSS" in lst}')
print(f'Is "bananas" in lst? {"bananas" in lst}\n')

# But the most interesting part about lists is SLICING
print(f"lst elements from indices 1 to 2: {lst[1:2]}")
print(f"all lst elements up to index 2: {lst[:2]}")
print(f"all lst elements starting from index 1: {lst[1:]}")
print(f"all lst elements but the last two: {lst[:-2]}")
