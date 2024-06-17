# SPDX-License-Identifier: BSD-3-Clause

flag_file = open("../src/flag", "rb")
jumbled_flag = flag_file.read()

# There are no hints, so we have to generate all possible flags.
# This means all permutations of printable characters in the given flag
chunks = jumbled_flag[4:-1].split(b"\x80\x80\x80")


def permutations(l):
    if not l:  # Check if list is empty
        return []

    if len(l) == 1:
        return [l]

    new_l = []

    for i in range(len(l)):
        tmp = l[i]
        rest = l[:i] + l[i + 1 :]  # All l elements except the ith.

        # Generate all permutations that start with tmp
        for p in permutations(rest):
            new_l.append([tmp] + p)

    return new_l


# Now try each of them until you find the one that works.
for p in permutations(chunks):
    print(f'SSS{{{b"".join(p).decode()}}}')
