# SPDX-License-Identifier: BSD-3-Clause

my_dict = {"SSS": "Rullz", "Essentials": 10, True: 0.2, 2.2: 99}

print(my_dict["SSS"])  # Will print "Rullz"
print(my_dict[True])  # Will print 0.2
# And so on...

# Keys and values can be added or modified simply by referencing them.
my_dict["CTF"] = "pwned"
print(f'Added key CTF with value {my_dict["CTF"]}')

# You can also modify values in the same way.
my_dict[True] = 2.22
print(f"After the modfication: my_dict[True] = {my_dict[True]}")

# You can check if a key is in a dictionary just like you would do for a list:
print(f'Is "SSS" in my_dict? {"SSS" in my_dict}')
print(f'Is "bananas" in my_dict? {"bananas" in my_dict}')

# Accessing the value of a non-existent key results in a KeyError.
print(my_dict["bananas"])
