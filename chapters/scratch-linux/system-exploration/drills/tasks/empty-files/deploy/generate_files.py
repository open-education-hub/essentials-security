#! /bin/bash

from os import makedirs
from random import choice, randint

DIRECTORIES = [
    '/home/ctf/south-park/randy/tegridy',
    '/home/ctf/south-park/randy/pangolin',
    '/home/ctf/south-park/randy/lorde',

    '/home/ctf/south-park/al-gore/manbearpig',

    '/home/ctf/south-park/token/tolkien',
    '/home/ctf/south-park/token/tupperware',

    '/home/ctf/south-park/timmy/timmeh',

    '/home/ctf/south-park/cartman/respect-my-authoritah',
    '/home/ctf/south-park/cartman/cartmenez',
    '/home/ctf/south-park/cartman/scott-tenorman'
]

FLAG = open('/home/ctf/flag', 'r').read().rstrip()

for directory in DIRECTORIES:
    makedirs(directory, 0o755)

all_files = []
for i in range(100):
    i_str = str(i)
    directory = choice(DIRECTORIES)
    filename = directory + '/' + '0' * (3 - len(i_str)) + i_str

    open(filename, 'w').close()
    all_files.append(filename)

flag_files = []
for _ in FLAG:
    flag_letter_file = randint(0, len(FLAG) - 1)
    while flag_letter_file in flag_files:
        flag_letter_file = randint(0, len(FLAG) - 1)

    flag_files.append(flag_letter_file)

flag_files = sorted(flag_files)
i = 0

for letter in FLAG:
    open(all_files[flag_files[i]], 'w').write(letter)
    i += 1
